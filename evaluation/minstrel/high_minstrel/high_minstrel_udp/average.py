import re

# Function to parse the bandwidth from the lines of the file
def parse_bandwidth(line):
    match = re.search(r'(\d+(\.\d+)?)\sMbits/sec', line)
    if match:
        return float(match.group(1))
    return None

# Function to read the file and extract the bandwidths
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    bandwidths = []
    for line in lines:
        bandwidth = parse_bandwidth(line)
        if bandwidth is not None:
            bandwidths.append(bandwidth)
    
    return bandwidths

# List of input files
file_paths = [
    'low_minstrel_AP_udp_1.txt',
    'low_minstrel_AP_udp_2.txt',
    'low_minstrel_AP_udp_3.txt'
]

# Read bandwidths from all files
all_bandwidths = []
for file_path in file_paths:
    bandwidths = read_file(file_path)
    all_bandwidths.append(bandwidths)

# Transpose the list to group bandwidths by intervals
transposed_bandwidths = list(zip(*all_bandwidths))

# Calculate the average bandwidth for each interval
avg_bandwidths = [sum(interval) / len(interval) for interval in transposed_bandwidths]

# Write the average bandwidths to a new file
output_file_path = 'avg_bandwidths.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write("------------------------------------------------------------\n")
    output_file.write("Client connecting to 192.168.2.81, UDP port 5001\n")
    output_file.write("Sending 1470 byte datagrams, IPG target: 74.77 us (kalman adjust)\n")
    output_file.write("UDP buffer size:  208 KByte (default)\n")
    output_file.write("------------------------------------------------------------\n")
    output_file.write("[  3] local 192.168.2.85 port 36758 connected with 192.168.2.81 port 5001\n")
    output_file.write("[ ID] Interval       Transfer     Bandwidth\n")

    for i, avg_bandwidth in enumerate(avg_bandwidths):
        start_time = i
        end_time = i + 1
        interval = f"{start_time:6.1f}-{end_time:3.1f} sec"
        transfer = f"{avg_bandwidth / 8:6.2f} MBytes"  # Convert Mbits to MBytes for the transfer column
        bandwidth = f"{avg_bandwidth:6.1f} Mbits/sec"
        output_file.write(f"[  3] {interval:<13} {transfer:<12} {bandwidth}\n")

    total_transfer = sum(avg_bandwidths) / 8  # Convert total Mbits to GBytes for the summary
    avg_total_bandwidth = sum(avg_bandwidths) / len(avg_bandwidths)
    output_file.write(f"[  3]  0.0-{len(avg_bandwidths):<4.1f} sec  {total_transfer:.2f} GBytes  {avg_total_bandwidth:6.1f} Mbits/sec\n")
    output_file.write("[  3] Sent X datagrams\n")
    output_file.write("[  3] Server Report:\n")
    output_file.write(f"[  3]  0.0-{len(avg_bandwidths):<4.1f} sec  {total_transfer:.2f} GBytes  {avg_total_bandwidth:6.1f} Mbits/sec   0.000 ms X/X (0%)\n")

print(f"Average bandwidths file created: {output_file_path}")
