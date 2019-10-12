#!/bin/python3

import os
import datetime

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def time_differences(dates):
    # type: (list[str]) -> (list[str])
    """Take a list of date strings of format "Day dd Mon yyyy hh:mm:ss +xxxx" and
    return the difference between each pair.

    Args:
        dates (list[str]): Dates to be compared.
    """
    # %a: Weekday abbreviation
    # %d: zero padded day of month
    # %b: Month abbreviation
    # %Y: full Year decimal
    # %H: 24-hour hour
    # %M: Zero Padded minute
    # %S: Zero Padded second
    # %z: UTC Offset
    dates = [
        datetime.datetime.strptime(date, "%a %d %b %Y %H:%M:%S %z") for date in dates
    ]

    # Pair dates for easier computation
    date_pairs = [(dates[i], dates[i + 1]) for i in range(0, len(dates), 2)]

    # Subtract dates
    # Timedelta to absolute seconds
    # total_seconds() returns a float so we convert to int
    date_offsets = [int(abs(date[0] - date[1]).total_seconds()) for date in date_pairs]
    return date_offsets


if __name__ == "__main__":
    # Multiply count by 2 because it represents the number of test pairs
    dates_count = int(input().strip()) * 2

    dates = []

    for _ in range(dates_count):
        date = input().strip()
        dates.append(date)

    results = time_differences(dates)

    # Write to file if there is one specified to be written to.
    if os.environ.get("OUTPUT_PATH"):
        with open(os.environ["OUTPUT_PATH"], "w") as fptr:
            fptr.write("\n".join(map(str, results)))
            fptr.write("\n")
    else:
        for result in results:
            print(result)
