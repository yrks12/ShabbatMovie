
```markdown
# Shabbat Movie Player

This project automates the process of playing movies using VLC Media Player at a scheduled time. It simulates user activity to prevent the computer from going idle and then plays movies from a specified folder.

## Requirements

- Python 3.x
- VLC Media Player

## Installation

1. Clone the repository or download the script files.
2. Install the required Python package using the following command:

   ```bash
   pip install pyautogui
   ```

## Configuration

1. Ensure that VLC Media Player is installed on your system. You can download it from [VideoLAN's official website](https://www.videolan.org/vlc/).
2. Verify that the path to the VLC executable (`vlc.exe`) in the script matches the actual installation path on your system. The default path in the script is:
   ```
   C:\Program Files (x86)\VideoLAN\VLC\vlc.exe
   ```
   Modify this path if your VLC is installed in a different location.

3. Set the `folder_path` variable in the script to the directory containing your movie files. The default path is:
   ```
   D:\ShabbatMovie
   ```

## Usage

1. Open a terminal or command prompt.
2. Run the script using the following command:

   ```bash
   python script_name.py
   ```

   Replace `script_name.py` with the actual name of the script file.

3. The script will wait until the scheduled time (Friday at 16:40) and then start simulating user activity.
4. After the simulation, it will open and play all movies in the specified folder one by one.

## Customization

- **Change Scheduled Time**: 
  To change the scheduled time, modify the `wait_for_time` function's parameters (`target_hour`, `target_minute`, and `target_weekday`).

- **Adjust User Activity Simulation**: 
  To modify the user activity simulation, you can change the actions in the `simulate_user_activity` function.

## Important Notes

- Ensure that the computer does not go into sleep mode, as this will interrupt the script.
- The script includes a fail-safe for `pyautogui` (moving the mouse to the top-left corner of the screen will abort the script).

## License

This project is licensed under the MIT License.

## Acknowledgments

- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) for simulating user input.
- [VideoLAN](https://www.videolan.org/) for VLC Media Player.
```
