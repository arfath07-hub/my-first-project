'''for i in range(6):2

    print(i*"*",end=" ")
    print(i)'''

'''for i in range(1,6):
    print("*",i,end="   ")'''

'''for i in range(5,0,-1):
    print("*"*i)'''

'''n=int(input("enter the number:"))
for i in range(n):
    print(" "*(n-i-1),"* "*(i+1))'''

'''for i in range(5):
    print(i)'''

''''for i in range(5):     #i=0; j=0,1,2,3,4,5    (0,0)(0,1)(0,3)(0,4)
    for j in range(6):
        print(i,j)'''

class student:
  def __init__(self,name,age,sex):
    self.name = name
    self.age = age
    self.sex = sex
s1=student("arfath,",23," ,male")
s2=student("atahar,",20," ,male")
s3=student("azahar,",18," ,male")
print(s1.name,s1.age,s1.sex)
print(s2.name,s2.age,s2.sex)
print(s3.name,s3.age,s3.sex)