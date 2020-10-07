#!/usr/bin/env python3
"""
This holds the code responsible for determining a valid IP address and subnet mask and then determining the correct subnet
"""
import re

__author__ = "Alex DeCesare"
__version__ = "30-September-2020"

IPV6_MAX_COLONS = 7
NETMASK_MAX_PERIODS = 3

def validate_ipv4_address(ipv4_address):

    """
    Checks if the given address is in valid ipv4 format
    """

    valid_ipv4_regex = r"^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}$"

    if (re.match(valid_ipv4_regex, ipv4_address)):
        return True

    return False

def validate_ipv6_address(ipv6_address):

    """
    Checks if the given address is in valid ipv6 format
    """

    if (ipv6_address.count(':') > IPV6_MAX_COLONS):

        return False

    valid_ipv6_regex = r"^((((?:[0-9A-F]{1,4}))(((?::[0-9A-F]{1,4}){7})|((((?::[0-9A-F]{1,4}))){0,5}((?:(::)[0-9A-F]{0,4}))(((?::[0-9A-F]{1,4}))){0,5})))|(?:(::)[0-9A-F]{0,4}))$"

    if (re.match(valid_ipv6_regex, ipv6_address, re.IGNORECASE)):
        return True

    return False

def validate_netmask_ip_format(netmask):

    """
    Checks if the given netmask is in a valid ip format
    for example: 255.255.0.0 is valid but 16 is not.
    """

    if (netmask.count('.') != NETMASK_MAX_PERIODS):
        return False

    valid_netmask_ip_regex = r"^(((255)((\.255){0,2}(?:(((\.254)|(\.252)|(\.248)|(\.240)|(\.224)|(\.192)|(\.128)))){0,1}(\.0){0,2}))|(((254)|(252)|(248)|(240)|(224)|(192)|(128)|(0))(\.0){3}))$"

    if (re.match(valid_netmask_ip_regex, netmask)):
        return True

    return False

def validate_netmask_bit_format(netmask):

    """
    Checks if the given netmask is in a valid bit format
    for example: 16 is valid but 255.255.0.0 is not
    """

    valid_netmask_ip_regex = r"^(([1-9])|((1|2)[0-9])|(3[0-1]))$"

    if (re.match(valid_netmask_ip_regex, netmask)):
        return True

    return False
