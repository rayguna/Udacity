import argparse
from importlib.resources import path
import QuoteEngine
import glob
import random

from urllib import request


def main():
    """
    Uses the ImageCaptioner class that inherits from the
    Ingstor class, which, in turns, uses the DocxIngestor, PDFIngestor, 
    and CSVIngestor classes to read quotation from different text formats.
    The ImageCaptioner class also uses MemeEngine to make meme.

    The program is executable from the command line.
    It takes three OPTIONAL arguments and uses ArgumentParser to parse the 
    following CLI arguments:

      • path - path to an image file
      • body - quote body to add to the image
      • author - quote author to add to the image

    Return a path to a generated image.
    If any argument is not defined, a random selection is used.

    Note: User input arguments must be enclosed in quotations.
    """
    parser = argparse.ArgumentParser(description="Generate a random/specific captioned image.")

    parser.add_argument('--path', type=str, 
                        default="",\
                            help="Provide an image url.") #optional input with a default

    parser.add_argument('--body', type=str, 
                        default="",\
                            help="Provide the quote.") #optional input with a default
    parser.add_argument('--author', type=str, 
                        default="",\
                            help="Provide the author.") #optional input with a default

    args = parser.parse_args()

    quote = args.body
    author = args.author
    image_path = args.path

    #get a list of quotes 
    quote_files=[file for file in glob.glob("./static/DogQuotes/*.*")]
    make_im_captioner=QuoteEngine.ImageCaptioner(quote_files)

    #get a list of img paths
    lstImgFiles=[file for file in glob.glob("./static/photos/dog/*.*")]

    full_quote="" #initialize full_quote
    
    #if any of the inputs are not provided, generate a random answer
    if quote=="" or author=="" or image_path=="":
        #Generate a random image like pressing the random button
        print("No inputs are provided. A random captioned image will be generated.")  

        #make a random quote from stored files
        lstQuotes=make_im_captioner.lstQuotes
        full_quote=QuoteEngine.QuoteModel(random.choice(lstQuotes))

        #make a random image from stored files
        image_path=random.choice(lstImgFiles)

    #if information is provided...
    elif quote!="" and author!="" and image_path!="": 
        #make_meme
        full_quote=QuoteEngine.QuoteModel('"%s" - %s' %(quote, author))
        
        #check if image path is a url
        if "http" in image_path:
            #Download image from url and save it locally
            path="static/photos/dog/"
            full_img_path="%s%s" %(path, image_path.split("/")[-1])

            with open(full_img_path, 'wb') as f:
                f.write(request.urlopen(image_path).read())
            
            #overwrite image_path with full_image_path 
            image_path=full_img_path

    #check image file type
    if image_path.endswith(".jpg"):
        #convert quote into the standard format
        message=full_quote.getQuote_and_Author

        #generate a meme
        out_path=make_im_captioner.generate_captioned_image(message=message, image_path=image_path)

        print("You have provided the following info.:") 
        print("    • Image url: %s" %(image_path))
        print('    • Quote: %s' %(str(message).strip("\n"))) #remove line breaks
        print("")
        print("Meme generation successful. It can be found here: %s" %out_path)

    else:
        raise Exception("This program currently only supports .jpg format.")

if __name__ == "__main__":
    main()