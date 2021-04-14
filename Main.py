import discord

import main

client = discord.Client()
token = 'NzEwNDg0NTQzOTM2NjU5NTU4.Xr1ISw.rPDaWUczXHn0xygGyIoOU8vmpQU'


@client.event
async def on_ready():
    print("Bot is ON!")


@client.event
async def on_message(message):
    if message.content.startswith('!url '):
        ip_info = main.main_function(message.content[5:])
        data = f"""ip: {ip_info['ip']}\n
                region: {ip_info['region']}\n
                country: {ip_info['country']}\n
                city: {ip_info['city']}\n
                provider: {ip_info['provider']}\n
                port: {ip_info['port']}"""
        await message.channel.send(embed=discord.Embed(title=f'{message.content[5:]}', description=f'{data}'))
        del message.content


client.run(token)
