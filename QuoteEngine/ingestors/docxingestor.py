from .ingestorinterface import IngestorInterface
import docx

class DocxIngestor(IngestorInterface):
    """Instantiate a docxfile name object from a docx file

    params
    -------
    docxfile: a text file with lines of quotes 
    """
    def __init__(self, docxfile):
        self.docxfile=docxfile

    @property
    def parse(self)->list:
        """Get a list of quotes from the docxfile

        params
        ------ 
        self.docxfile: docx filename object

        return an array of quotes extracted from the docx file
        """
        doc = docx.Document(self.docxfile)
        
        lstDocx=[]
        for line in doc.paragraphs:
            lstDocx.append(line.text)
        
        #remove empty elements
        lstDocx=list(filter(None, lstDocx))

        return lstDocx

    @classmethod
    def can_ingest(cls, path)->bool:
        """Check if the file can be ingested.
        """
        if DocxIngestor.docxfile.endswith('docx'):
            return True