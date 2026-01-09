import sys
import pygame
from pygame._sdl2 import Window
import time
import os
from pathlib import Path
import random
from Font.config import FontConfig
from Font.render import Renderer
from Font.funcs import cv2, putTTFText
import Font.character as character
from plyer import notification
import subprocess
import pybase64
from moviepy import VideoFileClip
import tempfile
import re
print("##############")
print("# Calculator #")
print("##############")
print("Made by An_npc *my name in roblox*")
print("Also if the python not working Download sys")
print("If there is bug please report it to my github")
print("Dont forget to give me a star in github!")
print("Created Date: 11/7/2025, Updated Date: 9/01/2026, Time: 10:14 AM")
def run_video_player():
    """A simple video player using OpenCV with sound support"""
    
    video_path = input("Enter the full path of the video file: ")
    
    # Check if the file exists
    if not Path(video_path).is_file():
        print("Error: File not found.")
        return choose_math_mode()
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return choose_math_mode()
    
    # Load video with moviepy to extract and play audio
    audio_path = None
    try:
        video = VideoFileClip(video_path)
        if video.audio is not None:
            print("Loading audio...")
            # Save audio to a temporary file
            temp_audio = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
            audio_path = temp_audio.name
            temp_audio.close()
            video.audio.write_audiofile(audio_path, verbose=False, logger=None)
            
            # Play audio with pygame
            pygame.mixer.init()
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()
            print("Audio loaded successfully!")
        else:
            print("No audio track found in video.")
        video.close()
    except Exception as e:
        print(f"Warning: Could not load audio: {e}")
    
    print("-" * 40)
    print("      VIDEO PLAYER WITH SOUND")
    print("-" * 40)
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("End of video or cannot read the video.")
            break
        
        cv2.imshow('Video Player', frame)
        
        # Press 'q' to exit the video player
        if cv2.waitKey(25) & 0xFF == ord('q'):
            print("Video playback stopped by user.")
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    # Stop music and clean up
    try:
        pygame.mixer.music.stop()
    except:
        pass
    
    # Clean up temporary audio file
    if audio_path:
        try:
            os.remove(audio_path)
        except:
            pass
    
    return choose_math_mode()
def run_music_playlist():
    """Play a music playlist using pygame.mixer"""
    pygame.mixer.init()
    
    # Define your playlist (add your music file paths here)
    playlist = [
        input("Please input the full path of your music file 1: "),
        input("Please input the full path of your music file 2: "),
        input("Please input the full path of your music file 3: "),
        input("Please input the full path of your music file 4: "),
        input("Please input the full path of your music file 5: ")
    ]
    
    current_track = 0
    playing = True
    
    print("-" * 40)
    print("      MUSIC PLAYLIST PLAYER")
    print("-" * 40)
    print(f"Playlist loaded: {len(playlist)} songs")
    
    while playing:
        try:
            # Load and play current track
            print(f"\nNow playing: {playlist[current_track]}")
            pygame.mixer.music.load(playlist[current_track])
            pygame.mixer.music.play()
            
            # Wait for music to finish
            while pygame.mixer.music.get_busy():
                time.sleep(5)
            
            # Move to next track
            current_track += 1
            
            # Loop playlist if at the end
            if current_track >= len(playlist):
                current_track = 0
                print("\nPlaylist finished. Looping...")
                
        except pygame.error as e:
            print(f"Error playing music: {e}")
            break
        except KeyboardInterrupt:
            print("\nPlaylist stopped by user")
            break
    
    pygame.mixer.music.stop()
    return choose_math_mode()
