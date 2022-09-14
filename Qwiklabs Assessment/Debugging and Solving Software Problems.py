#!/usr/bin/env python3


import csv
import datetime
import requests


FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"


def get_start_date():
"""Interactively get the start date to query for."""


print()
print('Getting the first start date to query for.')
print()
print('The date must be greater than Jan 1st, 2018')
year = int(input('Enter a value for the year: '))
month = int(input('Enter a value for the month: '))
day = int(input('Enter a value for the day: '))
print()


return datetime.datetime(year, month, day)


def get_file_lines(url):
"""Returns the lines contained in the file at the given URL"""


# Download the file over the internet
response = requests.get(url, stream=True)
lines = []


for line in response.iter_lines():
lines.append(line.decode("UTF-8"))
return lines


def prepare_dict():
data = get_file_lines(FILE_URL)
reader = csv.reader(data[1:])


csv_dict={}
for row in reader:
row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
row_list = csv_dict.get(row_date, [])
row_list.append("{} {}".format(row[0], row[1]))
csv_dict[row_date]=row_list
return csv_dict


def list_newer(start_date):
csv_dict = prepare_dict()
while start_date < datetime.datetime.today():
result = csv_dict.get(start_date,0)
if result is not 0:
print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), result))


# Now move the date to the next one
start_date = start_date + datetime.timedelta(days=1)


def main():
start_date = get_start_date()
list_newer(start_date)


if __name__ == "__main__":
main()
