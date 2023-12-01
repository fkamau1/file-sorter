import os
from time import sleep
from shutil import move
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

src_folder = "/Users/Fredrick/Downloads/Documents"
dest_folder = "/Users/Fredrick/Downloads"

class DocumentMoverHandler(FileSystemEventHandler):
    def move_existing_files(self):
        for entry in os.scandir(src_folder):
            if entry.is_file() and entry.name.endswith((".doc", ".docx", ".pdf")):
                move(entry.path, dest_folder)
                print(f"Moved {entry.name} to {dest_folder}")

    def on_created(self, event):
        self.move_all_files()

    def on_modified(self, event):
        self.move_all_files()

    def move_all_files(self):
        for entry in os.scandir(src_folder):
            if entry.is_file() and entry.name.endswith((".doc", ".docx", ".pdf")):
                move(entry.path, dest_folder)
                print(f"Moved {entry.name} to {dest_folder}")

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