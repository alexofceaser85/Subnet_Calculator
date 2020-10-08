#!/usr/bin/env python3

import unittest
import subnet_calculator

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

class TestValidateNetmaskIpFormat(unittest.TestCase):

    def test_empty_netmask(self):
        
        is_valid = subnet_calculator.validate_netmask_ip_format('')
        self.assertFalse(is_valid)

    def test_netmask_with_no_digits_in_octet(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('....')
        self.assertFalse(is_valid)

    def test_netmask_with_octets_well_below_four(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('255')
        self.assertFalse(is_valid)

    def test_netmask_with_octets_one_below_four(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('255.255.255')
        self.assertFalse(is_valid)

    def test_netmask_with_octets_at_four(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('255.255.255.0')
        self.assertTrue(is_valid)

    def test_netmask_with_octets_one_above_four(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('255.255.255.0.0')
        self.assertFalse(is_valid)

    def test_netmask_with_octets_well_above_four(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('255.255.255.255.255.255.255.0')
        self.assertFalse(is_valid)

    def test_netmask_with_empty_octet(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('255..0.0')
        self.assertFalse(is_valid)

    def test_netmask_with_one_non_zero_after_one_zero(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('0.255.0.0')
        self.assertFalse(is_valid)

    def test_netmask_with_many_non_zeros_after_one_zero(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('0.255.255.255')
        self.assertFalse(is_valid)

    def test_netmask_with_one_non_zero_after_many_non_zeros(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('0.0.0.255')
        self.assertFalse(is_valid)

    def test_netmask_with_octet_less_than_255_before_255(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('0.255.0.0')
        self.assertFalse(is_valid)

    def test_netmask_with_octets_all_zero(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('0.0.0.0')
        self.assertTrue(is_valid)

    def test_netmask_with_octets_all_255(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('255.255.255.255')
        self.assertFalse(is_valid)

    def test_netmask_with_one_non_255_or_0_number(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('255.248.0.0')
        self.assertTrue(is_valid)

    def test_netmask_with_one_more_than_one_non_255_or_0_number(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('255.248.240.0')
        self.assertFalse(is_valid)

    def test_netmask_with_well_more_than_one_non_255_or_0_number(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('254.248.240.128')
        self.assertFalse(is_valid)

    def test_maximum_bit_netmask_ending_in_254(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('255.255.255.254')
        self.assertTrue(is_valid)

    def test_netmask_with_one_octet_with_valid_value_of_254(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('255.255.255.254')
        self.assertTrue(is_valid)

    def test_netmask_with_one_octet_with_valid_value_of_252(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('255.255.255.252')
        self.assertTrue(is_valid)

    def test_netmask_with_one_octet_with_valid_value_of_248(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('255.255.255.248')
        self.assertTrue(is_valid)

    def test_netmask_with_one_octet_with_valid_value_of_240(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('255.255.255.240')
        self.assertTrue(is_valid)

    def test_netmask_with_one_octet_with_valid_value_of_224(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('255.255.255.224')
        self.assertTrue(is_valid)

    def test_netmask_with_one_octet_with_valid_value_of_192(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('255.255.255.192')
        self.assertTrue(is_valid)

    def test_netmask_with_one_octet_with_valid_value_of_128(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('255.255.255.128')
        self.assertTrue(is_valid)
    
    def test_netmask_with_non_valid_octet_value(self):

        is_valid = subnet_calculator.validate_netmask_ip_format('255.255.255.180')
        self.assertFalse(is_valid)

class ValidateNetmaskBitFormat(unittest.TestCase):

    def test_empty_netmask(self):

        is_valid = subnet_calculator.validate_netmask_bit_format('')
        self.assertFalse(is_valid)

    def test_netmask_well_below_zero(self):

        is_valid = subnet_calculator.validate_netmask_bit_format('-99')
        self.assertFalse(is_valid)

    def test_netmask_one_below_zero(self):

        is_valid = subnet_calculator.validate_netmask_bit_format('-1')
        self.assertFalse(is_valid)

    def test_netmask_at_zero(self):

        is_valid = subnet_calculator.validate_netmask_bit_format('0')
        self.assertFalse(is_valid)

    def test_netmask_one_above_zero(self):

        is_valid = subnet_calculator.validate_netmask_bit_format('1')
        self.assertTrue(is_valid)

    def test_netmask_well_above_zero(self):

        is_valid = subnet_calculator.validate_netmask_bit_format('12')
        self.assertTrue(is_valid)

    def test_netmask_well_below_31(self):

        is_valid = subnet_calculator.validate_netmask_bit_format('18')
        self.assertTrue(is_valid)

    def test_netmask_one_below_31(self):

        is_valid = subnet_calculator.validate_netmask_bit_format('30')
        self.assertTrue(is_valid)

    def test_netmask_at_31(self):

        is_valid = subnet_calculator.validate_netmask_bit_format('31')
        self.assertTrue(is_valid)

    def test_netmask_one_above_31(self):

        is_valid = subnet_calculator.validate_netmask_bit_format('32')
        self.assertFalse(is_valid)

    def test_netmask_well_above_31(self):

        is_valid = subnet_calculator.validate_netmask_bit_format('99')
        self.assertFalse(is_valid)

    def test_netmask_with_letters(self):

        is_valid = subnet_calculator.validate_netmask_bit_format('9f')
        self.assertFalse(is_valid)

    def test_netmask_with_symbols(self):

        is_valid = subnet_calculator.validate_netmask_bit_format('9.0')
        self.assertFalse(is_valid)

class TestCalculateIpv4Subnet(unittest.TestCase):

    def test_calculate_ipv4_with_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('0.0.0.0', '128.0.0.0')
        self.assertEquals('0.0.0.0', subnet)

    def test_calculate_ipv4_with_minimum_ip_and_one_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('0.0.0.0', '192.0.0.0')
        self.assertEquals('0.0.0.0', subnet)

    def test_calculate_ipv4_with_minimum_ip_and_well_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('0.0.0.0', '255.240.0.0')
        self.assertEquals('0.0.0.0', subnet)

    def test_calculate_ipv4_with_one_above_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('1.1.1.1', '0.0.0.0')
        self.assertEquals('0.0.0.0', subnet)

    def test_calculate_ipv4_with_well_above_minimum_ip_and_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('160.160.160.160', '0.0.0.0')
        self.assertEquals('0.0.0.0', subnet)

    def test_calculate_ipv4_with_one_above_minimum_ip_and_one_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('1.1.1.1', '128.0.0.0')
        self.assertEquals('0.0.0.0', subnet)

    def test_calculate_ipv4_with_well_above_minimum_ip_and_well_above_minimum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('160.160.160.160', '255.248.0.0')
        self.assertEquals('160.160.0.0', subnet)


    def test_calculate_ipv4_with_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('255.255.255.255', '255.255.255.254')
        self.assertEquals('255.255.255.254', subnet)

    def test_calculate_ipv4_with_maximum_ip_and_one_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('255.255.255.255', '255.255.255.252')
        self.assertEquals('255.255.255.252', subnet)

    def test_calculate_ipv4_with_maximum_ip_and_well_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('255.255.255.255', '255.255.240.0')
        self.assertEquals('255.255.240.0', subnet)

    def test_calculate_ipv4_with_one_below_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('254.254.254.254', '255.255.255.254')
        self.assertEquals('254.254.254.254', subnet)

    def test_calculate_ipv4_with_well_below_maximum_ip_and_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('160.160.160.160', '255.255.255.254')
        self.assertEquals('160.160.160.160', subnet)

    def test_calculate_ipv4_with_one_below_maximum_ip_and_one_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('254.254.254.254', '255.255.255.252')
        self.assertEquals('254.254.254.252', subnet)

    def test_calculate_ipv4_with_well_below_maximum_ip_and_well_below_maximum_subnet(self):

        subnet = subnet_calculator.calculate_ipv4_subnet('160.160.160.160', '255.255.240.0')
        self.assertEquals('160.160.160.0', subnet)


if __name__ == '__main__':
    unittest.main()
