import mysql.connector as mysql_connector
import hashlib
from random import randint
import urllib.request as urllib_request


class Database():

    def __init__(self, user="W39cSeLp8A", database="W39cSeLp8A", host="remotemysql.com", port="3306", password="6b2V9LddHa"):
        self.user = user
        self.database = database
        self.host = host
        self.port = port
        self.password = password

        self.init_connnection()

        self.current_username = "username"

    #INIT CONNECTION TO CURRENT SELECTED DATABASE
    def init_connnection(self):
        try:
            self.connection = mysql_connector.connect(user=self.user, database=self.database, host=self.host, port=self.port, password=self.password)
            self.mycursor = self.connection.cursor()
        except:
            self.connection = None
            self.mycursor = None
            print( "no connection" )
        #self.connection.   (buffered=True,dictionary=True)\

    #ADDS USER DETAILS TO DATABASE
    def add_user_to_database(self,username, hash_password, random_string, email, phone):
        sql = "INSERT INTO users (USERNAME,PASSWORD,RAND_STRING,EMAIL_ADD,CELL_NUM) VALUES (%s,%s,%s,%s,%s)"
        vals = (username, hash_password, random_string, email, phone)
        self.mycursor.execute(sql, vals)
        self.connection.commit()

    #CONCAT RAW_PASSWORD AND RANDOM_GENERATED STRING
    def concat_password_random_string(self, password, random_string):
        return password+random_string

    #database.create_user(username=username, password=password, email=email, phone=phone)
    def create_user(self, username, email, phone, password):
        self.print_table()
        random_string = get_random_string(10)
        password = self.concat_password_random_string( password=password, random_string=random_string)
        hash_password = self.hash_password( password )
        self.add_user_to_database(username, hash_password, random_string, email, phone)

    #DELETE USER ACCOUNT
    def remove_user( self, username, password ):
        sql = "remove from users where username=(%s) and password=(%s)"
        self.mycursor.execute( sql, [username, password] )


    #given password = raw_password+rand_string returns hashed password
    def hash_password(self, password):
        hash_password = hashlib.sha1( password.encode() )
        hash_password = hash_password.hexdigest()
        return hash_password

    #PRINT TABLE USERS FROM DATABASE
    def print_table(self):
        self.mycursor.execute("select * from users")
        results = self.mycursor.fetchall()
        for i in results:
            print( i )

    #CHECKS IF USERNAME IS IN DATABASE TABLE USERS
    def username_exist(self, username):
        sql = "select * from users where username=(%s)"
        self.mycursor.execute( sql, [username] )
        result = self.mycursor.fetchall()
        if( result == [] ):
            return False
        else:
            return True

    # RETURNS TRUE IF USERNAME AND PASSWORD MATCH IN DATABASE TABLE USERS ELSE FALSE
    def username_password_match(self, username, password ):
        return self.valid_login( username, password )

    #RETURNS TRUE IF USERNAME AND PASSWORD MATCH IN DATABASE TABLE USERS ELSE FALSE
    def valid_login(self, username, password):
        random_string = get_stored_random_string( username )
        if random_string != []:
            random_string = random_string[0][0]
            password += random_string
            password = self.hash_password( password )
            sql = "select * from users where username=(%s) and password=(%s)"
            vals = [username, password]
            self.mycursor.execute( sql , vals )
            result = self.mycursor.fetchall()
            if len( result ) != 0:
                return True
            else:
                return False
        else:
            return False

    #SETS CURRENT USERNAME
    def set_current_username(self, username ):
        self.current_username = username

    #RETURN CURRENT USERNAME
    def get_current_username(self):
        if self.current_username == None:
            return "no username selected"
        else:
            return self.current_username

    # RETURNS STORED RAND_STRING STORED IN DATABASE TABLE USERS
    def get_stored_random_string(self, username):
        sql = "select rand_string from users where username=(%s)"
        self.mycursor.execute(sql, [username])
        results = self.mycursor.fetchall()
        return results

    # RETURNS HASHED PASSWORD DATABASE TABLE USERS
    def get_hashed_password(self, username):
        sql = "select password from users where username=(%s)"
        self.mycursor.execute(sql, [username])
        result = self.mycursor.fetchall()
        return result

    #RETURNS CELL_NUM
    def get_cell_num(self, username ):
        sql = "select cell_num from users where username=%s"
        self.mycursor.execute( sql, [username] )
        result = self.mycursor.fetchall()
        print( result )
        return result

    #RETURNS EMAIL AADDRESS
    def get_email_add(self, username ):
        sql = "select email_add from users where username=%s"
        self.mycursor.execute( sql, [username] )
        result = self.mycursor.fetchall()
        return result

    #TEST IF THERE IS INTERNET CONNECTION
    def test_connection( self, host="http://www.google.com/"):
        try:
            urllib_request.urlopen(host, timeout=5)
            self.connection_available = True
            return True
        except urllib_request.URLError:
            self.connection_available = False
            return False

    #CHANGE USERNAME IN DATABASE
    def change_username(self, username, value):
        if self.username_exist( value ):
            print( "username already exist" )
        else:
            sql = "update users set username=%s where username=%s"
            vals = [ value, username]
            self.mycursor.execute( sql, vals )
            self.connection.commit()
            print( "change username" )

    def change_email(self, username , email):
        sql = "update users set email_add=%s where username=%s"
        vals = [ email, username ]
        self.mycursor.execute( sql, vals )
        self.connection.commit()

    def change_cellnum(self, username , cell_num):
        sql = "update users set cell_num=%s where username=%s"
        vals = [ cell_num, username ]
        self.mycursor.execute( sql, vals )
        self.connection.commit

    def change_password(self, username, password):
        random_string = get_random_string(10)
        password = self.concat_password_random_string( password=password, random_string=random_string )
        password = self.hash_password( password )
        sql = "update users set password=%s where username=%s"
        vals = [ password, username ]
        self.mycursor.execute( sql, vals )
        self.connection.commit()

        self.change_random_string( username, random_string )

    def change_random_string(self, username ,random_string):
        sql = "update users set rand_string=%s where username=%s"
        vals = [ random_string, username ]
        self.mycursor.execute( sql, vals )
        self.connection.commit()

    def testing(self, username ,column ):
        print( "column =",column, "username =",username )
        sql = "select %s from users where username=%s"
        vals = [ column, username ]
        self.mycursor.execute( sql, vals )
        result = self.mycursor.fetchall();

        return result




