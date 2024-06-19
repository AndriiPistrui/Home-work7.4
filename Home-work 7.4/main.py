def common_elements():

    divisible_by_3 = [i for i in range(100) if i % 3 == 0]

    divisible_by_5 = [i for i in range(100) if i % 5 == 0]

    set_3 = set(divisible_by_3)
    set_5 = set(divisible_by_5)

    common_set = set_3 & set_5

    return common_set

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

print('ОК')

