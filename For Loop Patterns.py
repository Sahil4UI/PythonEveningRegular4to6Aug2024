'''
*
**
***
****
*****
'''
'''
for i in range(1,6):
    print("*"*i)
'''
'''
    *
   **
  ***
 ****
*****
'''
'''
for i in range(1,6):
    print(" "*(5-i)+"*"*i)
'''
'''
    *
   * *
  * * *
 * * * *
* * * * *
'''
'''
for i in range(1,6):
    print(" "*(5-i)+"* "*i)
'''
'''
*
**
***
****
*****
'''
'''
for row in range(1,6):
    for col in range(row):
        print("*",end="")
    print()
'''
'''
1
12
123
1234
12345

1
22
333
4444
55555
'''
for row in range(1,6):
    for col in range(row):
        print(row,end="")
    print()


    
        





    
