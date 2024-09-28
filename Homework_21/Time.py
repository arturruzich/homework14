import os
from datetime import datetime

def analyze_heartbeat(log_file, output_file, key='TSTFEED0300|7E3E|0400'):
    timestamps = []


    with open(log_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if key in line:

                timestamp_position = line.find("Timestamp ")
                if timestamp_position != -1:
                    timestamp_str = line[timestamp_position + len("Timestamp "):timestamp_position + len("Timestamp ") + 8].strip()


                    try:
                        current_timestamp = datetime.strptime(timestamp_str, '%H:%M:%S')
                        timestamps.append(current_timestamp)
                    except ValueError:
                        print(f"Time error: {timestamp_str}")
                        continue


    if not timestamps:
        print("Not found keys.")
        return


    timestamps.sort()
    print(f"Found {len(timestamps)} time markers. Analysis...")

    previous_timestamp = None


    with open(output_file, 'w') as log:
        for current_timestamp in timestamps:
            if previous_timestamp:

                heartbeat = (current_timestamp - previous_timestamp).total_seconds()


                if 31 < heartbeat < 33:
                    log.write(f"WARNING: Heartbeat {heartbeat:.1f} seconds at {current_timestamp.strftime('%H:%M:%S')}\n")
                elif heartbeat >= 33:
                    log.write(f"ERROR: Heartbeat {heartbeat:.1f} seconds at {current_timestamp.strftime('%H:%M:%S')}\n")
                else:
                    print(f"Heartbeat {heartbeat:.1f} seconds (no log) at {current_timestamp.strftime('%H:%M:%S')}")


            previous_timestamp = current_timestamp

current_dir = os.path.dirname(os.path.abspath(__file__))

log_file = os.path.join(current_dir, 'hblog.txt')
output_file = os.path.join(current_dir, 'hb_test.log')

analyze_heartbeat(log_file, output_file)

if os.path.exists(output_file):
    print(f"Result was recorded in {output_file}.")
else:
    print("File was not created.")

