
def output(invitees):
    """
    This function writes information regarding the invitees to an output file
    """

    f = open('output.txt', 'w+') # Create output file

    f.write("The following customers are invited to the Dublin office.\n\n")
    f.write("Id\t\tName\n")
    f.write("-----------------------\n")
    for invitee in invitees: # For each invitee write information to file
        user_id = str(invitee['user_id'])
        if invitee['user_id'] < 10: # For better formatting of output file
            user_id = "0" + str(invitee['user_id'])
        f.write(user_id + "\t\t" + invitee['name'] + "\n")

    f.close()
