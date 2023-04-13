import mysql.connector

connection = None

try:
	connection = mysql.connector.connect(
		host='db',
		user='root',
		passwd='P@ssw0rd',
		db='discord')
	cursor = connection.cursor()
	# sql = '''
	# 	CREATE TABLE students (
	# 		student_id VARCHAR(255) NOT NULL PRIMARY KEY,
	# 		name VARCHAR(255) NOT NULL,
	# 		joine_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	# 		created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	# 		updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	# 	)'''
	# sql = '''
	# 	DROP TABLE students;
	# )'''
	# cursor.execute(sql)

	cursor.execute("show columns from students;")
	print(cursor.fetchall())

	cursor.close()

except Exception as e:
	print(f"Error Occurred: {e}")

# finally:
# 	if connection is not None and connection.is_connected():
# 		connection.close()

def join_user(member):
	print(connection)
	cursor = connection.cursor()
	sql = '''
    INSERT INTO students (student_id, name, joine_at, created_at, updated_at)
    VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
	''' % ('\"' + str(member.id) + '\"', '\"' + member.name + '\"')

	cursor.execute(sql)
	connection.commit()

	cursor.execute('select * from students')
	print(cursor.fetchall())

	cursor.close()