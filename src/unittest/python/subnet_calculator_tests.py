#!/usr/bin/env python3

import unittest
import subnet_calculator

IPV4_NETMASK_MAX_LENGTH = 35
IPV6_NETMASK_MAX_LENGTH = 135
IPV4_NETMASK_PERIOD_INDEX = 9
IPV6_NETMASK_PERIOD_INDEX = 17

class TestValidateIpv4Address(unittest.TestCase):

    def test_empty_ipv4_address(self):

        is_valid = subnet_calculator.validate_ipv4_address('')
        self.assertFalse(is_valid)
    
    def test_ipv4_with_no_digits_in_octet(self):

        is_valid = subnet_calculator.validate_ipv4_address('....')
        self.assertFalse(is_valid)

    def test_ipv4_with_well_less_than_three_digits_in_octet(self):
        
        is_valid = subnet_calculator.validate_ipv4_address('1.1.1.1')
        self.assertTrue(is_valid)

    def test_ipv4_with_one_less_than_three_digits_in_octet(self):

        is_valid = subnet_calculator.validate_ipv4_address('11.11.11.11')
        self.assertTrue(is_valid)

    def test_ipv4_with_three_digits_in_octet(self):

        is_valid = subnet_calculator.validate_ipv4_address('111.111.111.111')
        self.assertTrue(is_valid)

    def test_ipv4_with_one_more_than_three_digits_in_octet(self):

        is_valid = subnet_calculator.validate_ipv4_address('1111.1111.1111.1111')
        self.assertFalse(is_valid)

    def test_ipv4_with_well_more_than_three_digits_in_octet(self):

        is_valid = subnet_calculator.validate_ipv4_address('123456.123456.123456.123456')
        self.assertFalse(is_valid)

    def test_ipv4_with_one_octets_well_below_valid(self):

        is_valid = subnet_calculator.validate_ipv4_address('123')
        self.assertFalse(is_valid)

    def test_ipv4_with_octets_one_below_valid(self):

        is_valid = subnet_calculator.validate_ipv4_address('123.123.123')
        self.assertFalse(is_valid)

    def test_ipv4_with_four_octets_valid(self):

        is_valid = subnet_calculator.validate_ipv4_address('123.123.123.123')
        self.assertTrue(is_valid)

    def test_ipv4_with_octets_one_above_valid(self):

        is_valid = subnet_calculator.validate_ipv4_address('123.123.123.123.123')
        self.assertFalse(is_valid)

    def test_ipv4_with_octets_well_above_valid(self):

        is_valid = subnet_calculator.validate_ipv4_address('123.123.123.123.123.123.123.123')
        self.assertFalse(is_valid)

    def test_ipv4_with_empty_octet(self):

        is_valid = subnet_calculator.validate_ipv4_address('123..123.123')
        self.assertFalse(is_valid)

    def test_ipv4_with_all_octet_values_well_below_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('-255.-255.-255.-255')
        self.assertFalse(is_valid)

    def test_ipv4_with_all_octet_values_one_below_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('-1.-1.-1.-1')
        self.assertFalse(is_valid)

    def test_ipv4_with_all_octet_values_at_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.0.0.0')
        self.assertTrue(is_valid)

    def test_ipv4_with_all_octet_values_one_above_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('1.1.1.1')
        self.assertTrue(is_valid)

    def test_ipv4_with_all_octet_values_well_above_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('100.200.100.200')
        self.assertTrue(is_valid)

    def test_ipv4_with_all_octet_values_well_below_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('50.50.50.50')
        self.assertTrue(is_valid)

    def test_ipv4_with_all_octet_values_one_below_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('254.254.254.254')
        self.assertTrue(is_valid)

    def test_ipv4_with_all_octet_values_at_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('255.255.255.255')
        self.assertTrue(is_valid)

    def test_ipv4_with_all_octet_values_one_above_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('256.256.256.256')
        self.assertFalse(is_valid)

    def test_ipv4_with_all_octet_values_well_above_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('999.999.999.999')
        self.assertFalse(is_valid)

    def test_ipv4_with_first_octet_value_well_below_zero(self):
 
        is_valid = subnet_calculator.validate_ipv4_address('-255.5.5.5')
        self.assertFalse(is_valid)

    def test_ipv4_with_first_octet_value_one_below_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('-1.1.1.1')
        self.assertFalse(is_valid)

    def test_ipv4_with_first_octet_value_at_zero(self):
        is_valid = subnet_calculator.validate_ipv4_address('0.10.10.10')
        self.assertTrue(is_valid)

    def test_ipv4_with_first_octet_value_one_above_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('1.0.0.0')
        self.assertTrue(is_valid)

    def test_ipv4_with_first_octet_value_well_above_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('100.0.0.0')
        self.assertTrue(is_valid)

    def test_ipv4_with_first_octet_value_well_below_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('50.255.255.255')
        self.assertTrue(is_valid)

    def test_ipv4_with_first_octet_value_one_below_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('254.0.0.0')
        self.assertTrue(is_valid)

    def test_ipv4_with_first_octet_value_at_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('255.0.0.0')
        self.assertTrue(is_valid)

    def test_ipv4_with_first_octet_value_one_above_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('256.0.0.0')
        self.assertFalse(is_valid)

    def test_ipv4_with_first_octet_value_well_above_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('999.0.0.0')
        self.assertFalse(is_valid)

    def test_ipv4_with_second_octet_value_well_below_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('5.-255.5.5')
        self.assertFalse(is_valid)

    def test_ipv4_with_second_octet_value_one_below_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('1.-1.1.1')
        self.assertFalse(is_valid)

    def test_ipv4_with_second_octet_value_at_zero(self):
        is_valid = subnet_calculator.validate_ipv4_address('10.0.10.10')
        self.assertTrue(is_valid)

    def test_ipv4_with_second_octet_value_one_above_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.1.0.0')
        self.assertTrue(is_valid)

    def test_ipv4_with_second_octet_value_well_above_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.50.0.0')
        self.assertTrue(is_valid)

    def test_ipv4_with_second_octet_value_well_below_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('255.50.255.255')
        self.assertTrue(is_valid)

    def test_ipv4_with_second_octet_value_one_below_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.254.0.0')
        self.assertTrue(is_valid)

    def test_ipv4_with_second_octet_value_at_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.255.0.0')
        self.assertTrue(is_valid)

    def test_ipv4_with_second_octet_value_one_above_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.256.0.0')
        self.assertFalse(is_valid)

    def test_ipv4_with_second_octet_value_well_above_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.999.0.0')
        self.assertFalse(is_valid)

    def test_ipv4_with_third_octet_value_well_below_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('5.5.-255.5')
        self.assertFalse(is_valid)

    def test_ipv4_with_third_octet_value_one_below_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('1.1.-1.1')
        self.assertFalse(is_valid)

    def test_ipv4_with_third_octet_value_at_zero(self):
        is_valid = subnet_calculator.validate_ipv4_address('10.10.0.10')
        self.assertTrue(is_valid)

    def test_ipv4_with_third_octet_value_one_above_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.0.1.0')
        self.assertTrue(is_valid)

    def test_ipv4_with_third_octet_value_well_above_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.0.50.0')
        self.assertTrue(is_valid)

    def test_ipv4_with_third_octet_value_well_below_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('255.255.50.255')
        self.assertTrue(is_valid)

    def test_ipv4_with_third_octet_value_one_below_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.0.254.0')
        self.assertTrue(is_valid)

    def test_ipv4_with_third_octet_value_at_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.0.255.0')
        self.assertTrue(is_valid)

    def test_ipv4_with_third_octet_value_one_above_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.0.256.0')
        self.assertFalse(is_valid)

    def test_ipv4_with_third_octet_value_well_above_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.0.999.0')
        self.assertFalse(is_valid)

    def test_ipv4_with_fourth_octet_value_well_below_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('5.5.5.-255')
        self.assertFalse(is_valid)

    def test_ipv4_with_fourth_octet_value_one_below_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('1.1.1.-1')
        self.assertFalse(is_valid)

    def test_ipv4_with_fourth_octet_value_at_zero(self):
        is_valid = subnet_calculator.validate_ipv4_address('10.10.10.0')
        self.assertTrue(is_valid)

    def test_ipv4_with_fourth_octet_value_one_above_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.0.0.1')
        self.assertTrue(is_valid)

    def test_ipv4_with_fourth_octet_value_well_above_zero(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.0.0.50')
        self.assertTrue(is_valid)

    def test_ipv4_with_fourth_octet_value_well_below_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('255.255.255.50')
        self.assertTrue(is_valid)

    def test_ipv4_with_fourth_octet_value_one_below_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.0.0.254')
        self.assertTrue(is_valid)

    def test_ipv4_with_fourth_octet_value_at_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.0.0.255')
        self.assertTrue(is_valid)

    def test_ipv4_with_fourth_octet_value_one_above_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.0.0.256')
        self.assertFalse(is_valid)

    def test_ipv4_with_fourth_octet_value_well_above_255(self):

        is_valid = subnet_calculator.validate_ipv4_address('0.0.0.999')
        self.assertFalse(is_valid)

    def test_ipv4_with_incorrect_leading_zero_padding(self):

        is_valid = subnet_calculator.validate_ipv4_address('160.010.25.007')
        self.assertFalse(is_valid)

    def test_ipv4_with_correct_following_zero_padding(self):

        is_valid = subnet_calculator.validate_ipv4_address('160.100.25.700')
        self.assertFalse(is_valid)

class TestValidateIpv6Address(unittest.TestCase):

    def test_abbreviated_zero_at_middle_group(self):

        is_valid = subnet_calculator.validate_ipv6_address('2001:4515::4548')
        self.assertTrue(is_valid)

    def test_abbreviated_zero_at_end_group(self):

        is_valid = subnet_calculator.validate_ipv6_address('2001:4545::')
        self.assertTrue(is_valid)

    def test_abbreviated_zero_at_eight_groups(self):

        is_valid = subnet_calculator.validate_ipv6_address('7848:4848:4564:4518:1511::4845:4844')
        self.assertTrue(is_valid)

    def test_abbreviated_zero_one_above_eight_groups(self):

        is_valid = subnet_calculator.validate_ipv6_address('7848:4848:4564:4518:1511::4845:4844:4854')
        self.assertFalse(is_valid)

    def test_abbreviated_zero_well_above_eight_groups(self):

        is_valid = subnet_calculator.validate_ipv6_address('7848:4848:4564:4518:1511::4845:4844:4854:4845:4844:4854:4848')
        self.assertFalse(is_valid)

    def test_ipv6_with_letters_between_a_to_f_lowercase(self):

        is_valid = subnet_calculator.validate_ipv6_address('784a:484b:45c4:4e18:1511:1515:48f5:4844')
        self.assertTrue(is_valid)

    def test_ipv6_with_letters_between_a_to_f_uppercase(self):

        is_valid = subnet_calculator.validate_ipv6_address('784A:484B:45C4:4E18:1511:1515:48F5:4844')
        self.assertTrue(is_valid)

    def test_ipv6_with_letters_between_g_to_z_lowercase(self):

        is_valid = subnet_calculator.validate_ipv6_address('784g:484h:45i4:4j48:m841:15p5:48v5:48z4')
        self.assertFalse(is_valid)

    def test_ipv6_with_letters_between_g_to_z_uppercase(self):

        is_valid = subnet_calculator.validate_ipv6_address('784G:484H:45I4:4J48:M841:15P5:48V5:48Z4')
        self.assertFalse(is_valid)

    def test_ipv6_with_no_groups(self):

        is_valid = subnet_calculator.validate_ipv6_address('20014515000000009999451500428329')
        self.assertFalse(is_valid)

    def test_ipv6_with_groups_well_below_eight(self):

        is_valid = subnet_calculator.validate_ipv6_address('4512:1245')
        self.assertFalse(is_valid)

    def test_ipv6_with_groups_one_below_eight(self):

        is_valid = subnet_calculator.validate_ipv6_address('2001:4515:0000:0000:9999:4515:0042')
        self.assertFalse(is_valid)

    def test_ipv6_with_groups_at_eight(self):

        is_valid = subnet_calculator.validate_ipv6_address('2001:4515:0000:0000:9999:4515:0042:8329')
        self.assertTrue(is_valid)

    def test_ipv6_with_groups_one_above_eight(self):

        is_valid = subnet_calculator.validate_ipv6_address('2001:4515:0000:0000:9999:4515:0042:8329:2515')
        self.assertFalse(is_valid)

    def test_ipv6_with_groups_well_above_eight(self):

        is_valid = subnet_calculator.validate_ipv6_address('2001:4515:0000:0000:9999:4515:0042:8329:2515:4848:1511:1451:4611:4844')
        self.assertFalse(is_valid)

    def test_ipv6_with_first_group_negative(self):

        is_valid = subnet_calculator.validate_ipv6_address('-2001:4515:0000:0000:9999:4515:0042:8329')
        self.assertFalse(is_valid)

    def test_ipv6_with_a_middle_group_negative(self):

        is_valid = subnet_calculator.validate_ipv6_address('2001:4515:0000:0000:-9999:4515:0042:8329')
        self.assertFalse(is_valid)

    def test_ipv6_with_last_group_negative(self):

        is_valid = subnet_calculator.validate_ipv6_address('2001:4515:0000:0000:9999:4515:0042:-8329')
        self.assertFalse(is_valid)

class TestIpv4ValidateNetmaskIpFormat(unittest.TestCase):

    def test_empty_netmask(self):
        
        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('')
        self.assertFalse(is_valid)

    def test_netmask_with_no_digits_in_octet(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('....')
        self.assertFalse(is_valid)

    def test_netmask_with_octets_well_below_four(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('255')
        self.assertFalse(is_valid)

    def test_netmask_with_octets_one_below_four(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('255.255.255')
        self.assertFalse(is_valid)

    def test_netmask_with_octets_at_four(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('255.255.255.0')
        self.assertTrue(is_valid)

    def test_netmask_with_octets_one_above_four(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('255.255.255.0.0')
        self.assertFalse(is_valid)

    def test_netmask_with_octets_well_above_four(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('255.255.255.255.255.255.255.0')
        self.assertFalse(is_valid)

    def test_netmask_with_empty_octet(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('255..0.0')
        self.assertFalse(is_valid)

    def test_netmask_with_one_non_zero_after_one_zero(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('0.255.0.0')
        self.assertFalse(is_valid)

    def test_netmask_with_many_non_zeros_after_one_zero(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('0.255.255.255')
        self.assertFalse(is_valid)

    def test_netmask_with_one_non_zero_after_many_non_zeros(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('0.0.0.255')
        self.assertFalse(is_valid)

    def test_netmask_with_octet_less_than_255_before_255(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('0.255.0.0')
        self.assertFalse(is_valid)

    def test_netmask_with_octets_all_zero(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('0.0.0.0')
        self.assertTrue(is_valid)

    def test_netmask_with_octets_all_255(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('255.255.255.255')
        self.assertFalse(is_valid)

    def test_netmask_with_one_non_255_or_0_number(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('255.248.0.0')
        self.assertTrue(is_valid)

    def test_netmask_with_one_more_than_one_non_255_or_0_number(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('255.248.240.0')
        self.assertFalse(is_valid)

    def test_netmask_with_well_more_than_one_non_255_or_0_number(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('254.248.240.128')
        self.assertFalse(is_valid)

    def test_maximum_bit_netmask_ending_in_254(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('255.255.255.254')
        self.assertTrue(is_valid)

    def test_netmask_with_one_octet_with_valid_value_of_254(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('255.255.255.254')
        self.assertTrue(is_valid)

    def test_netmask_with_one_octet_with_valid_value_of_252(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('255.255.255.252')
        self.assertTrue(is_valid)

    def test_netmask_with_one_octet_with_valid_value_of_248(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('255.255.255.248')
        self.assertTrue(is_valid)

    def test_netmask_with_one_octet_with_valid_value_of_240(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('255.255.255.240')
        self.assertTrue(is_valid)

    def test_netmask_with_one_octet_with_valid_value_of_224(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('255.255.255.224')
        self.assertTrue(is_valid)

    def test_netmask_with_one_octet_with_valid_value_of_192(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('255.255.255.192')
        self.assertTrue(is_valid)

    def test_netmask_with_one_octet_with_valid_value_of_128(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('255.255.255.128')
        self.assertTrue(is_valid)
    
    def test_netmask_with_non_valid_octet_value(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_ip_format('255.255.255.180')
        self.assertFalse(is_valid)

class ValidateIpv4NetmaskBitFormat(unittest.TestCase):

    def test_empty_netmask(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_bit_format('')
        self.assertFalse(is_valid)

    def test_netmask_well_below_zero(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_bit_format('-99')
        self.assertFalse(is_valid)

    def test_netmask_one_below_zero(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_bit_format('-1')
        self.assertFalse(is_valid)

    def test_netmask_at_zero(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_bit_format('0')
        self.assertFalse(is_valid)

    def test_netmask_one_above_zero(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_bit_format('1')
        self.assertTrue(is_valid)

    def test_netmask_well_above_zero(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_bit_format('12')
        self.assertTrue(is_valid)

    def test_netmask_well_below_31(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_bit_format('18')
        self.assertTrue(is_valid)

    def test_netmask_one_below_31(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_bit_format('30')
        self.assertTrue(is_valid)

    def test_netmask_at_31(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_bit_format('31')
        self.assertTrue(is_valid)

    def test_netmask_one_above_31(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_bit_format('32')
        self.assertFalse(is_valid)

    def test_netmask_well_above_31(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_bit_format('99')
        self.assertFalse(is_valid)

    def test_netmask_with_letters(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_bit_format('9f')
        self.assertFalse(is_valid)

    def test_netmask_with_symbols(self):

        is_valid = subnet_calculator.validate_ipv4_netmask_bit_format('9.0')
        self.assertFalse(is_valid)

class ValidateIpv6NetmaskBitFormat(unittest.TestCase):

    def test_empty_netmask(self):

        is_valid = subnet_calculator.validate_ipv6_netmask_bit_format('')
        self.assertFalse(is_valid)

    def test_netmask_well_below_zero(self):

        is_valid = subnet_calculator.validate_ipv6_netmask_bit_format('-99')
        self.assertFalse(is_valid)

    def test_netmask_one_below_zero(self):

        is_valid = subnet_calculator.validate_ipv6_netmask_bit_format('-1')
        self.assertFalse(is_valid)

    def test_netmask_at_zero(self):

        is_valid = subnet_calculator.validate_ipv6_netmask_bit_format('0')
        self.assertFalse(is_valid)

    def test_netmask_one_above_zero(self):

        is_valid = subnet_calculator.validate_ipv6_netmask_bit_format('1')
        self.assertTrue(is_valid)

    def test_netmask_well_above_zero(self):

        is_valid = subnet_calculator.validate_ipv6_netmask_bit_format('30')
        self.assertTrue(is_valid)

    def test_netmask_well_below_128(self):

        is_valid = subnet_calculator.validate_ipv6_netmask_bit_format('100')
        self.assertTrue(is_valid)

    def test_netmask_one_below_128(self):

        is_valid = subnet_calculator.validate_ipv6_netmask_bit_format('127')
        self.assertTrue(is_valid)

    def test_netmask_at_128(self):

        is_valid = subnet_calculator.validate_ipv6_netmask_bit_format('128')
        self.assertTrue(is_valid)

    def test_netmask_one_above_128(self):

        is_valid = subnet_calculator.validate_ipv6_netmask_bit_format('129')
        self.assertFalse(is_valid)

    def test_netmask_well_above_128(self):

        is_valid = subnet_calculator.validate_ipv6_netmask_bit_format('200')
        self.assertFalse(is_valid)

    def test_netmask_with_letters(self):

        is_valid = subnet_calculator.validate_ipv6_netmask_bit_format('9f')
        self.assertFalse(is_valid)

    def test_netmask_with_symbols(self):

        is_valid = subnet_calculator.validate_ipv6_netmask_bit_format('9.0')
        self.assertFalse(is_valid)


class TestConvertNetmaskBitsToBinary(unittest.TestCase):

    def test_minimum_netmask(self):

        binary_netmask = subnet_calculator.convert_netmask_bits_to_binary('1', IPV4_NETMASK_MAX_LENGTH, IPV4_NETMASK_PERIOD_INDEX)
        self.assertEquals('10000000.00000000.00000000.00000000', binary_netmask)

    def test_netmask_one_above_minimum(self):

        binary_netmask = subnet_calculator.convert_netmask_bits_to_binary('2', IPV4_NETMASK_MAX_LENGTH, IPV4_NETMASK_PERIOD_INDEX)
        self.assertEquals('11000000.00000000.00000000.00000000', binary_netmask)

    def test_netmask_well_above_minimum(self):

        binary_netmask = subnet_calculator.convert_netmask_bits_to_binary('12', IPV4_NETMASK_MAX_LENGTH, IPV4_NETMASK_PERIOD_INDEX)
        self.assertEquals('11111111.11110000.00000000.00000000', binary_netmask)

    def test_maximum_ipv4_netmask(self):

        binary_netmask = subnet_calculator.convert_netmask_bits_to_binary('31', IPV4_NETMASK_MAX_LENGTH, IPV4_NETMASK_PERIOD_INDEX)
        self.assertEquals('11111111.11111111.11111111.11111110', binary_netmask)

    def test_one_below_maximum_ipv4_netmask(self):

        binary_netmask = subnet_calculator.convert_netmask_bits_to_binary('30', IPV4_NETMASK_MAX_LENGTH, IPV4_NETMASK_PERIOD_INDEX)
        self.assertEquals('11111111.11111111.11111111.11111100', binary_netmask)

    def test_well_below_maximum_ipv4_netmask(self):

        binary_netmask = subnet_calculator.convert_netmask_bits_to_binary('16', IPV4_NETMASK_MAX_LENGTH, IPV4_NETMASK_PERIOD_INDEX)
        self.assertEquals('11111111.11111111.00000000.00000000', binary_netmask)

    def test_minimum_ipv6_netmask(self):

        binary_netmask = subnet_calculator.convert_netmask_bits_to_binary('1', IPV6_NETMASK_MAX_LENGTH, IPV6_NETMASK_PERIOD_INDEX)
        self.assertEquals('1000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000', binary_netmask)

    def test_one_above_minimum_ipv6_netmask(self):

        binary_netmask = subnet_calculator.convert_netmask_bits_to_binary('2', IPV6_NETMASK_MAX_LENGTH, IPV6_NETMASK_PERIOD_INDEX)
        self.assertEquals('1100000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000', binary_netmask)

    def test_well_above_minimum_ipv6_netmask(self):

        binary_netmask = subnet_calculator.convert_netmask_bits_to_binary('55', IPV6_NETMASK_MAX_LENGTH, IPV6_NETMASK_PERIOD_INDEX)
        self.assertEquals('1111111111111111.1111111111111111.1111111111111111.1111111000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000', binary_netmask)

    def test_maximum_ipv6_netmask(self):

        binary_netmask = subnet_calculator.convert_netmask_bits_to_binary('128', IPV6_NETMASK_MAX_LENGTH, IPV6_NETMASK_PERIOD_INDEX)
        self.assertEquals('1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111', binary_netmask)

    def test_one_below_maximum_ipv6_netmask(self):

        binary_netmask = subnet_calculator.convert_netmask_bits_to_binary('127', IPV6_NETMASK_MAX_LENGTH, IPV6_NETMASK_PERIOD_INDEX)
        self.assertEquals('1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111110', binary_netmask)

    def test_well_below_maximum_ipv6_netmask(self):

        binary_netmask = subnet_calculator.convert_netmask_bits_to_binary('64', IPV6_NETMASK_MAX_LENGTH, IPV6_NETMASK_PERIOD_INDEX)
        self.assertEquals('1111111111111111.1111111111111111.1111111111111111.1111111111111111.0000000000000000.0000000000000000.0000000000000000.0000000000000000', binary_netmask)

class TestCalculateIpv4Subnet(unittest.TestCase):

    def test_calculate_subnet_in_ip_format_with_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('0.0.0.0', '128.0.0.0')
        self.assertEquals('0.0.0.0', subnet)

    def test_calculate_subnet_in_ip_format_with_minimum_ip_and_one_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('0.0.0.0', '192.0.0.0')
        self.assertEquals('0.0.0.0', subnet)

    def test_calculate_subnet_in_ip_format_with_minimum_ip_and_well_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('0.0.0.0', '255.240.0.0')
        self.assertEquals('0.0.0.0', subnet)

    def test_calculate_subnet_in_ip_format_with_one_above_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('1.1.1.1', '128.0.0.0')
        self.assertEquals('0.0.0.0', subnet)

    def test_calculate_subnet_in_ip_format_with_well_above_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('160.160.160.160', '128.0.0.0')
        self.assertEquals('128.0.0.0', subnet)

    def test_calculate_subnet_in_ip_format_with_one_above_minimum_ip_and_one_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('1.1.1.1', '128.0.0.0')
        self.assertEquals('0.0.0.0', subnet)

    def test_calculate_subnet_in_ip_format_with_well_above_minimum_ip_and_well_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('160.160.160.160', '255.248.0.0')
        self.assertEquals('160.160.0.0', subnet)

    def test_calculate_subnet_in_ip_format_with_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('255.255.255.255', '255.255.255.254')
        self.assertEquals('255.255.255.254', subnet)

    def test_calculate_subnet_in_ip_format_with_maximum_ip_and_one_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('255.255.255.255', '255.255.255.252')
        self.assertEquals('255.255.255.252', subnet)



    def test_calculate_subnet_in_ip_format_maximum_ip_and_well_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('255.255.255.255', '255.255.240.0')
        self.assertEquals('255.255.240.0', subnet)

    def test_calculate_subnet_in_ip_format_with_one_below_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('254.254.254.254', '255.255.255.254')
        self.assertEquals('254.254.254.254', subnet)

    def test_calculate_subnet_in_ip_format_with_well_below_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('160.160.160.160', '255.255.255.254')
        self.assertEquals('160.160.160.160', subnet)

    def test_calculate_subnet_in_ip_format_with_one_below_maximum_ip_and_one_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('254.254.254.254', '255.255.255.252')
        self.assertEquals('254.254.254.252', subnet)

    def test_calculate_subnet_in_ip_format_with_well_below_maximum_ip_and_well_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('160.160.160.160', '255.255.240.0')
        self.assertEquals('160.160.160.0', subnet)

    def test_calculate_subnet_in_bit_format_with_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('0.0.0.0', '10000000.00000000.00000000.00000000')
        self.assertEquals('0.0.0.0', subnet)

    def test_calculate_subnet_in_bit_format_with_minimum_ip_and_one_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('0.0.0.0', '11000000.00000000.00000000.00000000')
        self.assertEquals('0.0.0.0', subnet)

    def test_calculate_subnet_in_bit_format_with_minimum_ip_and_well_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('0.0.0.0', '11111111.11110000.00000000.00000000')
        self.assertEquals('0.0.0.0', subnet)

    def test_calculate_subnet_in_bit_format_with_one_above_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('1.1.1.1', '10000000.00000000.00000000.00000000')
        self.assertEquals('0.0.0.0', subnet)

    def test_calculate_subnet_in_bit_format_with_well_above_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('160.160.160.160', '10000000.00000000.00000000.00000000')
        self.assertEquals('128.0.0.0', subnet)



    def test_calculate_subnet_in_bit_format_with_one_above_minimum_ip_and_one_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('1.1.1.1', '11000000.00000000.00000000.00000000')
        self.assertEquals('0.0.0.0', subnet)

    def test_calculate_subnet_in_bit_format_with_well_above_minimum_ip_and_well_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('160.160.160.160', '11111111.11111000.00000000.00000000')
        self.assertEquals('160.160.0.0', subnet)

    def test_calculate_subnet_in_bit_format_with_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('255.255.255.255', '11111111.11111111.11111111.11111110')
        self.assertEquals('255.255.255.254', subnet)

    def test_calculate_subnet_in_bit_format_with_maximum_ip_and_one_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('255.255.255.255', '11111111.11111111.11111111.11111100')
        self.assertEquals('255.255.255.252', subnet)

    def test_calculate_subnet_in_bit_format_maximum_ip_and_well_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('255.255.255.255', '11111111.11111111.11110000.00000000')
        self.assertEquals('255.255.240.0', subnet)

    def test_calculate_subnet_in_bit_format_with_one_below_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('254.254.254.254', '11111111.11111111.11111111.11111110')
        self.assertEquals('254.254.254.254', subnet)

    def test_calculate_subnet_in_bit_format_with_well_below_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('160.160.160.160', '11111111.11111111.11111111.11111110')
        self.assertEquals('160.160.160.160', subnet)

    def test_calculate_subnet_in_bit_format_with_one_below_maximum_ip_and_one_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('254.254.254.254', '11111111.11111111.11111111.11111100')
        self.assertEquals('254.254.254.252', subnet)

    def test_calculate_subnet_in_ip_format_with_well_below_maximum_ip_and_well_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('160.160.160.160', '11111111.11111111.11110000.0')
        self.assertEquals('160.160.160.0', subnet)

class TestCalculateIpv6Address(unittest.TestCase):

    def test_calculate_subnet_in_bit_format_with_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv6_subnet('0000:0000:0000:0000:0000:0000:0000:0000', '1000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000')
        self.assertEquals('0:0:0:0:0:0:0:0', subnet)
    
    def test_calculate_subnet_in_bit_format_with_minimum_ip_and_one_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv6_subnet('0000:0000:0000:0000:0000:0000:0000:0000', '1100000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000')
        self.assertEquals('0:0:0:0:0:0:0:0', subnet)

    def test_calculate_subnet_in_bit_format_with_minimum_ip_and_well_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv6_subnet('0000:0000:0000:0000:0000:0000:0000:0000', '1111111111111111.1111111100000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000')
        self.assertEquals('0:0:0:0:0:0:0:0', subnet)

    def test_calculate_subnet_in_bit_format_with_one_above_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv6_subnet('1111:1111:1111:1111:1111:1111:1111:1111', '1000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000')
        self.assertEquals('0:0:0:0:0:0:0:0', subnet)

    def test_calculate_subnet_in_bit_format_with_well_above_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv6_subnet('11f5:1a41:9c31:e1a1:1401:a0a5:c2c1:a9d1', '1000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000')
        self.assertEquals('0:0:0:0:0:0:0:0', subnet)

    def test_calculate_subnet_in_bit_format_with_one_above_minimum_ip_and_one_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv6_subnet('1111:1111:1111:1111:1111:1111:1111:1111', '1100000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000')
        self.assertEquals('0:0:0:0:0:0:0:0', subnet)

    def test_calculate_subnet_in_bit_format_with_well_above_minimum_ip_and_well_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv6_subnet('11f5:1a41:9c31:e1a1:1401:a0a5:c2c1:a9d1', '1111111111111111.1111111111111111.1111111111111111.1111111111110000.0000000000000000.0000000000000000.0000000000000000.0000000000000000')
        self.assertEquals('11f5:1a41:9c31:e1a0:0:0:0:0', subnet)

    def test_calculate_subnet_in_bit_format_with_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv6_subnet('ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', '1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111110')
        self.assertEquals('ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe', subnet)

    def test_calculate_subnet_in_bit_format_with_maximum_ip_and_one_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv6_subnet('ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', '1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111100')
        self.assertEquals('ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffc', subnet)

    def test_calculate_subnet_in_bit_format_maximum_ip_and_well_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv6_subnet('ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', '1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111110000.0000000000000000.0000000000000000.0000000000000000')
        self.assertEquals('ffff:ffff:ffff:ffff:fff0:0:0:0', subnet)

    def test_calculate_subnet_in_bit_format_with_one_below_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv6_subnet('eeee:eeee:eeee:eeee:eeee:eeee:eeee:eeee', '1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111110')
        self.assertEquals('eeee:eeee:eeee:eeee:eeee:eeee:eeee:eeee', subnet)

    def test_calculate_subnet_in_bit_format_with_well_below_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv6_subnet('55d5:a4ff:c585:d5c7:b999:c58c:ffd5:d784', '1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111110')
        self.assertEquals('55d5:a4ff:c585:d5c7:b999:c58c:ffd5:d784', subnet)

    def test_calculate_subnet_in_bit_format_with_one_below_maximum_ip_and_one_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv6_subnet('eeee:eeee:eeee:eeee:eeee:eeee:eeee:eeee', '1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111100')
        self.assertEquals('eeee:eeee:eeee:eeee:eeee:eeee:eeee:eeec', subnet)

    def test_calculate_subnet_in_ip_format_with_well_below_maximum_ip_and_well_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv6_subnet('55d5:a4ff:c585:d5c7:b999:c58c:ffd5:d784', '1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111000000.0000000000000000.0000000000000000')
        self.assertEquals('55d5:a4ff:c585:d5c7:b999:c580:0:0', subnet)
    
class TestExpandIpv6Address(unittest.TestCase):

    def test_no_empty_groups(self):

        expanded_ipv6_address = subnet_calculator.expand_ipv6_address('20f1:2a52:0000:0000:0000:0000:0000:2001')
        self.assertEquals('20f1:2a52:0000:0000:0000:0000:0000:2001', expanded_ipv6_address)

    def test_one_empty_group(self):

        expanded_ipv6_address = subnet_calculator.expand_ipv6_address('20f1:2a52:0000:0000:0000:0000::2001')
        self.assertEquals('20f1:2a52:0000:0000:0000:0000:0000:2001', expanded_ipv6_address)

    def test_many_empty_groups(self):

        expanded_ipv6_address = subnet_calculator.expand_ipv6_address('20f1:2a52::2001')
        self.assertEquals('20f1:2a52:0000:0000:0000:0000:0000:2001', expanded_ipv6_address)

    def test_only_empty_groups(self):

        expanded_ipv6_address = subnet_calculator.expand_ipv6_address('::')
        self.assertEquals('0000:0000:0000:0000:0000:0000:0000:0000', expanded_ipv6_address)

class TestCalculateBinaryOpposite(unittest.TestCase):

    def test_one_zero(self):

        binary_opposite = subnet_calculator.calculate_binary_opposite('0', 1)
        self.assertEquals('1', binary_opposite)

    def test_one_one(self):

        binary_opposite = subnet_calculator.calculate_binary_opposite('1', 1)
        self.assertEquals('0', binary_opposite)

    def test_small_binary_string(self):

        binary_opposite = subnet_calculator.calculate_binary_opposite('101001', 1)
        self.assertEquals('010110', binary_opposite)

    def test_large_binary_string(self):

        binary_opposite = subnet_calculator.calculate_binary_opposite('111010110111010101101', 1)
        self.assertEquals('000101001000101010010', binary_opposite)

    def test_seperated_binary_string(self):

        binary_opposite = subnet_calculator.calculate_binary_opposite('1101.1110.1111', 1)
        self.assertEquals('0010.0001.0000', binary_opposite)

class TestCalculateIpv4UpperRange(unittest.TestCase):

    def test_calculate_range_in_ip_format_with_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('0.0.0.0', '128.0.0.0')
        self.assertEquals('127.255.255.254', subnet)

    def test_calculate_range_in_ip_format_with_minimum_ip_and_one_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('0.0.0.0', '192.0.0.0')
        self.assertEquals('63.255.255.254', subnet)

    def test_calculate_range_in_ip_format_with_minimum_ip_and_well_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('0.0.0.0', '255.240.0.0')
        self.assertEquals('0.15.255.254', subnet)

    def test_calculate_range_in_ip_format_with_one_above_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('1.1.1.1', '128.0.0.0')
        self.assertEquals('127.255.255.254', subnet)

    def test_calculate_range_in_ip_format_with_well_above_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('160.160.160.160', '128.0.0.0')
        self.assertEquals('255.255.255.254', subnet)

    def test_calculate_range_in_ip_format_with_well_above_minimum_ip_and_well_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('160.160.160.160', '255.248.0.0')
        self.assertEquals('160.167.255.254', subnet)

    def test_calculate_range_in_ip_format_with_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('255.255.255.255', '255.255.255.254')
        self.assertEquals('255.255.255.254', subnet)

    def test_calculate_range_in_ip_format_with_maximum_ip_and_one_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('255.255.255.255', '255.255.255.252')
        self.assertEquals('255.255.255.254', subnet)

    def test_calculate_range_in_ip_format_maximum_ip_and_well_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('255.255.255.255', '255.255.240.0')
        self.assertEquals('255.255.255.254', subnet)

    def test_calculate_range_in_ip_format_with_one_below_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('254.254.254.254', '255.255.255.254')
        self.assertEquals('254.254.254.254', subnet)

    def test_calculate_range_in_ip_format_with_well_below_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('160.160.160.160', '255.255.255.254')
        self.assertEquals('160.160.160.160', subnet)

    def test_calculate_range_in_ip_format_with_one_below_maximum_ip_and_one_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('254.254.254.254', '255.255.255.252')
        self.assertEquals('254.254.254.254', subnet)

    def test_calculate_range_in_ip_format_with_well_below_maximum_ip_and_well_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('160.160.160.160', '255.255.240.0')
        self.assertEquals('160.160.175.254', subnet)

    def test_calculate_range_in_bit_format_with_minimum_ip_and_well_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('0.0.0.0', '11111111.11110000.00000000.00000000')
        self.assertEquals('0.15.255.254', subnet)

    def test_calculate_range_in_bit_format_with_one_above_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('1.1.1.1', '10000000.00000000.00000000.00000000')
        self.assertEquals('127.255.255.254', subnet)

    def test_calculate_range_in_bit_format_with_well_above_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('160.160.160.160', '10000000.00000000.00000000.00000000')
        self.assertEquals('255.255.255.254', subnet)

    def test_calculate_range_in_bit_format_with_one_above_minimum_ip_and_one_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('1.1.1.1', '11000000.00000000.00000000.00000000')
        self.assertEquals('63.255.255.254', subnet)

    def test_calculate_range_in_bit_format_with_well_above_minimum_ip_and_well_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('160.160.160.160', '11111111.11110000.00000000.00000000')
        self.assertEquals('160.175.255.254', subnet)

    def test_calculate_range_in_bit_format_with_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('255.255.255.255', '11111111.11111111.11111111.11111110')
        self.assertEquals('255.255.255.254', subnet)

    def test_calculate_range_in_bit_format_with_maximum_ip_and_one_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('255.255.255.255', '11111111.11111111.11111111.11111100')
        self.assertEquals('255.255.255.254', subnet)

    def test_calculate_range_in_bit_format_maximum_ip_and_well_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('255.255.255.255', '11111111.11111111.11110000.00000000')
        self.assertEquals('255.255.255.254', subnet)

    def test_calculate_range_in_bit_format_with_one_below_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('254.254.254.254', '11111111.11111111.11111111.11111110')
        self.assertEquals('254.254.254.254', subnet)

    def test_calculate_range_in_bit_format_with_well_below_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('160.160.160.160', '11111111.11111111.11111111.11111110')
        self.assertEquals('160.160.160.160', subnet)

    def test_calculate_range_in_bit_format_with_one_below_maximum_ip_and_one_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('254.254.254.254', '11111111.11111111.11111111.11111100')
        self.assertEquals('254.254.254.254', subnet)

    def test_calculate_range_in_bit_format_with_well_below_maximum_ip_and_well_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv4_range('160.160.160.160', '11111111.11111111.11110000.00000000')
        self.assertEquals('160.160.175.254', subnet)

class CalculateUpperIpv6Range(unittest.TestCase):

    def test_calculate_upper_range_at_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv6_range('0000::0000','1000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000')
        self.assertEquals('7fff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', subnet)

    def test_calculate_upper_range_one_above_minimum_ip_and_one_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv6_range('1111:1111:1111:1111:1111:1111:1111:1111','1100000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000')
        self.assertEquals('3fff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', subnet)

    def test_calculate_upper_range_well_above_minimum_ip_and_well_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv6_range('fe80:cd12:d45c:c150:1235:0000:211e:729c','1111111111111111.1111111111111111.1111111111111111.1111111111111000.0000000000000000.0000000000000000.0000000000000000.0000000000000000')
        self.assertEquals('fe80:cd12:d45c:c157:ffff:ffff:ffff:ffff', subnet)

    def test_calculate_upper_well_below_maximum_ip_and_well_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv6_range('fe88:df57:d56c:c557:57c5:7c55:588e:789c','1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.0000000000000000.0000000000000000.0000000000000000')
        self.assertEquals('fe88:df57:d56c:c557:57c5:ffff:ffff:ffff', subnet)

    def test_calculate_upper_one_below_maximum_ip_and_one_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv6_range('fe88:df57:d56c:c557:57c5:7c55:588e:789c','1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.0000000000000000.0000000000000000.0000000000000000')
        self.assertEquals('fe88:df57:d56c:c557:57c5:ffff:ffff:ffff', subnet)

    def test_calculate_upper_at_maximum_ip_and_at_maximum_subnet(self):

        subnet = subnet_calculator.calculate_upper_ipv6_range('ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff','1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111')
        self.assertEquals('ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', subnet)

class CalculateLowerIpv4Range(unittest.TestCase):

    def test_calculate_lower_in_bit_format_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_lower_ipv4_range('0.0.0.0', '10000000.00000000.00000000.00000000')
        self.assertEquals('0.0.0.1', subnet)

    def test_calculate_lower_in_bit_format_one_above_minimum_ip_and_one_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_lower_ipv4_range('1.1.1.1', '11000000.00000000.00000000.00000000')
        self.assertEquals('0.0.0.1', subnet)

    def test_calculate_lower_in_bit_format_well_above_minimum_ip_and_well_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_lower_ipv4_range('160.160.160.100', '11111111.11111100.00000000.00000000')
        self.assertEquals('160.160.0.1', subnet)

    def test_calculate_lower_in_bit_format_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_lower_ipv4_range('255.255.255.255', '11111111.11111111.11111111.11111110')
        self.assertEquals('255.255.255.255', subnet)

    def test_calculate_lower_in_bit_format_one_below_maximum_ip_and_one_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_lower_ipv4_range('254.254.254.254', '11111111.11111111.11111111.11111100')
        self.assertEquals('254.254.254.253', subnet)

    def test_calculate_lower_in_bit_format_well_below_maximum_ip_and_well_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_lower_ipv4_range('254.128.0.0', '11111111.11111111.11100000.00000000')
        self.assertEquals('254.128.0.1', subnet)

    def test_calculate_lower_in_ip_format_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_lower_ipv4_range('0.0.0.0', '128.0.0.0')
        self.assertEquals('0.0.0.1', subnet)

    def test_calculate_lower_in_ip_format_one_above_minimum_ip_and_one_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_lower_ipv4_range('1.1.1.1', '192.0.0.0')
        self.assertEquals('0.0.0.1', subnet)

    def test_calculate_lower_in_ip_format_well_above_minimum_ip_and_well_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_lower_ipv4_range('160.160.160.100', '255.252.0.0')
        self.assertEquals('160.160.0.1', subnet)

    def test_calculate_lower_in_ip_format_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_lower_ipv4_range('255.255.255.255', '255.255.255.254')
        self.assertEquals('255.255.255.255', subnet)

    def test_calculate_lower_in_ip_format_one_below_maximum_ip_and_one_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_lower_ipv4_range('254.254.254.254', '255.255.255.252')
        self.assertEquals('254.254.254.253', subnet)

    def test_calculate_lower_in_ip_format_well_below_maximum_ip_and_well_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_lower_ipv4_range('254.128.0.0', '255.255.224.0')
        self.assertEquals('254.128.0.1', subnet)

if __name__ == '__main__':
    unittest.main()
