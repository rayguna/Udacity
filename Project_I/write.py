"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""

import csv
import json


def format(results, type):
    """Convert result list of objects into a string according to the desired format types:

    :param results: a colllection of approach objects. each object contains a collection of neo objects. 
    :param type: convert results into a collection of strings either in a csv or a dictionary format. 

    E.g., 
        csv:
            ['datetime_utc', 'distance_au', 'velocity_km_s', 'designation',\
                'name', 'diameter_km', 'potentially_hazardous']
        json:
            [
            {...},
            {
                "datetime_utc": "2025-11-30 02:18",
                "distance_au": 0.397647483265833,
                "velocity_km_s": 3.72885069167641,
                "neo": {
                "designation": "433",
                "name": "Eros",
                "diameter_km": 16.84,
                "potentially_hazardous": false
                }
            },
            ...
            ]
    """

    results_format=[]

    for row in results:
        if type=='csv':
            results_format.append(list(results[0].serialize().values())+list(results[0].neo.serialize().values()))
        
        elif type=='json':
            dictResult=results[0].serialize()
            dictResult["neo"]=results[0].neo.serialize()
            results_format.append(dictResult)

    return results_format

def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """

    fieldnames = ['datetime_utc', 'distance_au', 'velocity_km_s', 'designation',\
         'name', 'diameter_km', 'potentially_hazardous']
    
    with open(filename, 'w') as outfile:
        writer = csv.writer(outfile)
        
        #add fieldnames first
        writer.writerow(fieldnames)
        
        for row in format(results, 'csv'):
            writer.writerow(row)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.
    
    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    
    with open(filename, 'w') as outfile:
        json.dump(format(results, 'json'), outfile)