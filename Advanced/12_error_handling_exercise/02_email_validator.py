"""
You will be given some emails until you receive the command "End". Create the following custom exceptions to
validate the emails:
•	NameTooShortError - raise it when the name in the email is less than or equal to 4 ("peter" will be the name in the
email "peter@gmail.com")
•	MustContainAtSymbolError - raise it when there is no "@" in the email
•	InvalidDomainError - raise it when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org)
When an error is encountered, raise it with an appropriate message:
•	NameTooShortError - "Name must be more than 4 characters"
•	MustContainAtSymbolError - "Email must contain @"
•	InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"
Hint: use the following syntax to add a message to the Exception: MyException("Exception Message")
If the current email is valid, print "Email is valid" and read the next one
"""

from custom_exceptions import NameTooShortError, MustContainAtSymbolError, InvalidDomainError

valid_domains = [".com", ".bg", ".net", ".org"]

while True:
    command = input()
    if command == "End":
        break

    if "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")

    email, domain = command.split("@")
    domain_name, domain_top = domain.split(".")

    if "." + domain_top not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    if len(email) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    print("Email is valid")
