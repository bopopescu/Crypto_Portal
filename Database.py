import mysql.connector as mysql
import hashlib
from random import randint


def get_random_character():
    mode = randint(0, 1)
    if (mode == 0):
        return chr(randint(65, 90))
    else:
        return chr(randint(97, 122))


def get_random_string(length=10):
    string = ""
    print( type( length) )
    for i in range(0, length):
        string += get_random_character()
    return string

class Database():

    def __init__(self, user="W39cSeLp8A", database="W39cSeLp8A", host="remotemysql.com", port="3306", password="6b2V9LddHa"):
        self.user = user
        self.database = database
        self.host = host
        self.port = port
        self.password = password

        self.connection = mysql.connect( user=self.user, database=self.database, host=self.host, port=self.port,password=self.password )
        self.mycursor = self.connection.cursor()

    #INIT CONNECTION TO CURRENT SELECTED DATABASE
    def init_connnection(self):
        self.connection = mysql.connect( user=self.user, database=self.database, host=self.host, port=self.port,password=self.password )
        self.mycursor = self.connection.cursor()

    #ADDS USER DETAILS TO DATABASE
    def add_user_to_database(self,username, hash_password, random_string, email, phone):
        #print( "add_user_to_database" )
        #print( "hash_password =", hash_password )
        sql = "INSERT INTO users (USERNAME,PASSWORD,RAND_STRING,EMAIL_ADD,CELL_NUM) VALUES (%s,%s,%s,%s,%s)"
        vals = (username, hash_password, random_string, email, phone)
        self.mycursor.execute(sql, vals)
        self.connection.commit()

    #CONCAT RAW_PASSWORD AND RANDOM_GENERATED STRING
    def concat_password_random_string(self, password, random_string):
        return password+random_string


    def create_user(self, username, email, phone, password):
        #print( "database.create_user" )
        random_string = get_random_string(10)
        password = self.concat_password_random_string( password=password, random_string=random_string)
        hash_password = self.hash_password( password )
        self.add_user_to_database(username, hash_password, random_string, email, phone)

    #given password = raw_password+rando_string returns hashed password
    def hash_password(self, password):
        #print("database.hash_password")
        hash_password = hashlib.sha1( password.encode() )
        hash_password = hash_password.hexdigest()
        return hash_password

    #PRINT TABLE USERS FROM DATABASE
    def print_table(self):
        self.mycursor.execute("select * from users")
        print(self.mycursor.fetchall())

    #CHECKS IF USERNAME IS IN DATABASE TABLE USERS
    def username_exist(self, username):
        sql = "select * from users where username=(%s)"
        self.mycursor.execute( sql, [username] )
        result = self.mycursor.fetchall()
        if( result == [] ):
            return False
        else:
            return True

    #RETURNS STORED RAND_STRING STORED IN DATABASE TABLE USERS
    def get_stored_random_string( self, username ):
        #print( "get_random_string" )
        sql = "select rand_string from users where username=(%s)"
        self.mycursor.execute( sql, [username] )
        results = self.mycursor.fetchall()
        #print( "results =", results )
        return results


    #RETURNS HASHED PASSWORD DATABASE TABLE USERS
    def get_hashed_password( self, username ):
        #print( "get_hashed_password" )
        sql = "select password from users where username=(%s)"
        self.mycursor.execute( sql , [username] )
        result = self.mycursor.fetchall()
        return result

    #RETURNS TRUE IF USERNAME AND PASSWORD IN DATABASE TABLE USERS ELSE FALSE
    def valid_login(self, username, password):
        #print("login function")
        random_string = get_stored_random_string( username )
        #print( "random_string =",random_string )
        if random_string != []:
            random_string = random_string[0][0]
            password += random_string
            password = self.hash_password( password )
            #print( "hash_password =",password )
            sql = "select * from users where username=(%s) and password=(%s)"
            vals = [username, password]
            self.mycursor.execute( sql , vals )
            result = self.mycursor.fetchall()
            if len( result ) != 0:
                print( "correct login" )
                return True
            else:
                print( "invalid username or password" )
                return False
        else:
            print( "invalid username or password" )
            return False

mydatabase = Database()


#username_exist
def username_exist( username ):
    #print( "username_exist" )
    return mydatabase.username_exist( username )

def create_user( username, email, phone, password ):
    mydatabase.create_user( username, email, phone, password )

def get_stored_random_string( username ):
    return mydatabase.get_stored_random_string( username )

def valid_login( username, password):
    return mydatabase.valid_login( username, password )

if __name__ == "__main__":
    print("__name__ == \"__main__\"")
    db = Database()
    db.init_connnection()
    db.print_table()


