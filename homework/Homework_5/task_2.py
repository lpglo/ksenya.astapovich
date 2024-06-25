
result1 = "результат операции: 42"
result2 = "результат операции: 514"
result3 = "результат работы программы: 9"


def process_result(result):
    colon_index = result.index(":")

    number_str = result[colon_index + 2:]

    number = int(number_str)

    new_number = number + 10

    print(new_number)


process_result(result1)
process_result(result2)
process_result(result3)