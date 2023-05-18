from .csvingestor import CSVIngestor
from .docxingestor import DocxIngestor
from .textingestor import TextIngestor
from .pdfingestor import PDFIngestor

class Ingestor:
    """Determine file type (csv, docx, pdf, or text) and process the file 
        accordingly to generate a list of quotes.

        params
        ------
        lstFilenames: a list of filename with different file extensions
    """
    def __init__(self, lstFilenames):
        """Determine file type from the filename and 
            process accordingly.
        """
        self.lstFilenames=lstFilenames
        self.lstQuotes=[]

        for filename in lstFilenames:
            
            if filename.endswith(".csv"):

                try:
                    read_quotes=CSVIngestor(filename)
                except:
                    raise Exception("Error reading .csv file. Please check.")

            elif filename.endswith(".txt"):
                try:
                    read_quotes=TextIngestor(filename)
                except:
                    raise Exception("Error reading .txt file. Please check.")    

            elif filename.endswith(".docx"):
                try:
                    read_quotes=DocxIngestor(filename)
                except:
                    raise Exception("Error reading .docx file. Please check.")

            elif filename.endswith(".pdf"):
                try:
                    read_quotes=PDFIngestor(filename)
                except:
                    raise Exception("Error reading .pdf file. Please check.")

            else:
                #inform user if a file type is invalid
                print("File has been skipped because the file extension '%s' is not recognized." %(filename.split(".")[-1]))
            
            #generate a list of quotes and append data to existing quotes
            self.lstQuotes+=read_quotes.parse
            
            

