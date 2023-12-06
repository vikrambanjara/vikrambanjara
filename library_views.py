import library_models
import library_controler
import datetime




def cheak():
   print("ENTER 1 FOR USER_LOG_IN: ")
   print("ENTER 2 FOR LIBARIAN_LOG_IN: ")
   

def librarian_func():
  print("enter 1 for add librarian")
  print("enter 2 for add_book")
  print("enter 3 for get add_user")
  print("enter 4 for delete user")
  print("enter 5 for upadte_Book_detail")
  print("enter 6 for delete_book")
  print("enter any number for exit")

def user_func():
   print("enter 1 for rent a book: ")
   print("enter 2 for rent out book: ")
   print("enter any key for exit")


# def user_choice(n):
#    if n==1:
#       rent_book()
#    elif n==2:
#       rent_out_book()
#    else:
#       print("invalid choice")


def librarian_choice(n):
  if n==1: 
    add_librarian()
  elif n==2:
    ADD_BOOK()
  elif n==3:
    ADD_USER()
  elif n==4:
     delete_user()
  elif n==5:
     UPDATE_BOOK_DETAIL()
  elif n==6:
    DELETE_BOOK()

  else:
    print("Invalid choice")




def add_librarian():
    name = input("Enter Librarian Name : ")
    username = input("Create Librarian Username : ")
    password = input("Create Password : ")
    mobile_no = input("Enter Mobile_No : ")
    data = (name,username,password,mobile_no)
    library_controler.check_librarian(data)

def ADD_BOOK():
  BOOK_AUTHOR=input("ENTER AUTHOR NAME: ")
  BOOK_NAME = input("Enter Book Name : ")
  PUBLICATION_DATE = input("Enter Publication Company : ")
  data = (BOOK_AUTHOR,BOOK_NAME,PUBLICATION_DATE)
  library_controler.check_book(data)


def ADD_USER():
   NAME = input("Enter User Name : ")
   USER_NAME = input("Create User Username : ")
   PASSWORD = input("Create Password : ")
   data = (NAME,USER_NAME,PASSWORD)
   library_controler.check_user(data)


def delete_user():
    username = input("Enter Username For Delete User : ")
    if library_models.delete_user(username):
        print("User Delete Successfully")
    else:
        print("Username Already not exists")

def UPDATE_BOOK_DETAIL():
    book_name = input("Enter Book Name : ")
    new_author = input("Enter New Author Name : ")
    new_book_name = input("Enter New Book Name : ")
    new_publication_company = input("Enter New Publication Company : ")
    data = (new_author,new_book_name,new_publication_company,book_name)
    if library_controler.update_book_details(data,book_name):
        print("Book Update successfully")
    
  
    

def DELETE_BOOK():
  BOOK_NAME = input("Enter Book Name For Delete Book : ")
  if library_models.DELETE_BOOK(BOOK_NAME):
        print("Book Delete Successfully")
  else:
        print("Book Name  not exists")



def log_in():
   user_name=input("enter your user_name: ")
   password=input("enter your pasword: ")
   if library_controler.LOG_IN(user_name,password):
      print("wlcome in to library")
      cheak()
      choose_no=int(input("enter a number: "))
      user_func()  

   


log_in()





