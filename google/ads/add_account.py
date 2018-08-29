#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Initializes an AdWordsClient without using yaml-cached credentials.

While our LoadFromStorage method provides a useful shortcut to instantiate a
client if you regularly use just one set of credentials, production applications
may need to swap out users. This example shows you how to create an OAuth2
client and an AdWordsClient without relying on a yaml file.
"""


from googleads import adwords
from googleads import oauth2
from datetime import  datetime
import _locale
_locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf-8'])

from client import  Client

# OAuth2 credential information. In a real application, you'd probably be
# pulling these values from a credential storage.
CLIENT_ID = '413010591024-jboften13risuj2fk23cv7pmio2qc33m.apps.googleusercontent.com'
CLIENT_SECRET = 'zdz75pa9SUAHQJcH4iAcc9OS'
REFRESH_TOKEN = '1/z_iA0r3m5bvcU9n0q6zxUmGZUxZ43pN1fkY_qWlggko'

# AdWords API information.
DEVELOPER_TOKEN = '9_rUnKuMInGNUiwv6C4icg'
USER_AGENT = 'test_python_ads'
CLIENT_CUSTOMER_ID = '566-531-9705'


def main(adwords_client):
  managed_customer_service = adwords_client.GetService(
    'ManagedCustomerService', version='v201806')

  today = datetime.today().strftime('%Y%m%d %H:%M:%S')
  # Construct operations and add campaign.
  operations = [{
    'operator': 'ADD',
    'operand': {
      'name': 'Account created with ManagedCustomerService on %s' % today,
      'currencyCode': 'EUR',
      'dateTimeZone': 'Europe/London',
    },
    # For whitelisted users only, uncomment the inviteeEmail and inviteeRole
    # attributes to invite a user to have access to an account on an ADD. An
    # email will be sent inviting the user to have access to the newly created
    # account.
    # 'inviteeEmail': 'invited_user1@example.com',
    # 'inviteeRole': 'ADMINISTRATIVE'
  }]

  # Create the account. It is possible to create multiple accounts with one
  # request by sending an array of operations.
  accounts = managed_customer_service.mutate(operations)

  # Display results.
  for account in accounts['value']:
    print('Account with customer ID "%s" was successfully created.'
          % account['customerId'])


if __name__ == '__main__':
  # main(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN, DEVELOPER_TOKEN, USER_AGENT,
  #      CLIENT_CUSTOMER_ID)
  main(Client().ins)

