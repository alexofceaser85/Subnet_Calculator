#!/usr/bin/env python3
"""
This holds the code responsible for determining a valid IP address and subnet mask and then determining the correct subnet
"""
import re

__author__ = "Alex DeCesare"
__version__ = "30-September-2020"

IPV6_MAX_COLONS = 7
IPV6_MAX_GROUPS = 8
IPV4_MAX_BINARY_DIGITS = 8
IPV6_MAX_BINARY_DIGITS = 16
IPV4_NETMASK_MAX_PERIODS = 3
IPV6_NETMASK_MAX_PERIODS = 7
IPV4_NETMASK_MAX_LENGTH = 35
IPV6_NETMASK_MAX_LENGTH = 135

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

def validate_ipv4_netmask_ip_format(netmask):
    """
    Checks if the given netmask is in a valid ipv4 format
    for example: 255.255.0.0 is valid but 16 is not.
    """

    if (netmask.count('.') != IPV4_NETMASK_MAX_PERIODS):
        return False

    valid_netmask_ip_regex = r"^(((255)((\.255){0,2}(?:(((\.254)|(\.252)|(\.248)|(\.240)|(\.224)|(\.192)|(\.128)))){0,1}(\.0){0,2}))|(((254)|(252)|(248)|(240)|(224)|(192)|(128)|(0))(\.0){3}))$"

    if (re.match(valid_netmask_ip_regex, netmask)):
        return True

    return False

def validate_ipv4_netmask_bit_format(netmask):
    """
    Checks if the given ipv4 netmask is in a valid bit format
    for example: 16 is valid but 255.255.0.0 is not
    """
    valid_netmask_bit_regex = r"^(([1-9])|((1|2)[0-9])|(3[0-1]))$"
    
    if (re.match(valid_netmask_bit_regex, netmask)):
        return True

    return False

def validate_ipv6_netmask_bit_format(netmask):

    """
    Checks if the given ipv6 netmask is in a valid bit format
    for example: 64 is valid but 255.255.255.255.255.255.255.255 is not
    """
    valid_netmask_bit_regex = r"^(([1-9])|([1-9][0-9])|(1[0-2][0-8]))$"

    if (re.match(valid_netmask_bit_regex, netmask)):
        return True

    return False


def convert_netmask_bits_to_binary(netmask, max_length, period_index):
    """
    Converts netmask bits to a binary string
    """

    netmask_bits_index = 0
    current_netmask_bits = int(netmask)
    binary_netmask = ''

    while(netmask_bits_index <= max_length):

        if (netmask_bits_index % period_index == 0):
            binary_netmask += '.'
            netmask_bits_index += 1
        elif (current_netmask_bits != 0):
            binary_netmask += '1'
            current_netmask_bits -= 1
            netmask_bits_index += 1
        else:
            binary_netmask += '0'
            netmask_bits_index += 1
    
    binary_netmask_no_leading_period = binary_netmask[1:]
    return binary_netmask_no_leading_period

def calculate_ipv4_subnet(ip_address, netmask):
    """
    calculates an ip address given that it is in valid ipv4 format
    """
    split_ip_address = ip_address.split('.')
    subnet = ""
    current_octet_index = 0
    split_netmask = netmask.split('.')
    
    for octet in split_ip_address:        
        if (validate_ipv4_netmask_ip_format(netmask)):
            current_netmask_as_integer = int(split_netmask[current_octet_index])
        else:
            current_netmask_as_integer = int(split_netmask[current_octet_index], 2)

        binary_octet = bin(int(octet) & current_netmask_as_integer)
        current_octet_index += 1
        octet_without_binary_indicator = binary_octet.replace('0b', '')
        subnet += '.' + str(int(octet_without_binary_indicator, 2))
    
    subnet_without_leading_period = subnet[1:]
    return subnet_without_leading_period



def expand_ipv6_address(ip_address):
    """
    searches the ipv6 address for shortened zero groups (::) and expands them to include the zeros in the groups
    """

    split_ip_address = ip_address.split(':')
    group_index = 0
    expanded_ipv6 = ''
    integer_base = 16

    for group in split_ip_address:
        if not group:
            group = '0000'

            while(len(split_ip_address) < IPV6_MAX_GROUPS):     
                split_ip_address.insert(group_index, '0000')
        
        expanded_ipv6 += ':' + group
        group_index += 1

    expanded_ipv6_without_leading_colon = expanded_ipv6[1:]
    
    return expanded_ipv6_without_leading_colon

def calculate_ipv6_subnet(ip_address, netmask):

    """
    calculates an ip address given it is in valid ipv6 format
    """

    expanded_ipv6_address = expand_ipv6_address(ip_address)
    split_ip_address = expanded_ipv6_address.split(':')
    split_netmask = netmask.split('.')
    current_group_index = 0
    subnet = ""

    for group in split_ip_address:
        current_netmask_as_integer = int(split_netmask[current_group_index], 2)
        binary_group = bin(int(group, 16) & current_netmask_as_integer)
        binary_group_without_indicator = binary_group.replace('0b', '')
        subnet_as_hexadecimal = hex(int(binary_group_without_indicator, 2))
        hexadecimal_without_indicator = subnet_as_hexadecimal[2:] 
        subnet += ':' + hexadecimal_without_indicator
        current_group_index += 1
    
    subnet_without_leading_period = subnet[1:]
    return subnet_without_leading_period

def calculate_binary_opposite(binary_string, max_length_for_leading_zeros):
    """
    returns the opposite of the binary string given
    i.e: 101 is 010
    """
    binary_opposite_string = ''

    for number in binary_string:

        if(number == '0'):
            binary_opposite_string += '1'

            if (len(binary_string) < max_length_for_leading_zeros):
                while(len(binary_opposite_string) < max_length_for_leading_zeros):
                    binary_opposite_string += '1'

        elif(number == '1'):
            binary_opposite_string += '0'
        else:
            binary_opposite_string += number

    opposite_binary_no_indicator = binary_opposite_string.replace('1b', '')

    return opposite_binary_no_indicator

def calculate_upper_ipv4_range(ip_address, netmask):
    """
    calculates the upper ipv4 range
    """
    netmask_group = netmask.split('.')
    ip_address_group = ip_address.split('.')
    upper_range = ''
    group_index = 0

    for group in netmask_group:
        opposite_binary = calculate_binary_opposite(bin(int(group)), 8)
        ip_address_binary = bin(int(ip_address_group[group_index])).replace('0b', '')
        character_index = 0
        current_binary = ''
        
        while (len(ip_address_binary) < 8):
            ip_address_binary += '0'
        
        for character in ip_address_binary:
        
            if (ip_address_binary[character_index] == '1' and opposite):
                current_binary += '1'
            else:
                current_binary += '0'
            character_index += 1
       
        print(opposite_binary)
        print(ip_address_binary)
        print(current_binary)
        upper_range += '.' + str(int(current_binary, 2))
        group_index += 1

    print(upper_range)
    return upper_range[1:]

if (__name__ == '__main__'):
    calculate_upper_ipv4_range('160.160.160.160', '255.255.192.0')