def run_pygame_mode_old():
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
            return choose_math_mode()
            pygame.quit()
        screen.fill("black")
        pygame.draw.rect(screen, "red", square_pos)
        pygame.draw.rect(screen, "blue", circle_pos) 
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
def choose_math_mode_old():
    print("Created Date: 11/1/2025, Updated Date: 11/2/2025, Time: 10:14 AM")
    print("Version: 1.0.0 TEST")
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
                    return choose_math_mode_old()
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
                    return run_pygame_mode_old()
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
                    else:
                        if thanks.lower() == "skibidi":
                            print("You Brainrot Kids, why You type it hahaha")
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
def run_pingpong_game():
    # Simple Ping Pong Game using Pygame 
    pygame.init()
    
    # Screen dimensions
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),  pygame.FULLSCREEN)
    pygame.display.set_caption("Ping Pong Game")
    clock = pygame.time.Clock()
    
    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    
    # Paddle dimensions
    PADDLE_WIDTH = 15
    PADDLE_HEIGHT = 90
    PADDLE_SPEED = 6
    
    # Ball dimensions
    BALL_SIZE = 10
    BALL_SPEED = 5
    
    # Paddle positions
    left_paddle = pygame.Rect(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = pygame.Rect(SCREEN_WIDTH - 25, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    # Ball position and velocity
    ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
    ball_velocity = [BALL_SPEED, BALL_SPEED]
    
    # Score
    left_score = 0
    right_score = 0
    font = pygame.font.Font(None, 74)
    
    running = True
    while running:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Paddle controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and left_paddle.bottom < SCREEN_HEIGHT:
            left_paddle.y += PADDLE_SPEED
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and right_paddle.bottom < SCREEN_HEIGHT:
            right_paddle.y += PADDLE_SPEED
        
        # Ball movement
        ball.x += ball_velocity[0]
        ball.y += ball_velocity[1]
        
        # Ball collision with top/bottom
        if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
            ball_velocity[1] = -ball_velocity[1]
        
        # Ball collision with paddles
        if ball.colliderect(left_paddle) and ball_velocity[0] < 0:
            ball_velocity[0] = -ball_velocity[0]
        if ball.colliderect(right_paddle) and ball_velocity[0] > 0:
            ball_velocity[0] = -ball_velocity[0]
        
        # Ball out of bounds
        if ball.left <= 0:
            right_score += 1
            ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
            ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            ball_velocity = [BALL_SPEED, BALL_SPEED]
        if ball.right >= SCREEN_WIDTH:
            left_score += 1
            ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
            ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            ball_velocity = [-BALL_SPEED, BALL_SPEED]
        
        # Drawing
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, left_paddle)
        pygame.draw.rect(screen, WHITE, right_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
        
        # Score display
        left_text = font.render(str(left_score), True, WHITE)
        right_text = font.render(str(right_score), True, WHITE)
        screen.blit(left_text, (SCREEN_WIDTH // 4, 50))
        screen.blit(right_text, (3 * SCREEN_WIDTH // 4, 50))
        
        pygame.display.flip()
        
        if left_score == 10:
            print("Left Player Wins!")
            time.sleep(2)
            pygame.quit()
            return choose_math_mode()
        if right_score == 10:
            print("Right Player Wins!")
            time.sleep(2)
            pygame.quit()
            return choose_math_mode()
    pygame.quit()
    return choose_math_mode()
def choose_math_mode():
    print("Version: 1.1.3 Demo")
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
        'Bootloader': 'Choose Your Boot',
        'Music': 'Music Playlist Player',
        'Notepad': 'Open My Notepad.py',
        'Base64': 'Base64 Encoder/Decoder',
        'Run': 'Windows Run Command',
        'Video': 'Video Player',
        'Folder':'A Folder'
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
                    number1 = float(input())
                    print("+")
                    number2 = float(input())
                    equal = number1 + number2
                    print("= "+str(equal))
                    
                if choice == '2':
                    
                    print("Please type the number for Minus the number")
                    numb1 = float(input())
                    print("-")
                    numb2 = float(input())
                    answer1 = numb1 - numb2
                    print("= "+str(answer1))
                    
                if choice == '3':
                    
                    print("Please input the number for Multiply the number")
                    numbe1 = float(input())
                    print("*")
                    numbe2 = float(input())
                    answer = numbe1 * numbe2
                    
                    print("= "+str(answer))
                if choice == '4':
                    
                    print("Please input the number for share *why share cuz is division* the number")
                    num1 = float(input())
                    print("/")
                    num2 = float(input())
                    equali = num1 / num2
                    print("= "+str(equali))
                    
                if choice == '5':
                    print("You in Pygame mode, Please wait the pygame open...")
                    print("Error Is in here")
                    return run_pingpong_game()
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
                    print("Please Choose the Error Mode.. You gona be kidding right?")
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
                if choice == 'Music':
                    
                    print("You in Music Playlist Player mode, Please wait the music player open...")
                    return run_music_playlist()
                if choice == 'Bootloader':
                    print("Restarting...")
                    time.sleep(5)
                    print("File Saved")
                    print("Loading...")
                    time.sleep(3)
                    
                    return bootloader_windows()
                if choice == 'Notepad':
                    print("You in Notepad mode, Please wait the notepad open...")
                    subprocess.run([sys.executable, "f:/Python File/My Notepad.py"])
                    
                    return choose_math_mode()
                if choice == 'Base64':
                    print("You in Base64 Encoder/Decoder mode, Please wait...")
                    subprocess.run([sys.executable, "f:/Python File/Untitled-1.py"])
                if choice == 'Run':
                    print("You in Windows Run Command mode, Please wait...")
                    command = input("Enter the command to run (e.g., notepad, calc): ")
                    exit_code = os.system(command)
                    if exit_code == 0:
                        print("Other Script ran successfully.")
                        
                        choose_math_mode()
                    else:
                        print(f"Other Script failed with exit code {exit_code}.")
                        
                        choose_math_mode()
                if choice == 'Video':
                    print("You in Video Player mode, Please wait the video player open...")
                    re.sub("")
                    return run_video_player()
                if choice == 'Folder':
                    print("You in Folder mode, Please wait the folder open...")
                    time.sleep(6)
                    Folderfile = [
                        'A:',
                        'C:',
                        'D:',
                        'USB Drive (E:)'
                    ]
                    print("Available Drives:")
                    for idx, drive in enumerate(Folderfile, start=1):
                        print(f"  [{idx}] {drive}")
                    print("You Cannot Access The Drives. We In Working On It.")
                    print("The Feature Will Be Available In Future Updates. Stay Tuned!")
                    print("You are in Demo Version of this Feature.")
                    print("Are You Want To Close The Folder Mode?")
                    close_folder = input("Type 'yes' to close or 'no' to return to mode chooser: ").strip().lower()
                    if close_folder in ['yes', 'ye', 'y', 'YES', 'Yes', 'Y']:
                        print("Closing Folder Mode...")
                        time.sleep(2)
                        
                        return choose_math_mode()
                    else:
                        print("Shutdowning...")
                        bootloader_windows()
                if choice == 'Dev Mode':
                    print("Welcome To Dev Mode")
                    Password = input("Please Input The Password To Access Dev Mode: ")
                    print("Password Is Hidded In Github")
                    if Password == "Pr0duc5Pass034dIsThis!":
                        print("Access Granted. Welcome to Dev Mode!")
                        time.sleep(2)
                        print("Loading Dev Version...")
                        time.sleep(3)
                        print("Are You Sure You Want To Download Dev Version?")
                        print("It's Available In Github. But The Version Is In Building. We Gona Make It!")
                        print("Wait The Info!")
                    else:
                        print("Access Denied. Incorrect Password.")
                        
                        return choose_math_mode()
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