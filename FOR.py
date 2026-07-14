#Print the elements of the following list using a loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# nums=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# for val in nums:
#     print(val)

# Search for a number x in this tuple using loop:
#(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
tup=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x=36
idx=0
for val in tup:
    if(val==x):
        print("value found at idx ",idx)
        break
    idx+=1