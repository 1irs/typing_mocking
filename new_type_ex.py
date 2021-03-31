from typing import NewType, Union

UserId = NewType('UserId', int)
AccountId = NewType('AccountId', str)
ProfileId = NewType('ProfileId', str)

some_id = UserId(524313)

def find_account(entity_id: AccountId):
    pass

def find_profile(entity_id: ProfileId):
    pass

id1: AccountId = AccountId('123')
id2: ProfileId = ProfileId('234')

find_account(id1)
find_profile(id2)



