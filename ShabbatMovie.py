from datetime import datetime, timedelta
import os
import subprocess
import pyautogui
import time

# Enable the failsafe for PyAutoGUI to ensure safety during testing
pyautogui.FAILSAFE = True

def simulate_user_activity():
    """
    Simulates user activity to prevent the computer from going idle.
    This function moves the cursor in a square pattern around the screen 
    and performs clicks at each corner. It also presses the 'Caps Lock' key 
    during the process to simulate keyboard activity.

    The cursor moves to the center of the screen, performs actions, and then moves
    right, down, left, and up, clicking at each point. The process is repeated 5 times
    with a 1-second delay between each action.
    
    PyAutoGUI's fail-safe mechanism is enabled, allowing the user to interrupt 
    the script by moving the mouse to the upper-left corner of the screen.
    """
    try:
        screen_width, screen_height = pyautogui.size()  # Get the screen resolution
        for _ in range(5):  # Simulate activity for 5 cycles
            # Move cursor to the center of the screen and click
            pyautogui.moveTo(screen_width / 2, screen_height / 2)
            pyautogui.click()  # Click at the center of the screen
            pyautogui.press('capslock')  # Press the 'Caps Lock' key

            # Move and click at different directions relative to the current position
            time.sleep(1)
            pyautogui.moveRel(100, 0)  # Move 100 pixels to the right
            pyautogui.click()  # Click at the new position

            time.sleep(1)
            pyautogui.moveRel(0, 100)  # Move 100 pixels down
            pyautogui.click()  # Click at the new position

            time.sleep(1)
            pyautogui.moveRel(-100, 0)  # Move 100 pixels to the left
            pyautogui.click()  # Click at the new position

            time.sleep(1)
            pyautogui.moveRel(0, -100)  # Move 100 pixels up
            pyautogui.click()  # Click at the new position

            time.sleep(1)
    
    except pyautogui.FailSafeException:
        # Handle if the fail-safe is triggered by moving the mouse to the top-left corner
        print("Fail-safe triggered. Exiting user activity simulation.")
    except Exception as e:
        # Catch and print any unexpected errors during simulation
        print(f"An error occurred during user activity simulation: {e}")

def wait_for_time(target_hour=16, target_minute=40, target_weekday=5):
    """
    Pauses the execution of the script until a specified time is reached.
    The default target is Friday (weekday=5) at 16:40, but this can be customized.

    The function calculates how much time is left until the next occurrence of the 
    specified day and time. If the current weekday is after the target, it waits until 
    the next week. The script checks the time every 30 seconds to minimize CPU usage.

    Args:
        target_hour (int): The hour of the day to wait for (24-hour format). Default is 16 (4 PM).
        target_minute (int): The minute of the target time. Default is 40.
        target_weekday (int): The weekday to wait for (0=Monday, 6=Sunday). Default is 5 (Friday).
    """
    now = datetime.now()  # Get the current time
    scheduled_time = now.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)  # Set the scheduled time
    
    if now.weekday() != target_weekday:
        # Calculate how many days ahead the next occurrence of the target weekday is
        days_ahead = target_weekday - now.weekday()
        if days_ahead <= 0:
            # If the target weekday has already passed this week, set it for the next week
            days_ahead += 7
        # Add the calculated days to the scheduled time
        scheduled_time += timedelta(days=days_ahead)

    print(f"Scheduled to start on {scheduled_time.strftime('%A, %Y-%m-%d at %H:%M:%S')}")

    # Continuously check the time until the scheduled time is reached
    while datetime.now() < scheduled_time:
        time.sleep(30)  # Sleep for 30 seconds between checks to reduce CPU usage

def open_movies(folder_path):
    """
    Opens and plays video files from the specified folder using VLC Media Player.
    The function looks for all `.mp4` and `.mkv` files in the directory and plays 
    them in fullscreen mode sequentially. It waits for each movie to finish before 
    starting the next one.

    Args:
        folder_path (str): The path to the folder containing movie files.
    """
    # Path to VLC Media Player (ensure it's correctly installed at this location)
    vlc_path = r'C:\Program Files (x86)\VideoLAN\VLC\vlc.exe'
    
    # Iterate through all files in the folder
    for file in os.listdir(folder_path):
        if file.endswith(('.mp4', '.mkv')):  # Only process video files with .mp4 or .mkv extensions
            file_path = os.path.join(folder_path, file)  # Full path to the file
            print(f"Starting movie: {file} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            # Start VLC Media Player in fullscreen mode and wait for the movie to finish
            process = subprocess.Popen([vlc_path, '--fullscreen', '--play-and-exit', file_path])
            process.wait()  # Wait until the movie finishes before playing the next one

def main():
    """
    The main orchestration function that runs the script.
    It waits for the scheduled time, simulates user activity to prevent the computer 
    from going idle, and finally plays all movies from a specified folder.
    """
    folder_path = r'D:\ShabbatMovie'  # Path to the folder where movies are stored

    wait_for_time()  # Wait until the specified time
    simulate_user_activity()  # Simulate user activity to prevent the system from idling
    open_movies(folder_path)  # Play movies from the folder

    print("All movies played successfully.")  # Print a completion message

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
