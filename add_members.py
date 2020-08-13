"""
Open a csv and populate a dictionary with its contents. Prompt the user to
add members.
"""

from functions import (open_csv_populate_lst,
                       get_domain,
                       prompt_user_for_domain,
                       prompt_user_for_prefix,
                       concat_lists,
                       write_lst_to_csv)

employees = open_csv_populate_lst('employees.csv')
domain = get_domain(employees)
domain_confirmed = prompt_user_for_domain(domain)
employees_to_add = prompt_user_for_prefix(domain, employees)
all_employees = concat_lists(employees, employees_to_add)
write_lst_to_csv('employees.csv', all_employees, ['email'])
