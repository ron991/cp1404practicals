"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
"""
Enter name: Guido
(H)ello
(G)oodbye
(Q)uit
>>> A
Invalid choice
(H)ello
(G)oodbye
(Q)uit
>>> H
Hello Guido
(H)ello
(G)oodbye
(Q)uit
>>> G
Goodbye Guido
(H)ello
(G)oodbye
(Q)uit
>>> Q
Finished.
"""


def main():
    menu = "(H)ello\n(G)oodbye\n(Q)uit"
    name = input("Please enter your name: ")
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "H":
            print("Hello", name)
        elif choice == "G":
            print("Goodbye", name)
        else:
            print("Invalid choice")
        print(menu)
        choice = input(">>> ").upper()
    print("Finished.")


main()
