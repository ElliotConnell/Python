#Write a program that prints the next 20 leap years


#import calender library

print("List of next 20 leap years")

import calendar

#set the variables

current = 2020
year = current + 1
count = 0


for i in range(current, ):
		year += 1
		if (calendar.isleap(year)) == True:
			print(year)
			count += 1
		if count == 20:
			break
