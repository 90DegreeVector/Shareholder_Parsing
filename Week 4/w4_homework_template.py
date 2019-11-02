import re
from w4_bank_accounts import account_info as ai


def print_invalid_line(desc, dict_line):
    """
    This method will prepend 'Invalid' to desc and print it out <25 chars.
    It will also display the dict_line directly after.

    :param str desc: The keyword that failed
    :param dict dict_line: The line that failed validation.
    :return: None
    """

    print("Invalid {:<15}{}".format(desc, dict_line))


# Loop through each element (dict) in the list of account information.
for line in ai:

    # Check that the balance is only a valid number
    found = re.match(r'FILL IN REGEX HERE', line['balance'])
    if not found:
        print_invalid_line("Balance", line)

    # Check that it is a valid first name (within reason)
    found = re.match(r'FILL IN REGEX HERE', line['firstname'], re.I)
    if not found:
        print_invalid_line("Firstname", line)

    # Check that it is a valid last name (within reason)
    found = re.match(r'FILL IN REGEX HERE', line['lastname'], re.I)
    if not found:
        print_invalid_line("Lastname", line)

    # Check that it is a valid age
    found = re.match(r'FILL IN REGEX HERE', line['age'])
    if not found:
        print_invalid_line("Age", line)

    # Check that it is a valid email address
    found = re.match(r'FILL IN REGEX HERE', line['email'])
    if not found:
        print_invalid_line("Email", line)

    # Check that it is a valid State abbreviation.
    found = re.match(r'FILL IN REGEX HERE', line['state'])
    if not found:
        print_invalid_line("State", line)
