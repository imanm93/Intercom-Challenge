from src.parse import parse
from src.invite import invite
from src.output import output
from src.constants import FILE_NAME

def main():
    """Creates output.txt of invitees

    This function outputs a text file containing all customers within a 100km of the Dublin office
    """

    # 1. Get customers from text file
    customers = parse(FILE_NAME)

    # 2. Get invite list
    invitees = invite(customers)

    # 3. Sort invitee list by user id
    invitees = sorted(invitees, key=lambda invitee : invitee['user_id'])

    # 4. Output invite list to file (output.txt)
    output(invitees)

if __name__ == '__main__':
    main()
