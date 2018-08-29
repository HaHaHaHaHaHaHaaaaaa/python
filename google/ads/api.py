from googleads.oauth2 import GoogleRefreshTokenClient
from googleads.adwords import AdWordsClient
from googleads.common import ZeepServiceProxy
from googleads.errors import GoogleAdsError
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    # def __init__(self, client_id, client_secret, refresh_token,
    #              manager_account_id, dev_token):
    #     """Initializes an APIHandler.
    #
    #     Args:
    #       client_id:  '413010591024-jboften13risuj2fk23cv7pmio2qc33m.apps.googleusercontent.com' The client customer id retrieved from the Developers Console.
    #       client_secret:'zdz75pa9SUAHQJcH4iAcc9OS' The client secret retrieved from the Developers Console.
    #       refresh_token: The refresh token retrieved with generate_refresh_token.py.
    #       manager_account_id: '566-531-9705' The AdWords manager account Id.
    #       dev_token:'9_rUnKuMInGNUiwv6C4icg' The AdWords Developer Token.
    #
    #     """
    #     credentials = GoogleRefreshTokenClient(client_id, client_secret,
    #                                            refresh_token)
    #     self.client = AdWordsClient(dev_token, credentials, self._USER_AGENT,
    #                                 client_customer_id=manager_account_id,
    #                                 cache=ZeepServiceProxy.NO_CACHE)

    def get(self):
        self.write("Hellow,world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler()),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()




