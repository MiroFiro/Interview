import os
import shutil
import time
import argparse

# Define a class for folder synchronization
class FolderSynchronizer:
    def __init__(self, source_folder, replica_folder, log_file):
        # Constructor to initialize FolderSynchronizer object with source folder, replica folder, and log file paths
        self.source_folder = source_folder
        self.replica_folder = replica_folder
        self.log_file = log_file

    def synchronize_folders(self):
        try:
            # Check if replica folder exists, remove it if it does
            if os.path.exists(self.replica_folder):
                shutil.rmtree(self.replica_folder)
            # Copy contents of source folder to replica folder
            shutil.copytree(self.source_folder, self.replica_folder)
            # Log synchronization completion
            self.log_event("Synchronization completed.")
        except Exception as e:
            # Log error if synchronization fails
            self.log_event(f"Error during synchronization: {str(e)}")

    def log_event(self, message):
        # Method to log event message with timestamp to both log file and console
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, 'a') as f:
            f.write(f"[{timestamp}] {message}\n")
        print(f"[{timestamp}] {message}")

# Main function to parse command line arguments and start synchronization process
def main():
    parser = argparse.ArgumentParser(description='Folder synchronization program')
    parser.add_argument('source_folder', type=str, help='Path to the source folder')
    parser.add_argument('replica_folder', type=str, help='Path to the replica folder')
    parser.add_argument('log_file', type=str, help='Path to the log file')
    parser.add_argument('interval', type=int, help='Synchronization interval in seconds')
    args = parser.parse_args()

    # Create FolderSynchronizer instance with provided arguments
    synchronizer = FolderSynchronizer(args.source_folder, args.replica_folder, args.log_file)

    # Perform synchronization periodically
    while True:
        synchronizer.synchronize_folders()
        time.sleep(args.interval)

# Entry point of the program
if __name__ == "__main__":
    main()