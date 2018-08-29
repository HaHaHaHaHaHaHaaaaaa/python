

from googleads import adwords

from googleads import oauth2
import _locale
_locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf-8'])

CLIENT_ID = '413010591024-jboften13risuj2fk23cv7pmio2qc33m.apps.googleusercontent.com'
CLIENT_SECRET = 'zdz75pa9SUAHQJcH4iAcc9OS'
REFRESH_TOKEN = '1/z_iA0r3m5bvcU9n0q6zxUmGZUxZ43pN1fkY_qWlggko'

# AdWords API information.
DEVELOPER_TOKEN = '9_rUnKuMInGNUiwv6C4icg'
USER_AGENT = 'test_python_ads'
CLIENT_CUSTOMER_ID ='739-323-1792'
    #'566-531-9705'

class Client:

    def __init__(self):
        # Initialize client object.
        oauth2_client = oauth2.GoogleRefreshTokenClient(
            CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)
        adwords_client = adwords.AdWordsClient(
            DEVELOPER_TOKEN, oauth2_client, USER_AGENT,
            client_customer_id=CLIENT_CUSTOMER_ID)
        self.ins=adwords_client
        print("Client got")
if __name__ == '__main__':
    Client()

