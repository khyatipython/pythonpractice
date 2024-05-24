a=int(input("Maths: "))
b=int(input("Guj: "))
c=int(input("Sci: "))
d=int(input("SS: "))
total=a+b+c+d

print("Total marks is: ",total)
per=total/4

print("Persantage is : ",per)

if per>70:
    print("grade is A")
elif per>60:
    print("grade is B")
elif per>50:
    print("garde is c")
elif per>40:
    print("garde is D")
else:
    print("Fail")