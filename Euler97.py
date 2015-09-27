digits=28433
for i in range(7830457):
    digits=digits*2
    digits=digits%10000000000
print(digits+1)
