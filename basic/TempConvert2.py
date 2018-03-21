#TempConvert2.py
TempStr = input()
if TempStr[0] in ['F']:
    C = (eval(TempStr[1:]) - 32) / 1.8
    print("C{:.2f}".format(C))
else:
    F = 1.8*eval(TempStr[1:]) + 32
    print("F{:.2f}".format(F))

