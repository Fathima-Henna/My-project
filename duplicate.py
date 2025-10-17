#Write a Python program to remove duplicates from a list.

dupli=[8,7,8,6,4,3,2,8,9,7,6,8,6,7,2,4,]
# print(set(dupli))
# print(list(set(dupli)))
num1=[]
for i in dupli:
    if i not in num1 :
        num1.append(i)
print("list:",dupli)
print("List after removing duplicates:",num1)

#userdefined
list1=input("Enter list of values: ")
num2=[]
for i in list1:
    if i not in num2 :
        num2.append(i)
print("list:",list1)
print("List after removing duplicates:",num2)

#user input
n=int(input("Enter number of data:"))
list1=[]
for i in range(n):
    item=input("Enter the values: ")
    if item not in list1:
        list1.append(item)
print(list1)