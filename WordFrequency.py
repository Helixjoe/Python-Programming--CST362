#Program to find the frquency of a word in a string
s=input("Enter the string: ")
l=s.split()
d={}
for i in l:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)

