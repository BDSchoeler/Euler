count=0
sum=0

for i in range(200,-1,-200):
    for j in range(i,-1,-100):
        for k in range(j,-1,-50):
            for l in range(k,-1,-20):
                for t in range(l,-1,-10):
                    for n in range(t,-1,-5):
                        for m in range(n,-1,-2):
                            count+=1
print (count)
