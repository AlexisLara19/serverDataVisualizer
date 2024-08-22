import os
import datetime
#Casos para cada elemento:
def et01fcn(serial,datos=''):
    print("EN FUNCION ET01")
    pathET01='ENSAMBLE1.txt'
    data=datos[0:49] #8 Torques 5 digitos + 1 guion bajo x 8 = 48 +1 guion bajo = 49
    count=data.count("_")
    lista = []
    key = None
    if(count==7 and data[5]=='_' and data[-6]=='_'):
        saveWorkStation1(serial,data)

        datetime_value = datetime.datetime.now()  # Esto es solo un ejemplo, podrías tener tu propio valor datetime
        # Formatear datetime_value como una cadena en el formato 'YYYY-MM-DD HH:MM:SS'
        datetime_string = datetime_value.strftime('%Y-%m-%d %H:%M:%S')
        lista = [data, datetime_string, '1']
        key = 'ET01'

    else:

        saveError(f'{serial}_{data}')

    return key, lista
def et02fcn(serial,datos=''):
    data = datos
    docs={
        "1": 'ENSAMBLE2sec1.txt',
        "2": 'ENSAMBLE2sec2.txt',
        "3": 'ENSAMBLE2sec3.txt'
    }
    secuencias = {
        "1":181, #30 Torques 5 digitos + 1 guion bajo x 30 = 180 +1 guion bajo = 181
        "2":115, #19 Torques 5 digitos + 1 guion bajo x19= 114+1=115
        "3":67 #11 torques 5 digitos +1 guion bajo x11=66+1=67
    }
    try:
        finalstr=secuencias[datos[0]]
        fdata=data[2:finalstr]

        datetime_value = datetime.datetime.now()  # Esto es solo un ejemplo, podrías tener tu propio valor datetime
        # Formatear datetime_value como una cadena en el formato 'YYYY-MM-DD HH:MM:SS'
        datetime_string = datetime_value.strftime('%Y-%m-%d %H:%M:%S')
        lista = []
        key = None
        #Verificar el formato de inicio y cierre de cadena
        if fdata[5]=='_' and fdata[-6]=='_':
            if datos[0]=='1':
                saveWorkStation2a(serial,fdata)
                lista = [fdata,datetime_string,'1']
                key = 'ET02'
            elif datos[0]=='2':
                saveWorkStation2b(serial,fdata[:59],fdata[60:])
                lista = [fdata[:59], fdata[60:],datetime_string,'1']
                key = 'ET02a'
            elif datos[0]=='3':
                saveWorkStation2c(serial,fdata[:47],fdata[48:])
                lista = [fdata[:47], fdata[48:],datetime_string,'1']
                key = 'ET02b'
        else:
            saveError(f'{serial}_{data}')

        return key, lista
    except:
        saveError(f'{serial}_{data}')
def et03fcn(serial,datos=''):
    pathET03 = 'ENSAMBLE3.txt'
    data =datos
    try:
        et1stx=data.index('ET01') #0
        et1fnl=data.index('_') #22
        et3stx=data.index('ET02') #23
        et3fnl = data.index('_',et3stx)  #45

        lenet1 = et1fnl - et1stx
        lenet2 = et3fnl - et3stx

        datos = data[et3fnl + 1:et3fnl + 114] #114 caracteres - el ultimo guion bajo
        lista = []
        key = None

        #Verificacion de cadena (falta agregar los guiones bajos del inicio y final de datos):
        if lenet1 == 22 and lenet2 == 22 and datos[5]=='_' and datos[-6]=='_':
            ET01=data[et1stx:et1fnl]
            ET02=data[et3stx:et3fnl]
            saveWorkStation3(serial,ET01,ET02,datos)
            datetime_value = datetime.datetime.now()  # Esto es solo un ejemplo, podrías tener tu propio valor datetime
            # Formatear datetime_value como una cadena en el formato 'YYYY-MM-DD HH:MM:SS'
            datetime_string = datetime_value.strftime('%Y-%m-%d %H:%M:%S')
            lista = [ET01, ET02, datos, datetime_string, '1']
            key = 'ET03'
        else:
            saveError(f'{serial}_{data}')
        return key, lista

    except :
        saveError(f'{serial}_{data}')




    #Verificar la longitud de los datos restantes
def et04fcn(serial,datos=''):

    pathET04 = 'ENSAMBLE3.txt'
    data = datos[0:71] #12 Torques 5 digitos + 1 guion bajo x 12 = 72 +1 guion bajo = 73
    count = data.count("_") #Deben de tener 11 separadores
    separadorstrx=data[5]
    separadorfnl=data[-6]
    lista = []
    key = None
    if count==11 and separadorstrx=='_' and separadorfnl=="_":
        print(f'Ensamble en la mesa 4: {serial} , datos: {data}')
        fstring = f'{serial} - {data}'
        saveWorkStation4(serial,data)
        datetime_value = datetime.datetime.now()  # Esto es solo un ejemplo, podrías tener tu propio valor datetime
        # Formatear datetime_value como una cadena en el formato 'YYYY-MM-DD HH:MM:SS'
        datetime_string = datetime_value.strftime('%Y-%m-%d %H:%M:%S')
        lista = [data, datetime_string, '1']
        key = 'ET04'

    else:
        saveError(f'{serial}_{data}')
    return key, lista
