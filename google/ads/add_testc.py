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
import datetime
import uuid
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
    campaign_service = adwords_client.GetService('CampaignService', version='v201806')
    budget_service = adwords_client.GetService('BudgetService', version='v201806')

    # Create a budget, which can be shared by multiple campaigns.
    budget = {
        'name': 'Interplanetary budget #%s' % uuid.uuid4(),
        'amount': {
            'microAmount': '50000000'
        },
        'deliveryMethod': 'STANDARD'
    }

    budget_operations = [{
        'operator': 'ADD',
        'operand': budget
    }]

    # Add the budget.
    budget_id = budget_service.mutate(budget_operations)['value'][0][
        'budgetId']

    # Construct operations and add campaigns.
    operations = [{
        'operator': 'ADD',
        'operand': {
            'name': 'Interplanetary Cruise #%s' % uuid.uuid4(),
            # Recommendation: Set the campaign to PAUSED when creating it to
            # stop the ads from immediately serving. Set to ENABLED once you've
            # added targeting and the ads are ready to serve.
            'status': 'PAUSED',
            'advertisingChannelType': 'SEARCH',
            'biddingStrategyConfiguration': {
                'biddingStrategyType': 'MANUAL_CPC',
            },
            'endDate': (datetime.datetime.now() +
                        datetime.timedelta(365)).strftime('%Y%m%d'),
            # Note that only the budgetId is required
            'budget': {
                'budgetId': budget_id
            },
            'networkSetting': {
                'targetGoogleSearch': 'true',
                'targetSearchNetwork': 'true',
                'targetContentNetwork': 'false',
                'targetPartnerSearchNetwork': 'false'
            },
            # Optional fields
            'startDate': (datetime.datetime.now() +
                          datetime.timedelta(1)).strftime('%Y%m%d'),
            'frequencyCap': {
                'impressions': '5',
                'timeUnit': 'DAY',
                'level': 'ADGROUP'
            },
            'settings': [
                {
                    'xsi_type': 'GeoTargetTypeSetting',
                    'positiveGeoTargetType': 'DONT_CARE',
                    'negativeGeoTargetType': 'DONT_CARE'
                }
            ]
        }
    }, {
        'operator': 'ADD',
        'operand': {
            'name': 'Interplanetary Cruise banner #%s' % uuid.uuid4(),
            'status': 'PAUSED',
            'biddingStrategyConfiguration': {
                'biddingStrategyType': 'MANUAL_CPC'
            },
            'endDate': (datetime.datetime.now() +
                        datetime.timedelta(365)).strftime('%Y%m%d'),
            # Note that only the budgetId is required
            'budget': {
                'budgetId': '1570302429'
            },
            'advertisingChannelType': 'DISPLAY'
        }
    }]
    campaigns = campaign_service.mutate(operations)

    # Display results.
    for campaign in campaigns['value']:
        print('Campaign with name "%s" and id "%s" was added.'
              % (campaign['name'], campaign['id']))


if __name__ == '__main__':
  # main(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN, DEVELOPER_TOKEN, USER_AGENT,
  #      CLIENT_CUSTOMER_ID)
  main(Client().ins)

