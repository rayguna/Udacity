from PIL import Image, ImageDraw, ImageFont
import os
import random

class MemeEngine:
    """Instantiates an image object onto which the user can generate quotes 

    Arguments
        in_path {str}: the file location for the input image.
        message {str} -- a string of text to print onto the image. 

    Usage example:
        print(generate_postcard('./imgs/img.jpg', 
                                './imgs/out.jpg',
                                'woof!',
                                (450, 900, 900, 1300),
                                200))
    """
    def __init__(self, in_path, message=None):
        #get current directory
        #print("CHECK CURRENT PATH")
        #print(os.path.abspath(os.getcwd()))
        #need to go up one directory to get to the static folder
        self.in_path=in_path 
        self.message=message

        #generate an image
        self.img = Image.open(self.in_path)
        
    def make_meme(self, out_path, crop=None, width=None)->str:
        """Create a Postcard With a Text Greeting

        Arguments:
            out_path {str} -- the desired location for the output image.
            crop {tuple} -- The crop rectangle, as a (left, upper, right, lower)-tuple. Default=None.
            width {int} -- The pixel width value. Default=None.
        Returns:
            str -- the file path to the generated output image.
        """
        if crop is not None:
            """Crop image
            """
            self.img = self.img.crop(crop)

        if width is not None:
            """Resize image according to the specified width,
                while maintaining the aspect ratio
            """
            ratio = width/float(self.img.size[0])
            height = int(ratio*float(self.img.size[1]))
            self.img = self.img.resize((width, height), Image.NEAREST)

        if self.message is not None:
            """Draw a message on the image
            """
            draw = ImageDraw.Draw(self.img)
            font = ImageFont.truetype("QuoteEngine/Roboto-Regular.ttf", 30) #ImageFont.truetype("arial.ttf", 30)
            
            #place quote in a random position on the picture
            #set the y value to be between 10 and y-40
            y=random.randint(10,self.img.size[1]-60)
            draw.text((10, y), self.message, font=font, fill='white')

        self.img.save(out_path)
        return out_path

