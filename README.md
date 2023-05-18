# Meme Generator

------------------    

## 1. Overview

The combination of pictures and words capture our emotions and inspire our minds. This program called *Meme Generator* simplifies the process of combining memorable pictures with meaningful and, at the same time, motivational messages.  The user can either provide his/her own picture and a quotation or let the program retrieve a random picture and a quotation from stored files. 

## 2. Features

This program can either be deployed on a browser or via a command line interface. Although the platforms are different, the functions are the same. In both case, the user can either obtain a randomly generated meme from stored files or by inputting a specific image and a quotation. 

On a browser, the user can provide his/her own quotation and image via the meme_form.html page. Here, the user provides an image url (must be in a .jpg format), as well as a quote and the author.

On a command line interface, the user provides the path to the .jpg image, as well as a quote body and the author.

This project has been deployed online via a heroku platform url: https://meme-generator-py.herokuapp.com/.

## 3. Running the project

This program has been tested on an anaconda environment on a windows machine. The required python library dependencies can be installed into an existing anaconda environment by typing pip install -r requirements.txt.

The PDFIngestor class uses the pdftotext.exe file via the subprocess module to extract strings in a pdf file. The executable file runs only on a Windows machine. However, a try/except block was added to catch the exception (i.e., if the executable file is inaccessible); in this case, the PyPDF2 python package is used instead.   

The program can be run either on a web browser or on a command line interface. 

On a browser, the user fills out the appropriate textfields to specify the image source and quotation. The python script for running the application on a browser is called **app.py**. To run the browser application, open an anaconda terminal, activate the appropriate anaconda environment, and type python app.py. Once the application is activated, open a browser, and navigate to http://127.0.0.1:5000 to run the web application. 

On a command line interface, the user specify the input following the required arguments. The python script for running the application on a command line interface is called **meme.py**. To tun the application, just type *python meme.py* on an anaconda terminal with the appropriate environment activated. A random quotation and image will be used to generate a meme and a path to the generated meme file will be printed on the terminal. 

Alternatively, specify the path, body, and author arguments to customize the meme output, e.g., *python meme.py --path "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Cute_dog.jpg/800px-Cute_dog.jpg" --body "To be, or not to be, that is the question" --author "William Shakespeare"*. 

In the above example, it uses an image that was originally posted to Flickr by leisergu at https://www.flickr.com/photos/59216720@N00/2873249326. It was reviewed on 29 July 2014 by FlickreviewR and was confirmed to be licensed under the terms of the cc-by-2.0. 

## 4. Dependencies

The optional inputs are:

- Body and author: may be supplied from files of various formats (i.e., .pdf, .txt, .docx, or csv). 

- Image: currently only supports .jpg. 

These inputs are stored within the subfolders called DogQuotes and photos, respectively. These subfolders are saved within the static folder.

The user interacts with a web browser via html files, including: **base.html, meme.html, and meme_form.html**

The various python modules are stored in the QuoteEngine folder. The main modules are: 

- imagecaptioner.py

- memeengine.py

- quotemodel.py

Furthermore, the QuoteEngine folder contains ingestors subfolder that contains the following modules:

- ingestor.py

- ingestorinterface.py

- csvingestor.py

- docxingestor.py

- pdfingestor.py

- textingestor.py

- pdftotext.exe

The quotations that are stored in the various text file formats are extracted using the various ingestor classes (i.e., csvingestor.py, docxingestor.py, pdfingestor.py, and textingestor.py). pdftotext.exe is a dependency of pdfingestor.py and is a part of xpdf toolkit, which is available as open source. More information about the toolkit can be found here: https://www.xpdfreader.com/about.html. 

Detailed description about each of the module can be found in its respective docstrings, which can be accessed using the help() function.

The message written on the images are generate using Roboto-Regular.ttf font, which was downloaded from https://fonts.google.com/specimen/Roboto. This font is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0). 

This folder structure of the program is as follows:

    app.py

    meme.py

    +-QuoteEngine

        |

        +-ingestors

                csvingestor.py

                docxingestor.py            

                ingestor.py

                ingestorinterface.py

                pdfingestor.py

                pftotext.exe

                textingestor.py           

        imagecaptioner.py

        memeengine.py

        quotemodel.py

    +-static

        |

        +-DogQuotes

                DogQuotesCSV.csv

                DogQuotesDOCX.docs

                DogQuotesPDF.pdf

                DogQuotesTXT.txt

           +-photos

                +-dog

                        xander_1.jpg

                        ...            

            +-SimpleLines

                    SimpleLines.csv

                    SimpleLines.docx

                    SimpleLines.pdf

                    SimpleLines.txt                

    +-templates

            base.html

            meme.html

            meme_form.html
