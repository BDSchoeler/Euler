def ifBinary(n):
    if int(bin(n)[:1:-1], 2)==int(bin(n),2):
        return True
    return False
def ifDecimal(n):
    if str(n)==str(n)[::-1]:
        return True
    return False

totalSum=0

for i in range(1000000):
    if ifBinary(i) and ifDecimal(i):
        totalSum=totalSum+i
print(totalSum)
