import random
import json
import argparse

def generate_random_params(num_streams, min_duration, max_duration, min_bandwidth, max_bandwidth, min_start_time, max_start_time):
    params = []
    for _ in range(num_streams):
        duration = random.randint(min_duration, max_duration)  # Duration between min_duration and max_duration seconds
        bandwidth = random.randint(min_bandwidth, max_bandwidth)  # Bandwidth between min_bandwidth and max_bandwidth Mbps
        start_time = random.randint(min_start_time, max_start_time)  # Start time between min_start_time and max_start_time seconds
        params.append((duration, bandwidth, start_time))
    return params

def main(num_streams, min_duration, max_duration, min_bandwidth, max_bandwidth, min_start_time, max_start_time):
    params = generate_random_params(num_streams, min_duration, max_duration, min_bandwidth, max_bandwidth, min_start_time, max_start_time)

    # Save parameters to a JSON file
    with open('params.json', 'w') as f:
        json.dump(params, f)

    print("Generated parameters:")
    for param in params:
        print(param)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate random parameters for iperf.')
    parser.add_argument('num_streams', type=int, help='Number of iperf streams')
    parser.add_argument('min_duration', type=int, help='Minimum duration for iperf in seconds')
    parser.add_argument('max_duration', type=int, help='Maximum duration for iperf in seconds')
    parser.add_argument('min_bandwidth', type=int, help='Minimum bandwidth for iperf in Mbps')
    parser.add_argument('max_bandwidth', type=int, help='Maximum bandwidth for iperf in Mbps')
    parser.add_argument('min_start_time', type=float, help='Minimum start time for iperf in seconds')
    parser.add_argument('max_start_time', type=float, help='Maximum start time for iperf in seconds')
    args = parser.parse_args()

    main(args.num_streams, args.min_duration, args.max_duration, args.min_bandwidth, args.max_bandwidth, args.min_start_time, args.max_start_time)
