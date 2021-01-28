class MenuItem:
    def __init__(self, text, number):
        self.text = text
        self.number = number
    def display(self):
        return self

class Menu:
    def __init__(self, header, menuItems):
        self.header = header
        self.menuItems = menuItems
    def display(self, display_header):
        i = 1
        if display_header == True:
            print(self.header)
        for item in self.menuItems:
            print(f"{i} - {item}")
            i += 1
    def add_menu_item(self,text,number):
        new_item = MenuItem(text,number)
        self.menuItems.append(new_item)

class User:
    menu_items = []
    menu = Menu(header="",menuItems=menu_items)
    def __init__(self, name, password):
        self.name = name
        self.password = password
    def display(self):
        return self.name,self.password
    def menu_builder(self,header,menu_items):
        self.menu = Menu(header=header,menuItems=menu_items)
        self.menu.display(True)

class Admin(User):
    menu_items = ["List books","Create a book","Delete a book","Search for a book","Change number of a copies for a book","Show students borrowed a book by ""ID","List Users","Create User","Delete User","Exit"]
    menu = Menu(header="Welcome to admin menu",menuItems=menu_items)
    def __init__(self,name,password):
        User.__init__(self,name,password)
        self.role = "admin"
    def menu_builder(self):    
        User.menu_builder(self,header="Welcome to admin menu",menu_items=self.menu_items)

class Student(User):
    menu_items = ["Search for a book","Add a book to my list","delete a book from my book list","show my borrowed books","Exit"]
    menu_flag = False
    book_list = []
    menu = Menu(header="Welcome to student menu",menuItems=menu_items)
    def __init__(self,name,password):
        User.__init__(self,name,password)
        self.role = "student"
    def menu_builder(self):    
        User.menu_builder(self,header="Welcome to student menu",menu_items=self.menu_items)
    def add_book(self,bid):
        self.book_list.append([bid,Library(False).book_objects[bid]])
    def remove_book(self,bid):
        for item in self.book_list:
            if item[0] == bid:
                self.book_list.remove(item)
    def show_borrowed_books(self):
        return self.book_list

class UserDB:
    example_users = {'Ahmet': ['1234','student'], 'Ayse': ['4321','student'], "admin": ["0000", 'admin']}
    users_objects = {}

    def add_user(self,name,password,role):
        if role == "student":
            x = Student(name,password)
            self.users_objects[name] = [password,role]
        if role == "admin":
            x = Admin(name,password)
            self.users_objects[name] = [password,role]
    def remove_user(self,name):
        del self.users_objects[name]
    def list_user(self):
        return self.users_objects
    def validate_user(self,name,password):
        if name in self.example_users.keys() and password in self.example_users[name][0]:
            return True
        else:
            return False
    def create_example_users(self):
        k = list(self.example_users.keys())
        v = list(self.example_users.values())
        for i in range(len(k)):
            self.add_user(k[i],v[i][0],v[i][1])
    def __init__(self,example_users_flag=True):
        self.example_users_flag = example_users_flag
        if self.example_users_flag == True:
            self.create_example_users()    

class Book:
    def __init__(self,bid,name,no_of_copies,list_of_authors):
        self.bid = bid
        self.name = name
        self.no_of_copies = no_of_copies
        self.list_of_authors = list_of_authors
    def display(self):
        return self.bid,self.name,self.no_of_copies,self.list_of_authors

class Library:
    example_books = {"001":["Biology",2,["Alice","Bob"]],"002":["Chemistry",3,["Alice"]]}
    author_to_books = {}
    book_objects = {}
    def add_book(self,bid,name,copies,authors):
        
        self.author_to_books[authors] = [bid,name,copies]
        self.book_objects[bid] = [name,copies,authors]
    def remove_book(self,bid):
        for item in self.author_to_books:
            if self.author_to_books[item] == self.book_objects[bid][2]:
                del self.author_to_books[item]
        del self.book_objects[bid] 
    def list_book(self):
        return self.book_objects
    def search_book(self):
        g = str(input("For seaching books with name press N/for searching books with author press A")).lower()
        g2 = str(input("Please write books name or author according to your previous choose"))
        if g == "n":
            for bid in self.book_objects:
                if self.book_objects[bid][0] == g2:
                    print("Found!" + bid + " " + str(self.book_objects[bid]))
                    return 0
            print("Not found!")
        if g == "a":
            for bid in self.book_objects:
                if self.book_objects[bid][2] == g2:
                    print("Found" + bid + " " + str(self.book_objects[bid]))
                    return 0
            print("Not found! \n")
    def update_book_copies(self):
        books_bid = str(input("Please write the book's bid number that you want to change it's copy number: "))
        copy_number = int(input("Please write your book's new copy number: "))
        for bid in self.book_objects:
            if books_bid == bid:
                self.book_objects[bid][1] = copy_number
                print("Copy number updated!")
    def create_example_books(self):
        k = list(self.example_books.keys())
        v = list(self.example_books.values())
        for i in range(len(k)):
            toggle = tuple(v[i][2])
            self.add_book(k[i],v[i][0],v[i][1],toggle)
    def __init__(self,example_books_flag=True):
        self.example_books_flag = example_books_flag
        if self.example_books_flag == True:
            self.create_example_books()
