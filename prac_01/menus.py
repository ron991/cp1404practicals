# display menu
# get choice
# while choice != quit option
#     if choice == first option
#         do first task
#     else if choice == <second option>
#         do second task
#     ...
#     else if choice == <n-th option>
#         do n-th task
#     else
#         display invalid input error message
#     display menu
#     get choice
# do final thing, if needed


MENU = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
print(MENU)
menu_choice = input("").upper()
while menu_choice != "Q":
    if menu_choice == "H":
        print(f"Hello {name}")
    elif menu_choice == "G":
        print(f"Goodbye {name}")
    else:
        print(f"Invalid choice")
        menu_choice = input("").upper()
print(f"Finished.")