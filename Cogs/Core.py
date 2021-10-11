import discord
from discord.ext import commands

class Core(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="출력") #수정
    async def printit(self, ctx): #수정
        await ctx.send(":) Python Bot에 의해 출력됨.")
    
    @commands.command(name="참여")
    async def join(self, ctx):
        try:
            global vc
            vc = await ctx.message.author.voice.channel.connect()
            
        except:
            try:
                await ctx.move_to(ctx.message.author.voice.channel)
            except:
                await ctx.send("채널에 유저가 접속해있지 않네요..")
    
    @commands.command(name="나가")
    async def leave(self, ctx):
        try:
            await vc.disconnect()
        except:
                await ctx.send("이미 그 채널에 속해있지 않아요!")
                     
        
    
    

def setup(bot):
    bot.add_cog(Core(bot))
