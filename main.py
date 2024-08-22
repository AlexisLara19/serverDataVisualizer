import sys

from PySide6.QtGui import QColor, QBrush
# from ui_files.prueba_estilos import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QStyleFactory, QWidgetItem, QMessageBox, QTableWidgetItem
from PySide6.QtCore import Qt, QThread

from ui_files.ServerApp_MainWindow import Ui_MainWindow  # Clase con el frontend de la aplicacion
from server_r0 import ChatServer  # Clase que maneja la aplicacion como servidor, muestra los eventos ocurridos
from dbCatManager import managerDataBase  # Clase que maneja la conexion con la base de datos

from logman import logManager
import report_fc

import datetime


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(2)
        # self.ui.tabWidget.setTabEnabled(0,False)

        self.ui.msg_edit.clear()
        self.ui.event_list.clear()
        self.ui.client_cb.clear()
        self.ui.msg_edit.close()
        self.ui.sendMsg_bt.close()
        self.ui.sendAll_cb.close()
        self.ui.client_cb.close()
        self.ui.label_8.close()
        self.ui.verticalLayout_12.deleteLater()
        self.ui.pushButton_2.setText("OK")

        # Create and run Server
        self.chatServer = ChatServer('localhost', 4503)
        # Set Callbacks to update events list
        self.chatServer.setNewEvent_fc(self.printCadena)
        self.chatServer.setNewClient_fc(self.updateClients)

        # Run Server at new thread
        self.chat_server_thread = WorkerThread(self.chatServer)
        self.chat_server_thread.start()

        # SQL functions
        self.ui.pushBuscarSQL.clicked.connect(self.searchElements)
        self.sqlDB = managerDataBase()
        if not self.sqlDB.status:
            self.ui.label_info.setText("NO DATABASE CONNECTION TRY AGAIN")
            self.ui.pushBuscarSQL.setEnabled(False)
            self.ui.pb_getDatapz.setEnabled(False)
            self.ui.pb_getReport.setEnabled(False)


        # Unir los mensajes que recibe ChatServer con las funciones de agregacion de managerDataBase.
        self.chatServer.setSendServer_fc(self.addToDB)
        self.chatServer.setToAddToDB_fc(self.sqlDB.addMember)

        # Log Manager
        self.logManager = logManager()
        self.logManager.updateAllRegisters()

        self.ui.pushBuscarEnLogs.clicked.connect(self.getElement)

        # self.ui.comboModelLog.closestr(currBlower)
        self.ui.comboStatusLog.close()
        self.ui.lineEditDesdeLog.close()
        self.ui.lineEditHastaLog.close()
        self.ui.label.close()
        self.ui.label_2.close()
        self.ui.checkBoxLog.close()
        self.ui.labelStatus.close()
        self.ui.pushBuscarLog.setText("Actualizar")
        self.ui.pushBuscarLog.clicked.connect(self.updateModel)

        self.ui.add2DataBase.clicked.connect(self.addToDataBase)
        self.ui.labelDataView.clear()
        self.ui.pb_getDatapz.clicked.connect(self.getFromDB)
        self.ui.pb_getReport.clicked.connect(self.getReport)


    # Muestra en el event list la actividad del server
    def printCadena(self, cadena):
        self.ui.event_list.addItem(cadena)
        self.ui.event_list.scrollToBottom()
        self.ui.event_list.setCurrentRow(self.ui.event_list.count() - 1)

    # Agrega clientes al checkbox NO SE USA
    def updateClients(self, status, addr):
        if status:
            self.ui.client_cb.addItem(addr)
        else:
            elements = self.ui.client_cb.count()
            for element in range(0, elements):
                if addr in self.ui.client_cb.itemText(element):
                    self.ui.client_cb.removeItem(element)
                    self.ui.client_cb.setCurrentIndex(0)

    # Callback para llamar a la funcion addToDB desde otra clase
    def addToDB(self, tupla_valores, mesa_str):
        try:
            self.sqlDB.addMember(tupla_valores, mesa_str)
        except Exception as e:
            print(e)

    # Llamado a getMemberInfo para visualizar la informacion de la base de datos en el recuadro de labelDataSql
    def getFromDB(self):

        # Obtener el arreglo de elementos seleccionados
        elementos = self.ui.dataTableSQL.selectedItems()

        # Obtener el primer elemento
        cadena_label = None
        element = elementos[0]
        register = 'NO DISPONIBLE'

        color = None
        columna = 0

        # Obtener el contenido y el color (estatus) del elemento seleccionado
        try:
            # register = self.ui.dataTableLog.currentItem().text()
            # color = self.ui.dataTableLog.currentItem().background()
            # columna = self.ui.dataTableLog.currentItem().column()
            register = element.text()
            color = element.background()
            columna = element.column()
        except:
            register = 'NO DISPONIBLE'

        verde = QBrush(QColor(144, 238, 144))

        # Si el estatus es ok ( si el color es verde ) se obtienen los datos via MySQL y se pasan a labelDataSql para mostrar
        cadena = ''
        if color == verde:
            # Si le pertenece a la estacion 05
            if register[3] == '5':
                lista = self.sqlDB.getMemberInfo('ET051', register)
                fecha = lista.pop(-1)
                cadena1 = '\n'.join(lista)
                lista2 = self.sqlDB.getMemberInfo('ET052', register)
                cadena2 = '\n'.join(lista2)
                cadena = f'{cadena1}\n{cadena2}\n{fecha}'

            #Si le pertenece a cualquiera de las otras estaciones de sub ensamble
            else:
                lista = self.sqlDB.getMemberInfo(register[0:4], register)
                cadena = '\n'.join(lista)

        else:
            cadena = 'NO DISPONIBLE'

        # Se asigna el valor de cadena con los datos a labelDataSql
        cadena_label = cadena
        self.ui.labelDataSql.setText(cadena_label)


    def getReport(self):

        # elementos = self.ui.dataTableSQL.selectedItems()
        try:
            columnas = self.ui.dataTableSQL.selectedRanges()[0].columnCount()
            filas = self.ui.dataTableSQL.selectedRanges()[0].rowCount()
            elementos = self.ui.dataTableSQL.selectedItems()

            if columnas == 6:
                # Generar reporte individual
                if filas == 1:
                    flag_complete = 0
                    rojo = QBrush(QColor(255, 99, 71))
                    componentDic = {}
                    for index, elemento in enumerate(elementos):
                        color = elemento.background()

                        if color == rojo:
                            flag_complete = 1
                            break

                        if index == 1:
                            lista = self.sqlDB.getMemberInfo('ET051', elemento.text())

                            mesa = lista[4]
                            electrica = lista[5]
                            Serie = elemento.text()[4:10]
                            Fecha = elemento.text()[10:16]
                            Fecha = Fecha[:2] + '-' + Fecha[2:4] + '-' + Fecha[4:]
                            Hora = elemento.text()[16:22]
                            Hora = Hora[:2] + ':' + Hora[2:4] + ':' + Hora[4:]

                            componentDic["Serial"] = f'{Serie}'
                            componentDic["Date"] = f'{Fecha}'
                            componentDic["Hora"] = f'{Hora}'

                            lista = self.sqlDB.getMemberInfo('ET052', elemento.text())

                            torque = lista[0]
                            frame = lista[1]
                            componentDic["ET05a"] = f'{electrica}'
                            componentDic["ET05b"] = f'{torque}'
                            componentDic["Fr"] = f'{frame}'

                            componentDic["Mesa"] = f'{mesa}'

                        elif index == 2:

                            lista = self.sqlDB.getMemberInfo('ET04', elemento.text())
                            print('Condenser')
                            print(elemento.text())
                            componentDic["ET04"] = f'{lista[1]}'
                            componentDic["Condenser"] = f'{elemento.text()}'

                        elif index == 3:
                            print('Conditioner')
                            print(elemento.text())
                            lista = self.sqlDB.getMemberInfo('ET03', elemento.text())
                            componentDic["ET03"] = f'{lista[3]}'
                            componentDic["Condtioner"] = f'{elemento.text()}'

                        elif index == 4:

                            lista = self.sqlDB.getMemberInfo('ET02', elemento.text())
                            componentDic["ET02"] = f'{lista[2]}'
                            componentDic["Partial"] = f'{elemento.text()}'

                        elif index == 5:

                            lista = self.sqlDB.getMemberInfo('ET01', elemento.text())
                            componentDic["ET01"] = f'{lista[1]}'
                            componentDic["Valve"] = f'{elemento.text()}'

                    if flag_complete == 0:
                        print('Generar reporte individual')
                        report_fc.funcionexcel(componentDic)
                        print(componentDic)
                    else:
                        print('Elementos incompletos')

                else:
                    # Generar reporte grupal
                    lista = []
                    contador_columnas = 0
                    verde = QBrush(QColor(144, 238, 144))
                    componentDic = {}
                    complete_flag = 0
                    for index, elemento in enumerate(elementos):
                        contador_columnas = contador_columnas + 1

                        if elemento.background() == verde:

                            if contador_columnas == 2:

                                lista = self.sqlDB.getMemberInfo('ET051', elemento.text())
                                electrica = lista[5]
                                lista = self.sqlDB.getMemberInfo('ET052', elemento.text())
                                torque = lista[0]
                                frame = lista[1]
                                componentDic["ET05a"] = f'{electrica}'
                                componentDic["ET05b"] = f'{torque}'
                                componentDic["Fr"] = f'{frame}'

                            elif contador_columnas == 3:

                                lista = self.sqlDB.getMemberInfo('ET04', elemento.text())
                                componentDic["ET04"] = f'{lista[1]}'

                            elif contador_columnas == 4:

                                lista = self.sqlDB.getMemberInfo('ET03', elemento.text())
                                componentDic["ET03"] = f'{lista[3]}'

                            elif contador_columnas == 5:

                                lista = self.sqlDB.getMemberInfo('ET02', elemento.text())
                                componentDic["ET02"] = f'{lista[2]}'

                            elif contador_columnas == 6:

                                lista = self.sqlDB.getMemberInfo('ET01', elemento.text())
                                componentDic["ET01"] = f'{lista[1]}'
                        else:
                            complete_flag = complete_flag + 1
                        if contador_columnas == 6:
                            contador_columnas = 0

                            if complete_flag == 1:
                                print(componentDic)
                            else:
                                print('Elemento incompleto')

                            complete_flag = 0


            else:
                print('No se puede generar reporte de piezas individuales')
        except Exception as e:
            print(e)
            QMessageBox.warning(self.ui.centralwidget, "Error", "No elements selected", QMessageBox.StandardButton.Ok)

    def searchElements(self):
        rangeFlag = False
        errorFlag = False
        num1 = 0
        num2 = 0
        if self.ui.checkBoxSQL.isChecked():
            rangeFlag = True
            try:
                num1 = int(self.ui.lineEditDesdeSQL.text())
                num2 = int(self.ui.lineEditHastaSQL.text())
                # print(f'Busqueda por rango [ {num1} , {num2}]')
                if (num1 == 0 and num2 == 0) or (num1 < 0 or num2 < 0):
                    raise ValueError("No se puede dividir entre cero")
            except:
                QMessageBox.warning(self.ui.centralwidget, "Error", "No valid Value", QMessageBox.StandardButton.Ok)
                num1 = 0
                num2 = 0
                # rangeFlag = False
                errorFlag = True

        model = self.ui.comboModelSQL.currentIndex()
        status = self.ui.comboStatusSQL.currentIndex()

        if not errorFlag:
            if rangeFlag:
                self.ui.label_info.setText(f'Piezas status {self.ui.comboStatusSQL.itemText(status)} '
                                           f'{self.ui.comboModelSQL.itemText(model)} en el rango [{num1},{num2}]')

                # GetInRange(model,status,inicio,final)
                model_select = self.ui.comboModelSQL.currentIndex() + 1
                status_select = self.ui.comboStatusSQL.currentIndex() + 1

                data = self.sqlDB.getInRange(model_select, status_select, num1, num2)

                row_count = self.ui.dataTableSQL.rowCount() - 1
                # row_count = self.ui.dataTableSQL.rowCount()
                for row in range(row_count - 1, 0, -1):
                    self.ui.dataTableSQL.removeRow(row)
                # self.ui.dataTableSQL.insertRow(0)
                self.fillTableSQL(data)

            else:

                self.ui.label_info.setText(f'Piezas status {self.ui.comboStatusSQL.itemText(status)} '
                                           f'{self.ui.comboModelSQL.itemText(model)}')
                # GetAll(model,status)
                model_select = self.ui.comboModelSQL.currentIndex() + 1
                status_select = self.ui.comboStatusSQL.currentIndex() + 1
                data = self.sqlDB.getAll(model_select, status_select)

                row_count = self.ui.dataTableSQL.rowCount() - 1
                # row_count = self.ui.dataTableSQL.rowCount()
                for row in range(row_count - 1, 0, -1):
                    self.ui.dataTableSQL.removeRow(row)
                # self.ui.dataTableSQL.insertRow(0)
                self.fillTableSQL(data)

    def fillTableSQL(self, tabla):
        for fila, registro in enumerate(tabla, 1):
            if fila >= self.ui.dataTableSQL.rowCount():  # Verificar si la fila siguiente existe
                self.ui.dataTableSQL.insertRow(fila)
            valores = list(registro.values())
            for columna, dato in enumerate(valores, 1):
                if columna > 6:
                    break
                datox = dato
                if columna == 1:
                    datox = int(dato)
                item = QTableWidgetItem(str(datox))

                encontrado = valores[columna - 1 + 5]
                if columna > 1:
                    if encontrado == 'e':
                        item.setBackground(QColor(144, 238, 144))
                        item.setForeground(QBrush(QColor(0, 0, 0)))
                    else:
                        item.setBackground(QColor(255, 99, 71))
                        item.setForeground(QBrush(QColor(0, 0, 0)))

                self.ui.dataTableSQL.setItem(fila - 1, columna - 1, item)
        self.ui.dataTableSQL.resizeColumnsToContents()

    def fillTableLog(self, tabla):
        for fila, registro in enumerate(tabla, 1):
            if fila >= self.ui.dataTableLog.rowCount():  # Verificar si la fila siguiente existe
                self.ui.dataTableLog.insertRow(fila)
            valores = list(registro.values())
            for columna, dato in enumerate(valores, 1):
                if columna > 6:
                    break
                datox = str(dato)

                if len(datox) > 22:
                    datox = datox[:22]

                if columna == 1:
                    datox = int(dato)

                item = QTableWidgetItem(str(datox))

                encontrado = valores[columna - 1 + 5]
                if columna > 1:
                    if encontrado == 'e':
                        item.setBackground(QColor(144, 238, 144))
                        item.setForeground(QBrush(QColor(0, 0, 0)))
                    else:
                        item.setBackground(QColor(255, 99, 71))
                        item.setForeground(QBrush(QColor(0, 0, 0)))

                self.ui.dataTableLog.setItem(fila - 1, columna - 1, item)
        self.ui.dataTableLog.resizeColumnsToContents()

    def getElement(self):
        elementos = self.ui.dataTableLog.selectedItems()
        cadena_label = None
        element = elementos[0]
        register = 'NO DISPONIBLE'

        color = None
        columna = 0
        try:
            # register = self.ui.dataTableLog.currentItem().text()
            # color = self.ui.dataTableLog.currentItem().background()
            # columna = self.ui.dataTableLog.currentItem().column()
            register = element.text()
            color = element.background()
            columna = element.column()
        except:
            register = 'NO DISPONIBLE'

        verde = QBrush(QColor(144, 238, 144))

        cadena = ''
        if color == verde:
            cadena = self.logManager.getElement(register, columna)

        else:
            cadena = 'NO DISPONIBLE'
        cadena_label = cadena
        self.ui.labelDataView.setText(cadena_label)

    def addToDataBase(self):
        elementos = self.ui.dataTableLog.selectedItems()
        cadena_label = None
        piezas_agregadas = 0
        if len(elementos) < 13:
            for element in elementos:
                # print(element.text())
                register = 'NO DISPONIBLE'
                color = None
                columna = 0
                try:
                    # register = self.ui.dataTableLog.currentItem().text()
                    # color = self.ui.dataTableLog.currentItem().background()
                    # columna = self.ui.dataTableLog.currentItem().column()
                    register = element.text()
                    color = element.background()
                    columna = element.column()
                except:
                    register = 'NO DISPONIBLE'

                verde = QBrush(QColor(144, 238, 144))

                cadena = ''
                if color == verde:
                    cadena = self.logManager.getElement(register, columna)

                    # Agregar a base de datos
                    arreglo = cadena.split('\n')
                    fecha = arreglo[0][10:16]
                    hora = arreglo[0][16:]

                    fecha = str(datetime.datetime.now())
                    status = '1'

                    if (arreglo[0][3]) == '5':
                        # arreglo.append(fecha)
                        et = arreglo[0]
                        mesa = arreglo.pop(1)
                        arreglo.insert(4, mesa)

                        lista1 = arreglo[0:6]
                        lista1.append(fecha)
                        lista1.append(status)

                        lista2 = arreglo[6:]
                        frame = lista2.pop(0)

                        lista2.insert(0, et)

                        lista2.append(fecha)
                        lista2.append(status)
                        lista2.append(frame)
                        'INSERT INTO estacion_05_electrico (serialnumber, customer_sn, serialnumber_03, serialnumber_04, '
                        'final_assembly, electrica, fecha_creacion, estatus) VALUES (%s, %s, %s,%s,%s,%s,%s,%s)'

                        'INSERT INTO estacion_05_torques (serialnumber, torques, fecha_creacion, estatus, framesn) VALUES (%s, '
                        '%s, %s,%s,%s)'

                        table1_flag = True
                        table2_flag = True
                        if not self.sqlDB.getMember("ET051", et):
                            print('AGREGAR A TABLA1: ')

                            self.sqlDB.addMember(lista1, 'ET051')
                            piezas_agregadas = piezas_agregadas + 1
                            table1_flag = False

                        if not self.sqlDB.getMember("ET052", et):
                            print('AGREGAR A TABLA2: ')
                            self.sqlDB.addMember(lista2, 'ET052')
                            table2_flag = False

                        if table1_flag and table2_flag:
                            QMessageBox.warning(self.ui.centralwidget, "Error",
                                                f'Registro: {arreglo[0]} previo encontrado',
                                                QMessageBox.StandardButton.Ok)

                    else:
                        arreglo.append(fecha)
                        arreglo.append(status)
                        tabla = arreglo[0][:4]

                        if not self.sqlDB.getMember(tabla, arreglo[0]):

                            # print(f'AGREGAR A TABLA {tabla}: ')
                            self.sqlDB.addMember(arreglo, tabla)
                            piezas_agregadas = piezas_agregadas + 1
                        else:
                            QMessageBox.warning(self.ui.centralwidget, "Error",
                                                f'Registro: {arreglo[0]} previo encontrado',
                                                QMessageBox.StandardButton.Ok)

                else:
                    cadena = 'NO DISPONIBLE'
            if piezas_agregadas > 0:
                QMessageBox.warning(self.ui.centralwidget, " ", f'{piezas_agregadas} elementos agregados existosamente',
                                    QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.warning(self.ui.centralwidget, "Error", f'Demasiados elementos seleccionados',
                                QMessageBox.StandardButton.Ok)

    def updateModel(self):
        model = self.ui.comboModelLog.currentIndex() + 1

        data = self.logManager.getRegister(model)

        row_count = self.ui.dataTableLog.rowCount() - 1
        # row_count = self.ui.dataTableSQL.rowCount()
        for row in range(row_count - 1, 0, -1):
            self.ui.dataTableLog.removeRow(row)
        self.fillTableLog(data)


class WorkerThread(QThread):
    def __init__(self, server):
        super().__init__()
        self.server = server

    def run(self):
        self.server.runServer()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec())



