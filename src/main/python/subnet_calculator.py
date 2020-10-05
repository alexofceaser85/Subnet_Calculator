#!/usr/bin/env python3
"""
This holds the code responsible for determining a valid IP address and subnet mask and then determining the correct subnet
"""
import re

__author__ = "Alex DeCesare"
__version__ = "30-September-2020"

IPV6_MAX_COLONS = 7

def validate_ipv4_address(ipv4_address):

    valid_ipv4_regex = r"^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}$"

    if (re.match(valid_ipv4_regex, ipv4_address)):
        return True

    return False

def validate_ipv6_address(ipv6_address):

    if (ipv6_address.count(':') > IPV6_MAX_COLONS):

        return False

    valid_ipv6_regex = r"^((((?:[0-9A-F]{1,4}))(((?::[0-9A-F]{1,4}){7})|((((?::[0-9A-F]{1,4}))){0,5}((?:(::)[0-9A-F]{0,4}))(((?::[0-9A-F]{1,4}))){0,5})))|(?:(::)[0-9A-F]{0,4}))$"

    if (re.match(valid_ipv6_regex, ipv6_address, re.IGNORECASE)):
        return True

    return False


