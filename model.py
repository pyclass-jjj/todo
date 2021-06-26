import sqlite3
#import sys
#import traceback

class Modelo:

    def abre_conexion(self):
        self.connection =  sqlite3.connect('todo.db', check_same_thread = False)
        self.cursor = self.connection.cursor()

    def cierra_conexion(self):
        self.cursor.close()
        self.connection.close()

    def query(self, query):
        self.abre_conexion()

        try:
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            #print("Exception class is: ", er.__class__)
            #print('SQLite traceback: ')
            #exc_type, exc_value, exc_tb = sys.exc_info()
            #print(traceback.format_exception(exc_type, exc_value, exc_tb))

    def signup(self, username, password):

        self.query(f"SELECT pk from users where username='{username}' order by pk DESC")
        exist = self.cursor.fetchone()

        if exist == None:
            self.query(f"INSERT INTO USERS(username, password) VALUES('{username}', '{password}')")
            mensaje = [1, f'Usuario {username} Registrado Exitosamente']

        else:
            mensaje = [0, f'Usuario {username} ya existe, elige otro.']

        self.cierra_conexion()
        return mensaje

    def get_users(self):
        self.query(f"SELECT username from users order by pk DESC")
        db_users = self.cursor.fetchall()
        users = []

        for i in range(len(db_users)):
            person = db_users[i][0]
            users.append(person)

        self.cierra_conexion()
        return users

    def valida_acceso(self, username, password):
        query = f"SELECT username, password from users where username='{username}' and password='{password}' order by pk DESC"
        self.query(query)

        existe = self.cursor.fetchone()
        mensaje = [0, 'Usuario o password incorrectos'] if existe is None else [1, 'Usuario Válido']

        self.cierra_conexion()
        return mensaje

    def get_tareas(self, username, id_tarea='%'):
        id_usuario = self.get_id_user(username)
        query = f"SELECT tasks.pk,lists.name,task,start_date,end_date,status,categoria FROM tasks INNER JOIN lists ON tasks.id_list=lists.pk where id_usuario={id_usuario} and tasks.pk like '{id_tarea}'"
        print(query)
        self.query(query)
        tareas = self.cursor.fetchall()
        self.cierra_conexion()
        return tareas

    def get_id_user(self, usuario):
        self.query(f"SELECT pk from users where username='{usuario}'")
        return self.cursor.fetchone()[0]

    def editar_tarea(self, datos):
        query = f"""UPDATE tasks SET
                     id_list = '{datos['categoria']}',
                     task = '{datos['tarea']}',
                     start_date = '{datos['fechaini']}',
                     end_date = '{datos['fechafin']}',
                     status = '{datos['estatus']}'
                     WHERE pk={datos['id_tarea']}
                 """
        self.query(query)
        return 0

    def nueva_tarea(self, datos, username):

        id_usuario = self.get_id_user(username)

        query = f"""INSERT INTO tasks(
                        id_usuario,
                        id_list,
                        task,
                        start_date,
                        end_date,
                        status
                    )
                    VALUES(
                        {id_usuario},
                        '{datos['categoria']}',
                        '{datos['tarea']}',
                        '{datos['fechaini']}',
                        '{datos['fechafin']}',
                        '{datos['estatus']}'
                    )
                 """
        self.query(query)

    def nueva_categoria(self, categoria):

        query = f"""INSERT INTO lists(
                        name
                    )
                    VALUES(
                        '{categoria}'
                    )
                 """
        print(query)
        self.query(query)


    def eliminar_tarea(self, id_tarea):
        query = f"DELETE from tasks where pk={id_tarea}"
        self.query(query)
        return 0

    def get_categorias(self):
        query = "SELECT pk, name from lists"
        self.query(query)
        categorias = self.cursor.fetchall()
        self.cierra_conexion()
        return categorias


if __name__=='__main__':

    modelo = Modelo()
    signup = modelo.signup('jjayala3', '12345')
    print(signup)

    #usuarios = modelo.get_users()
    #print(usuarios)

    #acceso = modelo.valida_acceso('jjayala', '12345')
    #print(acceso)


