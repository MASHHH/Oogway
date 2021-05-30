
def calculate_rant(intent_name,entity_name,score=1):
  if entity_name == "sad":
    if intent_name == "fact":
      score = 7
    elif intent_name == "encouragement":
      score = 9
    elif intent_name == "conversation":
      score = 8
    else:
      score = 1
  elif entity_name == "frustration":
    if intent_name == "fact":
      score = 1
    elif intent_name == "encouragement":
      score = 3
    elif intent_name == "conversation":
      score = 2
    else:
      score = 1
  else:
    if intent_name == "fact":
      score = 4
    elif intent_name == "encouragement":
      score = 6
    elif intent_name == "conversation":
      score = 5
    else:
      score = 1
  return score