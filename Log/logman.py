import sys
import os

class logManager():
    def __init__(self):
        print("Inicializando el manager")
        pathSource = "Log/"
        pathDestiny = 'dataSplitByET/'

        # Crear lista de archivos disponibles en la carpera
        doclist = []
        for archivo in os.listdir(pathSource):
            ruta_completa = os.path.join(pathSource, archivo)
            if os.path.isfile(ruta_completa) and ('.py' not in ruta_completa):
                doclist.append(ruta_completa)

        print(f'{len(doclist)} documentos encontrados')
        # Eliminar los anteriores
        for archivo in os.listdir(pathDestiny):
            ruta_completa = os.path.join(pathDestiny, archivo)
            if os.path.isfile(ruta_completa):
                os.remove(ruta_completa)
        # Abrir todos los archivos y vaciar los registros en el documento de la mesa correspondiente
        try:
            for archivo in doclist:
                with open(archivo, 'r') as file:
                    lineas = file.readlines()  # Lee todas las líneas del archivo en una lista
                    for line in lineas:

                        if 'ET01' in line[:15]:
                            with open('dataSplitByET/ET01.txt', 'a') as archivo_destino:
                                archivo_destino.write(line)
                        elif 'ET02' in line[:15]:
                            with open('dataSplitByET/ET02.txt', 'a') as archivo_destino:
                                archivo_destino.write(line)
                        elif 'ET03' in line[:15]:
                            with open('dataSplitByET/ET03.txt', 'a') as archivo_destino:
                                archivo_destino.write(line)
                        elif 'ET04' in line[:15]:
                            with open('dataSplitByET/ET04.txt', 'a') as archivo_destino:
                                archivo_destino.write(line)
                        elif 'ET05' in line[:15]:
                            with open('dataSplitByET/ET05.txt', 'a') as archivo_destino:
                                archivo_destino.write(line)
        except:
            print("ERROR")

        print(f'Separados por estacion')
        #self.registrosCompletos(1,0)
    def registrosCompletos(self,model):
        #Tomar todos los registros de ET05 que contengan el _1_ despues del numero de serie
        pathDestiny = 'dataSplitByET/ET05.txt'
        #Abrir el documento:
        datalist=[]
        with open(pathDestiny, 'r') as file:
            lineas = file.readlines()
            for i,linea in enumerate(lineas,1):
                #Tomar el numero serial
                strSN = linea.index('ET0')
                endSN = linea.index('_', strSN + 1)
                serial = linea[strSN:endSN]
                secuencia=linea[endSN+1:endSN+2]
                if len(serial)==22 and secuencia == '1':
                    endModel=linea.index('_', endSN + 3)
                    modelo= linea[endSN+3:endModel]
                    endcondenser=linea.index('_', endModel + 1)
                    endconditioner=linea.index('_', endcondenser + 1)
                    conditioner=linea[endModel+1:endcondenser]
                    condenser=linea[endcondenser+1:endconditioner]
                    modelocomp=''
                    if model==0:
                        modelocomp='6114360'
                    else:
                        modelocomp = '6164288'
                    if len(condenser)==22 and len(conditioner)==22 and modelo==modelocomp:
                        #print(f' {i} Serial encontrado: {serial} Modelo {modelo} Condenser:{condenser} Conditioner: {conditioner}')
                        data=f'{serial}_{condenser}_{conditioner}'
                        datalist.append(data)
        return datalist
        #print(datalist)