from distutils.text_file import TextFile
import random
import os
import requests
from flask import Flask, render_template, abort, request, redirect, url_for, session

import random
#from QuoteEngine import memeengine, quotemodel 
import QuoteEngine
#from QuoteEngine.ingestors import ingestor 
import QuoteEngine.ingestors

from templates import *

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import textwrap

from urllib import request

import glob

#set a static folder to retrieve images
app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY']='mysecretkey'


class GenerateMeme(FlaskForm):
    #all data is required 
    image_url=StringField("Please enter a valid image url:", validators=[DataRequired()],\
        default="https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Cute_dog.jpg/800px-Cute_dog.jpg")
    quote_body=StringField("Please enter a quote:", validators=[DataRequired()],
        default="To be or not to be")
    author_name=StringField("Please enter the author:", validators=[DataRequired()],
        default="Shakespeare")

    submit=SubmitField("Create Meme!")

@app.route('/meme_form.html', methods=['GET','POST'])
def generate_meme():
    image_url=""
    quote_body=""
    author_name=""

    form=GenerateMeme()

    if form.validate_on_submit():
        #Use user information to make meme
        img_url = form.image_url.data #get image path
        #Check image extension. Process only if jpg.
        if img_url.endswith(".jpg"):
            #Download image from url and save it locally
            path="static/photos/dog/"
            save_img_path="%s%s" %(path, img_url.split("/")[-1])

            with open(save_img_path, 'wb') as f:
                f.write(request.urlopen(img_url).read())

            #reformat quote using QuoteModel class
            quote=QuoteEngine.QuoteModel("%s - %s" %(form.quote_body.data,\
                form.author_name.data))
            #wrap text, in case it is too long
            quote = '\n'.join(textwrap.wrap(quote.getQuote_and_Author, 35)) 

            #meme.make_meme(img, quote.body, quote.author)
            #add message to picture
            meme=QuoteEngine.MemeEngine(save_img_path, quote)
            
            out_path=meme.make_meme("%s%s_meme.%s" %(path,\
                save_img_path.split("/")[-1].split(".")[0],\
                save_img_path.split("/")[-1].split(".")[-1]),\
                width=500)

            return render_template('meme.html', path=out_path) 

        else:
            raise Exception("This program currently only supports .jpg format.")  

    return render_template('meme_form.html', form=form, image_url=image_url, \
        quote_body=quote_body, author_name=author_name)

@app.route('/meme')
def meme():
    """redirect form to meme.html page 
       pass parameters from meme_form.html via session dictionary
    """
    return render_template('meme.html') 


def setup():
    """ Load all resources """

    quote_files=[file for file in glob.glob("./static/DogQuotes/*.*")]

    #Use the Ingestor class to parse all files in the
    #Initialize quotes
    quotes = [] 
    
    """
    quote examples:
        • "Dogs are not our whole life, but they make our lives whole – Roger Caras"
        • "A dog is the only thing on earth that loves you more than he loves himself – Josh Billings"
        • "If there are no dogs in Heaven, then when I die I want to go where they went – Will Rogers"
    """
    
    #combine quotes with those extracted from various text files
    lstQuotes=QuoteEngine.ingestors.Ingestor(quote_files).lstQuotes
    quotes+=lstQuotes

    images_path = "./static/photos/dog/"

    # Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = [im for im in os.listdir(images_path)] #None

    return quotes, imgs

quotes, imgs = setup()

@app.route('/')
def meme_rand():
    """ Generate a random meme 
    
        Use the random python standard library class to:
            1. select a random image from imgs array
            2. select a random quote from the quotes array
    """
    #randomly select images that don't have meme suffixes
    img = random.choice([im for im in imgs if "meme" not in im])
    path = "static/photos/dog/%s" %(img) #set image path 

    #reformat quote using QuoteModel class
    quote=QuoteEngine.QuoteModel(random.choice(quotes))
    #wrap text, in case it is too long
    quote = '\n'.join(textwrap.wrap(quote.getQuote_and_Author, 35)) 

    #meme.make_meme(img, quote.body, quote.author)
    #add message to picture
    meme=QuoteEngine.MemeEngine(path, quote)
    
    out_path=meme.make_meme("%s_meme.jpg" %(path.split(".")[0]), width=500)

    return render_template('base.html', path=out_path)   

if __name__ == "__main__":
    app.run(debug=True)