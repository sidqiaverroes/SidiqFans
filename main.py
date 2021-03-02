import discord
from discord.client import Client
import os 
from discord.utils import get
from replit import db
import datetime
import pytz
from server import keep_alive

client = discord.Client()

timezone = pytz.timezone('Asia/Jakarta')
enjing = timezone.localize(datetime.datetime(2002,9,26,00,00,00))
siang = timezone.localize(datetime.datetime(2002,9,26,11,59,00))
dalu = timezone.localize(datetime.datetime(2002,9,26,17,00,00))


sidiq = ["sidiq", "siddick", "sidick"]

def update_messages(message):
  if 'lobby' in db.keys():
    lobby = db['lobby']
    lobby.append(message)


@client.event
async def on_ready():
    print('Hello nama gue sidiq salam kenal')

@client.event
async def on_message(message):

    pki = get(client.emojis, name='sidiqpki')
    oppa = get(client.emojis, name='sidiqoppa')
    makanbang = get(client.emojis, name='sidiqmakanbang')
    ngefak = get(client.emojis, name='sidiqngefak')
    poggers = get(client.emojis, name='pogger')


    now = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
    if(message.author == client.user) :
        return

    if(message.content.lower().startswith(tuple(sidiq))):
        pesan = message.content.lower().split()
        
        if(len(pesan) == 1):
          await message.channel.send('opo nyuk!')

        else:
          if(pesan[1] == 'alus' and pesan[2] == 'mode'):
            if(now.time() >= enjing.time() and now.time() <= siang.time()):
              await message.channel.send('Assalamualaikum Wr.Wb., sugeng enjing nami kula sidick @everyone')
            elif(now.time() >= siang.time() and now.time() <= dalu.time()):
              await message.channel.send('Assalamualaikum Wr.Wb., sugeng siang nami kula sidick @everyone')
            else:
              await message.channel.send('Assalamualaikum Wr.Wb., sugeng dalu nami kula sidick @everyone')

    if(client.user.mentioned_in(message)) :
      await message.channel.send('rasah ngetag-ngetag')
    
    if(message.author.id == 755411438494810193):

      await message.add_reaction(pki)
      await message.add_reaction(oppa)
      await message.add_reaction(makanbang)
      await message.add_reaction(ngefak)
      await message.add_reaction('🇸')
      await message.add_reaction('🇮')
      await message.add_reaction('🇩')
      await message.add_reaction('ℹ️')
      await message.add_reaction('🇨')
      await message.add_reaction('🇰')
      await message.channel.send('ampun lort')
    
    if('<@!755411438494810193>' in message.content) :
      await message.add_reaction(ngefak)
      await message.channel.send('rasah ngetag-ngetag')
    
@client.event
async def on_guild_join(guild):
  lobby = client.get_channel(691683864925438021)
  await lobby.send('salken gue siddick @everyone')
      
keep_alive()
client.run(os.getenv('')) #masukkan token bot mu gan