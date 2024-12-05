import re

# Name Regular Expression
name = r"^[A-Z][a-zA-Z'-]+(?: [A-Z][a-zA-Z'-]+)*$"
name_regex = re.compile(name)

# Phone Number Regular Expression
phone_number = r"^(?:\d{10}|\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$"
phone_regex = re.compile(phone_number)

# Email Address Regular Expression
email_address = r"^[a-zA-Z][\w.]*@[a-zA-Z]+\.[a-zA-Z]{2,}$"
email_regex = re.compile(email_address)
