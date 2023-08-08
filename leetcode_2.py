l1 = [2,4,3,7]
l2 = [3,3,4]




output = []
v1=v2=0
ind1=ind2=0
summ=0
ostatok=ost=0
len1=len(l1)
len2=len(l2)
rizn=len1-len2
while True:


    v1 = l1[ind1]
    v2 = l2[ind2]

    if ind1<len1-1:
        ind1+=1

    if ind2<len2-1:
        ind2+=1

    if len(output)==ind1+1 or len(output)==ind2+1:
        break


    if ostatok>0:
        summ=v1+v2+ostatok
        ostatok=0
    else:
        summ=v1+v2
    if summ>9:
        ostatok=summ//10
        ost=summ%10
        output.append(ost)
    else:
        output.append(summ)





    v1=v2=summ=0
    ost=0
if rizn==1:
    output.append(ind1)


print(output)