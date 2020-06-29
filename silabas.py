import csv
from tqdm import tqdm

with open('Top80-silabas.csv', newline='') as f:
    reader = csv.reader(f)
    silabas = list(reader)

#print(silabas[0][10])

with open('silabario.txt','w') as f:
    for silaba1 in tqdm(silabas[0]):
        f.write(silaba1+"\n")
        for silaba2 in silabas[0]:
            f.write(silaba1+silaba2+"\n")
            for silaba3 in silabas[0]:
                f.write(silaba1+silaba2+silaba3+"\n")
                for silaba4 in silabas[0]:
                    f.write(silaba1+silaba2+silaba3+silaba4+"\n")
