input_numbers = input("Введи числа, разделенные пробелом: ")
square = lambda x: x ** 2
numbers = list(map(int, input_numbers.split()))
squared_numbers = list(map(square, numbers))
squared_numbers_string = list(map(str, squared_numbers))
output = '. '.join(squared_numbers_string)
print("Квадраты этих чисел:", output)
