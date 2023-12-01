
import sqlite3
connection = sqlite3.connect('blooddatabase.db')
cursur = connection.cursor()


def find_username(username):
   cursur.execute("SELECT * FROM user WHERE username=?",(username,))
   data=cursur.fetchone()
   if data:
      return True
   return False

   

def create_user(data):
    cursur.execute("INSERT INTO user (username,name,pasword,role ) ,VALUE(?,?,?)",data)
    connection.commit()
    connection.close()

def donote_date(username):
    cursur.execute("SELECT donote_date FROM blood_donote WHERE username(?)",username)
    data=cursur.fetchone()
    if data:
        return data
    return False

def receiver_date(username):
    cursur.execute("SELECT receiver_date FROM blood_receiver WHERE username(?)",username)
    data=cursur.fetchall()
    if data:
       return data
    return False

    


def blood_donor(data):
    cursur.execute("INSERT INTO blood_donor, VALUES(?,?,?,?,?)",data)
    connection.commit()


    
def blood_receiver(data):
    cursur.execute("INSERT INTO blood_receiver ,VALUES(?,?,?,?,?)",data)
    connection.commit()

def users_info():
    cursur.execute("SELECT * FROM USERS")
    data = cursur.fetchall()
    return data

def user_info(username):
    cursur.execute("SELECT * FROM user WHERE username=(?)",(username,))
    data = cursur.fetchall()
    return data

def user_update(username):
    cursur.execute("UPDATE FROM user WHERE username=(?) ",(username,))
    connection.commit()


def delete_user(username):
    cursur.execute("DELETE FROM user WHERE username=(?) ",(username,))
    connection.commit()


connection.commit()


    



  