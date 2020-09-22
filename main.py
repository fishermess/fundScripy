from pgdb import Connection

connection = Connection(user = 'postgres',database = 'komablog',host = '172.17.0.2',password='123456')

a = connection.query("select * from posts")
print(a)
b = connection.get("select * from posts limit 1")
print(b)
#connection.execute("update ")

cursor = connection.cursor()
connection.commit()
connection.rollback()
connection.close()