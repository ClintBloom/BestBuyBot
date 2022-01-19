import json
import os

info_file = {
    'First Name': 'Type in between the Apostrophes',
    'Last Name': '',
    'Login Email': '',
    'Login Pass': '',
    'Address': '',
    'ZipCode': '',
    'City': '',

    'Card Number': '',
    'Card Expire Month': '',
    'Card Expire Year': '',
    'Card CVV 3 Digits': '',
}


# Old way of creating files
# def check_files(text_file):
#     if os.path.exists(text_file):
#         filename = open(text_file, 'r').read()
#         print('{} Exists!'.format(text_file))
#     else:
#         filename = open(text_file, 'w')
#         print('{} Created!'.format(text_file))
#         print('End program and edit {} before continuing'.format(text_file))
#     return filename


# Updated way of creating one file for entire user input
def check_files_2():
    if os.path.exists('account.txt'):
        filename = open('account.txt', 'r').read()
        print('{} Exists!, Ensure you have edited this file!'.format('account.txt'))
        filename = json.loads(filename)
    else:
        filename = open('account.txt', 'w')
        print('{} has been created!'.format('account.txt'))
        json.dump(info_file, filename, indent=1)
        print('Exit program and edit {} before continuing'.format('account.txt'))
    return filename


class Account:
    def __init__(self):
        # Login
        self.account = 'login_email.txt'
        self.password = 'login_pass.txt'
        # Name
        self.name = 'first_name.txt'
        self.last = 'last_name.txt'
        # Address
        self.address = 'address.txt'
        self.zip = 'zipcode.txt'
        self.city = 'city.txt'
        # Card
        self.card = 'card_number.txt'
        self.cvv = 'card_cvvcode.txt'
        self.expire = '2_digit_expire_month.txt'
        self.year = '4_digit_expire_year.txt'
        self.platform = (
            self.account,
            self.password,
            self.name,
            self.last,
            self.address,
            self.zip,
            self.city,
            self.card,
            self.cvv,
            self.expire,
            self.year
        )

    def checking_files(self):
        for i in self.platform:
            check_files(i)
