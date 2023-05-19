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


def main():
    logins = parse_args(sys.argv)
    ftClient = ftapi.FtClient(ftCLIENT_ID, ftCLIENT_SECRET)
    ftClient.setAccessToken()
    ftUsers = ftClient.getUsers(logins)
    for user in ftUsers:
        print(user.displayname, user.login, user.email)


if __name__ == "__main__":
    main()
