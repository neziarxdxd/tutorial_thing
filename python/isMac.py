def isMAC48Address(inputString):
    
    d= 0
    
    if not("-" in inputString):
        return False
    else:
        for i in inputString.split("-"):
            if not(isHex(i)):
                d+=1
        return d ==0 

    
def isHex(seg):
    x =["A","B","C","D","E","F","0","1","2","3","4","5","6","7","8","9"]
    if len(seg) ==2:
        return (seg[0] in x) and (seg[1] in x)
    else:
        return False

print(isMAC48Address("02-03-04-05-06-07-"))