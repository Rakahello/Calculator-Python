import sys
import time
print("##############")
print("# Calculator #")
print("##############")
print("Made by An_npc *my name in roblox*")
print("Also if the python not working Download sys")
print("If there is bug please report it to my github")
print("Dont forget to give me a star in github!")
print("Created Date: 11/1/2025, Updated Date: 11/2/2025, Time: 10:14 AM")
print("Version: 1.0.0")
def choose_math_mode():
    """
    Presents a menu for the user to select an arithmetic operation mode.
    Returns the name of the chosen mode as a string.
    """
    
    # Define the available modes using a dictionary for easy mapping
    modes = {
        '1': 'Addition (+)',
        '2': 'Subtraction (-)',
        '3': 'Multiplication (*)',
        '4': 'Division (/)',
        '5': 'Pygame(simple game damn)',
        '6': 'Exit if you want to exit'
    }

    print("-" * 40)
    print("      MATH MODE SELECTOR")
    print("-" * 40)
    
    # Display the menu options
    print("Please choose an operation mode:")
    for key, value in modes.items():
        print(f"  [{key}] {value}")
        
    print("-" * 40)

    chosen_mode = None

    # Loop until a valid choice is made
    while chosen_mode is None:
        try:
            # Get user input
            choice = input("Enter the number of your choice (1-5): ").strip()
            
            # Check if the choice key exists in the modes dictionary
            if choice in modes:
                chosen_mode = modes[choice]
                
                # Confirmation message
                print("\n" + "=" * 40)
                print(f"SUCCESS: You have selected the {chosen_mode} mode.")
                print("=" * 40)
                
                # Optional: demonstrate a simple use case
                if choice == '1':
                    print("Please type the number for Add the number")
                    number1 = int(input())
                    print("+")
                    number2 = int(input())
                    equal = number1 + number2
                    print("= "+str(equal))
                    return choose_math_mode()
                if choice == '2':
                    print("Please type the number for Minus the number")
                    numb1 = int(input())
                    print("-")
                    numb2 = int(input())
                    answer1 = numb1 - numb2
                    print("= "+str(answer1))
                    return choose_math_mode()
                if choice == '3':
                    print("Please input the number for Multiply the number")
                    numbe1 = int(input())
                    print("*")
                    numbe2 = int(input())
                    answer = numbe1 * numbe2
                    print("= "+str(answer))
                    return choose_math_mode()
                if choice == '4':
                    print("Please input the number for share *why share cuz is division* the number")
                    num1 = int(input())
                    print("/")
                    num2 = int(input())
                    equali = num1 / num2
                    print("= "+str(equali))
                    return choose_math_mode()
                if choice == '5':
                    print("You in Pygame mode, Please wait the pygame open...")
                    return run_pygame_mode()
                if choice == '6':
                    print("Exiting the program. Goodbye!")
                    print(10)
                    time.sleep(1)
                    print(9)
                    time.sleep(1)
                    print(8)
                    time.sleep(1)
                    print(7)
                    time.sleep(1)
                    print(6)
                    time.sleep(1)
                    print(5)
                    time.sleep(1)
                    print(4)
                    time.sleep(1)
                    print(3)
                    time.sleep(1)
                    print(2)
                    time.sleep(1)
                    print(1)
                    time.sleep(1)
                    print("Exiting the program...")
                    print("If you want to be faster in exit, Please Press Ctrl+C or Ctrl+Z")
                    thanks = input("Please type 'thanks' to exit: ")
                    if thanks.lower() == "thanks":
                        sys.exit(0)
                    if thanks.lower() != "notexit":
                        return choose_math_mode()
                    sys.exit(0)
                return chosen_mode
            else:
                # Handle invalid numbers or letters
                print(f"Error: '{choice}' is not a valid option. Please enter a number between 1 and 5.")
                
        except EOFError:
            # Handle Ctrl+D/Ctrl+Z (End of File)
            print("\nExiting the mode chooser.")
            sys.exit(0)
        except Exception as e:
            # Catch other unexpected errors
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)
# Entry point of the script
if __name__ == "__main__":
    mode = choose_math_mode()
    # You can now use the 'mode' variable (e.g., 'Addition (+)') in the rest of your program
    # print(f"\nYour program is now running in: {mode}")


