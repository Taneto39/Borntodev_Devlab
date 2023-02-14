from itertools import cycle


def check_digit(card_number):
    # format number
    card_number = [c for c in card_number if c.isdigit()]
    # calculate
    for i, multiplies in zip(range(len(card_number)), cycle((2, 1))):
        number = str(int(card_number[i]) * multiplies)
        card_number[i] = int(number[0]) + int(number[1]) if len(number) == 2 else int(number)
    if sum(card_number) % 10 == 0:
        return 0
    return 10-(sum(card_number) % 10)


if __name__ == '__main__':
    print(check_digit(input()))
