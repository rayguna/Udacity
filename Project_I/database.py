"""A database encapsulating collections of near-Earth objects and their close approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.
"""

from xml.etree.ElementPath import prepare_descendant

class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """

    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        As a precondition, this constructor assumes that the collections of NEOs
        and close approaches haven't yet been linked - that is, the
        `.approaches` attribute of each `NearEarthObject` resolves to an empty
        collection, and the `.neo` attribute of each `CloseApproach` is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO. This
        constructor modifies the supplied NEOs and close approaches to link them
        together - after it's done, the `.approaches` attribute of each NEO has
        a collection of that NEO's close approaches, and the `.neo` attribute of
        each close approach references the appropriate NEO.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """

        self._neos = neos
        self._approaches = approaches
        
        #make cad data a dictionary
        dictCAD={}
        
        for i, approach in enumerate(self._approaches):
            #assign neo to each approach attribute with the same designation 
            self._approaches[i].neo=self.get_neo_by_designation(approach._designation)

            #create a dictionary of approaches by approach designation as the key
            if approach._designation not in dictCAD.keys():
                #initialize dictionary and add
                dictCAD[approach._designation]=[]
                dictCAD[approach._designation].append(approach)
            else:
                dictCAD[approach._designation].append(approach)

        for i, neo in enumerate(self._neos):
            #get a list of approaches object by neo designation
            if neo.designation in dictCAD.keys():
                self._neos[i].approaches=dictCAD[neo.designation]


    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation, or `None`.
        """

        for neo in self._neos:
            #change name to lowercase
            if neo.designation==designation:
                #return a neo object when called by its designation
                return neo

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """

        for neo in self._neos:
            if str(neo.name).lower()==str(name).lower():
                #return neo object when its name is called
                return neo

    def query(self, filters={}):
        """Query close approaches to generate those that match a collection of filters.

        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.

        If no arguments are provided, generate all known close approaches.

        The `CloseApproach` objects are generated in internal order, which isn't
        guaranteed to be sorted meaningfully, although is often sorted by time.

        :param filters: A collection of filters capturing user-specified criteria.
        :return: A stream of matching `CloseApproach` objects.
        """

         #> if no filter is specified
        if filters=={'date': None, 'start_date': None, 'end_date': None, 'distance_min': None, 
        'distance_max': None, 'velocity_min': None, 'velocity_max': None, 'diameter_min': None, 
        'diameter_max': None, 'hazardous': None} or filters=={}:
            return self._approaches
            
        #> if some of the parameters are not None
        else:
            expected=[]
            #using a 2d array to store data
            #if the value is none, the set remains empty
            for i in range(10):
                expected.append([])
            
            #> if on a specific date
            for approach in self._approaches:
                if filters['date'] != None and approach.time.date() == filters['date']:
                    expected[0].append(approach)
            
                #> if given a start_date 
                if filters['start_date'] != None and (filters['start_date'] <= approach.time.date()):
                    expected[1].append(approach)
                
                #> if only given an end date
                if filters['end_date'] != None and (approach.time.date() <= filters['end_date']):
                    expected[2].append(approach)
            
                #> if only given a distance_min
                if filters['distance_min'] != None and (approach.distance >= filters['distance_min']):
                    expected[3].append(approach)

                #> if only given a distance_max
                if filters['distance_max'] != None and (approach.distance <= filters['distance_max']):
                    expected[4].append(approach)

                #> if only given a velocity_min
                if filters['velocity_min'] != None and (approach.velocity >= filters['velocity_min']):
                    expected[5].append(approach)

                #> if only given a velocity_max
                if filters['velocity_max'] != None and (approach.velocity <= filters['velocity_max']):
                    expected[6].append(approach)

                #> if only given diameter_min
                if filters['diameter_min'] != None and (approach.neo.diameter>=filters['diameter_min']):
                    expected[7].append(approach)

                #> if only given diameter_max
                if filters['diameter_max'] != None and (approach.neo.diameter<=filters['diameter_max']):
                    expected[8].append(approach)

                #> if only given hazardous
                if filters['hazardous'] != None and filters['hazardous']==approach.neo.hazardous: 
                    expected[9].append(approach) 
            
            #collect all data into a dictionary
            dictTotal={}

            #> dates
            dictTotal['date']=set(expected[0]) #a single date

            if filters['start_date']!=None and filters['end_date']!=None:
                expected1and2=set(expected[1]).intersection(expected[2]) 
                if filters['date']==None:
                    dictTotal['date']=expected1and2
                elif filters['date']!=None:#ignore the start and end date if filters['date']!=None, weird, but just following the unit-test
                    dictTotal['date']=set(expected[0])

            #if either of start_date or end_date is empty
            elif filters['start_date']!=None and filters['end_date']==None:
                dictTotal['date']=dictTotal['date'].union(expected[1])
            elif filters['start_date']==None and filters['end_date']!=None:
                dictTotal['date']=dictTotal['date'].union(expected[2])
 
            #> distance
            dictTotal['distance']=set()

            if filters['distance_min']!=None and filters['distance_max']!=None:
                expected3and4=set(expected[3]).intersection(expected[4]) 
                dictTotal['distance']=dictTotal['distance'].union(expected3and4)
            elif filters['distance_min']!=None and filters['distance_max']==None:
                dictTotal['distance']=dictTotal['distance'].union(expected[3])
            elif filters['distance_min']==None and filters['distance_max']!=None:
                dictTotal['distance']=dictTotal['distance'].union(expected[4])

            #> velocity
            dictTotal['velocity']=set()

            if filters['velocity_min']!=None and filters['velocity_max']!=None:
                expected5and6=set(expected[5]).intersection(expected[6]) 
                dictTotal['velocity']=dictTotal['velocity'].union(expected5and6)
            elif filters['velocity_min']!=None and filters['velocity_max']==None:
                dictTotal['velocity']=dictTotal['velocity'].union(expected[5])
            elif filters['velocity_min']==None and filters['velocity_max']!=None:
                dictTotal['velocity']=dictTotal['velocity'].union(expected[6])

            #> diameter
            dictTotal['diameter']=set()

            if filters['diameter_min']!=None and filters['diameter_max']!=None:
                expected7and8=set(expected[7]).intersection(expected[8]) 
                dictTotal['diameter']=dictTotal['diameter'].union(expected7and8)
            elif filters['diameter_min']!=None and filters['diameter_max']==None:
                dictTotal['diameter']=dictTotal['diameter'].union(expected[7])
            elif filters['diameter_min']==None and filters['diameter_max']!=None:
                dictTotal['diameter']=dictTotal['diameter'].union(expected[8])

            #> hazardous
            dictTotal['hazardous']=set()

            if filters['hazardous']!=None:
                dictTotal['hazardous']=dictTotal['hazardous'].union(expected[9])
            
            
            #> Combine all information 
            total=set()
            for k,v in dictTotal.items():
                if v!=set():
                    #First, initialize total because you get set() if the initial value is set()
                    if total==set():
                        total=dictTotal[k]
                    else:
                        total=total.intersection(dictTotal[k])

            return total