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
