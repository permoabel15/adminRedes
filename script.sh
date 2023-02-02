#!/bin/bash

ips=()
output=$(nmap -sP 192.168.5.0/24)

# List of IP addresses
ips=( $(echo "$output" | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b") )

# Name of script to run
script_name="run_script.sh"

# Run the script on each IP address
for ip in "${ips[@]}"; do
  ssh abelperez@"$ip" sh "$script_name"
done
