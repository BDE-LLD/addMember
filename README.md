# NewMember

## main.py

```sh
./main.py [...logins]
```

At the moment it will only check if the students have an active cursus.

## TODO

- [x] Check the logins
- [ ] Create a user per login [(doc)](https://developers.google.com/admin-sdk/directory/v1/guides/manage-users)
- [ ] Add the new users to the `actifs` group
- [ ] Send a mail to the new users to welcom them [(doc)](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send)
  - The mail must contain :
    - Temp password
    - Mail adress
    - Instructions to follow the calendar
    - Link to come on the private discord server ?
