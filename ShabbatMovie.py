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
    Moves the cursor in a square pattern and clicks at each corner,
    simulating keyboard activity by pressing 'Caps Lock'.
    """
    try:
        screen_width, screen_height = pyautogui.size()
        for _ in range(5):  # Number of interaction cycles
            pyautogui.moveTo(screen_width / 2, screen_height / 2)  # Move to the center
            pyautogui.click()  # Click at the center
            pyautogui.press('capslock')  # Press 'Caps Lock'
            time.sleep(1)
            pyautogui.moveRel(100, 0)  # Move right
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveRel(0, 100)  # Move down
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveRel(-100, 0)  # Move left
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveRel(0, -100)  # Move up
            pyautogui.click()
            time.sleep(1)
    except pyautogui.FailSafeException:
        print("Fail-safe triggered")
    except Exception as e:
        print(f"An error occurred: {e}")

def wait_for_time(target_hour=16, target_minute=40, target_weekday=5):
    """
    Waits until the specified time (default is Friday at 16:40) before proceeding.
    """
    now = datetime.now()
    scheduled_time = now.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)
    if now.weekday() != target_weekday:
        # Calculate days ahead to the next occurrence of the target weekday
        days_ahead = target_weekday - now.weekday()
        if days_ahead <= 0:  # If the target day has already passed this week
            days_ahead += 7
        scheduled_time += timedelta(days=days_ahead)
    print(f"Scheduled to start on {scheduled_time.strftime('%A, %Y-%m-%d at %H:%M:%S')}")
    while datetime.now() < scheduled_time:
        time.sleep(30)  # Sleep for 30 seconds to reduce CPU usage

def open_movies(folder_path):
    """
    Opens and plays movies in the specified folder using VLC Media Player.
    Plays all .mp4 and .mkv files in fullscreen mode.
    """
    vlc_path = r'C:\Program Files (x86)\VideoLAN\VLC\vlc.exe'  # Ensure VLC path is correct
    for file in os.listdir(folder_path):
        if file.endswith(('.mp4', '.mkv')):  # Check for video files
            file_path = os.path.join(folder_path, file)
            print(f"Starting movie: {file} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            process = subprocess.Popen([vlc_path, '--fullscreen', '--play-and-exit', file_path])
            process.wait()  # Wait for the video to finish before opening the next one

def main():
    """
    Main function to orchestrate waiting, simulating user activity, and playing movies.
    """
    folder_path = r'D:\ShabbatMovie'  # Folder containing the movie files
    wait_for_time()  # Wait until the scheduled time
    simulate_user_activity()  # Simulate user activity
    open_movies(folder_path)  # Play movies
    print("All movies played successfully.")

if __name__ == "__main__":
    main()
