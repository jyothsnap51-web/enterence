m=input("Do you have any medical condition? ")
if  m =="Yes":
    print("you are allowed to write the exam")
else:
    a=int(input("Please enter your annual attendence percent : "))
    if a>=75:
        print("you are not allowed to write the exam.")
    else:
        print("you are  allowed to write the exam")