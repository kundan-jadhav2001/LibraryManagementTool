def returnbook():
    id = input("Give id of book which you want to return : ")
    book = open("V://KUNDAN//Launguage//python//projects//storage.txt", "r")
    lines = book.readlines()
    linenum = 0
    for line in lines:
        if str(line[:2])== id:
            if line[-2:-1] == str(1):
                print("\t\tBook returned sucessfully\n")
                lines[linenum] = line[:-2] + "0\n"
                book.close()
                book = open("V://KUNDAN//Launguage//python//projects//storage.txt", "w")
                for x in lines:
                    book.write(x)
            else:
                print("\t\tThis book doesn't belong to you.\n")
        linenum+=1
    book.close()
def getbook():
    id = input("Give id of book which you want : ")
    book = open("V://KUNDAN//Launguage//python//projects//storage.txt", "r")
    lines = book.readlines()
    linenum = 0
    for line in lines:
        if str(line[:2])== id:
            if line[-2:-1] == str(0):
                print("\t\tThis book is now yours. Happy reading.\n")
                lines[linenum] = line[:-2] + "1\n"
                book.close()
                book = open("V://KUNDAN//Launguage//python//projects//storage.txt", "w")
                for x in lines:
                    book.write(x)
            else:
                print("\t\tThis book isn't avalible.\n")
        linenum+=1
    book.close()
def availablebook():
    book = open("V://KUNDAN//Launguage//python//projects//storage.txt", "r")
    lines = book.readlines()
    print("Avalible books are : ")
    for line in lines:
        if line[-2:-1] == str(0):
            print("\t",line[:-2])
    print("")
    book.close()

def yourbook():
    book = open("V://KUNDAN//Launguage//python//projects//storage.txt", "r")
    lines = book.readlines()
    print("Books you have are : ")
    for line in lines:
        if line[-2:-1] == str(1):
            print("\t",line[:-2])
    print("")
    book.close()

if __name__ == "__main__":
    choice = 1
    while (choice!=0):
        choice = int(input("Press 1 for see available books\nPress 2 for returning book\nPress 3 for buy a book\nPress 4 for see book you bought\nPress 0 for exit.\n"))
        if choice == 1:
            availablebook()
        elif choice == 2:
            returnbook()
        elif choice == 3:
            getbook()
        elif choice == 4:
            yourbook()
