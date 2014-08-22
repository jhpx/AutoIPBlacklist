# -*- coding: utf8 -*-
# Cheack_IP.py
# Author: Jiangmf
# Date: 2014-07-09
from itertools import groupby

# ---- helper functions ---- #

def prefix(x):
    """Calculate prefix for a single ip.
    For example,
    prefix('1.2.3.4') == '1.2'
    prefix('2.2.3.4') == '2.2'
    """
    return x[0:x.find(".", x.find(".") + 1)]


def min_ip(ip_list, prefix_length=0):
    """Find minimal ip in a ip group using logiic operator &.
    For example,
    min_ip(['1.2.3.4','1.2.3.3','1.2.3.2']) == '1.2.3.0'
    """
    if prefix_length == 0:
        prefix_length = count_prefix(ip_list)
    # trust this prefix_length
    bstr = binary_ip(ip_list[0])[:prefix_length] + '0' * (32 - prefix_length)

    return ".".join([str(int(bstr[8 * i:8 * (i + 1)], 2)) for i in range(4)])


def binary_ip(ip_str):
    """Change ip string into binary mode string.
    For example,
    binary_ip('1.1.1.1') == '00000001000000010000000100000001'
    binary_ip('1.2.3.4') == '00000001000000100000001100000100'
    """
    return "".join(["{0:08b}".format(int(x)) for x in ip_str.split('.')])


def count_prefix(ip_list):
    """Count common prefix length for a group of ip.
    For example,
    count_prefix(['1.2.3.4','1.2.3.8','1.2.3.7']) == 28
    count_prefix(['1.2.3.4','1.2.3.254']) == 24
    """
    x = 32
    bstr_list = [binary_ip(ip) for ip in ip_list]
    for i in range(32):
        # concat the character in ith position from all the binary string
        test = "".join([bstr[i] for bstr in bstr_list])
        # test should be all '0' string or all '1' string
        if test != '0' * len(bstr_list) and test != '1' * len(bstr_list):
            x = i
            break
    return x

# ---- main functions ---- #


def read_ip():
    """Read ip from 'st_visitors.csv'."""
    ip_data = [line.strip().replace('\"', '')
               for line in open('st_visitors.csv', 'r')]
    print "\nFind %s ip in st_visitors.csv." % len(ip_data)
    return ip_data


def group_ip(ip_data):
    """Group ip by ip's prefix."""
    ip_data_group = {}
    for key, group in groupby(sorted(ip_data), prefix):
        ip_data_group[key] = list(group)
    return ip_data_group


def calculate(ip_data_group):
    """Calculate the minimal ip aggregation"""
    ip_net_group = {}
    for key in ip_data_group.keys():
        ip_in_same_prefix = ip_data_group[key]
        length = count_prefix(ip_in_same_prefix)
        ip_minimal = min_ip(ip_in_same_prefix, length)
        ip_net_group[key] = ip_minimal + "/" + str(length)
    return ip_net_group


def update_blacklist(ip_net_group):
    """Update the file 'blacklist' (overide)."""
    file = open('blacklist', 'wb')
    count = 0
    for v in sorted(ip_net_group.values()):
        file.write("Deny from " + v + "\n")
        count += 1
    file.flush()
    file.close()
    print "Now %s rules in blacklist.\n" % count
    pass

# Script
if __name__ == "__main__":
#    ip_data = ['107.158.229.213', '107.158.23.23', '107.158.75.95',
#               '107.150.46.50', '107.150.49.242']
    ip_data = read_ip()
    ip_data_group = group_ip(ip_data)
    ip_net_group = calculate(ip_data_group)
#    print sorted(ip_net_group.values())
    update_blacklist(ip_net_group)
