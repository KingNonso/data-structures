"""Formatting Customer Names
Suppose that you are building a Customer Relationship Management (CRM) system,
and you want to display a user record in the following format: 'John Smith (California)'.
However, if you don't have a location in your system, you want just to see 'John Smith.'"""

def format_customer(fn, ln, location=None):
    locale = " (" + location + ")" if location is not None else ""
    r = fn + ' '+ ln + locale
    return r


if __name__ == "__main__":
    print(format_customer(fn, ln, location=None))
