#currency/converter.py
CurStr = input()
if CurStr[:3]=="RMB":
    USD = eval(CurStr[3:])/6.78
    print("USD{:.2f}".format(USD))
elif CurStr[:3]=="USD":
    RMB = eval(CurStr[3:])*6.78
    print("RMB{:.2f}".format(RMB))