mydatabase = Database()


#
def username_exist( username ):
    return mydatabase.username_exist( username )

def create_user( username, email, phone, password ):
    mydatabase.create_user( username, email, phone, password )

def get_stored_random_string( username ):
    return mydatabase.get_stored_random_string( username )

def valid_login( username, password):
    return mydatabase.valid_login( username, password )

def get_current_username():
    return mydatabase.get_current_username()

def set_current_username( username ):
    mydatabase.set_current_username( username )

def get_email_add( username ):
    return mydatabase.get_email_add( username=username )

def get_cell_num( username ):
    value = mydatabase.get_cell_num( username=username)
    return value

def get_random_character():
    mode = randint(0, 1)
    if (mode == 0):
        return chr(randint(65, 90))
    else:
        return chr(randint(97, 122))

def get_random_string(length=10):
    string = ""
    for i in range(0, length):
        string += get_random_character()
    return string

def change_password( username, new_password):
    mydatabase.change_password(username=username, password=new_password)

def change_email_add( username, new_email_add ):
    mydatabase.change_email(  username=username, email=new_email_add )

def change_cell_num( username, new_cell_num ):
    mydatabase.change_cellnum( username=username, cell_num=new_cell_num )

if __name__ == "__main__":
    print( "running database.py" )

    result = mydatabase.testing( username="username", column="password")
    print( result )
    print( mydatabase.get_hashed_password( username="username" ) )



# class Local_database():
#
#     def __init__(self, host="localhost", password="CNSPass980423", user="root",database_name=None):
#         self.host = host
#         self.password = password
#         self.user = user
#         self.database_name = None
#
#         self.init_connection()
#
#
#     #INITILISE CONNNECTION TO LOCAL DATABASE
#     def init_connection(self):
#         try:
#             if self.database_name == None:
#                 #connecting without database
#                 self.database = mysql_connector.connect(host=self.host, user=self.user, password=self.password)
#                 self.mycursor = self.database.cursor()
#                 self.create_default_database()
#
#             #CONNECTING TO CURRENT DATABASE_NAME
#             self.database = mysql_connector.connect(host=self.host, user=self.user, password=self.password, database=self.database_name)
#             self.mycursor = self.database.cursor()
#
#         except:
#             print( "cannot connect to database" )
#
#     #CREATES DEFAULT USERS DATABASE IF NOT EXIST
#     def create_default_database(self):
#         sql = "create database if not exists users_database"
#         self.mycursor.execute( sql )
#         self.database.commit()
#         self.database_name = "users_database"
#
#     #CREATE DEFAULT USERS TABLES IF NOT EXIST
#     def create_default_users_table(self):
#         sql = "create table if not exists users(id int auto_increment primary key, username varchar(50), password varchar(50), email_add varchar(50), cell_num varchar(15), rand_string varchar(30))"
#         self.mycursor.execute( sql )
#         #   self.add_unique_constraint(column="username")
#         self.database.commit()
#     """
#     def add_unique_constraint(self, column="username"):
#         #      alter table users add unique (ID);
#         sql = "alter table users add unique (%s)"
#         self.mycursor.execute( sql, [column] )
#         #self.database.commit()
#     """
#
#     #RETURNS DATABASES
#     def get_databases(self):
#         self.mycursor.execute( "show databases" )
#         results = self.mycursor.fetchall()
#         return results
#
#     #RETURNS TABLES FROM SELECTED DATABASE
#     def get_tables(self):
#         self.mycursor.execute( "show tables" )
#         #results = self.mycursor.fetchall()
#         return self.mycursor.fetchall()
#
#     #def add_user(self, username, password, email_add):
#
#     #PRINTS TABLES FROM SELECTED DATABASE
#     def print_tables(self):
#         tables = self.get_tables()
#         for i in tables:
#             print( i )
#
#     def print_users_table(self):
#         sql = "select * from users"
#         self.mycursor.execute( sql )
#         result = self.mycursor.fetchall()
#         for i in result:
#             print( i )
#
#
#
