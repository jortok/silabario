# Palabras en español obtenidas por permitaciones de las 80 sílabas más populares
He creado un script ya que como muchos saben es muy complicado encontrar un buen diccionario (wordlist) de palabras en español para el cracking de passwords. Por lo que tomé las 80 sílabas más populardes del español y en 4 bubles for, se genera un diccionario de  41.4M de filas. Muchas de las palabras formadas realmente son utilizadas en el español. 

## Uso

Solo hay que descargar los archivos y correr el archivo `silabas.py` junto con el CSV de las 80 sílabas más populares del español `Top80-silabas.csv`. Aquí podrías modificar el CSV con más o menos sílabas según lo que desees.

La lista de las sílabas fue obtenida de este blog [https://www.solosequenosenada.com/2015/10/23/frecuencia-de-letras-y-de-silabas-en-espanol/](https://www.solosequenosenada.com/2015/10/23/frecuencia-de-letras-y-de-silabas-en-espanol/). También subí una copia de su análisis en un archivo de MS Excel por si llegara a desaparecer su post `silabas.xlsx`.

## Resultado

Al correr el script en una PC con 8GB de RAM, tardó aproximadamente 5~10 minutos en generar la salida: `silabario.txt` con un total de 41'478,480 líneas un un tamaño de 438MB, por comodidad, lo he comprimido con 7Z Ultra en un archivo de 12.8 MB, bastante cómodo de manipular.

### Notas
Si algún día alguien encuentra una forma de validar cada palabra generada contra su existencia en la RAE. Por favor, hágamelo saber o haga su FORK.
