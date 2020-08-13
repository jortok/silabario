import csv
from tqdm import tqdm

with open('Top80-silabas.csv', newline='', encoding='latin-1') as f:
    reader = csv.reader(f)
    silabas = list(reader)

#print(silabas[0][10])

with open('silabario.txt','w') as f:
    for silaba1 in tqdm(silabas[0]):
        f.write(silaba1+"\n")
        for silaba2 in silabas[0]:
            f.write(silaba1+silaba2+"\n")
