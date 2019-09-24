class student:

	def __intit__(self):
		self.age=None
		self.marks=None
		self.sid=None

        def check_qualification(self):
             	if validate_age() and validate_marks() and marks>65:
			return True
		else:
			return False

	def set_details(self):
		print("\n-------Admission---------\n")	
		sid=int(input("Enter id\n"))
		marks=int(input("\nEnter marks\n"))
		age=int(input("\nEnter Age\n"))
		if check_qualification():
			return True
		else:
			return False

	def validate_marks(self):
		
		print("\nValidation....\n")
		if self.marks>0 and self.marks<=100:
			return True
		else:
			return False


	def validate_age(self):
		
		print("\nAge validation....\n")
		if self.age>20:
			return True
		else:
			return False


	def put_details(self):
		print("Student id=",self.sid)
		print("\nAge=",self.age)
		print("\nMarks=",self.marks)



s=student()
if s.set_details():
	s.put_details()
	print("Qualified")
else:
	print("Not qualified")
		
