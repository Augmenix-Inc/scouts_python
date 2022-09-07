import utils
import progressbadges.prog_requirements_completion

def get_prog_user_input():
    print(
        """
Now managing progress badges, select an action:
1. Update badge requirements completion status for single member
2. Update badge requirements completion status for all members
3. Update badge requirements completion status for members from a spreadsheet (coming soon)
4. Update progress badge completion status for single member
5. Update progress badge completion status for all members
6. Update progress badge completion status for members from a spreadsheet (coming soon)
b. Go back (to previous menu)
""")
    choice = input("Your choice (1-4, b): ")
    while not utils.validate_choice_input(choice, 4):
        choice = input("Invalid input. Re-enter your choice (1-4): ")
    print("")
    if choice == "1":
        progressbadges.prog_requirements_completion.get_update_member_req_user_input()
    elif choice == "b":
        utils.get_first_user_input()
