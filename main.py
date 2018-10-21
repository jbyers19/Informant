"""Script to monitor web services and detect outages"""

import json
from core.handler import Informant


# Start the script
def main():
    with open('./core/endpoints.json') as f:
        config = json.load(f)
        for endpoint in config:
            informant = Informant(endpoint, config[endpoint]['url'])
            informant.call()
    f.close()


if __name__ == '__main__':
    main()
