from abc import ABC, abstractmethod

class IngestorInterface(ABC):
    """Create a class that possess a common convert-to-text property
         which returns a list.
    """

    def __init__(self):
        pass

    @property
    @abstractmethod
    def parse(self)->list:
        """Generate a list of quotes from the specified file.
        """
        pass
    
    @classmethod
    def can_ingest(cls, path)->bool:
        """Check if the file can be ingested.
        """
        pass