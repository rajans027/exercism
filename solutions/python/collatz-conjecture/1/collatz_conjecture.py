def steps(number):

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    new_list = [number]   

    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1

        new_list.append(number)
        
    return len(new_list) - 1
