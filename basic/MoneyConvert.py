#MoneyConvert.py
MoneyStr = input()
if MoneyStr[0:3] in ["RMB"]:
    USD = eval(MoneyStr[3:]) / 6.78
    print("USD{:.2f}".format(USD))
else:
    RMB = eval(MoneyStr[3:]) * 6.78
    print("RMB{:.2f}".format(RMB))

