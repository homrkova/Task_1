while True:
    num = input()
    if num.isdigit():
        num = int(num)
        break
    else:
        print('Была введена строка, а не число.\nВведите число.')
count = 0
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

