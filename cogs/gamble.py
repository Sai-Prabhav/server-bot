import discord
from random import choice, randint
from discord.ext import commands


class gamble(commands.Cog, name='gamble'):
    def __init__(self, bot):
        self.client = bot

        print("connected to gamble ")

    @commands.command(aliases=["rmi", "star"])
    async def ratemyidea(self, ctx, *, reson=None):
        await ctx.send(f"{randint(0,5)} stars")

    @commands.command(aliases=['dice', 'rod'])
    async def rolladice(self, ctx, times=1):
        for i in range(times):
            await ctx.send(randint(1, 6))

    @commands.command(aliases=["toss","tac"])
    async def tossacoin(self, ctx):
        await ctx.send(choice(['heads', 'tails']))

    @commands.command(aliases=['yon', 'yesno'])
    async def yesorno(self, ctx, *, reson):
        await ctx.send(choice(["YES", "NO"]))


def setup(bot):
    bot.add_cog(gamble(bot))
