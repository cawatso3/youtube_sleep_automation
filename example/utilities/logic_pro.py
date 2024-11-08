import subprocess
import logging
import os
import time
from datetime import datetime


class LogicProAutomation:
    def __init__(self, scpt_path):
        """
        Initialize the LogicProAutomation class with the path to the .scpt file.

        Parameters:
        - scpt_path (str): Path to the compiled AppleScript (.scpt) file for Logic Pro automation.
        """
        self.scpt_path = os.path.abspath(scpt_path)
        self.temp_file = "/tmp/logic_pro_audio_path.txt"  # Temporary file for passing the audio file path
        self.verify_script_path()
        logging.info(f"LogicProAutomation initialized with script path: {self.scpt_path}")

    def verify_script_path(self):
        """Verify that the .scpt file exists at the specified path."""
        if not os.path.exists(self.scpt_path):
            raise FileNotFoundError(f"The specified AppleScript file was not found: {self.scpt_path}")

    def set_script_path(self, new_path):
        """
        Update the .scpt file path if needed.

        Parameters:
        - new_path (str): New path to the compiled AppleScript (.scpt) file.
        """
        self.scpt_path = os.path.abspath(new_path)
        self.verify_script_path()
        logging.info(f"Script path updated to: {self.scpt_path}")

    def run_automation(self, target_folder, save_to_folder):
        """
        Execute the AppleScript automation for Logic Pro.

        Parameters:
        - target_folder (str): Folder containing the music files to be imported.
        - save_to_folder (str): Dynamic output directory where the bounced file will be saved.
        """
        # Run the AppleScript with the target and save folders as environment variables
        logging.info("Starting Logic Pro automation for audio looping and export...")
        process = subprocess.Popen(
            ["osascript", self.scpt_path],
            env={"targetFolder": target_folder, "saveToFolder": save_to_folder},
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        # Monitor the output directory until the new file appears
        logging.info("Waiting for Logic Pro to complete the bounce and save the file...")
        latest_file = None
        latest_mtime = None

        while True:
            files = [os.path.join(save_to_folder, f) for f in os.listdir(save_to_folder)]
            files = [f for f in files if os.path.isfile(f)]

            if not files:
                time.sleep(1)
                continue

            most_recent_file = max(files, key=os.path.getmtime)
            most_recent_mtime = os.path.getmtime(most_recent_file)

            if most_recent_file != latest_file:
                latest_file = most_recent_file
                latest_mtime = most_recent_mtime
                logging.info(f"New file detected: {latest_file}. Waiting for completion...")
            elif most_recent_mtime == latest_mtime:
                logging.info(f"File '{latest_file}' appears to be saved completely.")
                break
            else:
                latest_mtime = most_recent_mtime

            time.sleep(1)

        return latest_file


# Usage example
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Initialize the LogicProAutomation class with the .scpt file path
    logic_pro_automation = LogicProAutomation("logic_pro_loop_and_bounce.scpt")

    # Define target and save folders
    target_folder = "/Users/mac/PycharmProjects/youtube_sleep_automation/staging_files/music"
    save_to_folder = "/Users/mac/PycharmProjects/youtube_sleep_automation/staging_files/10_hr_looped_music"

    # Run the automation process
    output_file = logic_pro_automation.run_automation(target_folder, save_to_folder)

    # Continue with the pipeline using `output_file`
    logging.info(f"File ready for further processing: {output_file}")
