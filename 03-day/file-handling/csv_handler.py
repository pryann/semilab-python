from csv import reader, writer
from os import chdir, path

chdir(path.join(path.dirname(__file__), 'files'))

def read_csv_file(filepath):
    with open(filepath, 'r') as file:
        reader_iter = reader(file)
        return [row for row in reader_iter]
    
print(read_csv_file('data.csv'))

columns = ['firstname', 'lastname', 'age']
rows = [
    ['John', 'Doe', '33'],
    ['Jane', 'Doe', '10'],
    ['Johnny', 'DoeDoe', '90'],
]

def write_csv(filepath, columns, rows):
    with open(filepath, 'w', newline='' ) as file:
        csv_writer = writer(file, delimiter=';')
        csv_writer.writerow(columns)
        csv_writer.writerows(rows)

write_csv('csv_users_test.csv', columns, rows)