import discord
import pickle
from discord.ext import commands
import asyncio

class Administrator(commands.Cog, name="관리자"):


    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="경고", help="[관리자 전용] 경고를 부여합니다.", usage="!경고 [유저] (경고 횟수)")
    @commands.has_permissions(administrator=True)
    async def give_warning(self, ctx, user_name: discord.Member, amount: int=1):
        try:
            with open("bin/warnings.bin", "rb") as f:
            warning_data = pickle.load(f)
        except FileNotFoundError:
            with open("bin/warnings.bin", "wb+") as f:
                warning_data = dict()
                pickle.dump(warning_data, f)

        if str(user_name.id) not in warning_data:
            warning_data[str(user_name.id)] = amount
        else: 
            warning_data[str(user_name.id)] += amount

        with open("bin/warnings.bin", "wb") as f:
            pickle.dump(warning_data, f)

        embed = discord.Embed(title="경고 부여됨", description=f"{user_name.mention}님에게 {amount}개의 경고가 부여되었습니다.\n관리자 : {ctx.author.mention}", color=0xFF0000)
        await ctx.send(embed=embed)

    @commands.command(name="경고보기", help="자신의 경고 수를 봅니다.", usage="!경고보기")
    async def show_warnings(self, ctx):
        try:
            with open("bin/warnings.bin", "rb") as f:
                warning_data = pickle.load(f)
        except FileNotFoundError:
            with open("bin/warnings.bin", "wb+") as f:
                warning_data = dict()
                pickle.dump(warning_data, f)

        if str(ctx.author.id) not in warning_data:
            warning_data[str(ctx.author.id)] = 0

        embed = discord.Embed(title=f"{ctx.author.name}님의 경고 수", description=f"{warning_data[str(ctx.author.id)]}개", color=0xFF0000)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Administrator(bot))
