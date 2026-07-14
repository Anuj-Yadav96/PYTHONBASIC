"""
dict={
    "name": "ANUJ",
    "course": "b.tech",
    "branch": "CSE"
}
print(dict["course"])
print(type(dict))  """

# Store following word meanings in a python dictionary :
"""table : “a piece of furniture”,“list of facts & figures”
cat : “a small animal” """

"""
dictionary={
    "table":["a piece of furniture","list a facts and figures"],
    "cat":"a small animal"

}
print(dictionary)  """


#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
#an empty dictionary & add one by one. Use subject name as key & marks as value.

marks={}

x=int(input("enter physics marks="))
marks.update({"physics":x})

y=int(input("enter maths marks="))
marks.update({"maths":y})

z=int(input("enter chemistry marks="))
marks.update({"chemistry":z})

print(marks)