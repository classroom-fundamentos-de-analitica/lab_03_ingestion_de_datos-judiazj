"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():

    #
    # Inserte su código aquí
    #
    with open("clusters_report.txt", "r") as file:
        lines = file.readlines()

        # Creación de los encabezados
        header1, header2 = [re.sub(r"\s{2,}", "-", line).strip().split("-") for line in lines[:2]]
        header1.pop()
        header2.pop(0)

        # Se añaden al futuro dataframe
        data = {
            header1[0].lower().replace(' ', '_'): [],
            f"{header1[1]} {header2[0]}".lower().replace(' ', '_'): [],
            f"{header1[2]} {header2[1]}".lower().replace(' ', '_'): [],
            header1[3].lower().replace(' ', '_'): [],
        }

        # A partir de que comienzan los datos
        for line in lines[2:]:
            # Se detectan más de dos espacios en blanco, se eliminan y se eliminan
            # los elementos vacíos 
            line = re.sub(r"\s{2,}", ".", line).strip().split(".")
            line = list(filter(lambda x: x, line))

            # Si hay un número, significa que es el comienzo de una nueva fila
            if line and line[0].isnumeric():
                data["cluster"].append(int(line[0]))
                data["cantidad_de_palabras_clave"].append(int(line[1]))
                data["porcentaje_de_palabras_clave"].append(float(line[2][:-2].replace(",", ".")))
                data["principales_palabras_clave"].append(" ".join(line[3:]))
            # De lo contrario, se continúa con las palabras clave de la fila anterior
            elif data["principales_palabras_clave"]:
                line = data["principales_palabras_clave"].pop() + " " + " ".join(line)                
                data["principales_palabras_clave"].append(line.strip())

        df = pd.DataFrame(data)
        return df
