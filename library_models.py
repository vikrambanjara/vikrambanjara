
import sqlite3
connection = sqlite3.connect('library.db')
cursur = connection.cursor()

cursur.execute("""CREATE TABLE IF NOT EXISTS USER
               (
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                NAME TEXT NOT NULL,
                USER_NAME TEXT NOT NULL,
                PASSWORD  NOT NULL UNIQUE
              
               )""")


cursur.execute("""CREATE TABLE IF NOT EXISTS BOOKS
               (
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                BOOK_AUTHOR TEXT NOT NULL,
                BOOK_NAME TEXT NOT NULL,
                PUBLICTION_DATE  NOT NULL 
              
               )""")

cursur.execute("""CREATE TABLE IF NOT EXISTS LIBRARIAN
               (
                
                NAME TEXT NOT NULL,
                USER_NAME TEXT UNIQUE NOT NULL,
                PASSWORD TEXT NOT NULL UNIQUE,
                PHONE_NUMBER INTERGER NOT NULL
                
               )""")
print("successfully create table")
# cursur.execute("INSERT INTO USER(NAME,USER_NAME,PASSWORD) VALUES('VICKY','VIKRAM','VIKRAM123')")

def LOG_IN(USER_NAME,PASSWORD):
    cursur.execute("SELECT PASSWORD FROM USER WHERE USER_NAME=(?)",USER_NAME)
    PASSWORD1=cursur.fetchone()
    if PASSWORD1 in PASSWORD:
       return True
    return False

def LIBRARIAN_LOG_IN(USER_NAME,PASSWORD):
    cursur.execute("SELECT PASSWORD FROM LIBRARIAN WHERE USER_NAME=(?)",(USER_NAME))
    PASSWORD=cursur.fetchone()
    if PASSWORD:
       if PASSWORD in PASSWORD:
          return True
       return False
    return False

def USER_LOG_IN(user_name,password):
   cursur.execute("SELECT PASSWORD FROM USER WHERE USER_NAME=(?)",user_name)
   password=cursur.fetchone()
   if password:
      if password in password:
         return True
      return False
   return False
   


def ADD_USER(DATA):
  cursur.execute ("INSERT INTO USER VALUES (?,?,?)",DATA)
  connection.commit()
  return True

def ADD_BOOK(DATA):
  cursur.execute("INSERT INTO BOOKS (BOOK_AUTHOR , BOOK_NAME, PUBLICTION_DATE ) VALUES(?,?,?)",DATA)
  connection.commit
  return True

def GET_BOOKS(BOOK_NAME):
   cursur.execute("SELECT*FROM BOOKS WHERE BOOK_NAME=(?)",BOOK_NAME)
   check=cursur.fetchone()
   return check

def DELETE_BOOK(book_name):
  if GET_BOOKS(book_name):
   cursur.execute ("DELETE FROM BOOKS WHERE BOOK_NAME=(?)",book_name)
   connection.commit()
   return True
  return False


def GET_ALL_BOOKS():
  cursur.execute("SELECT* FROM BOOKS")
  DATA=cursur.fetchall()
  return DATA

def UPDATE_BOOK_DETAIL(DATA):
  cursur.execute("UPDATE BOOKS SET(AUTHOR_NAME,BOOK_NAME,PUBLICATION_DATE)=(?,?,?) WHERE BOOK_NAME=(?)",DATA)
  connection.commit()

def DELETE_BOOK_USER(USER_NAME):
   cursur.execute("DELETE FROM USER WHERE USER_NAME=(?)",USER_NAME)
   connection.commit
   return True
   
connection.commit()
