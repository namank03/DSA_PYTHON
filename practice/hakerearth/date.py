from datetime import datetime

date = "11022012"


def date_palindrome(date):
    formated_date = datetime(date)
    print(f'formated_date -> {formated_date}')


date_palindrome(date)
