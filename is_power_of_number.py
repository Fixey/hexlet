# is input number a natural power of the number.
#method 1 using python function
def is_power_of_number(number, power):
  return (number ** 1/power).is_integer()

#method 2
def is_power_of_number2(number, power):
  remainder = (number ** 1/power) % 1
  return remainder == 0
