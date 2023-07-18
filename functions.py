# 1 Задание
def triangle():

    a = 3; b = 5; c = 3
    message = "null"

    if (a + b > c) and (a + c > b) and (b + c > a):
        if a == b == c:
            message = "Треугольник равносторонний"
            print(message)
        elif a == b or a == c or b == c:
            message = "Треугольник равнобедренный"
            print(message)
        else:
            message = "Треугольник разносторонний"
            print(message)

    else:
        message = "Треугольника с такими сторонами не существует"
        print(message)

# 2 Задание
def is_simple_number():

    number = 100; lower_bound = 1; upper_border = 100000
    message = "null"

    if lower_bound < number < upper_border:
        count = 0
        number_of_natural_divisors = 2

        for i in range(lower_bound, number):
            if number % i == 0:
                count += 1
                if count > number_of_natural_divisors:
                    message = f"число {number} является составным"
                    print(message)
                    break
        if count < number_of_natural_divisors:
            message = f"число {number} является простым"
            print(message)


    else:
        message = f"Число {number} не попадает в интервал: от {lower_bound} до {upper_border}"
        print(message)

