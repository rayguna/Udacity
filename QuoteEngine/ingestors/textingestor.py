from .ingestorinterface import IngestorInterface
from distutils import text_file

class TextIngestor(IngestorInterface):
    """Instantiate a textfile name object from a text file

    params
    -------
    txtfile: a text file with lines of quotes 
    """
    def __init__(self, txtfile):
        self.txtfile=txtfile
        
    @property
    def parse(self)->list:
        """Get a list of quotes from the textfile

        params
        ------ 
        self.txtfile: textfile object

        return an array of quotes extracted from the text file

        #note: set encoding='utf-8-sig' to remove the extra characters (ï»¿)
        """
        with open(self.txtfile, encoding='utf-8-sig') as f:
            lines = f.readlines() 
        return lines

    @classmethod
    def can_ingest(cls, path)->bool:
        """Check if the file can be ingested.
        """
        if TextIngestor.csv.endswith('txt'):
            return True