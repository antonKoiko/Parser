import os
import signal
import sys
import time
import threading

def print_current_time(interval):
    while True:
        current_time = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
        print(f"Current Time: {current_time}")
        time.sleep(interval)

def signal_handler(sig, frame):
    print("\nYou pressed Ctrl+C or sent a SIGTERM signal. Shutting down gracefully...")
    sys.exit(0)

def main():
    # Get the interval from the environment variable or use the default (10 seconds)
    interval = int(os.environ.get('INTERVAL', 10))

    # Register signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    print('Press Ctrl+C or send a SIGTERM signal to stop')

    # Start the background routine with the configurable interval
    background_thread = threading.Thread(target=print_current_time, args=(interval,), daemon=True)
    background_thread.start()

    try:
        while True:
            # Your main application logic can go here
            # For example, you can add some code that runs alongside the background routine

            time.sleep(1)  # Simulate other work being done in the main thread

    except KeyboardInterrupt:
        # This block will be executed when a SIGINT signal is received
        print("\nReceived SIGINT. Shutting down gracefully...")
        sys.exit(0)

if __name__ == "__main__":
    main()