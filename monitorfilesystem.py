import watchdog.observers
import watchdog.events
import time
import os

####### filter based on the pattern matching ########

class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.pdf'], ignore_directories=True, case_sensitive=False)
        
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
