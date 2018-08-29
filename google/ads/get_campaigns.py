#!/usr/bin/env python
#
# Copyright 2016 Google Inc. All Rights Reserved.
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

"""This example adds campaigns.

To get campaigns, run get_campaigns.py.

The LoadFromStorage method is pulling credentials and properties from a
"googleads.yaml" file. By default, it looks for this file in your home
directory. For more information, see the "Caching authentication information"
section of our README.

"""


import datetime
import uuid
from googleads import adwords

# from googleads import oauth2
import _locale

_locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf-8'])
from client import  Client

PAGE_SIZE = 100


def main(client):
  # Initialize appropriate service.
  campaign_service = client.GetService('CampaignService', version='v201806')

  # Construct selector and get all campaigns.
  offset = 0
  selector = {
      'fields': ['Id', 'Name', 'Status'],
      'paging': {
          'startIndex': str(offset),
          'numberResults': str(PAGE_SIZE)
      }
  }

  more_pages = True
  while more_pages:
    page = campaign_service.get(selector)
    print(page)
    # Display results.
    if 'entries' in page:
      for campaign in page['entries']:
        print ('Campaign with id "%s", name "%s", and status "%s" was '
               'found.' % (campaign['id'], campaign['name'],
                           campaign['status']))
    else:
      print("No campaigns were found.")
    offset += PAGE_SIZE
    selector['paging']['startIndex'] = str(offset)
    more_pages = offset < int(page['totalNumEntries'])




CLIENT_ID = '413010591024-jboften13risuj2fk23cv7pmio2qc33m.apps.googleusercontent.com'
CLIENT_SECRET = 'zdz75pa9SUAHQJcH4iAcc9OS'
REFRESH_TOKEN = '1/z_iA0r3m5bvcU9n0q6zxUmGZUxZ43pN1fkY_qWlggko'

# AdWords API information.
DEVELOPER_TOKEN = '9_rUnKuMInGNUiwv6C4icg'
USER_AGENT = 'test_python_ads'
CLIENT_CUSTOMER_ID = '566-531-9705'


if __name__ == '__main__':
  # Initialize client object.
  # oauth2_client = oauth2.GoogleRefreshTokenClient(
  #     CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)
  #
  # adwords_client = adwords.AdWordsClient(
  #     DEVELOPER_TOKEN, oauth2_client, USER_AGENT,
  #     client_customer_id=CLIENT_CUSTOMER_ID)

  main(Client().ins)
