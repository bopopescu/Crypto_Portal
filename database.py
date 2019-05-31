import mysql.connector as mysql_connector
import hashlib
from random import randint
import urllib.request as urllib_request


class Database:

    def __init__(self, user="W39cSeLp8A", database="W39cSeLp8A", host="remotemysql.com", port="3306", password="6b2V9LddHa"):
        self.user = user
        self.database = database
        self.host = host
        self.port = port
        self.password = password

        self.init_connnection()

    # INIT CONNECTION TO CURRENT SELECTED DATABASE
    def init_connnection(self):
        try:
            self.connection = mysql_connector.connect(user=self.user, database=self.database, host=self.host, port=self.port, password=self.password)
            self.mycursor = self.connection.cursor()
        except:
            self.connection = None
            self.mycursor = None
            print( "no connection" )

    # ADDS USER DETAILS TO DATABASE
    def add_user_to_database(self,username, hash_password, random_string, email, phone):
        sql = "INSERT INTO users (USERNAME,PASSWORD,RAND_STRING,EMAIL_ADD,CELL_NUM) VALUES (%s,%s,%s,%s,%s)"
        vals = (username, hash_password, random_string, email, phone)
        self.mycursor.execute(sql, vals)
        self.connection.commit()

    # CONCAT RAW_PASSWORD AND RANDOM_GENERATED STRING
    def concat_password_random_string(self, password, random_string):
        return password+random_string

    # database.create_user(username=username, password=password, email=email, phone=phone)
    def create_user(self, username, email, phone, password):
        self.print_table()
        random_string = get_random_string(10)
        password = self.concat_password_random_string( password=password, random_string=random_string)
        hash_password = self.hash_password(password)
        self.add_user_to_database(username, hash_password, random_string, email, phone)

    # DELETE USER ACCOUNT
    def remove_user( self, username, password ):
        sql = "remove from users where username=(%s) and password=(%s)"
        self.mycursor.execute(sql, [username, password])


    # given password = raw_password+rand_string returns hashed password
    def hash_password(self, password):
        hash_password = hashlib.sha1( password.encode())
        hash_password = hash_password.hexdigest()
        return hash_password

    # PRINT TABLE USERS FROM DATABASE
    def print_table(self):
        self.mycursor.execute("select * from users")
        results = self.mycursor.fetchall()
        for i in results:
            print(i)

    # CHECKS IF USERNAME IS IN DATABASE TABLE USERS
    def username_exist(self, username):
        sql = "select * from users where username=(%s)"
        self.mycursor.execute(sql, [username])
        result = self.mycursor.fetchall()
        if result == []:
            return False
        else:
            return True

    # RETURNS TRUE IF USERNAME AND PASSWORD MATCH IN DATABASE TABLE USERS ELSE FALSE
    def username_password_match(self, username, password ):
        return self.valid_login( username, password )

    # RETURNS TRUE IF USERNAME AND PASSWORD MATCH IN DATABASE TABLE USERS ELSE FALSE
    def valid_login(self, username, password):
        random_string = get_stored_random_string(username)
        if random_string != []:
            random_string = random_string[0][0]
            password += random_string
            password = self.hash_password(password)
            sql = "select * from users where username=(%s) and password=(%s)"
            vals = [username, password]
            self.mycursor.execute(sql, vals)
            result = self.mycursor.fetchall()
            if len(result) != 0:
                return True
            else:
                return False
        else:
            return False

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

    # RETURNS CELL_NUM
    def get_cell_num(self, username ):
        sql = "select cell_num from users where username=%s"
        self.mycursor.execute(sql, [username])
        result = self.mycursor.fetchall()
        return result

    # RETURNS EMAIL ADDRESS
    def get_email_add(self, username):
        sql = "select email_add from users where username=%s"
        self.mycursor.execute(sql, [username])
        result = self.mycursor.fetchall()
        return result

    # TEST IF THERE IS INTERNET CONNECTION
    def test_connection(self, host="http://www.google.com/"):
        try:
            urllib_request.urlopen(host, timeout=5)
            self.connection_available = True
            return True
        except urllib_request.URLError:
            self.connection_available = False
            return False

    # CHANGE USERNAME IN DATABASE
    def change_username(self, username, value):
        if self.username_exist(value):
            print("username already exist")
        else:
            sql = "update users set username=%s where username=%s"
            vals = [value, username]
            self.mycursor.execute(sql, vals)
            self.connection.commit()
            print("change username")

    def change_email(self, username, email):
        sql = "update users set email_add=%s where username=%s"
        vals = [email, username]
        self.mycursor.execute(sql, vals)
        self.connection.commit()

    def change_cellnum(self, username, cell_num):
        sql = "update users set cell_num=%s where username=%s"
        vals = [cell_num, username]
        self.mycursor.execute(sql, vals)
        self.connection.commit

    def change_password(self, username, password):
        random_string = get_random_string(10)
        password = self.concat_password_random_string(password=password, random_string=random_string)
        password = self.hash_password(password)
        sql = "update users set password=%s where username=%s"
        vals = [password, username]
        self.mycursor.execute(sql, vals)
        self.connection.commit()

        self.change_random_string(username, random_string)

    def change_random_string(self, username,random_string):
        sql = "update users set rand_string=%s where username=%s"
        vals = [random_string, username]
        self.mycursor.execute(sql, vals)
        self.connection.commit()

    # CREATE WALLET FOR USER
    def create_wallet(self, username, amount, wallet_id):
        sql = "insert into wallets (username, amount, type) values(%s,%s,%s);"
        vals = [username, amount, wallet_id]
        self.mycursor.execute(sql, vals)
        self.connection.commit()

    # CHECKS IF WALLET TYPE ALREADY EXIST
    def wallet_exist(self, username, wallet_id):
        wallet_types = self.get_wallets(username)
        wallet_types = [''.join(i) for i in wallet_types]
        if wallet_id in wallet_types:
            return True
        return False

    # RETURN USER WALLETS
    def get_wallets(self, username):
        sql = "select type from wallets where username=%s"
        vals = [username]
        self.mycursor.execute(sql, vals)
        res = self.mycursor.fetchall()
        return res

    def get_amount(self, username, wallet_id):
        print("username =", username, "walled_id =", wallet_id)
        sql = "select amount from wallets where username=%s and type=%s"
        vals = [username, wallet_id]
        self.mycursor.execute(sql, vals)
        res = self.mycursor.fetchall()

        return res


