import discord
from discord.ext import commands

class Core(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="출력") #수정
    async def printit(self, ctx): #수정
        await ctx.send(":) Python Bot에 의해 출력됨.")
    
    

def setup(bot):
    bot.add_cog(Core(bot))