'''
sal                                hra         da        pf      it
<=10000                            12            8         4      2
>10000 and <=20000                 16           10         7      4                
>20000 and <=30000                 21           15        10      7
>30000 and <=40000                 25           20        14     10
>40000 and <=50000                 28           23        19     14
>50000 and <=60000                 32           27        22     19
>60000 and <=75000                 35           30        26     20
>75000                             38           32        28     26
'''



st=input("enter name:")
sal=eval(input("enter sal:"))
if sal<=10000:
    hra=sal*0.12
    da=sal*0.08
    pf=sal*0.04
    it=sal*0.02
elif sal>10000 and sal<=20000:
    hra=sal*0.16
    da=sal*0.10
    pf=sal*0.07
    it=sal*0.04
elif sal>20000 and sal<=30000:
    hra=sal*0.21
    da=sal*0.15
    pf=sal*0.10
    it=sal*0.07
elif sal>30000 and sal<=40000:
    hra=sal*0.25
    da=sal*0.20
    pf=sal*0.14
    it=sal*0.10
elif sal>40000 and sal<=50000:
    hra=sal*0.28
    da=sal*0.23
    pf=sal*0.19
    it=sal*0.14
elif sal>50000 and sal<=60000:
    hra=sal*0.32
    da=sal*0.27
    pf=sal*0.22
    it=sal*0.19
elif sal>60000 and sal<=75000:
    hra=sal*0.35
    da=sal*0.30
    pf=sal*0.26
    it=sal*0.20
elif sal>75000:
    hra=sal*0.38
    da=sal*0.32
    pf=sal*0.28
    it=sal*0.26
gross=sal+hra+da
net=gross-pf-it
print("Name:", st)
print("Salary:", sal)
print("HRA:", hra)
print("DA:", da)
print("PF:", pf)
print("IT:", it)
print("Gross Salary:", gross)
print("Net Salary:", net)

