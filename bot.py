from telethon import TelegramClient, events
import asyncio
import time
from telethon import events
from telethon.errors import MessageIdInvalidError

api_id = 29111734
api_hash = '8869243388a6afcae5959eca05e02619' 
 
async def main(): 
    client = TelegramClient('session_name', api_id, api_hash)
    print('''
    
 ___                   _______            _________________                                          
|   |                /   ___   \         |______    _______|                                         
|   |               /   /   \   \               |   |                                                
|   |              /   /__ __\   \              |   |                                                
|   |    ___      /   ________\   \             |   |                                                
|   |___|   |    /   /         \   \      ______|   |______                                          
\___________/   /___/           \___\    |_________________|

                                              ''') 

    @client.on(events.NewMessage(from_users=572621020))
    async def _(event):
        if "appeared" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.click(0)  
                return
                
    @client.on(events.NewMessage(from_users=572621020))
    async def _(event):
        if "Battle begins!" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.click(0, 0) 
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.click(0, 0)
                return

    @client.on(events.MessageEdited(from_users=572621020))
    async def _(event):
        if "used" in event.raw_text:
            try:
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.click(0, 0)  
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass
                
    @client.on(events.MessageEdited(from_users=572621020))
    async def _(event):
        if "missed" in event.raw_text:
            try:
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.click(0, 0)  
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass
                
    @client.on(events.NewMessage(from_users=572621020))
    async def _(event):
        if "appeared" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.click(0) 
                return
          
    @client.on(events.MessageEdited(from_users=572621020))
    async def _(event):
        try:
            if "fainted." in event.raw_text:
               await asyncio.sleep(1)  # Add a delay of 1 seconds
               await event.client.send_message(572621020, "/hunt")
        except (asyncio.TimeoutError, MessageIdInvalidError):
            pass
     
    await client.start()
    await client.run_until_disconnected()
asyncio.run(main())