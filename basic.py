# -*- coding: utf-8 -*-

import OpenSSL.crypto
import base64
import urllib
import hashlib


class ChinaPay(object):

    def __init__(self, MerId, pfx_path, pfx_pwd, cer_path):
        """
        :param MerId: 商户号
        :param pfx_path: 交易证书路径
        :param pfx_pwd: 交易证书密码
        :param cer_path: 验签证书路径
        """

        self.MerId = MerId
        self.pfx = self._load_pfx(pfx_path, pfx_pwd)
        self.cer = self._load_cer(cer_path)

    def _load_pfx(self, pfx_path, pfx_pwd):
        """载入交易证书"""

        with open(pfx_path, 'rb') as f:
            pfx = OpenSSL.crypto.load_pkcs12(f.read(), pfx_pwd)
        return pfx

    def _load_cer(self, cer_path):
        """载入验签证书"""

        with open(cer_path, 'rt') as f:
            cer = OpenSSL.crypto.load_certificate(
                OpenSSL.crypto.FILETYPE_PEM, f.read())
        return cer

    def _get_sign_str(self, data):
        """将待签名dictionary转换成str"""

        keys = data.keys()
        keys.sort()
        return '&'.join(['%s=%s' % (key, data[key]) for key in keys])

    def sign(self, data):
        """签名
        :param data: 待签名的dictionary
        :param alg: 签名算法
        """

        alg = 'sha512'
        sign_raw_str = self._get_sign_str(data)

        signature = OpenSSL.crypto.sign(self.pfx._pkey, sign_raw_str, alg)
        return base64.b64encode(signature)

    def verify(self, data, is_bg=False):
        """验签
        :param data: 银联返回的已签名的dictionary
        :param alg: 签名算法
        :param is_bg: 是否是后台交易
        """

        # 如果是后台交易，需要对参数处理
        if is_bg:
            for k, v in data.items():
                data[k] = urllib.unquote_plus(v)

        alg = 'sha512'
        signature = base64.b64decode(data.pop('Signature'))
        sign_raw_str = self._get_sign_str(data)

        try:
            OpenSSL.crypto.verify(self.cer, signature, sign_raw_str, alg)
            return True
        except OpenSSL.crypto.Error:
            return False


class UnionPay(object):

    def __init__(self, MerId, pfx_path, pfx_pwd, cer_path):
        """
        :param MerId: 商户号
        :param pfx_path: 交易证书路径
        :param pfx_pwd: 交易证书密码
        :param cer_path: 验签证书路径
        """

        self.MerId = MerId
        self.pfx = self._load_pfx(pfx_path, pfx_pwd)
        self.cer = self._load_cer(cer_path)
        self.certId = self.pfx._cert.get_serial_number()

    def _load_pfx(self, pfx_path, pfx_pwd):
        """载入交易证书"""

        with open(pfx_path, 'rb') as f:
            pfx = OpenSSL.crypto.load_pkcs12(f.read(), pfx_pwd)
        return pfx

    def _load_cer(self, cer_path):
        """载入验签证书"""

        with open(cer_path, 'rt') as f:
            cer = OpenSSL.crypto.load_certificate(
                OpenSSL.crypto.FILETYPE_PEM, f.read())
        return cer

    def _get_sign_str(self, data):
        """将待签名dictionary转换成str"""

        keys = data.keys()
        keys.sort()
        return '&'.join(['%s=%s' % (key, data[key]) for key in keys])

    def sign(self, data):
        """签名
        :param data: 待签名的dictionary
        """

        data.update({'certId': str(self.certId)})

        alg = 'sha1'
        sign_raw_str = self._get_sign_str(data)
        sign_raw_str_sha1 = hashlib.sha1(sign_raw_str).hexdigest()

        signature = OpenSSL.crypto.sign(self.pfx._pkey, sign_raw_str_sha1, alg)
        data.update({'signature': base64.b64encode(signature)})
        return data

    def verify(self, data):
        """验签
        :param data: 银联返回的已签名的dictionary
        """

        alg = 'sha1'
        signature = base64.b64decode(data.pop('signature'))
        sign_raw_str = self._get_sign_str(data)
        sign_raw_str_sha1 = hashlib.sha1(sign_raw_str).hexdigest()

        try:
            OpenSSL.crypto.verify(self.cer, signature, sign_raw_str_sha1, alg)
            return True
        except OpenSSL.crypto.Error:
            return False