mydatabase = Database()


def username_exist(username):
    return mydatabase.username_exist(username)


def create_user(username, email, phone, password):
    mydatabase.create_user(username, email, phone, password)


def get_stored_random_string(username):
    return mydatabase.get_stored_random_string(username)


def valid_login(username, password):
    return mydatabase.valid_login(username, password)

def get_email_add(username):
    return mydatabase.get_email_add(username=username)


def get_cell_num(username):
    value = mydatabase.get_cell_num(username=username)
    return value


def get_random_character():
    mode = randint(0, 1)
    if mode == 0:
        return chr(randint(65, 90))
    else:
        return chr(randint(97, 122))


def get_random_string(length=10):
    string = ""
    for i in range(0, length):
        string += get_random_character()
    return string


def change_password(username, new_password):
    mydatabase.change_password(username=username, password=new_password)


def change_email_add(username, new_email_add):
    mydatabase.change_email(username=username, email=new_email_add)


def change_cell_num(username, new_cell_num):
    mydatabase.change_cellnum(username=username, cell_num=new_cell_num)


def create_wallet(username, wallet_id):
    mydatabase.create_wallet(username=username, wallet_id=wallet_id)

if __name__ == "__main__":
    print("start")
    res = mydatabase.get_amount(username="username", wallet_id="bitcoin")
    print(res)
    print("end")
