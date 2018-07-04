import csv

file_in = 'lista-duplicada.csv' # arquivo com registros duplicados
file_out = 'output.csv' # arquivo de saída apenas com registros inéditos
with open(file_in, 'r') as fin, open(file_out, 'w') as fout:
    reader = csv.reader(fin)
    writer = csv.writer(fout)
    d = {}
    for row in reader:
        color = row[0]
        if color not in d:
            d[color] = row
            writer.writerow(row)
result = d.values()