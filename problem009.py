#Project Euler Problem #009: Special Pythagorean triplet
#There exists exactly one Pythagorean triplet for wich a+b+c=1000, while a^2+b^2=c^2. Find the product a*b*c.

found = False
a = 2
b = 3
c = 4
while found == False:
    while b > a and a != 0:
        while a > 0:
            #print(a,b,c,a+b+c,found)
            if ((a*a)+(b*b) == c*c) and a + b + c == 1000:
                found = True
                #print("done")
                print("a=",a,"b=",b,"c=",c,"a+b+c=",a+b+c,"abc=",a*b*c)
            a = a - 1
        b = b - 1
        a = b - 1



    c = c + 1
    b = c - 1
    a = b - 1
