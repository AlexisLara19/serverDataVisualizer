import xlwings as xw

nombre_archivo_excel = "Template_Reporte_Individual_2024.xlsx"

def funcionexcel(diccionario):

    libro = xw.Book(nombre_archivo_excel)
    hoja = libro.sheets.active

    serial = diccionario.get('Serial', 'NO ENCONTRADO')
    hoja.cells(6, 4).value = serial
    mesa = diccionario.get('Mesa', 'NO ENCONTRADO')
    hoja.cells(6, 6).value = mesa
    hora = diccionario.get('Hora', 'NO ENCONTRADO')
    hoja.cells(6, 10).value = hora

    Condenser = diccionario.get('Condenser', 'NO ENCONTRADO')
    Conditioner = diccionario.get('Condtioner', 'NO ENCONTRADO')
    Partial = diccionario.get('Partial', 'NO ENCONTRADO')
    Valve = diccionario.get('Valve', 'NO ENCONTRADO')

    Et04 = f'CONDENSER {Condenser}'
    Et03 = f'CONDITIONER GP {Conditioner}'
    Et02 = f'PARTIAL CONDITIONER {Partial}'
    Et01 = f'VALVE GP {Valve}'

    hoja.cells(30, 1).value = Et04
    hoja.cells(23, 1).value = Et03
    hoja.cells(16, 1).value = Et02
    hoja.cells(9, 1).value = Et01

    date = diccionario.get('Date', 'NO ENCONTRADO')
    hoja.cells(6, 7).value = date
    print(f'fecha: {date}')

    table = 'ET01'
    resultado = diccionario.get(table, 'NO ENCONTRADO')
    partes = resultado.split('_')
    fila_inicial = 14
    columna_inicial = 1
    #print(partes)
    for i, valor in enumerate(partes):
        hoja.cells(fila_inicial, columna_inicial + i).value = valor

    table = 'ET02'
    resultado = diccionario.get(table, 'NO ENCONTRADO')
    partes = resultado.split('_')
    fila_inicial = 21
    columna_inicial = 1
    #print(partes)
    for i, valor in enumerate(partes):
        hoja.cells(fila_inicial, columna_inicial + i).value = valor

    table = 'ET03'
    resultado = diccionario.get(table, 'NO ENCONTRADO')
    partes = resultado.split('_')
    fila_inicial = 28
    columna_inicial = 1
    #print(partes)
    for i, valor in enumerate(partes):
        hoja.cells(fila_inicial, columna_inicial + i).value = valor

    table = 'ET04'
    resultado = diccionario.get(table, 'NO ENCONTRADO')
    partes = resultado.split('_')
    fila_inicial = 35
    columna_inicial = 1
    #print(partes)
    for i, valor in enumerate(partes):
        hoja.cells(fila_inicial, columna_inicial + i).value = valor

    table = 'ET05a'
    resultado = diccionario.get(table, 'NO ENCONTRADO')

    partes = resultado.split('_')

    leaktest = partes[0]
    f1Frec_b = partes[1]
    f1Curr_b = partes[2]
    f1Frec_a = partes[3]
    f1Curr_a = partes[4]

    f2Frec_b = partes[5]
    f2Curr_b = partes[6]
    f2Frec_a = partes[7]
    f2Curr_a = partes[8]

    blFrec_b = partes[9]
    blCurr_b = partes[10]
    blFrec_a = partes[11]
    blCurr_a = partes[12]

    valvClose = partes[14]
    valvOpen = partes[16]

    tempsens = partes[17]

    suction = partes[18]
    discharge = partes[19]

    newarray = (f'{leaktest}_{f1Curr_b}_{f1Frec_b}_{f2Curr_b}_{f2Frec_b}_{f1Curr_a}_{f1Frec_a}_{f2Curr_a}_{f2Frec_a}'
                f'_{blCurr_b}_{blFrec_b}_{blCurr_a}_{blFrec_a}_{valvClose}_{valvOpen}_{suction}_{discharge}_{tempsens}')
    partes = newarray.split('_')
    fila_inicial = 52
    columna_inicial = 1
    #print(partes)
    if partes[0] == '1':
        hoja.cells(fila_inicial, columna_inicial).value = "aprobado"
        hoja.cells(fila_inicial, columna_inicial + 1).value = "aprobado"

        columna_inicial += 2

        for i, valor in enumerate(partes[1:], start=columna_inicial):
            hoja.cells(fila_inicial, i).value = valor

    elif partes[0] == '0':
        hoja.cells(fila_inicial, columna_inicial).value = "rechazado"
        hoja.cells(fila_inicial, columna_inicial + 1).value = "rechazado"

        columna_inicial += 2

        for i, valor in enumerate(partes[1:], start=columna_inicial):
            hoja.cells(fila_inicial, i).value = valor
    else:
        for i, valor in enumerate(partes):
            hoja.cells(fila_inicial, columna_inicial + i).value = valor

    table = 'ET05b'
    resultado = diccionario.get(table, 'NO ENCONTRADO')
    partes = resultado.split('_')
    fila_inicial = 42
    columna_inicial = 1
    #print(partes)
    for i, valor in enumerate(partes):
        hoja.cells(fila_inicial, columna_inicial + i).value = valor

    table = 'Fr'
    resultado = diccionario.get(table, 'NO ENCONTRADO')
    fila_inicial = 45
    columna_inicial = 1
    print('FINAL')
    hoja.cells(fila_inicial, columna_inicial).value = resultado

    libro.save('Nuevo_reporte.xlsx')
    libro.close()
