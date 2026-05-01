name=input("Enter Name:")
cgpa=float(input("Enter CGPA:"))
print("Name :",name)
if cgpa>=9.5:
	print("Grade = O")
elif cgpa>=8.5:
	print("Grade = A")
elif cgpa>=7.5:
	print("Grade = B")
elif cgpa>=6.5:
	print("Grade = C")
else:
	print("Grade = F")