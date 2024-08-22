import socket
import select
import logging
import datetime
import sys
from sqlManager import managerDataBase
import threading
import filtrosWorkStations
from datetime import datetime
from PySide6.QtCore import Qt, QThread, Signal, QCoreApplication, QObject

msgDic = {
    "STARTMSG": '000000020000000000000000',
    "STOPMSG": '000000050000000000000042',
    "SELECTAPP": '000000050000000000000018',
    "DISABLETOOL": '000000050000000000000042',
    "ENABLETOOL": '000000050000000000000043',
    "SENDSUBSCRIBE": '000000050000000000000060'}

class ChatServer:

    def __init__(self, host, port):
        # Iniciar base de datos
        #self.database = managerDataBase()
        self.new_event = None
        self.new_client = None
        self.sendToServer = None
        self.addToDataBase = None

        self.connectionEvents_flag = False
        self.disconnectEvents_flag = False


        # Iniciar el servidor en modo escucha
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        # self.server_socket.setblocking(False)
        self.server_socket.listen(8)
        self.sockets_list = [self.server_socket]
        self.sockets_out = []
        self.sockets_error = []
        #self.allowed_users = {'192.168.100.8', '192.168.100.10', '127.0.0.1'}  # Lista de usuarios permitidos
        self.setup_logging()  # Configuración de logging
        print(f"Chat server iniciado en {host}:{port}")

    def setNewEvent_fc(self, callback):
        self.new_event = callback
    def setNewClient_fc(self, callback):
        self.new_client = callback
    def setSendServer_fc(self,callback):
        self.sendToServer = callback

    def setToAddToDB_fc(self,callback):
        self.addToDataBase = callback
    def setup_logging(self):
        logging.basicConfig(filename='server.log', level=logging.ERROR,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def send_message(self, client_socket, message):
        try:
            client_socket.send(message.encode())
            # print(f'Mensaje enviado a {client_socket}')
        except Exception as e:
            print(f"Error al enviar mensaje: {str(e)}")
    def send_2_addr(self, addr, mensaje_):
        socketclient = None
        for sock in self.sockets_out:
            if sock.getpeername()[0] == addr:
                socketclient = sock
                break
        if socketclient:
            print("Cliente encontrado")
            self.send_message(socketclient, mensaje_)
        else:
            print("No se encontro el cliente")
    def send_2_all(self,message):
        #message = 'Para todos'
        for client in self.sockets_out:
            client.send(message.encode())
    #Respalda los mensajes que llegan en un Log
    def writeLogRecive(self,str_recive):
        fecha_actual = datetime.today().strftime('%Y-%m-%d')
        with open(f'LogRecive/Log_{fecha_actual}', 'a') as logfile:
            logfile.write(f'{str_recive} {datetime.now()}\n')
    #Respalda los errores ocurridos en un Log de errores
    def writeLogError(self,str_recive):
        fecha_actual = datetime.today().strftime('%Y-%m-%d')
        with open(f'LogError/Log_{fecha_actual}', 'a') as logfile:
            logfile.write(f'{str_recive} {datetime.now()}\n')
    def runServer(self):

        while True:
            try:

                # Consulta el estado de los sockets abiertos
                read_sockets, writablesockets, errorsockets = select.select(self.sockets_list, self.sockets_out,
                                                                            self.sockets_list)
                for notified_socket in read_sockets:

                    #NEW CONNECTION EVENT
                    if notified_socket == self.server_socket:
                        # Acepta la conexion
                        client_socket, client_address = self.server_socket.accept()
                        self.sockets_list.append(client_socket)
                        self.sockets_out.append(client_socket)
                        print(f"Nueva conexión aceptada desde {client_address}")
                        if self.connectionEvents_flag:
                            self.new_event(f"Nueva conexión aceptada desde {client_address[0]}")
                        self.new_client(True, str(client_address[0]))
                        # self.event_manager.print_new_event.emit("Nueva conexion")

                        """
                        if client_address[0] in self.allowed_users:
                            self.sockets_list.append(client_socket)
                            print(f"Nueva conexión aceptada desde {client_address} ")
                            welcome_message = "¡Bienvenido al chat server! Ingresa 'exit' para salir.\n".encode('utf-8')
                            #client_socket.send(welcome_message)
                            #print("aceptado " , client_address[0])
                        else:
                            print(f"Intento de conexión no autorizado desde {client_address}")
                            #client_socket.send("Usuario no autorizado. Desconectando...\n".encode())
                            client_socket.close()
                        """
                    #READ AND CLOSE EVENTS
                    else:
                        # NEW MESSAGE EVENT
                        try:
                            message = notified_socket.recv(1024)
                            self.writeLogRecive(message)
                            message2 = message.replace(b'\x00', b'')
                            if message:

                                #self.new_event(f"{message2}")
                                # Filtrar el mensaje
                                cadena=str(message2)[2:-1]
                                print(f'Recibido: {cadena}')
                                try:
                                    key, lista = filtrosWorkStations.saveData(cadena)
                                    self.addToDataBase(lista, str(key))
                                    print(f'Insertar en {key}')

                                    self.new_event(f"{lista[0]} Registrado")
                                    #print(f'Datos: {lista}')

                                except Exception as e:
                                    print('Excepcion')
                                    print(e)

                                #RESPUESTA AUTOMATICA
                                #answer=msgDic.get(cadena,'NO ENCONTRADO')
                                #self.send_message(notified_socket, answer)

                            else:
                                print("No se recibio nada, cerrar", notified_socket.getsockname())
                                self.sockets_list.remove(notified_socket)
                                self.sockets_out.remove(notified_socket)
                                notified_socket.close()
                        #CLIENT CLOSE
                        except Exception as e:
                            print("Se cerro el cliente ", notified_socket.getpeername())
                            if self.connectionEvents_flag:
                                self.new_event(f"Se cerro el cliente {notified_socket.getpeername()[0]}")
                            self.new_client(False, str(notified_socket.getpeername()[0]))
                            self.sockets_list.remove(notified_socket)
                            if notified_socket in self.sockets_out:
                                self.sockets_out.remove(notified_socket)
                            notified_socket.close()
                            self.writeLogError(e)
            except Exception as e:
                print(f"Error inesperado: {str(e)}")
                self.writeLogError(e)

    def run(self):
        thread = threading.Thread(target=self.runServer)
        thread.start()
        """
        while True:
            message = input()
            if message == 'enviar':
                self.send_2_addr('192.168.100.8','mssss')
                print(f'El mensaje fue enviado')
            elif message == 'salir':
                for sock in self.sockets_out:
                    sock.close()
                    self.sockets_list.remove(sock)
                    self.sockets_out.remove(sock)
        """


if __name__ == "__main__":
    chat_server = ChatServer('192.168.100.10', 4500)
    chat_server.run()
