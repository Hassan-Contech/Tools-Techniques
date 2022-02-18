try:
    num = int(input("Enter an integer number: "))
    print("\nInput number is: " + str(num))
except ValueError:
    print("Exception while converting to integer!")	
except Exception as e:
	print("Exception error: " + str(e))
else:
    print("The result is correct if all operations are successful!")
	