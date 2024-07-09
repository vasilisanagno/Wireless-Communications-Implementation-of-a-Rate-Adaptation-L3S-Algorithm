# Wireless Communications Final Project

## Practical Rate Adaptation for Very High Throughput WLANs

### Authors
- Anagnostopoulos Vasileios
- Georgitziki Garyfalia
- Gavouras Dimitrios

### Date
June 28, 2024

## Introduction
This project compares the L3S (Long-term Stability and Short-term Responsiveness) algorithm and the Minstrel algorithm for WLANs. L3S adjusts transmission rates based on real-time conditions, while Minstrel uses acknowledgment feedback and periodic probing.

## Algorithms

### Rate Adaptation Algorithm
Optimizes WLAN performance by selecting the best data rate based on channel conditions. Types include statistic-based and signal-based algorithms.

### Minstrel
Implemented in the Linux kernel, it addresses packet loss and rate adaptation using acknowledgment feedback. It probes 10% of frames to gather information on unused rates.

## Implementation of L3S Algorithm
L3S, implemented in the Ath9k driver, maintains short-term and long-term statistics to dynamically adjust transmission rates. Key files modified:
- `rc80211_minstrel_ht.c`
- `rc80211_minstrel_ht.h`
- `rc80211_minstrel_ht_debugfs.c`

## Performance Evaluation

### Experiment Setup
- **Main Channel:** Node081 (Server), Node085 (Client), Channel 5, UDP/TCP traffic
- **First Interfering Channel:** Node088 (Server), Node075 (Client), Channel 3, UDP traffic
- **Second Interfering Channel:** Node093 (Server), Node089 (Client), Channel 6, UDP traffic

### Results
- **Low Interference:** Minstrel outperforms L3S in both UDP and TCP throughput.
- **Medium Interference:** Minstrel maintains higher throughput, though the gap narrows.
- **High Interference:** Throughput decreases for all; L3S shows competitive performance under severe interference.

### Analysis
- **Throughput Differences:** UDP achieves higher throughput than TCP due to lower overhead.
- **Algorithm Performance:** Minstrel excels in low interference; L3S Quick Probing adapts better in dynamic conditions.
- **Interference Impact:** L3S is more resilient to high interference.

## Conclusion
Minstrel generally outperforms L3S in terms of throughput, especially under low and medium interference. However, L3S Quick Probing shows promise under high interference, making it suitable for dynamic environments.

## References
1. Practical Rate Adaptation for Very High Throughput WLANs, Arafet Ben Makhlouf, Mounir Hamdi, 2013, IEEE
2. Rate Adaptation for 802.11 Wireless Networks: Minstrel, Andrew McGregor, Derek Smithies