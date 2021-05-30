import book
import food
import meetha
import movie
import quotes
import song_pet
import linker
import random
import reply



def response(lvl,id,intent,entity):
  respo = reply.generate_res(intent_name=intent, entity_name=entity)
  res =""
  if lvl==2:
    res= quotes.motivate()
  elif lvl==3:
    l= book.kitaab()
    sen= "our book recommendation is: "+l[0]+"\n"+l[2]+"\n"+"you can buy it at:\n "+l[1]
    res = sen
  elif lvl==4:
    stat= linker.getvnv(id)
    if stat.lower()=="veg":
      lveg=food.pickvegfood()
      res= "why don\'t you try a new dish like "+ lveg[0]+"\n find the recipe at: \n"+ lveg[1]
    elif stat.lower()=="nv":
      lnv=food.picknvfood()
      res= "why don\'t you try a new dish like "+lnv[0]+"\n find the recipe at: \n"+ lnv[1]
    else:
      pass
  elif lvl==5:
    artist= linker.getsinger(id)
    res= "come listen to a song by your favourite artist "+artist+"\n"+song_pet.song(artist)
  elif lvl==6:
    l=meetha.pickdessert()
    res= "try a sweet dish: "+l[0]+"\n find recipe at \n"+l[1]
  elif lvl==7:
    beast = linker.getanimal(id)
    res= "come watch videos of your favourite animal "+beast+"\n"+song_pet.animal(beast)
  elif lvl==8:
    stat= linker.getmov(id)
    if stat=="hw":
      lhw= movie.hollywood()
      res= "let us watch a hollywood movie: "+lhw[0]+"\n"+lhw[1]
    elif stat=="bw":
      lbw= movie.bollywood()
      res= "let us watch a bollywood movie: "+lbw[0]+"\n"+lbw[1]
    elif stat=="both":
      c=random.randint(1,2)
      if c==1:
        lhw= movie.hollywood()
        res= "let us watch a movie: "+lhw[0]+"\n"+lhw[1]
      elif c==2:
        lbw= movie.bollywood()
        res= "let us watch a movie: "+lbw[0]+"\n"+lbw[1]
  elif lvl==9:
      res= quotes.motivate()
      artist= linker.getsinger(id)
      res= "Come listen to a song by your favourite artist "+artist+"\n"+song_pet.song(artist)
    
  return respo +"\n"+ res
