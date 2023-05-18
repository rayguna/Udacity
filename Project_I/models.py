"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""

from helpers import cd_to_datetime, datetime_to_str
from database import NEODatabase

class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    
    def __init__(self, designation, name, diameter,hazardous):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """

        self.designation = str(designation)

        #name must be string and cannot be None
        if name=='':
            self.name=None
        else:
            self.name=str(name)

        #check diameter
        try:
            self.diameter=float(diameter)
        except:
            self.diameter=float('nan')

        #check hazardous
        if type(hazardous)==bool:
            self.hazardous=hazardous
        elif hazardous=='Y':
            self.hazardous=True
        elif hazardous=='N':
            self.hazardous=False
        else:
            self.hazardous=False
        
        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""

        return ''
        
    def __str__(self):
        """Return `str(self)`."""

        return f"{self.name} has a diameter of {self.diameter:.3f} km and %s potentially hazardous." %("is" if self.hazardous==True else "is not")

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"

    def serialize(self):
        """
        print(neo.serialize())
        {'designation': '433', 'name': 'Eros', 'diameter_km': 16.84, 'potentially_hazardous': False}
        """

        serial={}
        serial['designation']=self.designation
        serial['name']=self.name
        serial['diameter_km']=self.diameter
        serial['potentially_hazardous']=self.hazardous

        return serial


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, time, distance, velocity):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """

        self._designation = ''
        self.time = cd_to_datetime(time)  
        self.distance = float(distance)
        self.velocity = float(velocity)

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """

        return self.time

    def __str__(self):
        """Return `str(self)`."""
        
        return f"A CloseApproach ..."
        f"At {datetime_to_str(self.time)}, '{self.neo.name}' approaches Earth at a distance of {self.neo.distance:.2f} au and a velocity of {velocity:.2f} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        
        return f"CloseApproach(time={datetime_to_str(self.time)}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"

    def serialize(self):
        """ Convert result list of objects into a string

        print(approach.serialize())
        {'datetime_utc': '2025-11-30 02:18', 'distance_au': 0.397647483265833, 'velocity_km_s': 3.72885069167641}
        """
        
        serialize={}

        # format time to string to make it json serializable
        serialize['datetime_utc']=self.time.strftime("%Y-%m-%d %H:%M") 
        serialize['distance_au']=self.distance
        serialize['velocity_km_s']=self.velocity
        
        return serialize
