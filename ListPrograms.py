#Program to find the largest and smallest from a given list
'''lst=eval(input("Enter the list of numbers: "))
smallest=min(lst)
largest=max(lst)
print("The largest number is ",largest)
print("The smallest number is ",smallest)'''

#Program to find the third largest number
'''lst=eval(input("Enter the list of numbers: "))
l=list(set(lst))
l.sort(reverse=True)
print("The third largest number is ",l[2]) '''

#Program to take a list of integers and creates another list with those numbers in the master list that are less than a number entered by the user
'''lst=eval(input("Enter the list of numbers: "))
num=int(input("Enter the number: "))
new_lst=[]
for i in lst:
    if(i<num):
        new_lst.append(i)
print("The new list is: ",new_lst)'''

#Program to take a list of integers and create another list to store all the even numbers from the master list and print th enew list in ascending order
'''lst=eval(input("Enter the list of numbers: "))
even_lst=[]
for i in lst:
    if(i%2==0):
        even_lst.append(i)
even_lst.sort()
print("The list of even numbers: ",even_lst)'''

#Program to take two list of integers and return a list containing the elements that are common in both the list
l1=eval(input("Enter the first list of numbers: "))
l2=eval(input("Enter the second list of numbers: "))
l3=[]
for i in l1:
    if(i in l2):
        l3.append(i)
print("The list of common elements are: ",l3)
