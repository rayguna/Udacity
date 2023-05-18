#inherit from Ingestor class to adhere to the DRY principle
from logging import raiseExceptions
from .ingestors.ingestor import Ingestor
from QuoteEngine.memeengine import MemeEngine

import glob

class ImageCaptioner(Ingestor):
    """Draw a quotation on an image based on user inputs.
       If information is not provided, a random selection is used. 

       return: a path to the generated image.
    """

    def generate_captioned_image(self, message, image_path):
        """Generate captioned image if appropriate inputs are provided
        """
        meme=MemeEngine(image_path, message)

        try: 
            print(image_path.split("."))
            #check path
            path=image_path.split(".")
            get_path=''.join(image_path.split(".")[:-1])
            
            if len(path)>2:
                get_path = "." + get_path

            out_path=meme.make_meme("%s_meme.jpg" %(get_path), width=500)
            return out_path

        except:
            raise Exception("Please enter valid information!")


