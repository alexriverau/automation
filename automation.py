import re

with open("assets/potential-contacts.txt", 'r') as f:
    contents = f.read()

# find phone numbers regex
find_phone_nums = re.findall(r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}', contents)

set_phone_nums = set(find_phone_nums)
list_phone_nums = list(set_phone_nums)
list_phone_nums.sort()

phone_nums = ''
for num in list_phone_nums:
    phone_nums += num + ', '

# find emails regex
find_emails = re.findall(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', contents)

set_emails = set(find_emails)
list_emails = list(set_emails)
list_emails.sort()

emails = ''
for email in list_emails:
    emails += email + ', '

# write phone_numbers.txt
with open('assets/phone_numbers.txt', 'w') as f:
    phone_numbers = f.write(phone_nums)

# write emails.txt
with open('assets/emails.txt', 'w') as f:
    emails = f.write(emails)
