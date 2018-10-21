import requests
import core.util as util
import core.status as status

# Colors to make console output easier to read (if supported)
GREEN = '\33[32m'
RED = '\33[31m'
END = '\33[0m'


# Class for each endpoint
class Informant:

    def __init__(self, endpoint, url):
        self.endpoint = endpoint
        self.url = url

    """Make request to endpoint

       Currently only supports URL's without any params,
       headers, etc. but could be updated to take all of
       those as well as other calls besides GET. Could
       also add a new method to handle authentication.
    """
    def call(self):

        # Track time it took to get response
        start = util.get_time()
        call = requests.get(self.url)
        end = util.get_time()

        # When endpoint responds successfully...
        if call.status_code == requests.codes.ok:
            print(GREEN + 'GET {0}: {1} {2}'.format(self.endpoint,
                                                    call.status_code,
                                                    call.reason)
                  + END)

            # TODO add logging integration here

            # Get status from statuses.json and notify if there is a change
            if status.get_status(self.endpoint) == 'down':
                status.set_status(self.endpoint, 'up')

                # TODO add Slack notification integration here

        # When endpoint responds with a failure...
        else:
            print(RED + 'GET {0}: {1} {2}'.format(self.endpoint, call.status_code, call.reason) + END)

            # TODO add logging integration here

            # Get status from statuses.json and notify if there is a change
            if status.get_status(self.endpoint) == 'up':
                status.set_status(self.endpoint, 'down')

                # TODO add Slack notification integration here

        print('Call to {0} took {1}ms\n'.format(self.endpoint, end - start))

