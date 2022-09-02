def get_members_user_input():
    print(
        """
Now managing members, select an action:
1. Add member
2. Add multiple members from a spreadsheet
3. Remove member
4. Update details of member
""")
    choice = input("Your choice (1-4): ")
    from utils import validate_choice_input
    while not validate_choice_input(choice, 4):
        choice = input("Invalid input. Re-enter your choice (1-4): ")
    if (choice == "1"):
        from members.members_1 import get_addmember_user_input
        get_addmember_user_input()
