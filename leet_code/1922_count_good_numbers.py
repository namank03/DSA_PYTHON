
import snoop

el = "02468"
ol = "2357"


# @snoop
def is_good_number(n):
    n = str(n)
    for index, i in enumerate(n):
        if index % 2 == 0 and n[index] not in el:
            return False
        elif index % 2 != 0 and n[index] not in ol:
            return False
    print(n)
    return True


def count_good_numbers(n):
    return sum(is_good_number(val) for val in range(10**(n-1) - 1, 10**n))


print(count_good_numbers(3))
