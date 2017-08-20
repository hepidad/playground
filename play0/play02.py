import csv
import sys

dream = open('Cars.csv', 'rt')
try:
    reader = csv.reader(dream)
    for row in reader:
        print row
finally:
    dream.close()

    