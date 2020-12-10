"""Functions."""

from collections import namedtuple
import csv
import pyinputplus as pyip


def open_csv_populate_lst(file_name):
    """Open a csv and populate a list."""

    lst = []

    with open(file_name) as csv_file:
        f_csv = csv.reader(csv_file)
        headings = next(f_csv)
        member_row = namedtuple('Row', headings)
        for email in f_csv:
            row = member_row(*email)
            lst.append(row.email)

    return lst


def get_domain(lst2):
    """Extract the domain from an email address."""

    lst1 = lst2[0]
    return lst1.split('@')[1]


def prompt_user_for_domain(domain):
    """
    After extracting the domain from an email address, prompt the user to
    add more email addresses for that domain or another.
    """

    while True:
        print(f'\nIs {domain} your domain (yes or no)?')
        answer = pyip.inputYesNo('> ')
        if answer != 'yes':
            domain = input('What is your domain name?\n> ')
        else:
            break

    return domain


def prompt_user_for_prefix(domain, lst2):
    """Prompt user for email prefixes."""

    lst1 = []
    while True:
        print('Enter the employee\'s name (or enter nothing to stop.):')
        email_prefix = input('> ')
        email = email_prefix + '@' + domain
        if email not in lst2:
            if email_prefix == '':
                break
            lst1 = lst1 + [email]
        else:
            print(f'{email} is already in the list')

    return lst1


def concat_lists(lst1, lst2):
    """Concatenate lists."""

    return lst1 + lst2


def write_lst_to_csv(file, lst, header):
    """Write list to csv."""

    with open(file, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(header)
        for i in lst:
            out_csv.writerow([i])

        print(f'\n"{file}" exported successfull\n')
