from query import printResult
import discord
import asyncio
from discord.ext import commands
description = "Hydra-Bot"
client = discord.Client()
#CLOT RULES
Min_GameCount = 1
Max_GameCount = 5
#END OF RULES

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
                
@client.event
async def on_message(message):
    if message.content.startswith('!update'):
        async for log in client.logs_from(message.channel, limit=20):
            
            if log.content.startswith('All chances have been processed'):
                await client.send_message(message.channel, "All chances have been processed")
                break
                
            elif log.content.startswith('!clot'):
                
                command = log.content.split()
                print (command)
                if len(command) == 1:
                    await client.send_message(message.channel, "insert spreadsheet link")
                    
                elif command[1] == 'join':
                    if len(command) == 4:
                        try:
                            gamecount = int(command[3])
                        except ValueError:
                            await client.send_message(message.channel, (log.author.mention+ ': ' +log.content))
                            await client.send_message(message.channel, 'Make sure to use the correct syntax')
                        if gamecount < Min_GameCount or gamecount > Max_GameCount:
                            await client.send_message(message.channel, (log.author.mention+ ': ' +log.content))
                            await client.send_message(message.channel, 'Make sure to have minimal ' +str(Min_GameCount) +' and maximal ' +str(Max_GameCount)+ ' games')
                        else:
                            pass
                    else:
                        await client.send_message(message.channel, (log.author.mention+ ': ' +log.content))
                        await client.send_message(message.channel, 'Make sure to use the correct syntax')
                        
                elif command[1] == 'leave':
                    pass
                
                elif command[1] == 'set' and command[2] == 'gamecount':
                    if len(command) != 4:
                        await client.send_message(message.channel, (log.author.mention+ ': ' +log.content))
                        await client.send_message(message.channel, 'Make sure to have the correct syntax')
                    else:
                        try:
                            gamecount = command[3]
                        except ValueError:
                            await client.send_message(message.channel, (log.author.mention+ ': ' +log.content))
                            await client.send_message(message.channel, 'Make sure to have the correct syntax')
                        if gamecount < Min_GameCount or gamecount > Max_Gamecount:
                            await client.send_message(message.channel, (log.author.mention+ ': ' +log.content))
                            await client.send_message(message.channel, 'Make sure to have minimal ',Min_GameCount, ' and maximal ', Max_GameCount, ' games')
                
                        




client.run(token)
