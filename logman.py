import sys
import os
import threading
class logManager():
    def __init__(self):
        self.pathSource = "Log/"
        #pathSource = "E:/respaldo_21_05_25/Log"
        #pathSource = "E:/respaldo300424"
        self.pathDestiny = 'dataSplitByET/'
        self.documentList = 'dataSplitByET/documentList.txt'

    # Get a Log documents and dump information in documents divide by workstation prefix (ET01,ET02,ET03,...)
    def divideRegisters_full(self):

        # Delete all old documents before create new ones
        for fileDestiny in os.listdir(self.pathDestiny):
            # Create full address string
            delete_full_address = os.path.join(self.pathDestiny, fileDestiny)
            if os.path.isfile(delete_full_address):
                os.remove(delete_full_address)

        # Create a list of documents in source path
        doclist = []
        for fileSource in os.listdir(self.pathSource):
            # Create full address string
            registers_full_address = os.path.join(self.pathSource,fileSource)
            # No python files
            if os.path.isfile(registers_full_address) and ('.py' not in registers_full_address):
                doclist.append(registers_full_address)

        # Save the documents list in file
        with open(self.documentList,'w') as docsFile:
            for line in doclist:
                docsFile.write(f'{line}\n')

        # Dump docList info in new files divide by workstation
        try:
            # Go through the list
            for fileRegister in doclist:
                # Get information by file
                with open(fileRegister) as file :
                    lines = file.readlines()
                    # Read all lines and classify them by workstation prefix
                    for line in lines:
                        if 'ET01' in line[:15]:
                            with open('dataSplitByET/ET01.txt', 'a') as workstationFile:
                                workstationFile.write(line)
                        elif 'ET02' in line[:15]:
                            with open('dataSplitByET/ET02.txt', 'a') as workstationFile:
                                workstationFile.write(line)
                        elif 'ET03' in line[:15]:
                            with open('dataSplitByET/ET03.txt', 'a') as workstationFile:
                                workstationFile.write(line)
                        elif 'ET04' in line[:15]:
                            with open('dataSplitByET/ET04.txt', 'a') as workstationFile:
                                workstationFile.write(line)
                        elif 'ET05' in line[:15]:
                            with open('dataSplitByET/ET05.txt', 'a') as workstationFile:
                                workstationFile.write(line)
                        else:
                            with open('dataSplitByET/noMatch.txt', 'a') as workstationFile:
                                workstationFile.write(line)

        except:
            print("Error while dump information")

        # Open ET02 doc and take indentifier 2 lines (secuence 2 part 1), save on ET02c.txt
        # Open ET02 doc and take indentifier 3 lines (secuence 2 part 2), save on ET02d.txt
        with open('dataSplitByET/ET02.txt', 'r') as file:
            for line in file:
                indexET = line.index('ET0')
                indexFn = line.index('_', indexET)
                if line[indexFn + 1:indexFn + 2] == '2': # Check index to secuence 2 part 1
                    with open('dataSplitByET/ET02c.txt', 'a') as destiny:
                        destiny.write(f'{line[indexET:indexFn]}\n')
                if line[indexFn + 1:indexFn + 2] == '3': # Check index to secuence 2 part 2
                    with open('dataSplitByET/ET02d.txt', 'a') as destiny:
                        destiny.write(f'{line[indexET:indexFn]}\n')

        # Secuence 2 ET02 - full assemblies found
        # Open ET02c.txt and check line by line if the serial number exist in ET02d.txt
        # If exist add '_c' next to serial number to indicate the assemblie is complete
        with open('dataSplitByET/ET02c.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                with open('dataSplitByET/ET02d.txt', 'r') as file2:
                    for data in file2:
                        if line == data:
                            line = line.rstrip('\n') + '_c\n'
                            break
                file.write(line)

        # Create a file with ET05 part 2 recived
        with open('dataSplitByET/ET05.txt', 'r') as file:
            for line in file:
                indexET = line.index('ET0')
                indexFn = line.index('_', indexET)
                if (line[indexFn + 1:indexFn + 2] == '2') and (indexFn - indexET == 22):
                    with open('dataSplitByET/ET05sec2.txt', 'a') as destiny:
                        destiny.write(f'{line[indexET:indexFn]}\n')

        # Divide final station document (ET05) by model
        sourceFileET05 = 'dataSplitByET/ET05.txt'
        assemblyList = []

        #Create a list with Model 1 - 6114360
        with open(sourceFileET05,'r') as fileET05:
            lines = fileET05.readlines()
            for i,line in enumerate(lines,1):
                #Find serial number into string
                strSN = line.index('ET0')
                endSN = line.index('_',strSN + 1)
                serial = line[strSN:endSN]
                secuencia = line[endSN + 1:endSN + 2]

                # Verify datalenght and if data belongs to first seccition
                if len (serial) == 22 and secuencia == '1':
                    endModel = line.index('_', endSN + 3)
                    modelo = line[endSN + 3:endModel]
                    endcondenser = line.index('_', endModel + 1)
                    endconditioner = line.index('_', endcondenser + 1)
                    conditioner = line[endModel + 1:endcondenser]
                    condenser = line[endcondenser + 1:endconditioner]
                    modelcomp = '6114360'

                    # Add complete strings serial numbers to list
                    if len(condenser) == 22 and len(conditioner) == 22 and modelo == modelcomp:
                        # print(f' {i} Serial encontrado: {serial} Modelo {modelo} Condenser:{condenser} Conditioner: {conditioner}')
                        data = f'{serial}_{condenser}_{conditioner}'

                        assemblyList.append(data)

        # Save list Model 1 with components
        with open('dataSplitByET/ET05_m1.txt','w') as file:
            for assembly in assemblyList:
                file.write(f'{assembly}\n')

        assemblyList.clear()
        # Create a list with Model 2 - 6164288
        with open(sourceFileET05, 'r') as fileET05:
            lines = fileET05.readlines()
            for i, line in enumerate(lines, 1):
                # Find serial number into string
                strSN = line.index('ET0')
                endSN = line.index('_', strSN + 1)
                serial = line[strSN:endSN]
                secuencia = line[endSN + 1:endSN + 2]

                # Verify datalenght and if data belongs to first seccition
                if len(serial) == 22 and secuencia == '1':
                    endModel = line.index('_', endSN + 3)
                    modelo = line[endSN + 3:endModel]
                    endcondenser = line.index('_', endModel + 1)
                    endconditioner = line.index('_', endcondenser + 1)
                    conditioner = line[endModel + 1:endcondenser]
                    condenser = line[endcondenser + 1:endconditioner]
                    modelcomp = '6164288'

                    # Add complete strings serial numbers to list
                    if len(condenser) == 22 and len(conditioner) == 22 and modelo == modelcomp:
                        # print(f' {i} Serial encontrado: {serial} Modelo {modelo} Condenser:{condenser} Conditioner: {conditioner}')
                        data = f'{serial}_{condenser}_{conditioner}'

                        assemblyList.append(data)

        # Save list Model 2 with components
        with open('dataSplitByET/ET05_m2.txt', 'w') as file:
            for assembly in assemblyList:
                file.write(f'{assembly}\n')

        # Find components ET02 and ET01 of ET03 assemblies
        # Create ET03pv.txt
        with open('dataSplitByET/ET03.txt','r') as file:
            for linea in file:
                try:
                    # Take ET03 index in the line (start and end)
                    indexET3 = linea.index('ET03')
                    indexFn3 = linea.index('_', indexET3)
                    m_et03 = linea[indexET3:indexFn3]
                    statuset02 = 'i'
                    statuset01 = 'i'
                    # Check correct length
                    if (indexFn3-indexET3) == 22:
                        m_et02 = None
                        m_et01 = None

                        # Take ET02 index in the line (start and end)
                        try:
                            indexET2 = linea.index('ET02')
                            indexFn2 = linea.index('_', indexET2)
                            m_et02 = linea[indexET2:indexFn2]
                            # Check if the serial number has 22 chars or if it have the same number just next to it

                        except Exception as e:
                            #No existe ET02
                            pass

                        # Take ET01 index in the line (start and end)
                        try:
                            indexET1 = linea.index('ET01')
                            indexFn1 = linea.index('_', indexET1)
                            m_et01 = linea[indexET1:indexFn1]
                        except Exception as e:
                            #No existe ET01
                            print(e)

                        # Looking for ET01 taked in ET01.txt
                        # if find, ET01 -> statuset01 = 'e'
                        if m_et01:
                            #Abre el documento ET01
                            with open('dataSplitByET/ET01.txt','r') as fileET01:
                                for lineaEt01 in fileET01:
                                    if m_et01 in lineaEt01:
                                        statuset01 = 'e'
                                        break

                        # Looking for ET02 taked in ET02.txt or
                        # if find, ET02 -> statuset02 = 'e'
                        if m_et02:

                            #print(f'Search for {m_et02}')

                            # Looking for it in fisrt document
                            # Status is OK when m_et02 is found in document and secuence is '1'
                            with open('dataSplitByET/ET02.txt','r') as fileET02:
                                m_et02_sec = f'{m_et02}_1' #Add secuence 1 to pattern
                                for lineaEt02 in fileET02:
                                    if m_et02_sec in lineaEt02:
                                        statuset02 = 'e'
                                        break
                            # Looking for it in second document
                            # Status is Ok when m_et02 is found in document and there is a 'c' next to serial number
                            if statuset02 == 'i':
                                with open('dataSplitByET/ET02c.txt', 'r') as fileET02c:
                                    m_et02_status = f'{m_et02}_c' #Add complete identifier to pattern
                                    for lineaEt02c in fileET02c:
                                        if m_et02_status in lineaEt02c:
                                            statuset02 = 'e'
                                            break
                        #print(f'{m_et03}_{m_et02}_{m_et01}_{statuset02}_{statuset01}')

                        # Add to ET03pv.txt
                        # ET03000566040324125924_ET01000624040324082142_ET02000572020324133743_e_e
                        with open('dataSplitByET/ET03pv.txt','a') as fileET03:
                            fileET03.write(f'{m_et03}_{m_et02}_{m_et01}_{statuset02}_{statuset01}\n')

                except Exception as e:
                    print(e)

        # Create table structures files and save in ET05_m1full.txt and ET05_m2full.txt
        # ET05000624040324082142_ET04000624040324082142_ET03000566040324125924_ET02000572020324133743_ET01000624040324082142_e_e_e_e_e
        with open('dataSplitByET/ET05_m1.txt', 'r') as file:
            for linea in file:
                try:
                    # Search for ET03
                    indexET3 = linea.index('ET03')
                    # Get ET03 serial number
                    m_et03 = linea[indexET3:-1]

                    # Initialize strings
                    m_components = f'{None}_{None}'
                    m_status12 = f'i_i'
                    m_status3 = 'i'

                    # Get ET04 serial number
                    indexET4 = linea.index('ET04')
                    indexFn4 = linea.index('_', indexET4)
                    m_et04 = linea[indexET4:indexFn4]
                    m_status4 = 'i'

                    # Get ET05 serial number
                    indexET5 = linea.index('ET05')
                    indexFn5 = linea.index('_', indexET5)
                    m_et05 = linea[indexET5:indexFn5]
                    m_status5 = 'i'

                    # Search for ET03, ET02 and ET01
                    with open('dataSplitByET/ET03pv.txt', 'r') as fileET03:
                        for lineaET03 in fileET03:
                            if m_et03 in lineaET03:
                                m_components = lineaET03[23:-5] # Get ET01 and ET02 Serial Numbers
                                m_status12 = lineaET03[-4:-1]   # Get ET01 and ET02 status
                                m_status3 = 'e'                 # Set ET03 status
                                break

                    # Search for ET04
                    with open('dataSplitByET/ET04.txt', 'r') as fileET04:
                        for lineaET04 in fileET04:
                            if m_et04 in lineaET04:
                                m_status4 = 'e' #Set ET04 status
                                break

                    # Search for ET05 part 2
                    with open('dataSplitByET/ET05sec2.txt', 'r') as fileET05:
                        for lineaET05 in fileET05:
                            if m_et05 in lineaET05:
                                m_status5 = 'e'   # Set ET05 status
                                break

                    # Save components and status on table
                    with open('dataSplitByET/ET05_m1full.txt', 'a') as fileET05full:
                        fileET05full.write(
                            f'{linea[:-1]}_{m_components}_{m_status5}_{m_status4}_{m_status3}_{m_status12}\n')

                    # print(f'{linea[:-1]}_{m_components}_{m_status5}_{m_status4}_{m_status3}_{m_status12}')

                except Exception as e:
                    print(e)

        # Create table structures files and save in ET05_m2full.txt and ET05_m2full.txt
        # ET05000624040324082142_ET04000624040324082142_ET03000566040324125924_ET02000572020324133743_ET01000624040324082142_e_e_e_e_e
        with open('dataSplitByET/ET05_m2.txt', 'r') as file:
            for linea in file:
                try:
                    # Search for ET03
                    indexET3 = linea.index('ET03')
                    # Get ET03 serial number
                    m_et03 = linea[indexET3:-1]

                    # Initialize strings
                    m_components = f'{None}_{None}'
                    m_status12 = f'i_i'
                    m_status3 = 'i'

                    # Get ET04 serial number
                    indexET4 = linea.index('ET04')
                    indexFn4 = linea.index('_', indexET4)
                    m_et04 = linea[indexET4:indexFn4]
                    m_status4 = 'i'

                    # Get ET05 serial number
                    indexET5 = linea.index('ET05')
                    indexFn5 = linea.index('_', indexET5)
                    m_et05 = linea[indexET5:indexFn5]
                    m_status5 = 'i'

                    # Search for ET03, ET02 and ET01
                    with open('dataSplitByET/ET03pv.txt', 'r') as fileET03:
                        for lineaET03 in fileET03:
                            if m_et03 in lineaET03:
                                m_components = lineaET03[23:-5] # Get ET01 and ET02 Serial Numbers
                                m_status12 = lineaET03[-4:-1]   # Get ET01 and ET02 status
                                m_status3 = 'e'                 # Set ET03 status
                                break

                    # Search for ET04
                    with open('dataSplitByET/ET04.txt', 'r') as fileET04:
                        for lineaET04 in fileET04:
                            if m_et04 in lineaET04:
                                m_status4 = 'e' #Set ET04 status
                                break

                    # Search for ET05 part 2
                    with open('dataSplitByET/ET05sec2.txt', 'r') as fileET05:
                        for lineaET05 in fileET05:
                            if m_et05 in lineaET05:
                                m_status5 = 'e'   # Set ET05 status
                                break

                    # Save components and status on table
                    with open('dataSplitByET/ET05_m2full.txt', 'a') as fileET05full:
                        fileET05full.write(
                            f'{linea[:-1]}_{m_components}_{m_status5}_{m_status4}_{m_status3}_{m_status12}\n')

                    # print(f'{linea[:-1]}_{m_components}_{m_status5}_{m_status4}_{m_status3}_{m_status12}')

                except Exception as e:
                    print(e)

        print('All registers in files')

    # Get all registers by model on table format
    def getRegister(self,model=1):
        result_list=[]
        doc='dataSplitByET/ET05_m1full.txt'
        if model==2:
            doc = 'dataSplitByET/ET05_m2full.txt'

        with open(doc, 'r') as file:
            for linea in file:

                indexET5 = linea.index('ET05')
                indexFn5 = linea.index('_', indexET5)
                m_et05 = linea[indexET5:indexFn5]
                serial = int(m_et05[4:10])

                indexET4 = linea.index('ET04')
                indexFn4 = linea.index('_', indexET4)
                m_et04 = linea[indexET4:indexFn4]

                indexET3 = linea.index('ET03')
                indexFn3 = linea.index('_', indexET3)
                m_et03 = linea[indexET3:indexFn3]

                indexET2 = indexFn3 + 1
                indexFn2 = linea.index('_', indexET2)
                m_et02 = linea[indexET2:indexFn2]

                indexET1 = indexFn2 + 1
                indexFn1 = linea.index('_', indexET1)
                m_et01 = linea[indexET1:indexFn1]

                status = linea[indexFn1+1:-1]

                dictionary = {'consecutivo': serial, 'serialnumber': m_et05, 'serialnumber_04': m_et04, 'serialnumber_03': m_et03,
                        'serialnumber_02': m_et02, 'serialnumber_01': m_et01, 'encontrado05': status[0], 'encontrado04': status[2],
                        'encontrado03': status[4], 'encontrado02': status[6], 'encontrado01': status[8]}
                result_list.append(dictionary)
        return result_list

    # Get specific workstation element information
    def getElement(self,sn,column):
        cadena = 'NO DISPONIBLE'

        # ET05 - Final Assembly
        if column == 1:

            # Searching for Part 1
            with open('dataSplitByET/ET05.txt', 'r') as file:
                for fila in file:
                    if sn in fila:
                        # Serial Number
                        indexET = fila.index("ET0")
                        index_ = fila.index('_', indexET)
                        if fila[index_ + 1] == '1':
                            serialnumber = fila[indexET:index_]

                            # Get Model
                            indexmodel = fila.index("_", index_ + 3)
                            noserie = fila[index_ + 3:indexmodel]  # Model

                            # Get ET03
                            indexET3 = fila.index("ET03")
                            # Get ET04
                            indexET4 = fila.index("ET04")
                            indexET4_ = fila.index("_", indexET4)

                            # Get electric test data and workstation number
                            electriData = fila[indexET4_ + 1::]  # Get the rest of string
                            splitdata = electriData.split('_', 22)   # Split by '_'
                            noMesa = splitdata[0]  # First data is workstation number
                            splitdata[20] = splitdata[20][:3]  # Modify the last number to 3 digits number
                            electricTest = '_'.join(splitdata[1:21])  # Join the electric test data

                            # Part 1
                            cadena = f'{serialnumber}\n{noMesa}\n{noserie}\n{fila[indexET3:indexET4 - 1]}\n{fila[indexET4:indexET4_]}\n' \
                                     f'{electricTest}'

                            break

            # Searching for Part 2
            with open('dataSplitByET/ET05.txt', 'r') as file:
                for fila in file:
                    if sn in fila:
                        indexET = fila.index("ET0")
                        index_ = fila.index('_', indexET)
                        if fila[index_ + 1] == '2':  # Part 2
                            try:
                                indexa = fila.index("@")  # Key character
                                #indexframe = indexa - 18

                                dataf = fila[index_ + 3:indexa]
                                datasplit = dataf.split('_')
                                frame = datasplit[-1]
                                torques = '_'.join(datasplit[1:-1])


                                previa = cadena
                                #cadena = f'{previa}\n{fila[indexframe - 1:indexa]}\n{fila[index_ + 3:indexframe - 2]}'
                                cadena = f'{previa}\n{frame}\n{torques}'

                            except:

                                previa = cadena
                                datos = fila[index_ + 3:232]
                                cadena = f'{previa}\nNO FRAME\n{datos}'
                            break

        # ET04 - Condenser
        if column == 2:
            with open('dataSplitByET/ET04.txt', 'r') as file:
                for fila in file:
                    if sn in fila:
                        indexET = fila.index("ET0")
                        index_ = fila.index('_', indexET)
                        serialnumber = fila[indexET:index_]
                        data = fila[index_ + 1:index_ + 72]
                        cadena = f'{serialnumber}\n{data}'
                        break

        # ET03 - Conditioner
        if column == 3:
            with open('dataSplitByET/ET03.txt', 'r') as file:
                for fila in file:
                    if sn in fila:
                        indexET = fila.index("ET0")
                        index_ = fila.index('_', indexET)
                        serialnumber = fila[indexET:index_]

                        ET1 = fila.index("ET01")
                        ET1_ = fila.index("_", ET1)
                        ET01 = fila[ET1:ET1 + 22]

                        ET2 = fila.index("ET02")
                        ET2_ = fila.index("_", ET2)
                        ET02 = fila[ET2:ET2 + 22]

                        data = fila[ET2_ + 1:ET2_ + 114]

                        cadena = f'{serialnumber}\n{ET01}\n{ET02}\n{data}'
                        break

        # ET02 - Partial
        if column == 4:
            buscar3 = False
            with open('dataSplitByET/ET02.txt', 'r') as file:
                for fila in file:
                    if sn in fila:
                        ET2 = fila.index('ET02')
                        ET2_ = fila.index('_', ET2)
                        serialnumber = fila[ET2:ET2_]
                        if (len(serialnumber) == 22):
                            sec = fila[ET2_ + 1]
                            if sec == '1':
                                data = fila[ET2_ + 3: ET2_ + 182]
                                cadena = f'{serialnumber}\n{data}'

                            elif sec == '2':
                                data = fila[ET2_ + 3: ET2_ + 116]

                                cadena = f'{serialnumber}\n{data}'
                                buscar3 = True
                            break
            if buscar3:
                with open('dataSplitByET/ET02.txt', 'r') as file:
                    for fila in file:
                        if sn in fila:
                            ET2 = fila.index('ET02')
                            ET2_ = fila.index('_', ET2)
                            if fila[ET2_ + 1] == '3':
                                data = fila[ET2_ + 3: ET2_ + 68]
                                previa = cadena


                                #d1_3 = cadena[23:59+23]
                                d1_3 = cadena[0:59 + 23]
                                d5_6 = cadena[59+24 :]
                                d7 = data[-17:]
                                d4 = data[:-18]


                                cadena = f'{d1_3}_{d4}_{d5_6}_{d7}'

                                break

        # ET01 - Valve
        if column == 5:
            with open('dataSplitByET/ET01.txt', 'r') as file:
                for fila in file:
                    if sn in fila:
                        indexET = fila.index("ET0")
                        index_ = fila.index('_', indexET)
                        serialnumber = fila[indexET:index_]
                        data = fila[index_ + 1:index_ + 48]
                        cadena = f'{serialnumber}\n{data}'
                        break
        return cadena

    def updateAllRegisters(self):
        hilo = threading.Thread(target=self.divideRegisters_full)
        hilo.start()

if __name__ == "__main__":
    logManager = logManager()
    #logManager.divideRegisters_full()
    logManager.updateAllRegisters()
    print('esperando que acabe el hilo')

