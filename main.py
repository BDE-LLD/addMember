#!/usr/bin/env python3

# @Author: shocquen

# This script is for adding new member to the BDE
# Give it a list of login

import ftapi
import gapi

from email.message import EmailMessage
import sys
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
    try:
        logins = parse_args(sys.argv)
        ftClient = ftapi.FtClient(ftCLIENT_ID, ftCLIENT_SECRET)
        ftClient.setAccessToken()
        ftUsers = ftClient.getUsers(logins)
        check_users(ftUsers, logins)

        creds = gapi.creds()
        admin = gapi.getAdminService(creds=creds)
        gmail = gapi.getGmailService(creds=creds)
        for user in ftUsers:
            print(user.displayname, user.login, user.email)
            guser = gapi.User(
                name=gapi.UserName(
                    user.last_name,
                    user.first_name,
                    user.displayname,
                ),
                password=gapi.generatePassword(),
                primaryEmail=user.login + "@bde42.fr",
                recoveryEmail=user.email,
                changePasswordAtNextLogin=True,
            )

            guser.insert(admin)

            message = EmailMessage()
            message["To"] = guser.recoveryEmail
            message["From"] = "service-info@bde42.fr"
            message["Subject"] = "Welcome to the BDE LLD!"
            message["content-type"] = "text/html"

            message.set_content(
                f"""

Hi {guser.name.givenName}! Welcome to the BDE LLD!
    - First name: {guser.name.givenName}
    - Last name: {guser.name.familyName}
    - Display name: {guser.name.displayName}
    - Primary email: {guser.primaryEmail}
    - Recovery email: {guser.recoveryEmail}
    - Password: {guser.password}
    - Change password at next login: {guser.changePasswordAtNextLogin}

You can follow the BDE calendar here https://calendar.google.com/calendar/u/1?cid=Y19uMDdiZGEzczA5aHFlZ24xZjF2dnZsaGMza0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t
"""
            )
            gapi.sendGmail(gmail, message)
    except Exception as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
