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
    'med_l3s_quick_STA_udp_1.txt',
    'med_l3s_quick_STA_udp_2.txt',
    'med_l3s_quick_STA_udp_3.txt'
]

# Read bandwidths from all files
all_bandwidths = []
for file_path in file_paths:
    bandwidths = read_file(file_path)
    all_bandwidths.append(bandwidths)

# Transpose the list to group bandwidths by intervals
transposed_bandwidths = list(zip(*all_bandwidths))

# Calculate the average bandwidth for every 50-second interval
avg_bandwidths_50sec = []
interval_size = 50
num_intervals = len(transposed_bandwidths) // interval_size

for i in range(num_intervals):
    interval_bandwidths = transposed_bandwidths[i * interval_size:(i + 1) * interval_size]
    avg_bandwidth = sum(map(sum, interval_bandwidths)) / (len(interval_bandwidths) * len(interval_bandwidths[0]))
    avg_bandwidths_50sec.append(avg_bandwidth)

# Write the average bandwidths to a new file
output_file_path = 'avg50_med_l3s_quick_udp.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write("------------------------------------------------------------\n")
    output_file.write("Client connecting to 192.168.2.81, UDP port 5001\n")
    output_file.write("Sending 1470 byte datagrams, IPG target: 74.77 us (kalman adjust)\n")
    output_file.write("UDP buffer size:  208 KByte (default)\n")
    output_file.write("------------------------------------------------------------\n")
    output_file.write("[  3] local 192.168.2.85 port 36758 connected with 192.168.2.81 port 5001\n")
    output_file.write("[ ID] Interval       Transfer     Bandwidth\n")

    for i, avg_bandwidth in enumerate(avg_bandwidths_50sec):
        start_time = i * interval_size
        end_time = (i + 1) * interval_size
        interval = f"{start_time:6.1f}-{end_time:3.1f} sec"
        transfer = f"{avg_bandwidth / 8 * interval_size:6.2f} MBytes"  # Convert Mbits to MBytes for the transfer column and scale by interval size
        bandwidth = f"{avg_bandwidth:6.1f} Mbits/sec"
        output_file.write(f"[  3] {interval:<13} {transfer:<12} {bandwidth}\n")

    total_transfer = sum(avg_bandwidths_50sec) / 8 * interval_size  # Convert total Mbits to GBytes for the summary and scale by interval size
    avg_total_bandwidth = sum(avg_bandwidths_50sec) / len(avg_bandwidths_50sec)
    output_file.write(f"[  3]  0.0-{len(transposed_bandwidths):<4.1f} sec  {total_transfer:.2f} GBytes  {avg_total_bandwidth:6.1f} Mbits/sec\n")

print(f"Average bandwidths file created: {output_file_path}")
