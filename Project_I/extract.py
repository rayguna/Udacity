"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.
"""

import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """

    neos=[]
    with open(neo_csv_path, 'r') as file:
        csv_reader=csv.DictReader(file)
        for row in csv_reader:
        #   print(', '.join(row))
            #designation, name, diameter, hazardous
            neos.append(NearEarthObject(row['pdes'], row['name'], row['diameter'], row['pha']))
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """

    cad=[]

    with open(cad_json_path, 'r') as file:
        data=json.load(file)

    for each in data['data']:
        #time, distance, velocity
        closeapproach=CloseApproach(each[3], each[4], each[7])
        closeapproach._designation=each[0] #set designation property
        cad.append(closeapproach)
        
    return cad
