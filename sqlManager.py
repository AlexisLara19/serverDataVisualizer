
import MySQLdb # import the MySQLdb module

class managerDataBase():
    try:
        connection = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="AlexisLara19"
            #database="caterpillar_assemblies"
            )
        cursor= connection.cursor()
        database="cat"
        #cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database};")

        connection.database=database
        cursor.execute(f"USE {database};")
        """
        cursor.execute("CREATE TABLE IF NOT EXISTS assemblies("
                       "id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,"
                       "user VARCHAR(25) NOT NULL,"
                       "date DATETIME DEFAULT current_timestamp,"
                       "n_parte VARCHAR(10) NOT NULL,"
                       "f_etiqueta VARCHAR(12) NOT NULL,"
                       "n_rev CHAR,"
                       "n_serie VARCHAR(10) NOT NULL,"
                       "status VARCHAR(15) NOT NULL,"
                       "retrabajo CHAR);")
        """
        cursor.close()

        """cursor.execute(f"CREATE TABLE {database}(\
                id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,\
                user VARCHAR(25) NOT NULL,\
                date DATETIME DEFAULT current_timestamp,\
                n_parte VARCHAR(10) NOT NULL,\
                f_etiqueta VARCHAR(12) NOT NULL,\
                n_rev CHAR,\
                n_serie VARCHAR(10) NOT NULL,\
                status VARCHAR(15) NOT NULL,\
                retrabajo CHAR);")"""
        #cursor.execute(f"SHOW DATABASES LIKE '{database}'")
        #resultado = cursor.fetchone()
        #print(resultado)
    except MySQLdb.DatabaseError as e:
        print("No Database")
        print(e)
        exit()
    def __init__(self):
        self.cursor = self.connection.cursor()
        #self.deleteTable()
        #self.createTable()
    def createTable(self):
        create = "CREATE TABLE assemblies(\
        id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,\
        user VARCHAR(25) NOT NULL,\
        date DATETIME DEFAULT current_timestamp,\
        n_parte VARCHAR(10) NOT NULL,\
        f_etiqueta VARCHAR(12) NOT NULL,\
        n_rev CHAR,\
        n_serie VARCHAR(10) NOT NULL,\
        status VARCHAR(15) NOT NULL,\
        retrabajo CHAR);"
        self.cursor.execute(create)
        self.connection.commit()
    def deleteTable(self):
        delete = "DROP TABLE assemblies"
        self.cursor.execute(delete)
        self.connection.commit()
    def addMember(self,user="Airtemp",nparte="611-4360",
                  fetiqueta="17/05/2023",nrev="0",nserie="999999",
                  status="INCOMPLETO",retrabajo="0"):
        insert = "INSERT INTO assemblies (user, n_parte, f_etiqueta,n_rev,n_serie,status,retrabajo) VALUES (%s, %s, %s,%s, %s, %s, %s)"

        values = (user, nparte, fetiqueta, nrev, nserie, status, retrabajo)
        self.cursor.execute(insert, values)
        self.connection.commit()


    def addRandomMembers(self,n,m):
        usuario = 'Benjamin Rojas'
        n_parte = '611-4360'
        f_etiqueta = '17/05/2023'
        n_revision = '9'
        #n_serie = '000035'
        estado = "COMPLETADO"
        retrabajo = '0'
        insert_query = "INSERT INTO assemblies (user, n_parte, f_etiqueta,n_rev,n_serie,status,retrabajo) VALUES (%s, %s, %s,%s, %s, %s, %s)"

        for pz in range(n,m):
            numero_formateado = f"{pz:06d}"
            #impresionfinal="El numero es {}, el segundo numero es {}".format(numero_formateado,numero_dos)
            #print(impresionfinal)
            values = (usuario, n_parte, f_etiqueta, n_revision, numero_formateado, estado, retrabajo)
            self.cursor.execute(insert_query, values)
            self.connection.commit()
    def deleteRandomMembers(self):
        delete="DELETE FROM assemblies WHERE n_rev = 9;"
        self.cursor.execute(delete)
        self.connection.commit()
    def printTable(self):
        self.cursor.execute("SELECT * FROM estacion_01")
        table=self.cursor.fetchall()
        for member in table:
            print(member)
    def showLast10(self):
        self.cursor.execute("SELECT * FROM assemblies ORDER BY id DESC LIMIT 10")
        table = self.cursor.fetchall()
        #for member in table:
        #    print(member)
        return table
    def showRange(self,inicio,final):
        self.cursor.execute(f"SELECT * FROM assemblies WHERE id BETWEEN {inicio} AND {final}")
        table = self.cursor.fetchall()
        # for member in table:
        #    print(member)
        return table

    def showAllMembers(self,num=1):
        table = 'vw_estacion05modelo1full'
        if num == 2:
            table = 'vw_estacion05modelo2full'
        query=f'SELECT * FROM {table} ORDER BY consecutivo ;'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    def showCompleteMembers(self,num=1):
        table = 'vw_estacion05modelo1'
        if num==2:
            table = 'vw_estacion05modelo2'

        query = f'SELECT ' \
                f'serialnumber,' \
                f'serialnumber_04,' \
                f'serialnumber_03,' \
                f'serialnumber_02,' \
                f'serialnumber_01 ' \
                f'FROM {table} ' \
                f'WHERE ' \
                f'{table}.encontrado05 LIKE \'e\' AND ' \
                f'{table}.encontrado04 LIKE \'e\' AND ' \
                f'{table}.encontrado03 LIKE \'e\' AND ' \
                f'{table}.encontrado02 LIKE \'e\' AND ' \
                f'{table}.encontrado01 LIKE \'e\' ' \
                f'ORDER BY consecutivo ;'

        query2 = f'SELECT * ' \
                f'FROM {table} ' \
                f'WHERE ' \
                f'{table}.encontrado05 LIKE \'e\' AND ' \
                f'{table}.encontrado04 LIKE \'e\' AND ' \
                f'{table}.encontrado03 LIKE \'e\' AND ' \
                f'{table}.encontrado02 LIKE \'e\' AND ' \
                f'{table}.encontrado01 LIKE \'e\' ' \
                f'ORDER BY consecutivo ;'
        self.cursor.execute(query2)
        result = self.cursor.fetchall()
        return result
    def showIncompleteMembers(self,num=1):
        table = 'vw_estacion05modelo1full'
        if num == 2:
            table = 'vw_estacion05modelo2full'
        query = f'SELECT * FROM {table} '\
                f'WHERE ( '\
                f'({table}.encontrado05 LIKE \'i\' ) OR ({table}.encontrado05 IS NULL ) OR '\
                f'({table}.encontrado04 LIKE \'i\' ) OR ({table}.encontrado05 IS NULL) OR  '\
                f'({table}.encontrado03 LIKE \'i\' ) OR ({table}.encontrado05 IS NULL ) OR '\
                f'({table}.encontrado02 LIKE \'i\' ) OR ({table}.encontrado05 IS NULL ) OR '\
                f'({table}.encontrado01 LIKE \'i\' ) OR ({table}.encontrado01 IS NULL ) );'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    def showInRangeMembers(self,num=1,minnum=0,maxnum=1):
        desde = min(minnum, maxnum)
        hasta = max(minnum, maxnum)

        table = 'vw_estacion05modelo1full'
        if num == 2:
            table = 'vw_estacion05modelo2full'
        query = f'SELECT * FROM {table} WHERE consecutivo BETWEEN {desde} AND {hasta} ;'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
#db=managerDataBase()
#db.addRandomMembers(10,20)
#db.printTable()


