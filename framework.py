import signal
import sys
import time
import threading

def signal_handler(sig, frame):
    print('\nYou pressed Ctrl+C or sent a SIGTERM signal. Shutting down gracefully...')
    sys.exit(0)

def print_time():

    while True:
        print(time.ctime())
        time.sleep(10)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    print('Press Ctrl+C or send a SIGTERM signal to stop')
    t = threading.Thread(target=print_time)
    t.start()

if __name__ == "__main__":
    main()