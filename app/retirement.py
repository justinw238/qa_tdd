class Retirement():

	def retirement(self, age, salary, saving, goal):

		try:
			age = int(age)
			salary = int(salary)
			saving = int(saving)
			goal = int(goal)

		except ValueError:
			raise ValueError("Invalid Input")

		if (age < 0 or age >= 100):
			raise ValueError("Invalid Age")

		if (salary < 0):
			raise ValueError("Invalid Salary")

		if (saving < 0 or saving > 100):
			raise ValueError("Invalid Saving")

		if (saving < 0):
			raise ValueError("Invalid Goal")

		total = 0
		while age < 100:
			total += (salary * (saving / 100))
			if total >= goal:
				print(age)
				return age
			age+=1

		return 101
