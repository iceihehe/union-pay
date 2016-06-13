# 银联支付

封装了银联支付需要用到的方法

### 版本
1.0 添加了请求参数签名方法和返回参数验证签名方法

### 用法

##### 给请求参数签名，实例化四个参数依次是商户ID，交易证书路径（pfx文件），交易证书密码，验签证书路径
```python
>>>from basic import UnionPay
>>>up = UnionPay('merchant_id', 'path/to/transaction/certificate', 'transaction_certificate_password', 'path/to/verify/certificate')
>>>data = {"Version": 20140728, "OrderAmt": 1, "TranDate": 11111111, "BusiType": "0001", "MerBgUrl": "http://zfb.cdecube.com/", "MerPageUrl": "http://zfb.cdecube.com/", "MerOrderNo": 111, "TranTime": 111111, "MerId": "000001605260645"}
>>>sign = up.sign(data)
>>>sign
'LGx39hY/L/4HU5nyvqPfdns+kwfrwGngiCmpLQ/dy8dPVBOas5FxiYgWEMJIhd1I5ykoLGVGyy4XINidvqsYQjurEYRwQa7w/H2UYjEbqOKdijlzOsSkvUO3vVdR81B0RcE+QrV+VyndNERmJFMfVp4/EE/iY9dOQMQGJQV3Qtw='
```

##### 验签
```python
>>>from basic import UnionPay
>>>up = UnionPay('merchant_id', 'path/to/transaction/certificate', 'transaction_certificate_password', 'path/to/verify/certificate')
>>>data = {"TranType": "0001", "TranDate": "20160602", "MerId": "000001605260645", "BusiType": "0001", "AcqDate": "20160602", "CurryNo": "CNY", "TranTime": "023529", "CompleteDate": "20160602", "BankInstNo": "700000000000023", "Version": "20140728", "AcqSeqId": "0000000005841781", "Signature": "THHDUP2mlOraPcl6MY3ngC6%2FdWUSn4LFEVDzjS1BIpLsQxhsXe5Jao5V%2BzEzckpROQ8%2By4VzqwRlzphRABBN%2FyowGhJc%2FxJ9viTgE%2BGn%2Be6cErfkUxdH52Dz5G8jdvUgTR1g0SgZXBBvo%2BCmwk7scGkMYnvF2W9%2F0kvPTqBDGqQ%3D", "CompleteTime": "103237", "MerOrderNo": "770913", "OrderAmt": "1", "OrderStatus": "0000"}
>>>verify = up.verify(data)
>>>verify
True
```
