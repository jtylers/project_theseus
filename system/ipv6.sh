#!/bin/bash
# Place this file in /usr/bin/local
# to give your device the ipv6 address of fd00::1 no matter which network it is on
if ! /usr/bin/ip -6 addr show dev eth0|grep -q fd00::1
then
	ip a a fd00::1/64 dev eth0
fi

#If ipv6 is broke, run:
#/usr/local/bin/ipv6
#systemctl stop radvd
#systemctl start radvd

