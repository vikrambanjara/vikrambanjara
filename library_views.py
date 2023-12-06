import library_models
import library_controler
import datetime




def cheak():
   print("ENTER 1 FOR USER_LOG_IN: ")
   print("ENTER 2 FOR LIBARIAN_LOG_IN: ")
  
def cheak_no(n):
   if n==1:
    library_models.USER_LOG_IN
   elif n==2:
      library_models.LIBRARIAN_LOG_IN()
   else:
      print("invalid choice")

def user_log_in():
   print("ENTER 1 FOR RENT BOOK")
   print("ENTER 2 FOR RENTED OUT BOOK")
   print("ENTER ANY NUMBER FOR EXIT")

# def user(CHOICE,USER_NAME):
#    if CHOICE==1:
#       RENT_BOOK()
#    elif CHOICE==2:
#       RENTED_OUT_BOOK()
#    else:
#       print("INVALID CHOICE")

# # def RENT_BOOK(username):
#     rent_book_name = input("Enter Book name for rent a Book : ")
#     rented_date = datetime.datetime.now().date()
#     data = (rented_date,username,rent_book_name)
#     library_controler.RENT_BOOK(data,rent_book_name)

# def RENTED_OUT_BOOK():
#    rent_out_book_name = input("Enter Book Name for Rent Out : ")
#    library_controler.rent_out_book(rent_out_book_name)

      
   

def ADMIN_func():
  print("enter 1 for log_in")
  print("enter 2 for add_book")
  print("enter 3 for get add_user")
  print("enter 4 for upadte_Book_detail")
  print("enter 5 for delete_book")
  print("enter any number for exit")

def func_choice(n):
  if n==1:
    USER_LOG_IN() 
  elif n==2:
    ADD_BOOK()
  elif n==3:
    ADD_USER()
  elif n==5:
     UPDATE_BOOK_DETAIL()
  elif n==6:
    DELETE_BOOK()
  else:
    print("Invalid choice")


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

def librarian_log_in():
    ADMIN_func()
    choose_no = int(input("choose any no. : "))
    func_choice(choose_no)



def USER_LOG_IN():
   USER_NAME=input("ENTER YOUR USER_NAME: ")
   PASSWORD=input("ENTER YOUR PASSWORD: ")
   if library_controler.LOG_IN(USER_NAME,PASSWORD):
      print("Welcome to Libarary")
      cheak(cheak_no)
      
   elif library_models.LIBRARIAN_LOG_IN(USER_NAME,PASSWORD):
      print("WELCOME TO Libarary")
      librarian_log_in
     

      
  #  elif library_models.USER_LOG_IN(USER_NAME,PASSWORD):
  #     print("WELCOME LIBRARY")
  #     user_log_in()
   else:
      print("INVAIL USER_NAME,PASSWORD")


USER_LOG_IN()

    








