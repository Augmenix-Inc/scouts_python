# If modifying these scopes, delete the file token.json.
from utils import init

def get_user_input():
    print(
        """
Welcome to Stacked Admin Console (Python), select an action:
1. Manage members
2. Manage progress badges
3. Manage event badges
4. Manage unit achievements
""")
    choice = input("Your choice (1-4): ")
    from utils import validate_choice_input
    while not validate_choice_input(choice, 4):
        choice = input("Invalid input. Re-enter your choice (1-4): ")
    if choice == "1":
        from members.members_main import get_members_user_input
        get_members_user_input()


if init():
    get_user_input()