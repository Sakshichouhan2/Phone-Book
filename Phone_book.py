import re 
def Phone_book():
	file = open("contactbook.txt",'r')
	num=file.read()
	file.close()
	dictionary = {}
	x = num.split("\n")
	NameList = []
	PhoneList= []
	asset = []
	if num !='':
		for i in x :
			if (i!= '') : 
				y = i.split(" : ")
				dictionary[y[0]] = y[1]
				NameList.append(y[0])
				PhoneList.append(y[1])

		for i in sorted(NameList):
			 asset.append(i)
	else: 
		print("No Records Found")
		print("Let's Create your first record")


	Choice = input("Press 1. Show All Contact\nPress 2. Add New Contact\nPress 3. Update Exisiting Contact\nPress 4. Delete Contact\nPress 5. Search a contact\n")
	try:
		if Choice == "1":
			for i in range(1, len(asset)+1):
				print("{}. {} : {}".format(i,asset[i-1],dictionary[asset[i-1]]))
			#Call = input("Do you Want To Continue Y or Exit: ")
                
		elif Choice == "2":
			Name = input("Enter a  Name :")
			if re.match(r'^[aA-zZ\s]+$', Name):
				print("This is a valid name",Name)
			else:
				print("Its an Invalid name",Name) 

			Phone_Number = input("Enter a 10 digit Number :")
			if re.match(r'^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$', Phone_Number):
				print("This is a valid Number",Phone_Number)
			else:
				print("This is  not a valid Number")

			file = open("contactbook.txt",'a')
			file.write("{} : {}".format(Name,Phone_Number))
			file.write("\n")
			file.close()
			#Call = input("Do you Want To Continue Y or Exit: ")
		elif Choice =="3":
			user_choice = input("Enter Name :")
			if user_choice in asset :
				file = open("contactbook.txt","w")
				print("{} : {}".format(user_choice,dictionary[user_choice]))
				contact_choice = input("Enter New Contact Number :")
				dictionary[user_choice]=contact_choice
				print("Record Updated Successfully")
				file = open("contactbook.txt","w")
				for i in dictionary :
					file.write("{} : {}".format(i,dictionary[i]))
					file.write("\n")
				file.close()

			else : 
				print("Record Not Found")
			#Call = input("Do you Want To Continue Y or Exit: ")
			
		elif Choice =="4":
			Name = input("Enter Name Delete Contact: ")
			if Name in dictionary:
				dictionary.pop(Name)	
				print("Record Deleted Successfully")
				file = open("contactbook.txt","w")
				for i in dictionary :
					file.write("{} : {}".format(i,dictionary[i]))
					file.write("\n")
				file.close()
			else:
				print(Name ,"Record Not Found")
			#Call = input("Do you Want To Continue Y or Exit: ")
			
		elif Choice == "5":
			user_choice = input("Enter Name or Number you wish to search : ")
			if user_choice in dictionary:
				print("{} : {}".format(user_choice,dictionary[user_choice]))
			elif user_choice in dictionary.values():
				print("{} : {}".format(dictionary.index(user_choice),user_choice))
			else : 
				print("Record Not Found")

		else: 
			print("Invalid Choice")
			#Call = input("Do you Want To Continue Y or Exit: ")
		#Call = input("Do you Want To Continue Y or Exit: ")
	except SyntaxError:
		print("Invalid Syntax ")
	except NameError:
		print("Name is not def anywhere ")
	except FileNotFoundError:
		print("This File is not found in your Directory ")
	except SystemError:
		print("interpreter detects internal error")

def call_book():
	Call = input("Do you Want To Continue Y or N:\n ")
	while True:
		if Call == 'Y' or Call == 'y':
			Phone_book()
			call_book()
		elif Call == 'N' or Call == 'n':
			exit()
		else : 
			print("Invalid Choice")
			call_book()


Phone_book()
call_book()


	
