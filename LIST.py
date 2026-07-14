"""
num=[33,14,45,12]
print(num)
num.append(37)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)  """

# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.


"""
movies = []

movies.append(input("enter first movie: "))
movies.append(input("enter second movie: "))
movies.append(input("enter third movie: "))

print(movies)   """


# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
# [1, 2, 3, 2, 1]   [1,"abc","abc",1]

"""
a=[1,2,3,2,1]
b=a.copy()
b.reverse()
print(b==a)   """


# ["C","D","A","A","B","B","A"]
# Store the above values in a list & sort them from “A” to “D”

grade=["C","D","A","A","B","B","A"]
grade.sort()
print(grade)