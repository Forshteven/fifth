#task1:
my_string = input("Назовите цель своего прибытия? ") #создать строку my_string и присвоить ей значение строки с произвольным текстом с помощью input()
print(int(len(my_string))) #вывести количество символов введённого текста

#task2:
print(my_string.lower()) #вывести в верхнем регистре
print(my_string.upper()) #вывести в нижнем регистре
print(my_string.replace(' ','')) #удалить все пробелы из my_string
print(my_string[0]) #вывести первый символ строки my_string
print(my_string[-1]) #вывести последний символ строки my_string