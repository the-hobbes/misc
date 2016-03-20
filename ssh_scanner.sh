#!/bin/bash

# scan the network for machines.
# try to connect to each machine that is up, via ssh.
thisHost="$(ipconfig getifaddr en0)"
defaultGateway="$(netstat -nr | grep '^default' | awk '{print $2}')"
network="192.168.0.1/23"

for host in `nmap -sP $network 2> /dev/null | grep "for" | cut -d " " -f 5`; do
  if [ "$host" != "$thisHost" ] ; then
    if [ "$host" != "$defaultGateway" ] ; then
      nc -z $host 22
      if [ $? != 1 ]; then
        ssh -o ConnectTimeout=1 -o BatchMode=yes -o StrictHostKeyChecking=no phelan@$host &
        exit 0
      fi
    fi
  fi
done

echo All hosts on the network closed to ssh.
exit 1

