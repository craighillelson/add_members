"""Functions."""

import pyinputplus as pyip


def open_csv_populate_lst(file_name):
    """Open a csv and populate a dictionary."""
    import csv
    from collections import namedtuple

    lst = []

    with open(file_name) as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            row = Row(*r)
            lst.append(row.email)

    return lst


def get_domain(lst1, lst2):
    """Extract the domain from an email address."""
    lst1 = lst2[0]
    return lst1.split('@')[1]


def print_return():
    """Print return."""
    print('\n')


def prompt_user_for_domain(a):
    """
    After extracting the domain from an email address, prompt the user to
    add more email addresses for that domain or another.
    """
    while True:
        print(f'\nIs {a} your domain (yes or no)?')
        answer = pyip.inputYesNo('> ')
        if answer != 'yes':
            a = input('What is your domain name?\n> ')
            break
        else:
            break

    return a


def prompt_user_for_prefix(a, b):
    """Prompt user for email prefixes."""
    lst = []
    while True:
        print('Enter the employee\'s name (or enter nothing to stop.):')
        email_prefix = input('> ')
        email = email_prefix + '@' + a
        if email not in b:
            if email_prefix == '':
                break
            lst = lst + [email]
        else:
            print(f'{email} is already in the list')

    return lst


def concat_lists(lst1, lst2):
    """Concatenate lists."""
    return lst1 + lst2


def write_lst_to_csv(file, LST, HEADER):
    """Write list to csv."""
    import csv

    with open(file, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(HEADER)
        for i in LST:
            out_csv.writerow([i])

        print_return()
        print(f'"{file}" exported successfully')

    print_return()