def et05fcn(serial,datos=''):
    pathET05a = 'ENSAMBLE5a.txt'
    pathET05b = 'ENSAMBLE5b.txt'
    data=datos
    #print(f'Ensamble en la mesa 5: {serial}, secuencia {data[0]}, datos: {datos}')
    secuencia = data[0]
    lista =[]
    key = None
    if secuencia=='1':
        #print(f'Ensamble en la mesa 5: {serial}, secuencia {data[0]}, datos: {datos}')

        #Comprobar que existe modelo en la posicion

        modelstrx= data.index('_') #1
        modelfnl=data.index('_',modelstrx+1) #9
        model=data[modelstrx+1:modelfnl-1]
        key = None
        #Comprobar que existe ET03 en la posicion
        try:
            et3strx= data.index("ET03") #10
            et3fnl=data.index("_",et3strx+1) #32
            #print(f'ET03: {data[et3strx :et3fnl-1]} , {et3strx},{et3fnl}')
            partial=data[et3strx :et3fnl]

            et4strx = data.index("ET04")  # 33
            et4fnl = data.index("_", et4strx + 1)  # 55
            #print(f'ET04: {data[et4strx:et4fnl - 1]} , {et4strx},{et4fnl}')
            condenser=data[et4strx:et4fnl]

            electriData=data[et4fnl+1::]

            splitdata=electriData.split('_',22)
            noMesa =splitdata[0]
            #print(f'Split data: {splitdata}' )
            splitdata[20]=splitdata[20][:3]
            electricTest='_'.join(splitdata[1:21])
            saveWorkStation5a(serial,noMesa,partial,condenser,model,electricTest)
            datetime_value = datetime.datetime.now()  # Esto es solo un ejemplo, podrías tener tu propio valor datetime
            # Formatear datetime_value como una cadena en el formato 'YYYY-MM-DD HH:MM:SS'
            datetime_string = datetime_value.strftime('%Y-%m-%d %H:%M:%S')
            lista = [model, partial, condenser, noMesa,electricTest, datetime_string ,'1']
            key = 'ET051'

        except:
            saveError(f'{serial}_{data}')

        #Datos de prueba electrica 82 caracteres
    elif secuencia=='2':
        #print(f'Ensamble en la mesa 5: {serial}, secuencia {data[0]}, datos: {datos}')
        try:
            datafnl=datos.index('@') #CHG03 -219/220/224    CHG01 -230
            dataf=datos[:datafnl]
            countdata=dataf.count('_')
            datasplit=dataf.split('_')


            frame=datasplit[-1]
            torques='_'.join(datasplit[1:-1])

            saveWorkStation5b(serial,torques,frame)
            datetime_value = datetime.datetime.now()  # Esto es solo un ejemplo, podrías tener tu propio valor datetime
            # Formatear datetime_value como una cadena en el formato 'YYYY-MM-DD HH:MM:SS'
            datetime_string = datetime_value.strftime('%Y-%m-%d %H:%M:%S')
            lista = [torques, datetime_string, '1', frame ]
            key = 'ET052'
        except:
            saveError(f'{serial}_{data}')

    return key, lista
casos={
    "ET01":et01fcn,
    "ET02":et02fcn,
    "ET03":et03fcn,
    "ET04":et04fcn,
    "ET05":et05fcn
}
def saveData(line=''):
    try:

        strSN = line.index('ET0')
        endSN = line.index('_', strSN + 1)
        serial = line[strSN:endSN]
        lista = []
        key = None
        #print(f'Serial encontrado: {serial}')
        # Encontrar el resto de datos en la cadena
        if len(serial) == 22:
            datox = line[endSN + 1::].replace('\\x00', "")
            for substring, funcion in casos.items():
                if substring in serial:
                    key, lista = funcion(serial, datox)
                    lista.insert(0,serial)
                    break  # Detener la búsqueda después de ejecutar la primera función encontrada

        else:
            print("Serial fuera formato")
            saveError(line)

        return key, lista

    except Exception as e:
        print("No se pudo registrar")
        saveError(line)
        print(f'error: {e}')
        """
        for substring, funcion in casos.items():
            if substring in serial:
                funcion(serial, datos)
                break  # Detener la búsqueda después de ejecutar la primera función encontrada
        else:
            print("Ningún substring encontrado")
        """
def saveError(line=''):
    print("Error cadena fuera de formato:")
    print(line)




def saveWorkStation1(SN='',DATA=''):
    print(f'Registro agregado: {SN}')
    print(f'DATA: {DATA}')
def saveWorkStation2a(SN='',DATA=''):
    print(f'Registro agregado: {SN}')
    print(f'DATA: {DATA}')
def saveWorkStation2b(SN='',DATA1a3='',DATA5a6=''):
    print(f'Registro parcial agregado en A : {SN}')
    print(f'DATA 1-3: {DATA1a3}')
    print(f'DATA:5-6 {DATA5a6}')
def saveWorkStation2c(SN='',DATA4='',DATA7=''):
    print(f'Registro parcial agregado en B : {SN}')
    print(f'DATA 4 : {DATA4}')
    print(f'DATA 7 : {DATA7}')
def saveWorkStation3(SN='',ET01='',ET02='',DATA=''):
    print(f'Registro agregado: {SN}')
    print(f'Partes:{ET01} {ET02}')
    print(f'DATA: {DATA}')
def saveWorkStation4(SN='',DATA=''):
    print(f'Registro agregado: {SN}')
    print(f'DATA: {DATA}')
def saveWorkStation5a(SN='',MESA='',ET03='',ET04='',MODEL='',EDATA=''):
    print(f'REGISTRO AGREGADO: {SN} MODELO: {MODEL} MESA {MESA}')
    print(f'Piezas: {ET03} {ET04}')
    print(f'DATA: {EDATA}')
def saveWorkStation5b(SN='',DATA='',FRAME=''):
    print(f'REGISTRO AGREGADO: {SN}')
    print(f'DATA: {DATA}')
    print(f'FRAME: {FRAME}')