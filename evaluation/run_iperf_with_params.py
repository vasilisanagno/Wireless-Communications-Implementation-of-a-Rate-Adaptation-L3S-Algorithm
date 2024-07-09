import subprocess
import time
import json
import argparse
import threading

def run_iperf_command(ip, port, duration, bandwidth, start_time):
    time.sleep(start_time)
    command = [
        'iperf', '-c', ip, '-u', '-p', str(port), 
        '-b', str(bandwidth) + 'M', '-t', str(duration)
    ]
    
    print("Running command: {}".format(' '.join(command)))
    subprocess.Popen(command)

def load_params(filename):
    with open(filename, 'r') as f:
        params = json.load(f)
    return params

def main(ip, port, param_file):
    params = load_params(param_file)

    print("Loaded parameters:")
    for param in params:
        print(param)

    threads = []
    for duration, bandwidth, start_time in params:
        thread = threading.Thread(target=run_iperf_command, args=(ip, port, duration, bandwidth, start_time))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run iperf traffic with pre-generated parameters.')
    parser.add_argument('ip', type=str, help='IP address to transmit to')
    parser.add_argument('port', type=int, help='Port to transmit to')
    parser.add_argument('param_file', type=str, help='File with pre-generated parameters')
    args = parser.parse_args()

    main(args.ip, args.port, args.param_file)
