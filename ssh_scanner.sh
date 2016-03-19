#! /usr/bin/bash

# scan the network for machines.
# try to connect to each machine that is up, via ssh.
for host in `nmap -sP 192.168.0.1/24 2> /dev/null | grep "for" | cut -d " " -f 5`; do
  ssh -o ConnectTimeout=1 -o BatchMode=yes -o StrictHostKeyChecking=no phelan@$host
  echo "$?"
done

#TODO: make the network an argument. 
#TODO: make the password an argument.
#TODO: exit on success.
#TODO: exclude the current host from the ssh connection attempts.

