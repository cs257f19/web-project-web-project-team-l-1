class FizzBuzz:
	def divisibleBy3(self, num):
		return num % 3 == 0

	def divisibleBy5(self, num):
		return num % 5 == 0

	def divisibleBy15(self, num):
		return (num % 3 == 0) and (num % 5 == 0)

	def isNegative(self, num):
		return num < 0

	def isInteger(self, num):
		return isinstance(num, int)

	def play(self, num):
		if self.isNegative(num):
			return "invalid"

		result = ""

		if self.divisibleBy3(num):
			result = result + "fizz"
		if self.divisibleBy5(num):
			result = result + "buzz"

		if result == "":
			result = str(num)

		return result
