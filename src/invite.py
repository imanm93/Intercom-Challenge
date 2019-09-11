from src.point import Point
from src.distance import distance
from src.constants import DUBLIN_OFFICE_LOCATION

def invite(customers):
    """Return an array

    This function filters out customers that are farther than 100 km from the Dublin office
    """

    # Init variable to store invites
    invitees = []

    for customer in customers: # For each customer
        customer_location = Point(float(customer['latitude']), float(customer['longitude']))
        customer_distance_to_office = distance(customer_location, DUBLIN_OFFICE_LOCATION) # Calc distance to Dublin office
        if customer_distance_to_office <= 100.0: # If within 100 km invite customer to Dublin office
            invitees.append(customer)

    return invitees
