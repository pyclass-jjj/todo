import sqlite3

connection = sqlite3.connect('todo.db', check_same_thread = False)
cursor = connection.cursor()

#cursor.execute('DROP TABLE IF EXISTS users')
cursor.execute('DROP TABLE IF EXISTS lists')
cursor.execute('DROP TABLE IF EXISTS tasks')

cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            username varchar(16),
            password varchar(255)
        )
        """)

cursor.execute("""
        CREATE TABLE IF NOT EXISTS lists (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            name varchar(128),
            description varchar(255)
        )
        """)

cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER NOT NULL,
            id_list INTEGER NOT NULL,
            task varchar(64),
            categoria varchar(20),
            start_date varchar(20),
            end_date varchar(20),
            status varchar(20),
            FOREIGN KEY (id_list)
            REFERENCES lists(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
        )
        """)


cursor.execute("insert into lists (name, description) values('Trabajo','List number 1');")
cursor.execute("insert into lists (name, description) values('Escuela','List pendientes escuela ');")
cursor.execute("insert into lists (name, description) values('Familia','List para pendientes de la familia');")
#
cursor.execute("insert into tasks (id_usuario, id_list, task, status) values(1, 1,'Tarea 1 Lista 1', 'Pendiente');")
cursor.execute("insert into tasks (id_usuario, id_list, task, status) values(1, 1,'Tarea 2 Lista 1', 'Pendiente');")
cursor.execute("insert into tasks (id_usuario, id_list, task, status) values(1, 1,'Tarea 3 Lista 1', 'Pendiente');")
cursor.execute("insert into tasks (id_usuario, id_list, task, status) values(1, 1,'Tarea 4 Lista 1', 'Pendiente');")
cursor.execute("insert into tasks (id_usuario, id_list, task, status) values(1, 2,'Tarea 5 Lista 2', 'Pendiente');")
cursor.execute("insert into tasks (id_usuario, id_list, task, status) values(1, 2,'Tarea 6 Lista 2', 'Pendiente');")
cursor.execute("insert into tasks (id_usuario, id_list, task, status) values(1, 2,'Tarea 7 Lista 2', 'Pendiente');")
cursor.execute("insert into tasks (id_usuario, id_list, task, status) values(1, 2,'Tarea 8 Lista 2', 'Pendiente');")

cursor.execute("insert into tasks (id_usuario, id_list, task, status) values(2, 1,'Tarea 1 Lista 1', 'Pendiente');")
cursor.execute("insert into tasks (id_usuario, id_list, task, status) values(2, 1,'Tarea 2 Lista 1', 'Pendiente');")
cursor.execute("insert into tasks (id_usuario, id_list, task, status) values(2, 1,'Tarea 3 Lista 1', 'Pendiente');")
cursor.execute("insert into tasks (id_usuario, id_list, task, status) values(2, 1,'Tarea 4 Lista 1', 'Pendiente');")
cursor.execute("insert into tasks (id_usuario, id_list, task, status) values(2, 2,'Tarea 5 Lista 2', 'Pendiente');")
cursor.execute("insert into tasks (id_usuario, id_list, task, status) values(2, 2,'Tarea 6 Lista 2', 'Pendiente');")
cursor.execute("insert into tasks (id_usuario, id_list, task, status) values(2, 2,'Tarea 7 Lista 2', 'Pendiente');")
cursor.execute("insert into tasks (id_usuario, id_list, task, status) values(2, 2,'Tarea 8 Lista 2 ', 'Pendiente');")

connection.commit()
#
#
#try:
#    cursor.execute('DELETE FROM users')
#    connection.commit()
#
#except sqlite3.Error as er:
#    print('SQLite error: %s' % (' '.join(er.args)))
#    print("Exception class is: ", er.__class__)
#    print('SQLite traceback: ')
#    exc_type, exc_value, exc_tb = sys.exc_info()
#    print(traceback.format_exception(exc_type, exc_value, exc_tb))



cursor.close()
connection.close()
