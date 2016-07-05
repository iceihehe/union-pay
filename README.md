# 银联支付

封装了银联支付需要用到的方法

### 版本
v1.0 添加了chinapay的请求参数签名方法和返回参数验证签名方法
v2.0 添加了unionpay的请求参数签名方法和返回参数验证签名方法

### 用法

#### chinapay

##### 给请求参数签名，实例化四个参数依次是商户ID，交易证书路径（pfx文件），交易证书密码，验签证书路径
```python
>>>from basic import ChinaPay
>>>cp = ChinaPay('merchant_id', 'path/to/transaction/certificate', 'transaction_certificate_password', 'path/to/verify/certificate')
>>>data = {"Version": 20140728, "OrderAmt": 1, "TranDate": 11111111, "BusiType": "0001", "MerBgUrl": "http://zfb.cdecube.com/", "MerPageUrl": "http://zfb.cdecube.com/", "MerOrderNo": 111, "TranTime": 111111, "MerId": "000001605260645"}
>>>sign = cp.sign(data)
>>>sign
'LGx39hY/L/4HU5nyvqPfdns+kwfrwGngiCmpLQ/dy8dPVBOas5FxiYgWEMJIhd1I5ykoLGVGyy4XINidvqsYQjurEYRwQa7w/H2UYjEbqOKdijlzOsSkvUO3vVdR81B0RcE+QrV+VyndNERmJFMfVp4/EE/iY9dOQMQGJQV3Qtw='
```

##### 对银联异步通知请求验证签名
```python
>>>data = {"TranType": "0001", "TranDate": "20160602", "MerId": "000001605260645", "BusiType": "0001", "AcqDate": "20160602", "CurryNo": "CNY", "TranTime": "023529", "CompleteDate": "20160602", "BankInstNo": "700000000000023", "Version": "20140728", "AcqSeqId": "0000000005841781", "Signature": "THHDUP2mlOraPcl6MY3ngC6%2FdWUSn4LFEVDzjS1BIpLsQxhsXe5Jao5V%2BzEzckpROQ8%2By4VzqwRlzphRABBN%2FyowGhJc%2FxJ9viTgE%2BGn%2Be6cErfkUxdH52Dz5G8jdvUgTR1g0SgZXBBvo%2BCmwk7scGkMYnvF2W9%2F0kvPTqBDGqQ%3D", "CompleteTime": "103237", "MerOrderNo": "770913", "OrderAmt": "1", "OrderStatus": "0000"}
>>>verify = cp.verify(data)
>>>verify
True
```

#### unionpay

##### 给请求参数签名，实例化四个参数依次是商户ID，交易证书路径（pfx文件），交易证书密码，验签证书路径
```python
>>>from basic import UnionPay
>>>cp = UnionPay('merchant_id', 'path/to/transaction/certificate', 'transaction_certificate_password', 'path/to/verify/certificate')
>>>data = {"Version": 20140728, "OrderAmt": 1, "TranDate": 11111111, "BusiType": "0001", "MerBgUrl": "http://zfb.cdecube.com/", "MerPageUrl": "http://zfb.cdecube.com/", "MerOrderNo": 111, "TranTime": 111111, "MerId": "000001605260645"}
>>>data_signed = cp.sign(data)
>>>data_signed
{'TranDate': 11111111, 'BusiType': '0001', 'certId': '40220995861346480087409489142384722381', 'TranTime': 111111, 'Version': 20140728, 'OrderAmt': 1, 'signature': 'BWZv3S4kTbuAisX1/aibDg7AfTjWDG2XLIGrSyQ96iAnYRW+yVfnyUL1/0JCcBxl/XFpYKxhBwFTR6sAYEVP9HQsOPV5f62XC9/+vvsnO3RDj/41Y9mBnAOCKsa07aJhommkWhYKKeD9bxFL91/jcHo6kag+1ips5jA8dqVjc9Q=', 'MerBgUrl': 'http://zfb.cdecube.com/', 'MerPageUrl': 'http://zfb.cdecube.com/', 'MerOrderNo': 111, 'MerId': '000001605260645'}
```

##### 对银联异步通知请求验证签名
```python
>>>data = {"accessType":"0","bizType":"000201","certId":"68759585097","currencyCode":"156","encoding":"UTF-8","merId":"802310053110831","orderId":"4036074942","queryId":"201607041629538091698","respCode":"00","respMsg":"success","settleAmt":"1","settleCurrencyCode":"156","settleDate":"0704","signMethod":"01","signature":"P9ZwFBs5dCC3cHk4XULFfrk0I4DaDtdTufDRqwoh0VeM9F2I4IqrZs7yMKz8DO3KdJ8GONTHhEHUjrqq+rvVR2p+Hnusb1az/Lxc1X198d4uWekB4ieEhoSWXF0zY3EP8HARtPdcvBb/hR5aWUfOZeI/x1RBPCqReBBuVgMNUa2s5dWbESJYneu57djEaNmPrwiuTecdVrLNUNxnH8rRjvLJI0cJvTgcio9/1HjSCH+45bKKZ003PRhZY+VgDtR8xqY8/xtUfrvqotqF6TDuMPS4WN7sBNDBSHsFDaztv5htwJ9Z6H2Lnz5lgtEStlyu/VPCWYQ8XkcvO1ZcQJKbBA==","traceNo":"809169","traceTime":"0704162953","txnAmt":"1","txnSubType":"01","txnTime":"20160704162953","txnType":"01","version":"5.0.0"}
>>>verify = cp.verify(data)
>>>verify
True
```

### 备注
关于chinapay和unionpay的区别，请自行百度。
