import os
import chart
import discord
import msgboi
import random
import witapi
from alive import keep_alive

client = discord.Client() 

import sqlite3
mycon = sqlite3.connect('survey.db')
cur = mycon.cursor()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

status='start'
global storehouse
storehouse = []
global scoreboard
scoreboard = []
@client.event
async def on_message(message):
    global status 
    
    if message.author == client.user:
        return 
    if (status=='start'):
      try:
        cred="insert into log values('{}','{}',NULL,NULL,NULL,NULL,NULL);".format(str(message.author.id),message.author.name)
        cur.execute(cred)
        mycon.commit()
        await message.channel.send('Hi '+message.author.name+'! Let\'s do a quick survey for Master Oogway to know you better.')
        await message.channel.send('Mention some singers/bands you like:')
        status='singer'
      except:
        await message.channel.send('Welcome back '+message.author.name+'!\nMaster Oogway welcomes you!')
        status='rant'
    elif status=='singer':
        col1="update log set singer='{}' where id='{}'".format(message.content, str(message.author.id))
        cur.execute(col1)
        mycon.commit()
        await message.channel.send('Mention some of your favourite animals:')
        status='animal'
    elif status=='animal':
        col2="update log set animal='{}' where id='{}'".format(message.content, str(message.author.id))
        cur.execute(col2)
        mycon.commit()
        await message.channel.send("Please type 'veg' if you are a vegetarian and 'nv' if you are a non vegetarian")
        status='vnv'
    elif status=='vnv':
        col3="update log set veg_nv='{}' where id='{}'".format(message.content, str(message.author.id))
        cur.execute(col3)
        mycon.commit()
        await message.channel.send("Please mention your movie preference. Type 'bw' for Bollywood movies, 'hw' for hollywood movies and 'both' if you enjoy both.")
        status='movie'
    elif status=='movie':
        col4="update log set hw_bw='{}' where id='{}'".format(message.content, str(message.author.id))
        cur.execute(col4)
        mycon.commit()
        await message.channel.send('Thank You! Our survey ends here. \nMaster Oogway is all ears to your problems.')
        status='rant'
    elif status=='rant':
        if message.content!='!end':
            store= message.content
            intent,entity,trait = witapi.connectwit(store) 
            import level
            lev = level.calculate_rant(intent,entity)
            
            scoreboard.append(lev)
            text= msgboi.response(lev,message.author.id,intent,entity)
            await message.channel.send(text)
            storehouse.append(store)
        else:
            await message.channel.send('Bye! Here is a look at your mood graph: ')
            
            await message.channel.send(chart.plot(scoreboard))
            status='start'

secret = os.environ['tok']
keep_alive() 
client.run(secret) 