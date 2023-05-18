from .ingestorinterface import IngestorInterface
import pandas as pd

class CSVIngestor(IngestorInterface):
    """Instantiate a csv file name object from a csv file

    params
    -------
    csv_name: a csv file with two columns, body and author 
    """
    
    def __init__(self, csv):
        self.csv=csv
        
    @property
    def parse(self)->list:
        """convert the csv file into an array of quotes

        params
        ------ 
        self.csv: a csv file name

        return an array of quotes extracted from the csv file
        """
        df_csv=pd.read_csv(self.csv)
        lstQuotes=[]
        for row in df_csv.iterrows():
            myStr="%s - %s" %(row[1][0], row[1][1])
            lstQuotes.append(myStr)
        return lstQuotes

    @classmethod
    def can_ingest(cls, path)->bool:
        """Check if the file can be ingested.
        """
        if CSVIngestor.csv.endswith('csv'):
            return True