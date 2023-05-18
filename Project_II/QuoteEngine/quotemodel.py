class QuoteModel:
    """An object that separately generates a quote, an author,
        and both a quote and an author formatted accordingly.

        params
        quote_author: a string containing a quote and an author
    """
    def __init__(self, quote_author):
        self.quote_author=quote_author
        #split quote from author
        self.lstQuote_Author=self.quote_author.split(" - ")

    @property
    def getQuote(self):
        #remove quotations
        quote=self.lstQuote_Author[0].strip('"').strip("'")
        return '"%s"' %quote

    @property
    def getAuthor(self):
        author=self.lstQuote_Author[1]
        return author

    @property
    def getQuote_and_Author(self):
        #remove quotations
        quote_and_author='"%s" - %s' %(self.lstQuote_Author[0].strip('"').strip("'"),\
             self.lstQuote_Author[1])
        return quote_and_author