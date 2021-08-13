"""
Problem 5
You have several buckets whose sizes are represented by the list sizes. Find the number of different ways to arrange the buckets such that the first bucket’s size is greater than the second bucket’s size.

CONSTRAINTS
sizes is a list of positive integers.

If sizes has fewer than 2 buckets, return 0.

Some buckets may have the same size, but are nevertheless treated as unique buckets.

LIBRARY SUGGESTION
Consider using the itertools module.

EXAMPLES
Input	[10]
Output	0
Explanation	No arrangement is possible.
Input	[1, 2]
Output	1
Explanation	The possible arrangements are (1, 2) and (2, 1). Of these, only (2, 1) has a first bucket that is bigger than the second bucket.
Input	[1, 3, 1]
Output	2
Explanation	Only the arrangements (3, 1, 1) and (3, 1, 1) satisfy the property that the first bucket is bigger than the second bucket.
"""



import datetime
from datetime import date

import pandas


def diff_days(csv_contents: str) -> int:
    dates = csv_contents.split("\n")
    print("dates: ", dates)
    type_cont = 0
    types = dates[0].split(",")
    for i in types:
        if i == 'Date':
            break
        else:
            type_cont +=1
            continue

    date_list = []
    for i in range(1, len(dates)):
        if dates[i] == "":
            continue
        date_list.append(dates[i].split(",")[type_cont])
    if '' in date_list: date_list.remove('')
    print("date_list: ", date_list)

    date_list = [date.replace('-', '/') for date in date_list]
    date_list = sorted(date_list)
    print(date_list)
    
    year1, year2 = date_list[0][:4], date_list[len(date_list)-1][:4]
    month1, month2 = date_list[0][5:7], date_list[len(date_list)-1][5:7]
    day1, day2 = date_list[0][8:], date_list[len(date_list)-1][8:]

    date1 = datetime.date(int(year1), int(month1), int(day1))
    date2 = datetime.date(int(year2), int(month2), int(day2))
    print(abs((date2 - date1).days))
    return abs((date2 - date1).days)


    

# Examples  print(diff_days('Date,Price,Volume\n2014-01-27,550.50,1387\n2014-06-23,910.83,4361\n2014-05-20,604.51,5870'))