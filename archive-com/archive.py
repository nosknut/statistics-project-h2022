import os
import time
import sys
from threading import Thread
import serial

output_dir = "output"

# Make output directory
os.makedirs(output_dir, exist_ok=True)

file_path = output_dir
file_path += "/"
file_path += input("Name the output file: ")
file_path += "_%s.csv"

# Autoincrement filename
i = 0
while os.path.exists(file_path % i):
    i += 1

file_path = file_path % i

num_readings = 100e3
num_read = 0

def print_progress():
    while True:
        progress = round((num_read / num_readings) * 100, 3)
        if progress >= 100:
            sys.stdout.write("\rArchiving complete!")
            sys.stdout.flush()
            break
        sys.stdout.write("\rProgress: " + str(progress) + "%")
        sys.stdout.flush()
        time.sleep(1)

progress_thread = Thread(target=print_progress)
progress_thread.daemon = True
progress_thread.start()

# Fill csv file
with open(file_path, 'a', newline='') as csvfile:
    s = serial.Serial('COM3', 115200)
    csvfile.write("time, value, value2\n")
    while num_read <= num_readings:
        if s.in_waiting > 0:
            msg = s.read(s.in_waiting).decode("utf-8")
            csvfile.write(msg)
            num_read += msg.count("\n")

        if s.in_waiting > 1000:
            print("Buffer overflow: ", s.in_waiting)

        time.sleep(0.01)

progress_thread.join()
