from curses.ascii import isdigit


def validate_sclass_input(sclass: str):
    if len(sclass) != 5: return False
    if sclass[0] != "S": return False
    if not sclass[1].isdigit(): return False
    if not 1 <= int(sclass[1]) <= 4: return False
    if sclass[2:4] != "-0": return False
    if not sclass[4].isdigit(): return False
    if not 1 <= int(sclass[4]) <= 9: return False
    return True

def get_addmember_user_input():
    from utils import validate_choice_input
    print("Now adding a member, fill in the required details.")
    email = input("Enter email (must be a valid SST email): ")
    name = input("Enter name: ")
    sclass = input("Enter class (using format SX-0X): ")
    while not validate_sclass_input(sclass):
        sclass = input("Invalid input. Re-enter class (using format SX-0X): ")
    patrol = input("""Select patrol of member:
1. Exa
2. Nano
3. Tera
4. Zetta
Your choice (1-4): """)
    while not validate_choice_input(patrol, 4):
        patrol = input("Invalid input. Re-enter your choice (1-4): ")
    rank = input("""
Select patrol of member:
1. Patrol Leader
2. Assistant Patrol Leader
3. Logistics IC
4. Flag Raising IC
Your choice (1-4, leave blank for none): """)
    while not validate_choice_input(rank, 4) or rank == "":
        rank = input("Invalid input. Re-enter your choice (1-4, leave blank for none): ")
