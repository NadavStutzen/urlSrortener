from __future__ import print_function
from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import validators
import base64
import requests
import sys

from config import app_config

db = SQLAlchemy()    

# test methods (working partially)

# def testUrlValidation():
#     if validateUrl('aaaa'):
#         print('Failed, "aaaa" is not a valid url',file=sys.stderr)
#     elif validateUrl('$#%#$%$#%$#%') :
#         print('Failed, "$#%#$%$#%$#%" is not a valid url',file=sys.stderr)
#     elif validateUrl(' ') :
#         print('Failed, " " is not a valid url',file=sys.stderr)
#     elif not validateUrl('www.w3schools.com'):
#         print('Failed, "www.w3schools.com" is a valid url',file=sys.stderr)
#     elif not validateUrl('https://www.one.co.il/'):
#         print('Failed, "https://www.one.co.il/" is a valid url',file=sys.stderr)
#     elif not validateUrl('https://www.google.com/search?q=unittest+docker+flask&oq=unittest+docker+flask&aqs=chrome..69i57.8180j0j4&sourceid=chrome&ie=UTF-8'):
#         print('Failed, "https://www.google.com/search?q=unittest+docker+flask&oq=unittest+docker+flask&aqs=chrome..69i57.8180j0j4&sourceid=chrome&ie=UTF-8" is a valid url',file=sys.stderr)    
#     print('url validation test suite passed',file=sys.stderr)

# def addTODBFlowTest():
#     url1 = urlConverter(addUrlToDB('https://www.google.com'))
#     if not url1:
#         print('"https://www.google.com" failed to be added to db',file=sys.stderr)
#     url2 = urlConverter(addUrlToDB(123))
#     if url2:
#         print('Test failed. Integer should not be added to DB',file=sys.stderr)
#     url3 = urlConverter(addUrlToDB(True))
#     if url3:
#         print('Test failed. Boolean should not be added to DB',file=sys.stderr)
        
#     print(' add to DB flow passed',file=sys.stderr)    

        
# def shortUrlsTest(queryData):
#     for i in queryData:
#             r = requests.get(i.shortUrl)
#             break
#             if r.url != i.shortUrl:
#                 print(i.shortUrl + 'failed to be opened',file=sys.stderr)
            
#     print('shortened Urls test suite passed.',file=sys.stderr)
        
            
    


def addUrlToDB(url):
    newUrl = models.Url(longUrl=url)
    db.session.add(newUrl)
    db.session.commit()
    return newUrl.id

def urlConverter(urlID):
    domainStr = 'http://localhost:8000/'
    encodedId = base64.b64encode(bytes(urlID))
    urlInstance = models.Url.query.filter_by(id=urlID).first()
    urlInstance.shortUrl = domainStr + encodedId
    db.session.commit()
    return urlInstance.shortUrl

def validateUrl(dataUrl):
    if dataUrl.startswith('http'):
        if validators.url(dataUrl):
            return dataUrl
        else:
            return False   
    else:    
        url1 = 'http://' + dataUrl
        url2 = 'https://' + dataUrl
        if validators.url(url1):
            return url1
        elif validators.url(url2):
            return url2
        else:
            return False
        


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    
    @app.route('/<urlID>', methods=['GET'])
    def redirectUrl(urlID):
        domainStr = 'http://localhost:8000/'
        dbUrl = models.Url.query.filter_by(shortUrl = domainStr + urlID).first()
        if not dbUrl:
            return 'no such url'
        return redirect(dbUrl.longUrl, code=302)

    @app.route('/', methods=['GET', 'POST'])
    def urlShortener():
        if request.method == 'POST':
            
            dataUrl = request.form['url']
            validUrl = validateUrl(dataUrl)
            if not validUrl:
                return render_template('index.html', error = 'Not a valid address')
            
            queryRes = models.Url.query.filter_by(longUrl=validUrl).first()
            if queryRes:
                return render_template('shorturl.html', shortUrl = queryRes.shortUrl)
            
            shortUrl = urlConverter(addUrlToDB(validUrl))
            return render_template('shorturl.html', shortUrl = shortUrl)
            
        return render_template('index.html')
    
    
    #test route(not proud of it) 
    
    # @app.route('/tests')
    # def runTests():
    #     queryData = models.Url.query.all()
    #     testUrls = []
    #     testUrlValidation()
    #     addTODBFlowTest()
    #     shortUrlsTest(queryData)
    #     return 'tests run finished'

    migrate = Migrate(app, db)
    

    from app import models
    
    return app
