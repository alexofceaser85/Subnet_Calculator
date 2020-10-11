#!python
"""
This is the main method for the program
"""

import subnet_calculator
import service

__author__ = "Alex DeCesare"
__version__ = "11-October-2020"

def main():

    service.run('<h1>hello world</h1>')
    service.generate_handler('<h1>hello world</h1>')
    print(service.get_ip_address)
    print('x')

if __name__ == '__main__':
    main()
