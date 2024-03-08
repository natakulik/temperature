import convertor
import csv

with open('data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        if(row[0] == 'Date'): pass
        print(f'Mesurment date: {row[0]}')
        print(f'Mesurment distance: {row[1]} and {convertor.metersOrFeet(row[1])}')
        print(f'Mesurment temperature: {row[2]} and {convertor.farenheitOrCelcious(row[2])}')
