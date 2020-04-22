"""
Open a csv and populate a dictionary with its contents. Prompt the user to
add members.
"""

import functions

employees = functions.open_csv_populate_lst('employees.csv')
domain = functions.get_domain('email', employees)
domain_confirmed = functions.prompt_user_for_domain(domain)
employees_to_add = functions.prompt_user_for_prefix(domain, employees)
all_employees = functions.concat_lists(employees, employees_to_add)
functions.write_lst_to_csv('employees.csv', all_employees, ['email'])