class Main:
    current_user = None
    infolist = []
    def __init__(self):
        self.library = Library(example_books_flag=True)
        self.userDB = UserDB(example_users_flag=True)
        
    def login(self):
        
        choice = str(input("Do you want to create a new user? (Y/N)"))
       
        while True:
            if choice == "n":
                username = str(input("Please insert your user name: "))
                
                password = str(input("Please insert your password: "))
               
                kontrol=UserDB().validate_user(username,password)
                if kontrol==True:
                    self.infolist.append(username)
                    self.infolist.append(password)
                    self.current_user = {username:UserDB().users_objects[username]}
                    return self.current_user[username][1]
                    
                     
                else:
                    print("No such user exists!")

      

               

               
            elif choice == "y":
                username = str(input("Please insert your user name: "))
                self.infolist.append(username)
                password = str(input("Please insert your password: "))
                role = str(input("Please insert your role: "))
                kontrol=UserDB().validate_user(username,password)
                if kontrol==True:
                    print("such a user already exists")
              


        
                


            


    def show_admin_menu(self):
        Library()
        UserDB()
        while True:
            Admin(self.infolist[0],self.infolist[1]).menu_builder()
            option = int(input("Please insert your command's number: "))
            if option == 1:
                for item in Library(False).list_book():
                    print(f"{item} {Library(False).list_book()[item]}")
                    #yazış şekli düzeltilecek
            if option == 2:
                booksauthors = []
                bookbid = str(input("Please insert book's bid number"))
                bookname = str(input("Please insert book's name"))
                bookcopies = str(input("Please insert number of book's copies"))
                numberofauthors = int(input("How many authors wrote this book? (Please insert a number!)"))
                for i in range(numberofauthors):
                    booksauthors.append(str(input(f"{i+1}. author's name:")))
                Library(False).add_book(bookbid,bookname,bookcopies,tuple(booksauthors))
            if option == 3:
                Library(False).remove_book(input("Please insert the bid number of the book that you want to delete: "))
            if option == 4:
                Library(False).search_book()
                #yazış şekli düzenlenecek fonksiyon çalışıyor
            if option == 5:
                Library(False).update_book_copies()
            if option == 6:
                pass
            if option == 7:
                print("----------Users List----------")
                for item in UserDB(False).list_user():
                   
                    print(f"{item} {UserDB(False).list_user()[item]}")
                    #yazı şekli düzeltilecek
            if option == 8:
                username = str(input("Please insert your user name: "))
                #self.infolist[0] = username
                password = str(input("Please insert your password: "))
                #self.infolist[1] = password
                role = str(input("Please insert your preferred role: "))
                UserDB(False).add_user(username,password,role)
                self.current_user = {username:UserDB(False).users_objects[username]}
            if option == 9:
                UserDB(False).remove_user(input("Please insert the username of the user that you want to delete: "))
            if option == 10:
                break
            if input("Continue? (Y/N)") == "y":
                continue
            else:
                break
    def show_student_menu(self):
        while True:
            Student(self.infolist[0],self.infolist[1]).menu_builder()
            option = int(input("Please insert your command's number: "))
            if option == 1:
                Library(False).search_book()
            if option == 2:
                Student(self.infolist[0],self.infolist[1]).add_book(str(input("Please write the book's bid number that you want to add to your list: ")))
            if option == 3:
                Student(self.infolist[0],self.infolist[1]).remove_book(str(input("Please write the book's bid number that you want to delete from your list: ")))
            if option == 4:
                for item in Student(self.infolist[0],self.infolist[1]).show_borrowed_books():
                    print(f"{item}")
                    #yazı şekli düzenlenecek
            if option == 5:
                break
            if input("Continue? (Y/N)") == "y":
                continue
            else:
                break
    def display_users(self):
        print(UserDB().users_objects)

x = Main()
role=x.login()
if role=="student":
    x.show_student_menu()
else:
    x.show_admin_menu()


