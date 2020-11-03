TOKEN = "TokenGoesHere"
CHANNELID = 000000000000000000
ROLENAME = "RoleToGive"

import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix="^&%££%") # never used so can be literally anything
bot.remove_command("help")

@bot.event
async def on_ready():
    print("The bot is alive.")

@bot.event
async def on_voice_state_update(member, before, after):
    if not after.channel == None:
        if after.channel.id == CHANNELID:
            role = get(member.guild.roles, name=ROLENAME)
            await member.add_roles(role)
        else:
            role = get(member.guild.roles, name=ROLENAME)
            await member.remove_roles(role)
    else:
            role = get(member.guild.roles, name=ROLENAME)
            await member.remove_roles(role)


bot.run(TOKEN)