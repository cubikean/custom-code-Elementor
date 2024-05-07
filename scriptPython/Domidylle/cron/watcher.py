#!/usr/bin/env python
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil

class Watcher(FileSystemEventHandler):
    def process(self, event):
        """
        Process the event, in this case, execute your script.
        """
        # Check if the event is the creation of a new file
        if event.is_directory:
            return

        # Check if the new file is annonces.csv
        if event.src_path.endswith('Annonces.csv'):
            # Run your script
            print('Appel de cronAnnoncesModifier')
            os.system('cronAnnoncesModifier.py')

            # Rename the processed file with timestamp
            timestamp = time.strftime("%Y%m%d%H%M%S")
            new_name = f'annonces_{timestamp}.csv'
            os.rename('annonces.csv', new_name)

            # Move the processed file to 'pastAnnonces' folder
            past_folder = 'pastAnnonces'
            if not os.path.exists(past_folder):
                os.makedirs(past_folder)
            
            shutil.move(new_name, os.path.join(past_folder, new_name))

    def on_created(self, event):
        self.process(event)

if __name__ == "__main__":
    # Define the directory to watch
    directory_to_watch = '.'

    event_handler = Watcher()
    observer = Observer()
    observer.schedule(event_handler, directory_to_watch, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
