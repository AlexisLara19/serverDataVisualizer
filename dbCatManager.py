import MySQLdb  # import the MySQLdb module

USER = "root"
PASSWD = "AlexisLara19"
HOST = "localhost"
DB = 'cat'
PORT = 3306

queryDic = {
    "ET01": 'INSERT INTO estacion_01 (serialnumber, torques, fecha_creacion, estatus) VALUES (%s, %s, %s,%s)',
    "ET02": 'INSERT INTO estacion_02 (serialnumber, torques, fecha_creacion, estatus) VALUES (%s, %s, %s,%s)',
    "ET02a": 'INSERT INTO estacion_02a (serialnumber, torques1_3, torques5_6, fecha_creacion, estatus) VALUES (%s, '
             '%s, %s,%s,%s)',
    "ET02b": 'INSERT INTO estacion_02b (serialnumber, torques_4, torques_7, fecha_creacion, estatus) VALUES (%s, '
             '%s, %s,%s,%s)',
    "ET03": 'INSERT INTO estacion_03 (serialnumber, serialnumber_01, serialnumber_02, torques, fecha_creacion, '
            'estatus) VALUES (%s,%s,%s, %s,%s,%s)',
    "ET04": 'INSERT INTO estacion_04 (serialnumber, torques, fecha_creacion, estatus) VALUES (%s, %s, %s,%s)',
    "ET051": 'INSERT INTO estacion_05_electrico (serialnumber, customer_sn, serialnumber_03, serialnumber_04, '
             'final_assembly, electrica, fecha_creacion, estatus) VALUES (%s, %s, %s,%s,%s,%s,%s,%s)',
    "ET052": 'INSERT INTO estacion_05_torques (serialnumber, torques, fecha_creacion, estatus, framesn) VALUES (%s, '
             '%s, %s,%s,%s)'}

queryConsult = {"ET01": 'Select id from estacion_01 WHERE serialnumber = %s',
                "ET02": 'Select id from estacion_02 WHERE serialnumber = %s',
                "ET02a": 'Select id from estacion_02a WHERE serialnumber = %s',
                "ET03": 'Select id from estacion_03 WHERE serialnumber = %s',
                "ET04": 'Select id from estacion_04 WHERE serialnumber = %s',
                "ET051": 'Select id from estacion_05_electrico WHERE serialnumber = %s',
                "ET052": 'Select id from estacion_05_torques WHERE serialnumber = %s'}

queryInfo =    {"ET01": 'Select * from estacion_01 WHERE serialnumber = %s',
                "ET02": 'Select * from vw_estacion_02full WHERE serialnumber = %s',
                "ET03": 'Select * from estacion_03 WHERE serialnumber = %s',
                "ET04": 'Select * from estacion_04 WHERE serialnumber = %s',
                "ET051": 'Select * from estacion_05_electrico WHERE serialnumber = %s',
                "ET052": 'Select * from estacion_05_torques WHERE serialnumber = %s'}
class managerDataBase():
    conn = ''
    cur = ''

    def __init__(self):
        self.status = self.connection()

    def connection(self):
        try:
            self.conn = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB, port=PORT)
            self.cur = self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            #print("Conexion exitosa")
            return True

        except MySQLdb.DatabaseError as er:
            print(er)
            return False
    def getInRange(self, model, status, init, final):

        modelo = 'modelo1'
        if model == 2:
            modelo = 'modelo2'

        # STATUS: Todos
        """query = f'SELECT * FROM vw_estacion05{modelo}full ' \
                f'WHERE (consecutivo BETWEEN {init} AND {final})  ORDER BY consecutivo ;'"""

        query = f'SELECT * FROM vw_estacion05{modelo} ' \
                f'WHERE (consecutivo BETWEEN {init} AND {final})  ORDER BY consecutivo ;'
        # STATUS:Completos
        if status == 2:
            query = f'SELECT * FROM vw_estacion05{modelo} ' \
                    f'WHERE (consecutivo BETWEEN {init} AND {final})' \
                    f'AND' \
                    f'(vw_estacion05{modelo}.encontrado05 LIKE \'e\' AND ' \
                    f'vw_estacion05{modelo}.encontrado04 LIKE \'e\' AND ' \
                    f'vw_estacion05{modelo}.encontrado03 LIKE \'e\' AND ' \
                    f'vw_estacion05{modelo}.encontrado02 LIKE \'e\' AND ' \
                    f'vw_estacion05{modelo}.encontrado01 LIKE \'e\') ' \
                    f'ORDER BY consecutivo ;'
        # STATUS: INCOMPLETOS
        elif status == 3:
            query = f'SELECT * FROM vw_estacion05{modelo} ' \
                    f'WHERE (consecutivo BETWEEN {init} AND {final})' \
                    f'AND' \
                    f'(vw_estacion05{modelo}.encontrado05 LIKE \'i\' OR ' \
                    f'vw_estacion05{modelo}.encontrado04 LIKE \'i\' OR ' \
                    f'vw_estacion05{modelo}.encontrado03 LIKE \'i\' OR ' \
                    f'vw_estacion05{modelo}.encontrado02 LIKE \'i\' OR ' \
                    f'vw_estacion05{modelo}.encontrado01 LIKE \'i\') ' \
                    f'ORDER BY consecutivo ;'

        self.cur.execute(query)
        result = self.cur.fetchall() #Tupla de diccionarios
        #print(f'El tipo de variable es {type(result[0])}')
        return result
    def getAll(self, model, status):
        modelo = 'modelo1'
        if model == 2:
            modelo = 'modelo2'

        # STATUS: Todos
        """query = f'SELECT * FROM vw_estacion05{modelo}full ' \
                f'ORDER BY consecutivo ;'"""
        query = f'SELECT * FROM vw_estacion05{modelo} ' \
                f'ORDER BY consecutivo ;'
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result
    def addMember (self,values_tupla,table):

        values_tupla = tuple(values_tupla)
        query = queryDic.get(table, 'NO ENCONTRADO')
        self.cur.execute(query, values_tupla)
        self.conn.commit()
        print(f'Agregado: {values_tupla}')
    def getMember(self,et,serialnumber):
        query = queryConsult.get(str(et), 'NO ENCONTRADO')
        self.cur.execute(query, (serialnumber,))
        result = self.cur.fetchone()
        if result:
            #print('YA EN BASE DE DATOS')
            return True
        else:
            #print('NO SE ENCONTRO EL REGISTRO')
            return False
    def getMemberInfo(self,et,serialnumber):
        query = queryInfo.get(str(et), 'NO ENCONTRADO')


        self.cur.execute(query, (serialnumber,))
        result = self.cur.fetchall()
        lista = None




        if et == 'ET052':
            lista = list(result[0].values())[1:]
            del lista[2:4]
            del lista[0]
        else:
            lista = list(result[0].values())[1:-1]
            lista = map(str, lista)
            #fecha = str(lista.pop(-1))
            #lista.append(fecha)
            #print(fecha)

        lista_filtrada = [valor for valor in lista if valor is not None and valor != 'None']
        return lista_filtrada



