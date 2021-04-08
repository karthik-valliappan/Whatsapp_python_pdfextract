import watchdog.events
import watchdog.observers
import time
from watchdog.events import FileSystemEventHandler
import os


class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        print(event.event_type, event.src_path)

    def on_created(self, event):
        os.system('python3 /Users/karthik/PycharmProjects/monitorfiles/whatsapp.py')


if __name__ == "__main__":
    src_path = r"/Users/karthik/Downloads/"
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
