#!/usr/bin/python


import psutil


print("\n--- PSUTIL net_connections(), net_io_counters(), net_if_addrs() ---")

print("\n========================================================================\n")

print(psutil.net_connections(kind='inet'))

print("\n------------------------------------------------------------------------\n")

print(psutil.net_io_counters(pernic=False, nowrap=True))

print("\n------------------------------------------------------------------------\n")

print(psutil.net_if_addrs())

print("\n========================================================================\n")