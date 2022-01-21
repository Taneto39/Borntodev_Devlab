prime_list = [2, 3]
number = 3
while True:
    number += 1
    for i in prime_list:
        if number % i == 0:
            break
    else:
        prime_list.append(number)