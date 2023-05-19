#!/usr/bin/env python3

# @Author: shocquen

# This script is for adding new member to the BDE
# Give it a list of login

import sys
import ftapi
import os
from dotenv import load_dotenv

load_dotenv()

ftCLIENT_ID = os.getenv("FT_CLIENT_ID")
ftCLIENT_SECRET = os.getenv("FT_CLIENT_SECRET")


def parse_args(argv):
    logins = argv[1:]
    if len(argv) < 1:
        print("Usage: python3 main.py login1 login2 ...")
        sys.exit(1)
    return logins


def check_users(users: list[ftapi.User], logins: list[str]):
    print("Check if the following users are active students:")
    loginsNotFound = [l for l in logins if l not in [u.login for u in users]]
    if len(loginsNotFound) > 0:
        print("❌ The following logins were not found: " + ", ".join(loginsNotFound))
    userNonActive = [u.login for u in users if u.active == False]
    if len(userNonActive) > 0:
        print("❌ The following users are not active: " + ", ".join(userNonActive))

    if len(users) != 0:
        print("✅ Found " + str(len(users)) + " users")
    else:
        print("❌ No user found")
        exit(1)


def main():
    logins = parse_args(sys.argv)
    ftClient = ftapi.FtClient(ftCLIENT_ID, ftCLIENT_SECRET)
    ftClient.setAccessToken()
    ftUsers = ftClient.getUsers(logins)
    check_users(ftUsers, logins)


if __name__ == "__main__":
    main()
