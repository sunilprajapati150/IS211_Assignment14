#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Recursion to implement algorithms """


def fibonacci(position):

    if position == 1:
        return 1
    if position == 0:
        return 0

    return fibonacci(position-2) + fibonacci(position-1)


def gcd(num1, num2):

    if num2 == 0:
        return num1

    return gcd(num2, (num1 % num2))


def compareTo(s1, s2):

    next_char1 = s1[1:2]
    next_char2 = s2[1:2]

    if len(next_char1) == 0 and len(next_char2) != 0:
        return -1
    elif len(next_char1) != 0 and len(next_char2) == 0:
        return 1
    elif len(next_char1) == 0 and len(next_char2) == 0:
        return 0

    if ord(next_char1) < ord(next_char2):
        return -1
    elif ord(next_char1) > ord(next_char2):
        return 1

    return compareTo(s1[1:], s2[1:])


def main():

    print "Choose a recursive function you wish to run:\n" \
          "1 for FIBONACCI\n" \
          "2 for GCD\n" \
          "3 for STRING COMPARE\n"
    try:
        while True:
            decision = int(raw_input("\nYour choice: "))

            if decision == 1:
                pos = int(raw_input("What position in the Fibonacci Sequence do you want? "))
                print "Answer: ", fibonacci(pos)
            elif decision == 2:
                n1 = int(raw_input("Number 1: "))
                n2 = int(raw_input("Number 2: "))
                print "Answer: ", gcd(n1, n2)
            elif decision == 3:
                str1 = raw_input("String 1: ")
                str2 = raw_input("String 2: ")
                print "Response: ", compareTo(str1, str2)
            elif decision < 1 or decision > 3:
                print "Please enter 1, 2, or 3."

    except ValueError:
        print "Please enter a valid value."


if __name__ == "__main__":
    main()
