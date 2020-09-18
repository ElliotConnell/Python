

#import the csv module

import csv

with open('test.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in reader:
		print(', '.join(row))


row == ['Activity Calories', '2,513 C']:



	for row in reader:
		string = str(row)
		if 'Distance' in string:
			total_distance = int(i) for i in string.split() if i.isdigit():
			distance_km = int(total_distance)
			target_distance = round((distance_km * 1.1), 0)

			print(total_distance)
			print(target_distance)

