def revl(str1):
    lis1=str1.split(" ")
    lis1.reverse()
    print(lis1)
    a=" "
    s2=a.join(lis1)
    print(s2)
def revstr(str2):
    lis=str2.split(" ")
    lis2=" "
    for i in lis:
        lis2+=i[::-1]
        lis2+=""
    print(lis2)
str3=input("enter string")
revl(str3)
revstr(str3)
