import library_models

def LOG_IN(USER_NAME,PASSWORD):
    if USER_NAME=='book' and PASSWORD=='book':
        return True
    else:
        print("invalid user_name and password")
    


def check_librarian(data):
    if library_models.add_librarian(data):
        print("Librarian add successfully")
    else:
        print("This username already exists")

def check_book(data):
  if library_models.ADD_BOOK(data):
      print("add book successfully")
  else:
      print("This book already exists")


# # def RENT_BOOK(rent_book_name):


# # def rent_out_book():
        

def check_user(data):
    if library_models.ADD_USER(data):
        print("User add successfully")
    else:
        print("This username already exists")

def UPDATE_BOOK_DETAIL(DATA,BOOK_NAME):
    if library_models.GET_BOOKS(BOOK_NAME):
        library_models.UPDATE_BOOK_DETAIL(DATA)
        return True
