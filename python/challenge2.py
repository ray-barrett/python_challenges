#!/bin/python3

import os
import re

_EMAIL_EXP = "^[\\w-]+@[A-Za-z0-9]+\\.[a-z]{1,3}$"


def is_valid_email(email):
    return re.match(_EMAIL_EXP, email)


def validate_emails(emails):
    """Take a list of email address strings and return the valid emails

    For an email to be consdered valied it must comply with the following rules:
        * It must have the username@domainname.extension format type.
        * The username can only contain letters, digits, dashes and underscores.
        * The website name can only have letters and digits.
        * The maximum length of the extension is 3.

    Args:
        emails (list[str]): Strings which are expected to ba an email address

    Returns:
        list[str]: The emails which are valid
    """

    valid_emails = [email for email in emails if is_valid_email(email)]
    return sorted(valid_emails)


if __name__ == "__main__":
    email_count = int(input().strip())

    emails = []

    for _ in range(email_count):
        email = input().strip()
        emails.append(email)

    results = validate_emails(emails)

    # Write to file if there is one specified to be written to.
    if os.environ.get("OUTPUT_PATH"):
        with open(os.environ["OUTPUT_PATH"], "w") as fptr:
            fptr.write(str(results))
            fptr.write("\n")
    else:
        print(results)
