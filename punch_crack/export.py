import csv

def exportDictToCSV(exportFileName: str, fieldName: [str], content):
    with open(exportFileName, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldName)
        writer.writeheader()
        for row in content:
            writer.writerow(row)