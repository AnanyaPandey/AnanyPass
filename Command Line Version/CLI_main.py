import pyperclip
import time
from Functions import * 
from CheckPasswordStrength import check_password_strength

class TextColors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"

def main():
    # ... (same as in your original code)
    try:
        while True:
            passwords = generate_passwords()
            print("")
            print("Press Number to Select Chosen Password")
            print(TextColors.MAGENTA +"Press 11 to Regenerate Strong passwords"+TextColors.RESET)
            choice = int(input("OR Press ENTER to Exit: "))
            if choice != 11:
                
                if 1 <= choice <= len(passwords):
                    pyperclip.copy(passwords[choice - 1])
                    copied_text = pyperclip.paste()
                    if copied_text == passwords[choice - 1]: # Condition to check if copied to clipboard
                        print("")
                        print(TextColors.GREEN +"Password copied to clipboard!"+TextColors.RESET)

                        # Checking Strenght of the Password
                        Strenghdata = check_password_strength(passwords[choice - 1])
                        print(f"Great Choice - {Strenghdata[0]}")
                        print(f"It will take {Strenghdata[1]} Years to Crack the Password")
                        print(TextColors.RED +"------------------------------------------------------------"+TextColors.RESET)

                        # Giving Option to Save it in the Record with name of account or App
                        print("")
                        save_choice = input("What app or account do you want to save this with: ")
                        row = [passwords[choice - 1], save_choice]
                        CreateExcel(row)

                        #Feedback if succesfully added to the record
                        print(TextColors.GREEN + f"{row} - Added to the Passwords Records"+TextColors.RESET)
                        print("")
                        print(TextColors.CYAN +"Thanks for Using AnanyPass"+TextColors.RESET)
                        time.sleep(3)
                    else:
                        print("Copying to clipboard failed.")
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")
            elif choice == 11:
                pass
    except ValueError:
        print('Exiting')
        print(TextColors.CYAN +"Thanks for Using AnanyPass"+TextColors.RESET)
        time.sleep(2)

if __name__ == "__main__":
    main()
