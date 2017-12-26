import csv

"""************csv.DictReader*************"""

with open('names.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         print(row['first_name'], row['last_name'])


"""*************csv.DictWriter***************"""

with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader() #Writing fields as header

    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

"""************csv.reader***************"""

with open('some.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row

import csv
with open('passwd', 'rb') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in reader:
        print row

#A slightly more advanced use of the reader — catching and reporting errors:

import csv, sys
filename = 'some.csv'
with open(filename, 'rb') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            print row
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

#And while the module doesn’t directly support parsing strings, it can easily be done:

import csv
for row in csv.reader(['one,two,three']):
    print row

"""The corresponding simplest possible writing example is:"""

import csv
with open('some.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(someiterable)

