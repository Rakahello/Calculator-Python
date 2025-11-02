import sys
import pygame
from pygame._sdl2 import Window
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
def old_calculator_ver():
    print("##############")
print("# Calculator #")
print("##############")
print("Made by An_npc *my name in roblox*")
print("Also if the python not working Download sys")
print("If there is bug please report it to my github")
print("Dont forget to give me a star in github!")
print("Created Date: 11/1/2025, Updated Date: 11/2/2025, Time: 10:14 AM")
print("Version: 1.0.0")
def run_pygame_mode():
    pygame.init()
    screen = pygame.display.set_mode((845, 768),  pygame.RESIZABLE)
    window = Window.from_display_module()
    pygame.display.set_caption("Games")
    clock = pygame.time.Clock()
    square_pos = pygame.Rect(400, 400, 50, 50)
    circle_pos = pygame.Rect(400,300,40,40)
    while True:
        if pygame.event.get(pygame.QUIT): break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            circle_pos.y -= 20
        if keys[pygame.K_DOWN]:
            circle_pos.y += 20
        if keys[pygame.K_LEFT]:
            circle_pos.x -= 20
        if keys[pygame.K_RIGHT]:
            circle_pos.x += 20
        if keys[pygame.K_w]:
            square_pos.y -= 20
        if keys[pygame.K_s]:
            square_pos.y += 20
        if keys[pygame.K_a]:
            square_pos.x -= 20
        if keys[pygame.K_d]:
            square_pos.x += 20
        if keys[pygame.K_ESCAPE]:
            return choose_math_mode()
            pygame.quit()
        screen.fill("black")
        pygame.draw.rect(screen, "red", square_pos)
        pygame.draw.rect(screen, "blue", circle_pos) 
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
def choose_math_mode_old():
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
                    return choose_math_mode_old()
                if choice == '3':
                    print("Please input the number for Multiply the number")
                    numbe1 = int(input())
                    print("*")
                    numbe2 = int(input())
                    answer = numbe1 * numbe2
                    print("= "+str(answer))
                    return choose_math_mode_old()
                if choice == '4':
                    print("Please input the number for share *why share cuz is division* the number")
                    num1 = int(input())
                    print("/")
                    num2 = int(input())
                    equali = num1 / num2
                    print("= "+str(equali))
                    return choose_math_mode_old()
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
                        return bootloader_windows()
                    if thanks.lower() != "notexit":
                        return choose_math_mode_old()
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
def bootloader_windows():
    print("-" * 40)
    print("Bootloader Windows")
    print("-" * 40)
    modeboot = {
        '1': 'Start Calculator_Good.py',
        '2': 'Exit Bootloader',
        '3': 'Old Calculator Version'
    }
    for key, value in modeboot.items():
        print(f"  [{key}] {value}")
    bootchoice = None
    while bootchoice is None:
        bootinput = input("Enter the number of your choice (1-3): ").strip()
        if bootinput in modeboot:
            bootchoice = modeboot[bootinput]
            print(f"You have selected the {bootchoice} mode.")
            if bootinput == '1':
                print("Starting Calculator_Good.py...")
                time.sleep(2)
                return choose_math_mode()
            if bootinput == '2':
                print("Exiting Bootloader. Goodbye!")
                time.sleep(2)
                sys.exit(0)
            if bootinput == '3':
                print("Starting Old Calculator Version...")
                time.sleep(2)
                return choose_math_mode_old()
        else:
            print(f"Error: '{bootinput}' is not a valid option. Please enter a number between 1 and 2.")
