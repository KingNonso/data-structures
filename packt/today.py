"""

This script prints the current system date.

"""
import datetime

result = 0
# Recall that this loops through 1 to 10, not including 11
for n in range(1, 11):
    result += n

if __name__ == '__main__':
    print(datetime.date.today())
    print(result)
