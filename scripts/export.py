import csv

def run_export(rows):
    header = ['title', 'location']

    with open('assets/export.csv', 'w', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row_item in rows:
            writer.writerow(row_item)
