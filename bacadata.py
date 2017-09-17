import csv
import sys

dream = open('SalesJan2009.csv', 'rU')
try:
    reader = csv.reader(dream)
    for row in reader:
        print row
finally:
    dream.close()
