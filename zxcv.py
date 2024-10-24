print('Multiplication Table')
i = 1

number = int(input('Enter a number: '))

for i in range(1, 11):  # Changed to 1-10 for a standard multiplication table
    print(f'{i} x {number} = {i * number}')


