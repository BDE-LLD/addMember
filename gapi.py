from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


from email.message import EmailMessage
import base64

import secrets
import string

# If modifying these scopes, delete the file token.json.
SCOPES = [
    "https://mail.google.com/",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.compose",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/admin.directory.user",
    "https://www.googleapis.com/auth/admin.directory.group",
]


def generatePassword(psw_len: int = 12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = "".join(secrets.choice(alphabet) for i in range(psw_len))
        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3
        ):
            break
    return password


class UserName:
    familyName: str
    givenName: str
    displayName: str

    def __init__(self, familyName: str, givenName: str, displayName: str):
        self.familyName = familyName
        self.givenName = givenName
        self.displayName = displayName


class User:
    name = UserName
    password: str
    primaryEmail: str
    recoveryEmail: str
    changePasswordAtNextLogin: bool
    orgUnitPath: str = "/"

    def __init__(
        self,
        name: UserName,
        password: str,
        primaryEmail: str,
        recoveryEmail: str,
        changePasswordAtNextLogin: bool,
        orgUnitPath: str = "/",
    ):
        self.name = name
        self.password = password
        self.primaryEmail = primaryEmail
        self.recoveryEmail = recoveryEmail
        self.changePasswordAtNextLogin = changePasswordAtNextLogin
        self.orgUnitPath = orgUnitPath

    def toDict(self):
        return {
            "name": {
                "familyName": self.name.familyName,
                "givenName": self.name.givenName,
                "displayName": self.name.displayName,
            },
            "password": self.password,
            "primaryEmail": self.primaryEmail,
            "recoveryEmail": self.recoveryEmail,
            "changePasswordAtNextLogin": self.changePasswordAtNextLogin,
            "orgUnitPath": self.orgUnitPath,
        }

    def insert(self, service):
        try:
            res = service.users().insert(body=self.toDict()).execute()
            return res
        except HttpError as error:
            print("An error occurred: %s" % error)


def sendGmail(service, message: EmailMessage) -> dict:
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    body = {"raw": encoded_message}
    try:
        res = service.users().messages().send(userId="me", body=body).execute()
        return res
    except HttpError as error:
        print("An error occurred: %s" % error)


def creds() -> Credentials:
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def getGmailService(creds: Credentials):
    return build("gmail", "v1", credentials=creds)


def getAdminService(creds: Credentials):
    return build("admin", "directory_v1", credentials=creds)


def main():
    creds = creds()

    try:
        admin = build("admin", "directory_v1", credentials=creds)
        gmail = build("gmail", "v1", credentials=creds)

        # Call the Admin SDK Directory API
        # Insert dum user
        user = User(
            UserName("Doe", "John", "John Doe"),
            generatePassword(),
            "johnDoe@bde42.fr",
            "saky@bde42.fr",
            True,
        )
        user.insert(admin)

        message = EmailMessage()

        message["To"] = "saky@bde42.fr"
        message["From"] = "service-info@bde42.fr"
        message["Subject"] = "Automated draft"
        message["content-type"] = "text/html"

        message.set_content(
            f"""
One dumb user has been created:
    - First name: {user.name.givenName}
    - Last name: {user.name.familyName}
    - Display name: {user.name.displayName}
    - Primary email: {user.primaryEmail}
    - Recovery email: {user.recoveryEmail}
    - Password: {user.password}
    - Change password at next login: {user.changePasswordAtNextLogin}
"""
        )

        sendGmail(gmail, message)

    except HttpError as error:
        print("An error occurred: %s" % error)


if __name__ == "__main__":
    main()
