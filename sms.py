import os

from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

from numbers import numbers


username = os.environ.get('USERNAME')
apikey = os.environ.get('API_KEY')

to = numbers

message = "Hello Swahilipotter, \nVote for Mahmood Noor (Swahilipot Hub patron) for Outstanding Person in the Community. Click this link to vote https://goo.gl/qHuyiJ"

gateway = AfricasTalkingGateway(username, apikey)


def send_sms():
    # Any gateway errors will be captured by our custom Exception class below,
    # so wrap the call in a try-catch block
    try:
        # Thats it, hit send and we'll take care of the rest.

        results = gateway.sendMessage(to, message)

        for recipient in results:
            # status is either "Success" or "error message"
            print 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'], recipient['status'],
                                                                recipient['messageId'], recipient['cost'])
    except AfricasTalkingGatewayException, e:
        print 'Encountered an error while sending: %s' % str(e)
