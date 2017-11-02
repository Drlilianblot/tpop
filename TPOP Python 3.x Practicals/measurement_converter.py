'''
Created on 4 Nov 2016

@author: Lilian
'''

# Constants
METER_PER_INCH = 0.0254
INCHES_PER_FEET = 12

def feet_to_meters(feet, inches):
    """

    feet_to_meters(feet, inches) --> float

    return the measurement in meter when given the measurement in feet and
    inches.
    Raise a TypeError if the parameters are not int.

    """
    if isinstance(feet, int) and isinstance(inches, int):
        number_meters = (feet * INCHES_PER_FEET + inches) * METER_PER_INCH
        return number_meters
    else:
        raise TypeError("Feet and inches must be int!")


print("5 feet 10 inches is equivalent to", feet_to_meters(5, 10),"meters")