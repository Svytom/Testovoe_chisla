def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

def find_max_digit_sum():
    max_number = None
    max_sum = -1

    while True:
        try:
            num = int(input("Введите целое число (0 для завершения): "))

            if num == 0:
                break

            current_sum = sum_of_digits(num)

            if current_sum > max_sum:
                max_sum = current_sum
                max_number = num

        except ValueError:
            print("Пожалуйста, введите корректное целое число.")

    if max_number is not None:
        print(f"Число с максимальной суммой цифр: {max_number}")
    else:
        print("Вы не ввели ни одного числа.")

    input("Нажмите Enter для выхода...")

find_max_digit_sum()