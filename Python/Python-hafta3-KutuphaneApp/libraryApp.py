class MenuItem:
    def __init__(self,text,number):
        self.text=text
        self.number=number
    
    def display(self):
        print(self.text,self.number) #tupple döndürür
   

class Menu:
    def __init__(self,header=" ",menuItems=" "):
        self.header=header
        self.menuItems=menuItems
    
    def display(self,display_header):
        if display_header==True:
            print(header)
            print(menuItems)
        else:
            print(menuItems)

    def add_menu_item(self,text,number):
        MenuItem(text,number)



class user:
    menu=Menu("")
    menu_items=[]
    name=""
    password=""
    role=""

    def __init__(self):
        def menu_builder(self,menu):
            Menu(menu)

    def display(self):
        return user #print(f"{self.name} : {self.password}")
    

class Admin(user):
    menu_items = ["List books", "Create a book", "Delete a book","Search for a book",
    "Change number of a copies of a book", "Show students borrowed a book by ""ID",
    "List Users", "Create User","Delete User", "Exit"] 
    menu= Menu(header="Welcome to Admin Menu",menuItems=menu_items)
    def __init__(self,name,password):
        super().__init__(name,password)
        self.role="admin"
        menu_builder(menu)

class Student(user):
    menu_items = ["Search for a book", "Add a book to my book list",
     "delete a book from my book list","show my borrowed books", "Exit"]
    menu= Menu(header="Welcome to Admin Menu",menuItems=menu_items)
    menu_flag=False
    
    def __init__(self,name,password):
        super().__init__(name,password)
        self.role="student"
        menu.menu_builder(menu)
        

class userDB:
    
    example_users = {'Ahmet': ['1234', 'student'], 'Ayse': ['4321', 'student'], "admin":
["0000", 'admin']}
    users_objects={}
    example_users_flag=True
   
    def create_example_users(self):
        pass
    def add_user(self,name, password, role):
        self.name=name
        self.password=password
        self.role=role
    def remove_user(self):
        pass
    def list_user(self):
        pass
    def validate_user(self,uid, password):
        pass

class book:
    def __init__(self,bid,name,no_of_copies,list_of_authors):
        self.bid=bid
        self.name=name
        self.no_of_copies=no_of_copies
        self.list_of_authors=list_of_authors

        pass
    def display(self):
        pass

class library:
    example_books = {"001": ["Biology", 2, ["Alice", "Bob"]], "002": ["Chemistry", 3,["Alice"]]}
    author_to_books={}
    book_objects=Book()
    example_books_flag=True
    def __init__(self):
        def create_example_books(self):
                   pass
        


   
  
    
    def add_book(self,bid, name, copies, authors):
        pass
    def remove_book(self):
        pass
    def list_book(self):
        return list(book_object)
    def search_book(self):
        pass
    def update_book_copies(self):
        pass


class main:
    
    library
    userDB=userDB()
    current_user=""
    @classmethod
    def login(self):
        self.isim="Ahmet"
        self.password=1235
        if userDB.example_users[self.isim]==self.password:
            print("Başarılı")
        else:
            print("Başarısız")
    def show_admin_menu(self):
        pass
    def show_student_menu(self):
        Student("deneme","123456")
    
metin = """
**********************************************************
*                                                        *
*                -welcome to  Library-                   *
*                                                        *
**********************************************************
"""
if __name__ == "__main__":
    print(metin)
    
    
    main.show_student_menu()
    
    