def run_virus_mode():
    print("-" * 40)
    print("Welcome To Delete Mode")
    print("This mode will delete some functions in the program")
    print("Prossing...")
    print("Def run_pygame_mode(): is Deleted")
    print("Please wait...")
    time.sleep(5)
    print("def choose_math_mode(): is Deleted")
    print("Program is deleted")
    time.sleep(3)
    print("Program is not responding")
    print("Downloading Program.exe......")
    time.sleep(19)
    print("Download complete")
    print("Restrting...")
    print("-" * 40)
    print("Cmd.exe")
    print("-" * 40)
    print("taskkill /f /im Calculator_Good.py")
    print(".\Calculator_Good.py")
    print("Error: F:\Python File\Calculator_Good.py not responding")
    print("Please wait...")
    print("Error: Still not responding")
    moderun = {
        '1': 'Close Program',
        '2': 'Wait The program to respond'
    }
    for key, value in moderun.items():
        print(f"  [{key}] {value}")
    modchoice = None
    while modchoice is None:
        modinput = input("Enter the number of your choice (1-2): ").strip()
        if modinput in moderun:
            modchoice = moderun[modinput]
            print(f"You have selected the {modchoice} mode.")
            if modinput == '1':
                print("Closing the program...")
                time.sleep(3)
                return bootloader_windows()
            if modinput == '2':
                print("Waiting for the program to respond...")
                time.sleep(10)
                print("Program is responding now returning to mode chooser...")
                time.sleep(2)
                return choose_math_mode()
        else:
            print(f"Error: '{modinput}' is not a valid option. Please enter a number between 1 and 2.")
            return choose_math_mode()
def run_pygame_mode():
    pygame.init()
    screen = pygame.display.set_mode((545, 568),  pygame.RESIZABLE)
    window = Window.from_display_module()
    pygame.display.set_caption("Games")
    clock = pygame.time.Clock()
    square_pos = pygame.Rect(400, 400, 50, 50)
    circle_pos = pygame.Rect(400,300,40,40)
    while True:
        if pygame.event.get(pygame.QUIT): break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            circle_pos.y -= 20
        if keys[pygame.K_DOWN]:
            circle_pos.y += 20
        if keys[pygame.K_LEFT]:
            circle_pos.x -= 20
        if keys[pygame.K_RIGHT]:
            circle_pos.x += 20
        if keys[pygame.K_w]:
            square_pos.y -= 20
        if keys[pygame.K_s]:
            square_pos.y += 20
        if keys[pygame.K_a]:
            square_pos.x -= 20
        if keys[pygame.K_d]:
            square_pos.x += 20
        if keys[pygame.K_ESCAPE]:
            print("Exitting...")
            time.sleep(1)
            pygame.quit()
            return choose_math_mode()
        screen.fill("black")
        pygame.draw.rect(screen, "red", square_pos)
        pygame.draw.rect(screen, "blue", circle_pos) 
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
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
        '6': 'Exit if you want to exit',
        '2002Error': '',
        'Bootloader': 'Choose Your Boot'
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
                if choice == '2002Error':
                    moerror = {
                        '1': 'Python2002er',
                        '21': 'PythonGem'
                    }
                    print("Please Choose the Error Mode.. Error190w1")
                    for key, value in moerror.items():
                        print(f"  [{key}] {value}")
                    errchoice = None
                    while errchoice is None:
                        errinput = input("Enter the number of your choice (1-2): ").strip()
                        if errinput in moerror:
                            errchoice = moerror[errinput]
                            print(f"You have selected the {errchoice} mode.")
                            if errinput == '1':
                                print("Error Python is gliching status.")
                                print("Please wait...")
                                time.sleep(5)
                                print("Error fixed now you can use the calculator again.")
                                print("Main menu is Unknown status.")
                                print("Waiting for 10 seconds to return to main menu...")
                                print("Returning to Main Menu...")
                                print("Main Menu.pyc is not available.")
                                print("Please wait...")
                                print("downloading Main Menu.pyc...")
                                time.sleep(10)
                                print("Download complete.")
                                print("Restarting the program...")
                                return bootloader_windows()
                            if errinput == '21':
                                print("Error Game is loading...")
                                time.sleep(5)
                                print("Game is not working now returning to mode chooser...")
                                time.sleep(3)
                                print("Error, The return is failed, Please try again.")
                                print("Returning to Main Menu...")
                                time.sleep(10)
                                print("Error Main Menu not responding, Restarting the program...")
                                return run_virus_mode()
                            
                        else:
                            print(f"Error: '{errinput}' is not a valid option. Please enter a number between 1 and 2.")
                            return choose_math_mode()
                if choice == 'Bootloader':
                    return bootloader_windows()
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