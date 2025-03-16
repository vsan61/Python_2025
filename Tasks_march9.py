"""Task1:
a=input("Enter a name: ")
middle_char=a[len(a)//2]
print(f"The middle character of the name {a} is {middle_char}")

Task2:
string1=input("Enter a string1: ")
string2=input("Enter a string2: ")
print(string1.strip("*"))
print(string2.strip("*"))

Task3:
string1=input("Enter a string1: ")
string2=input("Enter a string2: ")
string3=input("Enter a string3: ")
a=string1.split(" ")
a_val=a[1]
b=string2.split(" ")
b_val=b[1]
c=string3.split(" ")
c_val=c[1]
final_out=float(a_val) + float(b_val) + float(c_val)
print(final_out)

Task4:
a=input("Enter a string1: ")
b=input("Enter a string2: ")
out=b[0]+a[1:]+a[0]+b[1:]+str(len(a))+str(len(b))+a[len(a)//2]+b[len(b)//2]
print(out)

Task5:
a=input("Enter a string1: ")
b=input("Enter a string2: ")
out=int(ord(a[len(a)//2])) + int(ord(b[len(b)//2]))
print(out)

Task6:
a=input("Enter a string1: ")
len_str=len(a[1:len(a)-1])
out=a[0] + str(len_str) + a[len(a)-1]
print(out)

Task7:
a=input("Enter a input from the user: ")
print(a)

Task8:Swapcase
a=input("Enter a input from the user: ")
print(a.swapcase())

Task9:What's Your Name?
a=input("Enter a string1: ")
b=input("Enter a string2: ")
print(f"Hello {a}{b}! You just delved into python.")

Task10:Mutation
a=input("Enter a input from the user: ")
out=a[:4]+"k"+a[5:]
print(out)"""






