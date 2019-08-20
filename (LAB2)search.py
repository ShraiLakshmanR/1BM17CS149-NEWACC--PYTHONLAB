def searchele(list1,i):
	print(list1)
	if i in list1:
		return True
	else:
		return False



list=[]
while True:
	a=int(input("\nEnter number to be inserted\n"))
	if a!=-1:
		list.append(a)
	else:
		break

b=int(input("\nEnter element to be searched\n"))
print("")
ans=searchele(list,b)

if(ans):
	print("\nElement is present\n")
else:
	print("Element not found\n")
