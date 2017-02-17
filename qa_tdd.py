from app.distance import Distance

def doChoice(choice):
	pass
	
def main():
	choice = -1
	choice_list = ['0','1','2','3','4','q', 'x']
	while choice != 0:
		while choice not in choice_list:
			print("1: Calculate Body Mass Index")
			print("2: Calculate Retirement")
			print("3: Calculate Distance")
			print("4: Verify Email")
			print("0: Quit")
			choice = input(">> ")
			if choice not in choice_list:
				print("Invalid choice.")
		
		if choice == '4':
			dist = Distance()
			x1 = input("Enter point X1: ")
			x2 = input("Enter point X2: ")
			y1 = input("Enter point Y1: ")
			y2 = input("Enter point Y2: ")
		
			result = dist.distance(x1, x2, y1, y2)
			
			print("Distance is", result)
			print()
			
		choice = -1
if __name__ == '__main__':
	main()
