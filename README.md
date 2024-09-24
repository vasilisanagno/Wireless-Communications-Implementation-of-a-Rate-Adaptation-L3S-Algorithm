# Wireless Communications Rate Adaptation Algorithm

## Practical Rate Adaptation for Very High Throughput WLANs

## Table of Contents

- [Introduction](#introduction)
- [Algorithms](#algorithms)
  - [Rate Adaptation Algorithm](#rate-adaptation-algorithm)
  - [Minstrel](#minstrel)
- [Implementation of L3S Algorithm](#implementation-of-l3s-algorithm)
- [Performance Evaluation](#performance-evaluation)
  - [Experiment Setup](#experiment-setup)
  - [Results](#results)
  - [Analysis](#analysis)
- [Project Structure](#project-structure)
- [Implementation Details](#implementation-details)
  - [Minstrel HT Algorithm](#minstrel-ht-algorithm)
  - [L3S Algorithm](#l3s-algorithm)
  - [Debugfs Interface](#debugfs-interface)
- [Conclusion](#conclusion)
- [References](#references)
- [More Details](#more-details)

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


## Project Structure

The project consists of several key files that contribute to the implementation and evaluation of the L3S algorithm:

- **rc80211_minstrel_ht.c**: The main source file where the core logic of the Minstrel HT rate adaptation algorithm is implemented. This file has been modified to incorporate the L3S algorithm's functionalities.
- **rc80211_minstrel_ht.h**: Header file containing the necessary data structures and function prototypes used by the Minstrel HT and L3S algorithms.
- **rc80211_minstrel_ht_debugfs.c**: This file manages the debugfs interface for Minstrel HT. It includes functions to display the rate statistics, including the newly added packet error rate (PER) statistics for each rate.
- **rc80211_minstrel_ht_quick.c**: Contains the quick probing mechanism of the L3S algorithm.
- **rc80211_minstrel_ht_slow.c**: Contains the slow probing mechanism of the L3S algorithm.
- **Patches**: The patch files associated with each C file contain the modifications made to integrate the L3S algorithm with the existing Minstrel HT framework.

## Implementation Details

### Minstrel HT Algorithm

The Minstrel HT algorithm is a rate control algorithm that dynamically selects the optimal transmission rate based on feedback from previously sent frames. It operates by periodically probing different rates to gather performance statistics, which are then used to select the best rate for future transmissions.

### L3S Algorithm

The L3S algorithm enhances the Minstrel HT by adding mechanisms that balance long-term stability with short-term responsiveness. It achieves this by maintaining both short-term and long-term statistics to dynamically adjust the transmission rates based on real-time channel conditions. The key components include:

- **Short-term Statistics**: Used to handle transient variations in the channel conditions.
- **Long-term Statistics**: Used to maintain stability over extended periods.
- **Probing Mechanisms**: L3S introduces two types of probing mechanisms - quick probing and slow probing - to adapt more efficiently to changing conditions.

### Debugfs Interface

The `rc80211_minstrel_ht_debugfs.c` file provides a debugfs interface to monitor the performance of the rate control algorithm. The debugfs entries allow users to view detailed statistics, including throughput, packet error rates, and probing intervals, which are crucial for evaluating the algorithm's effectiveness.

## Conclusion
Minstrel generally outperforms L3S in terms of throughput, especially under low and medium interference. However, L3S Quick Probing shows promise under high interference, making it suitable for dynamic environments.

## References
1. Practical Rate Adaptation for Very High Throughput WLANs, Arafet Ben Makhlouf, Mounir Hamdi, 2013, IEEE
2. Rate Adaptation for 802.11 Wireless Networks: Minstrel, Andrew McGregor, Derek Smithies

## More details
For more details, see the [Wireless_Communcations_Final_Project](Wireless_Communcations_Final_Project.pdf).
