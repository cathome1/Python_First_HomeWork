#  Напишите программу, которая по заданному номеру четверти, показывает диапазон 
#  возможных координат точек в этой четверти (x и y).
quarter = int(input('Введите номер четверти : '))
if (quarter == 1):
    print("x - любое число от 0 до бесконечности(положительное);\ny - любое число от 0 до бесконечности(положительное)")
elif (quarter == 2):
    print("x - любое число от 0 до минус бесконечности(отрицательное);\ny - любое число от 0 до бесконечности(положительное)")
elif (quarter == 3):
    print("x - любое число от 0 до минус бесконечности (отрицательное);\ny - любое число от 0 до минус бесконечности(отрицательное)")
elif (quarter == 4):
    print("x - любое число от 0 до бесконечности (положительное);\ny - любое число от 0 до минус бесконечности(отрицательное)")
else:
    print("Всего 4 четвертей")