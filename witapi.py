from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import sys
import json
from wit import Wit

wit_access_token ="JIDKBNGGWUJEW4UWDVPAK3TLMRWGHNYF"


def connectwit(rant):
  import requests
  url = 'https://api.wit.ai/message?v=20210528&q='+rant
  params = {'Authorization': 'Bearer JIDKBNGGWUJEW4UWDVPAK3TLMRWGHNYF'}
  try:
    solution = eval(requests.get(url,headers=params).text)
    text = str(solution.keys())
    intent_name = solution["intents"][0]["name"]
    intent_confidence = solution["intents"][0]["confidence"]
    entity_key = list(solution["entities"].keys())
    entity_key = entity_key[0]
    entity_name = solution["entities"][entity_key][0]["name"]
    traits = solution["traits"]["levels"][0]["value"]
   
  except:
    try:
      solution = eval(requests.get(url,headers=params).text)
      print(solution)
    
      text = str(solution.keys())
    
      entity_key = list(solution["entities"].keys())
      entity_key = entity_key[0]
      entity_name = solution["entities"][entity_key][0]["name"]
      traits = solution["traits"]["levels"][0]["value"]
     
    except:
      solution = requests.get(url,headers=params).text
      traits =""
      sol=requests.get(url,headers=params).text
      greet= sol.find("greeting")
      sad=sol.find("sad:sad")
      ang=sol.find("anger:anger")
      frus=sol.find("frustrated:frustrated")
      feel=[greet, sad, ang, frus]
      convo = sol.find("conversation")
      fact = sol.find("fact")
      encourage = sol.find("encouragement")
      body = [convo, fact, encourage]
      if greet==-1:
        if body.count(-1)==3:
          return "","",""
        else:
          return "","",""
      else:
        return "greeting","",""
     

      intent_name = None
      entity_name = None
      for i in range(3):
        if body[i]!= -1:
          c=i
          break
      if c==0:
        intent_name = "conversation"
      elif c==1:
        intent_name = "fact"
      elif c==2:
        intent_name = "encouragement"
       
      for i in range(4):
        if feel[i]!= -1:
          c=i
          break
      if c==0:
        entity_name = "greeting"
       
      elif c==1:
        entity_name = "sad"
       
      elif c==2:
        entity_name = "anger"
       
      elif c==3:
        entity_name = "frustration"
      
  return intent_name,entity_name,traits