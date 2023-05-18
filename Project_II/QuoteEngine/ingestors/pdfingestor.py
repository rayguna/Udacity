from .ingestorinterface import IngestorInterface
import subprocess
import sys
import re

import PyPDF2


class PDFIngestor(IngestorInterface):
    """Instantiate a pdffile name object from a pdf file

    params
    -------
    pdf_path: a pdf file with lines of quotes 
    """
    def __init__(self, pdf_path):
        self.pdf_path=pdf_path
    
    @property
    def parse(self)->list:
        """Get a list of quotes from the pdf file

        params
        ------ 
        self.pdf_path: pdf filename object

        return an array of quotes extracted from the pdf file
        """
        try:
            result=subprocess.run(["pdftotext.exe", self.pdf_path, "-"], capture_output=True, text=True)
    
            s=result.stdout
            
        except:
            #if subprocess doesn't work, try another pdf reader
            print("Failed to read pdf files via subprocess via pdftotext.exe. Using PyPDF2 instead.")

            pdfFile = open(self.pdf_path, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)

            strQuotes=""
            for pg in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pg)
                strQuotes += pageObj.extractText() 
            
            s=strQuotes

        #"(.+?)": extract quoted string
        #([A-Z]{1}[a-z]+( [A-Z]{1}[a-z]+)*): extract words separated by a space     
        tupleQuotes=re.findall(r'"(.+?)" - ([A-Z]{1}[a-z]+( [A-Z]{1}[a-z]+)*)', s)

        lstQuotes=[]
        for tupleQuote in tupleQuotes:
            lstQuotes.append("%s - %s" %(tupleQuote[0],tupleQuote[1]))

        return lstQuotes
            
    @classmethod
    def can_ingest(cls, path)->bool:
        """Check if the file can be ingested.
        """
        if PDFIngestor.pdf_path.endswith('pdf'):
            return True