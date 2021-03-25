while True:
    num = input()
    if num.isdigit():
        num = int(num)
        break
    else:
        print('Была введена строка, а не число.\nВведите число.')
flag = True
while flag:
    OperatNum = input().split()
    if OperatNum[0] == '+':
        num += int(OperatNum[1])
    elif OperatNum[0] == '*':
        num *= int(OperatNum[1])
    elif OperatNum[0] == '-':
        num -= int(OperatNum[1])
    elif OperatNum[0] == '/' and int(OperatNum[1]) == 0:
        print("Деление на ноль запрещено. \nВведите знак деления '/' через пробел задайте другое число")
    elif OperatNum[0] == '/':
        num /= int(OperatNum[1])
    elif OperatNum[0] == '**':
        num **= int(OperatNum[1])
    elif OperatNum[0] == '=':
        flag = False
        print('Результат:', num)
    else:
        print('Некорректный ввод. \nПропущен пробел или введен недопустимый символ. \nПопробуйте еще раз')
