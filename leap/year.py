#Leap Year exercise by Catalina De la cuesta



def divided_by(number):
	def divides_by(divisor):
		return number%divisor == 0
	return divides_by

def is_leap_year(year):
	divides_by = divided_by(year)
	return divides_by(400) or (divides_by(4) and not divides_by(100))
