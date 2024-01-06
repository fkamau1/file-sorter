import os
from time import sleep
from shutil import move
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

src_folder = "C:\\Users\\Fredrick\\Downloads"
dest_folder = "C:\\Users\\Fredrick\\Downloads\\Documents"

#Destination folder validation
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)
    print(f"Destination folder {dest_folder} created.")

class DocumentMoverHandler(FileSystemEventHandler):
    def move_existing_files(self):
        for entry in os.scandir(src_folder):
            if entry.is_file() and entry.name.endswith((".doc", ".docx", ".pdf")):
                #move(entry.path, dest_folder)
                self.move_file(entry)
                print(f"Moved {entry.name} to {dest_folder}")

    def on_created(self, event):
        self.move_all_files()

    def on_modified(self, event):
        self.move_all_files()

    def move_all_files(self):
        for entry in os.scandir(src_folder):
            if entry.is_file() and entry.name.endswith((".doc", ".docx", ".pdf")):
                #move(entry.path, dest_folder)
                self.move_file(entry)
                print(f"Moved {entry.name} to {dest_folder}")

    def move_file(self, entry):
        # Check if the source and destination folders are different
        if entry.path != dest_folder:
            try:
                move(entry.path, os.path.join(dest_folder, entry.name))
                print(f"Moved {entry.name} to {dest_folder}")
            except Exception as e:
                print(f"Error moving {entry.name}: {e}")

if __name__ == "__main__":
    event_handler = DocumentMoverHandler()

    # Move existing files immediately upon starting the script
    event_handler.move_existing_files()

    observer = Observer()
    observer.schedule(event_handler, src_folder, recursive=True)
    observer.start()

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()