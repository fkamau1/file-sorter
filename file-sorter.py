import os
from time import sleep
from shutil import move
from pathlib import Path, rglob 
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler

dest_folder = "/Users/Fredrick/Downloads"
src_folder = "/Users/Fredrick/Downloads/Documents"

class DocumentMoverHandler(FileSystemEventHandler):

    def on_created(self, event):
        self.on_modified(event)

    def on_modified(self, event):
        for entry in os.scandir("/Users/Fredrick/Downloads/Documents"):
            if (entry.is_file() and 
                entry.name.endswith((".doc", ".docx", ".pdf"))):
                move(entry.path, dest_folder)
                print(f"Moved {entry.name} to {dest_folder}")

    def move_existing(self, src_folder):
    
        for src_path in src_folder.rglob('*'):
            if src_path.is_file():
                dest_path = dest_folder + '/' + src_path.name
                if os.path.exists(dest_path):
                    os.remove(dest_path) 
                move(str(src_path), dest_path)

if __name__ == "__main__":
    event_handler = DocumentMoverHandler()
    observer = Observer()
    observer.schedule(event_handler, "/Users/Fredrick/Downloads/Documents", recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()