#!/usr/bin/env python3

"""This program calculate Fibbonacci number"""

import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


def fibonacci_func(number):
    """Calculate Fibbonacci number"""
    if number < 2:
        return number
    return fibonacci_func(number - 1) + fibonacci_func(number - 2)


def main():
    """ Main function """
    logging.info("Enter Fibonacci number:")
    logging.info(str(fibonacci_func(number=int(input()))))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Program was stoped with error")
