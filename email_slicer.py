a=input("Enter a string:\n")
a=a.lower()
print(a)
b=a.index('@')
c=a[:b]
print("Domain name is ", c)
print("ID is ", a[b+1:])
