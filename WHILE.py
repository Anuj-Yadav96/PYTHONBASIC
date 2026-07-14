# count=1
# while count<=5:
#     print("JAI SHREE RAM")
#     count+=1
# print(count)

#q1 print numbers from 1 to 100
"""
i=1
while i<=100:
    print(i)
    i+=1   """

# q2 print numbers from 100 to 1
"""
i=100
while i>=1:
    print(i)
    i-=1  """

# Q3 Print the multiplication table of a number n.
"""
n=int(input("Enter The Number n:"))
i=1
while  i<=10:
    print(i*n)
    i+=1  """

#Q4 Print the elements of the following list using a loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# lst=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# idx=0
# while idx<=len(lst)-1:
#     print(lst[idx])
#     idx+=1


# Q5 Search for a number x in this tuple using loop:
#(1, 4, 9, 16, 25, 36, 49, 64, 81,100)

nums=(1, 4, 9, 16, 25, 36, 49, 64, 81,100,36)
x=36
i=0
while i<len(nums):
    if(nums[i]==x):
        print("found at idx:",i)
        break
    else :
        print("Finding ")
    i+=1
print("end of loop")







