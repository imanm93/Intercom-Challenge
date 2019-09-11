import json

def parse(file):
    """Return an array

    This function parses a text file line by line and converts strings to json
    """

    # Init varaible to store parsed customer information
    customers = []

    try:
        f = open(file)
    except IOError:
        raise Exception("File cannot be found or read.")

    for line in f: # Read file line by line
        try:
            customer = json.loads(line) # Convert text to json

            key_error = ''
            if 'user_id' not in customer:
                key_error = 'user_id'
            if 'name' not in customer:
                key_error = 'name'
            if 'longitude' not in customer:
                key_error = 'longitude'
            if 'latitude' not in customer:
                key_error = 'latitude'

            if key_error == '':
                customers.append(customer)
            else:
                raise KeyError("Mandatory key: " + key_error + " missing from customer object in line -" + line)
        except json.decoder.JSONDecodeError:
            raise Exception("Line is not JSON formatted")

    f.close()

    return customers
