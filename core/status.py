import json

# Current status of the endpoints
statuses = None


# Returns the last status of an endpoint
def get_status(endpoint):
    global statuses
    with open('./core/statuses.json', 'r') as f:
        statuses = json.load(f)
        f.close()
    print('Current status: {0}'.format(statuses[endpoint]))
    return statuses[endpoint]


# Set current status of an endpoint
def set_status(endpoint, status):
    global statuses
    statuses[endpoint] = status
    with open('./core/statuses.json', 'w') as f:
        f.write(json.dumps(statuses))
        f.close()
    print('Setting status to: {0}'.format(status))
