#!/usr/bin/env python3

import getpass as gp


def get_password():
    print("Please enter your password: ")
    password1= gp.getpass()
    print("Please enter your password again: ")
    password2= gp.getpass()

    if password1 != password2:
        print("Passwords did NOT match")
    else:
        print("Passwords matched!")


if __name__ == "__main__":
    get_password()



