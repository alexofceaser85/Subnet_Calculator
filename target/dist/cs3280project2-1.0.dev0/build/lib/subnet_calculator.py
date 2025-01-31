#!/usr/bin/env python3
"""
This holds the code responsible for determining a valid IP address and subnet mask and then
determining the correct subnet
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

TWO_BIT_INTEGER = 2
SIXTEEN_BIT_INTEGER = 16

def validate_ipv4_address(ipv4_address):
    """
    Checks if the given address is in valid ipv4 format
    """

    if re.match(r'^([0-9]|[1-9][0-9]'
                r'|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\.([0-9]|[1-9][0-9]'
                r'|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}$', ipv4_address):
        return True

    return False

def validate_ipv6_address(ipv6_address):
    """
    Checks if the given address is in valid ipv6 format
    """

    if ipv6_address.count(':') > IPV6_MAX_COLONS:

        return False

    if re.match(r'^((((?:[0-9A-F]{1,4}))(((?::[0-9A-F]{1,4}){7})'
                r'|((((?::[0-9A-F]{1,4}))){0,5}((?:(::)[0-9A-F]{0,4}))'
                r'(((?::[0-9A-F]{1,4}))){0,5})))'
                r'|(?:(::)[0-9A-F]{0,4}))$', ipv6_address, re.IGNORECASE):
        return True

    return False

def validate_ipv4_netmask_as_ip(netmask):
    """
    Checks if the given netmask is in a valid ipv4 format
    for example: 255.255.0.0 is valid but 16 is not.
    """

    if netmask.count('.') != IPV4_NETMASK_MAX_PERIODS:
        return False

    if re.match(r'^(((255)((\.255){0,2}(?:(((\.254)|(\.252)|(\.248)|(\.240)|(\.224)|(\.192)'
                r'|(\.128)))){0,1}(\.0){0,2}))'
                r'|(((254)|(252)|(248)|(240)|(224)|(192)|(128)|(0))(\.0){3}))$', netmask):
        return True

    return False

def validate_ipv4_netmask_as_bit(netmask):
    """
    Checks if the given ipv4 netmask is in a valid bit format
    for example: 16 is valid but 255.255.0.0 is not
    """
    valid_netmask_bit_regex = r"^(([1-9])|((1|2)[0-9])|(3[0-1]))$"

    if re.match(valid_netmask_bit_regex, netmask):
        return True

    return False

def validate_ipv6_netmask_as_bit(netmask):
    """
    Checks if the given ipv6 netmask is in a valid bit format
    for example: 64 is valid but 255.255.255.255.255.255.255.255 is not
    """
    valid_netmask_bit_regex = r"^(([1-9])|([1-9][0-9])|(1[0-2][0-8]))$"

    if re.match(valid_netmask_bit_regex, netmask):
        return True

    return False


def convert_netmask_bits_to_binary(netmask, max_length, period_index):
    """
    Converts netmask bits to a binary string
    """
    netmask_bits_index = 0
    current_netmask_bits = int(netmask)
    binary_netmask = ''

    while netmask_bits_index <= max_length:

        if netmask_bits_index % period_index == 0:
            binary_netmask += '.'
            netmask_bits_index += 1
        elif current_netmask_bits != 0:
            binary_netmask += '1'
            current_netmask_bits -= 1
            netmask_bits_index += 1
        else:
            binary_netmask += '0'
            netmask_bits_index += 1

    netmask_no_leading_period = binary_netmask[1:]
    return netmask_no_leading_period

def calculate_ipv4_subnet(ip_address, netmask):
    """
    calculates an ip address given that it is in valid ipv4 format
    """
    split_ip_address = ip_address.split('.')
    subnet = ""
    current_octet_index = 0
    split_netmask = netmask.split('.')

    for octet in split_ip_address:
        if validate_ipv4_netmask_as_ip(netmask):
            current_netmask_as_integer = int(split_netmask[current_octet_index])
        else:
            current_netmask_as_integer = int(split_netmask[current_octet_index], TWO_BIT_INTEGER)

        binary_octet = bin(int(octet) & current_netmask_as_integer)
        current_octet_index += 1
        octet_without_binary_indicator = binary_octet.replace('0b', '')
        subnet += '.' + str(int(octet_without_binary_indicator, TWO_BIT_INTEGER))

    subnet_without_leading_period = subnet[1:]
    return subnet_without_leading_period

def expand_ipv6_address(ip_address):
    """
    searches the ipv6 address for shortened zero groups (::) and expands them to include the zeros
    in the groups
    """
    split_ip_address = ip_address.split(':')
    group_index = 0
    expanded_ipv6 = ''

    for group in split_ip_address:
        if not group:
            group = '0000'

            while len(split_ip_address) < IPV6_MAX_GROUPS:
                split_ip_address.insert(group_index, '0000')

        expanded_ipv6 += ':' + group
        group_index += 1

    ipv6_without_leading_colon = expanded_ipv6[1:]
    return ipv6_without_leading_colon

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
        current_netmask_as_integer = int(split_netmask[current_group_index], TWO_BIT_INTEGER)

        binary_group = bin(int(group, SIXTEEN_BIT_INTEGER) & current_netmask_as_integer)
        binary_group_without_indicator = binary_group.replace('0b', '')

        subnet_as_hexadecimal = hex(int(binary_group_without_indicator, TWO_BIT_INTEGER))
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

        if number == '0':
            binary_opposite_string += '1'

            if len(binary_string) < max_length_for_leading_zeros:
                while len(binary_opposite_string) < max_length_for_leading_zeros:
                    binary_opposite_string += '1'

        elif number == '1':
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
    ip_address_group = calculate_ipv4_subnet(ip_address, netmask).split('.')
    upper_range = ''
    group_index = 0

    for group in netmask_group:

        if validate_ipv4_netmask_as_ip(netmask):
            opposite_binary = calculate_binary_opposite(bin(int(group)), IPV4_MAX_BINARY_DIGITS)
        else:
            group_binary = bin(int(group, TWO_BIT_INTEGER))
            opposite_binary = calculate_binary_opposite(group_binary, IPV4_MAX_BINARY_DIGITS)
        ip_address_binary = bin(int(ip_address_group[group_index])).replace('0b', '')
        current_binary = ''
        character_index = 0

        while len(ip_address_binary) < IPV4_MAX_BINARY_DIGITS:
            ip_address_binary += '0'

        while character_index < len(ip_address_binary):
            netmask_length = len(netmask_group) - 1
            ip_length = len(ip_address_binary) - 1
            if (group_index == netmask_length) and (character_index == ip_length):
                current_binary += '0'
            elif opposite_binary[character_index] == '1':
                current_binary += '1'
            else:
                current_binary += ip_address_binary[character_index]

            character_index += 1
        upper_range += '.' + str(int(current_binary, TWO_BIT_INTEGER))
        group_index += 1
        upper_range_no_leading_period = upper_range[1:]
    return upper_range_no_leading_period

def calculate_upper_ipv6_range(ip_address, netmask):
    """
    calculates the upper ipv6 range
    """
    netmask_group = netmask.split('.')
    ip_address_group = calculate_ipv6_subnet(ip_address, netmask).split(':')
    upper_range = ''
    group_index = 0

    for group in netmask_group:
        binary_group_two_bit = bin(int(group, TWO_BIT_INTEGER))
        binary_group_sixteen_bit = bin(int(ip_address_group[group_index], SIXTEEN_BIT_INTEGER))

        opposite_binary = calculate_binary_opposite(binary_group_two_bit, IPV6_MAX_BINARY_DIGITS)
        ip_address_binary = binary_group_sixteen_bit.replace('0b', '')
        current_binary = ''
        character_index = 0

        if '1' not in ip_address_binary:
            while len(ip_address_binary) < IPV6_MAX_BINARY_DIGITS:
                ip_address_binary += '0'

        while character_index < len(ip_address_binary):
            if opposite_binary[character_index] == '1':
                current_binary += '1'
            else:
                current_binary += ip_address_binary[character_index]

            character_index += 1
        upper_range += ':' + hex(int(current_binary, TWO_BIT_INTEGER)).replace('0x', '')
        group_index += 1
    upper_range_no_leading_period = upper_range[1:]
    return upper_range_no_leading_period

def calculate_lower_ipv4_range(ip_address, netmask):
    """
    calculates the lower range of an ipv4 address
    """
    netmask_group = netmask.split('.')
    ip_address_group = calculate_ipv4_subnet(ip_address, netmask).split('.')
    lower_range = ''
    group_index = 0

    while group_index < len(netmask_group):

        ip_address_binary = bin(int(ip_address_group[group_index])).replace('0b', '')
        current_binary = ''
        character_index = 0

        while len(ip_address_binary) < IPV4_MAX_BINARY_DIGITS:
            ip_address_binary += '0'

        while character_index < len(ip_address_binary):
            group_length = len(ip_address_group) - 1
            binary_length = len(ip_address_binary) - 1
            if(group_index == group_length) and (character_index == binary_length):
                current_binary += '1'
            else:
                current_binary += ip_address_binary[character_index]

            character_index += 1
        lower_range += '.' + str(int(current_binary, TWO_BIT_INTEGER))
        group_index += 1
        lower_range_no_leading_period = lower_range[1:]
    return lower_range_no_leading_period

def calculate_lower_ipv6_range(ip_address, netmask):

    """
    calculates the lower ipv6 range
    """
    netmask_group = netmask.split('.')
    ip_address_group = calculate_ipv6_subnet(ip_address, netmask).split(':')
    lower_range = ''
    group_index = 0

    for group in netmask_group:
        two_bit_group = bin(int(group, TWO_BIT_INTEGER))
        sixteen_bit_group = bin(int(ip_address_group[group_index], SIXTEEN_BIT_INTEGER))

        opposite_binary = calculate_binary_opposite(two_bit_group, IPV6_MAX_BINARY_DIGITS)
        ip_address_binary = sixteen_bit_group.replace('0b', '')
        current_binary = ''
        character_index = 0

        if '1' not in ip_address_binary:
            while len(ip_address_binary) < IPV6_MAX_BINARY_DIGITS:
                ip_address_binary += '0'

        while character_index < len(ip_address_binary):
            if opposite_binary[character_index] == '1':
                current_binary += '0'
            else:
                current_binary += ip_address_binary[character_index]
            character_index += 1

        lower_range += ':' + hex(int(current_binary, TWO_BIT_INTEGER)).replace('0x', '')
        group_index += 1
    lower_range_no_leading_period = lower_range[1:]
    return lower_range_no_leading_period
