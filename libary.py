class library:
    def __init__(self,list,name):
        self.bookslist=list
        self.name=name
        self.lendDict={}
    
    def displaybooks(self):
        print(f"we have the following  books in the libary: {self.name}")
        for book in self.bookslist:
            print(book)
    
    def lendbook(self,user,book):
        if book  not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print(f"lender-book in datebase in updated ,you can take the books")
        else:
            print(f"book is already taken by{self.lendDict[book]}")
    

    def addbook(self,book):
        self.bookslist.append(book)
        print("book has been added to book list")
    
    def returnbook(self,book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    keshav  =  library(['python','java','c++','c'],"tatacompany")

    while(True):
        print(f"welcome to {keshav.name} libr3pythonary .enter your choice ")
        print("1. display a book")
        print("2. lend  a book")
        print("3. add a book")
        print("4. return  a book")
        user_choice=input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice==1:
            keshav.displaybooks()
        
        elif user_choice==2:
             book=input ("enter the name of the book:")
             user =input("enter your name")
             keshav.lendbook(user, book)
        
        elif user_choice==3:
            book=input("enter the name of the bokk you want to add: ")
            keshav.addbook(book)
        
        elif user_choice==4:
            book=input("enter the name of the book you want to return :")
            keshav.returnbook(book)
        
        else:
            print("not a valid option")
        

        print("press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 =  input()
            if user_choice2==  "q":
                exit()
            if user_choice2==  "c":
                continue


         
            


    