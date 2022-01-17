import pandas as pd
# C:/Users/Marquino/Desktop/Proyectos programación/Bases de Datos/Ejercicio05_intesivoPython.xlsx

fileLocation = input("Indique la ruta de su archivo .xslx para abrirlo:  ")
fileExcel = pd.read_excel(fileLocation)
print(fileExcel)
print("... convirtiendo fichero a CSV ... ")
fileExcel.to_csv('C:/Users/Marquino/Desktop/Proyectos programación/Bases de Datos/Nuevo_CSV.csv')
print("... fichero convertido con éxito ...")
fileCSV = pd.read_csv('C:/Users/Marquino/Desktop/Proyectos programación/Bases de Datos/Nuevo_CSV.csv')
print("... leyendo fichero CSV ... ")
print(fileCSV)