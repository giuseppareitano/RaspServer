"""
This is the Rasp module and supports all the ReST actions
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
temperatura = 50


def read_temperature():
    """
    This function responds to a get request for /api/temperatura
    with the value of temperature
    :return:        json string with value of temperature
    """
    # Create the list of people from our data
    TEMPERATURE = {'temperatura':temperatura}
    return TEMPERATURE


 # def read_one(lname):
 #    """
 #    This function responds to a request for /api/people/{lname}
 #    with one matching person from people
 #    :param lname:   last name of person to find
 #    :return:        person matching last name
 #    """
 #    # Does the person exist in people?
 #    if lname in PEOPLE:
 #        person = PEOPLE.get(lname)
 #
 #    # otherwise, nope, not found
 #    else:
 #        abort(
 #            404, "Person with last name {lname} not found".format(lname=lname)
 #        )
 #
 #    return person


# def create(person):
#     """
#     This function creates a new person in the people structure
#     based on the passed in person data
#     :param person:  person to create in people structure
#     :return:        201 on success, 406 on person exists
#     """
#     lname = person.get("lname", None)
#     fname = person.get("fname", None)
#
#     # Does the person exist already?
#     if lname not in PEOPLE and lname is not None:
#         PEOPLE[lname] = {
#             "lname": lname,
#             "fname": fname,
#             "timestamp": get_timestamp(),
#         }
#         return make_response(
#             "{lname} successfully created".format(lname=lname), 201
#         )
#
#     # Otherwise, they exist, that's an error
#     else:
#         abort(
#             406,
#             "Peron with last name {lname} already exists".format(lname=lname),
#         )


def update(newTemperature):
    """
    This function updates the temperature value
    :param newTemperature:   new value for temperature
    :return:        nulla
    """
    global temperatura
    temperatura = newTemperature
    return make_response("Temperature successfully updated",200)


# def delete(lname):
#     """
#     This function deletes a person from the people structure
#     :param lname:   last name of person to delete
#     :return:        200 on successful delete, 404 if not found
#     """
#     # Does the person to delete exist?
#     if lname in PEOPLE:
#         del PEOPLE[lname]
#         return make_response(
#             "{lname} successfully deleted".format(lname=lname), 200
#         )
#
#     # Otherwise, nope, person to delete not found
#     else:
#         abort(
#             404, "Person with last name {lname} not found".format(lname=lname)
#         )