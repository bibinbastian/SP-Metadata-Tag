import requests
import json
from dotenv import load_dotenv
import os #dotenv uses this package to bring environ variables

load_dotenv() #Function call to bring all environment var
#Requeuest URL
#https://{endpoint}/vision/v2.0/analyze[?visualFeatures][&details][&language]
#This is from the API Documentation.Below I modified based on my location
#Canada Central - canadacentral.api.cognitive.microsoft.com (endpoint ,also from API documentation)
requesturl='https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/analyze'

#Request Parameter
#All three paremeter sfor this function is optional.
#visualFeatures= 'Description'#describes the image content with a complete sentence in supported languages
parameters ={'language':'en','visualFeatures':'Description'} 

#Request Headers
ContentType='application/octet-stream' #Here we are passing the raw image file as request body.so stream is selected as type
SubscriptionKey=os.getenv('SubscriptionKey')
headers={'Content-Type':ContentType,'Ocp-Apim-Subscription-Key':SubscriptionKey}

#Request Body 
image_path='./polarbear.jpg'
image_data=open(image_path,'rb').read() #https://stackabuse.com/file-handling-in-python/ and found out rb is the best mode for images

#Response
response=requests.post(requesturl,headers=headers,params=parameters,data=image_data)
results=response.json()
#print(type(response))  --requests.models.Response'
#print(type(results)) --dictionary 
#.json function converted the response to a native python datastructure - dictionary

#Extracting      
# Now copy the below data  and use any json formatter and decide what to extract                                
#print(results)
resultid= results['requestId']
resulttag1=results['description']['tags'][0]
resulttag2=results['description']['tags'][1]
resulttag3=results['description']['tags'][2]
resultext=results['description']['captions'][0]['text']
resultconfidence=results['description']['captions'][0]['confidence'] # Reason being captions is a list """

modresult={
    'id':resultid
    ,'tag1':resulttag1
    ,'tag2':resulttag2
    ,'tag3':resulttag3
    ,'caption':resultext
    ,'confidence':resultconfidence
    
}
print(modresult)   

#print(type(response))  --requests.models.Response'
#print(type(results)) --dictionary 
#print(type(results['description'])) -- dictionary
