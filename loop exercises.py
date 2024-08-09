#find the sum of first 10 natural nos
# triple quotes are known as multi line comment
'''
res = 0
for i in range(1,11):
    res += i
print(res)
'''

#find the sum of digits of number 153->1+5+3=>9
'''
x = 123
res = 0
for i in range(len(str(x))):
    rem = x%10
    res+=rem
    x = x//10
print(res)
'''

#find the reverse of no-> 123 - 321
'''
x = 123
res = 0
for i in range(len(str(x))):
    rem = x%10
    res=res*10+rem
    x = x//10
print(res)
'''

#break and continue
#break - break statement is used to transfer the control flow of program outside the loop
'''
for i in range(1,11):
    if i>5:
        break
    print(i)
'''
#continue - it is used to transfer the control flow of program to the starting of the loop
'''
for i in range(1,11):
    if i%2==0:
        continue
        #skip
    print(i)
'''
'''
#Check whether a no is prime or not?
x = int(input("Enter a no:"))
for i in range(2,x):
    if x%i==0:
        print("Not Prime")
        break
else:
    print("Prime")
'''
'''
x=int(input("enter a no:"))
for i in range(5,x):
    if x%i==0:
        print("not prime")
        break
    else:
        print("prime")
'''
#nested Loop
'''
for i in range(1,4):
    for j in range(1,4):
        print(i,j)
'''
'''
for i in range(1,4):
    for j in range(0,i):
        print(i,j)
'''
#Pattern Program
'''
*
**
***
****
*****
******
'''
for i in range(1,7):
    print("*"*i)







