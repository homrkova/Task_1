num = input()
count = 0
if num.isdigit():
    if int(num) == 0:
        print(f'{num} - не является натуральным числом')
    elif int(num) > 1:
        for i in range(2, int(num) // 2 + 1):
            if int(num) % i == 0:
                count = count + 1
        if count == 0:
            print(f'{num} - простое число')
        else:
            print(f'{num} - не простое число')
    else:
        print(f'{num} - не простое число')
else:
    print('Некорректный ввод')

