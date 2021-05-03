import discord
from discord.ext import commands
import time
from libs import *
import numpy as np
import matplotlib.pyplot as plt


class makeiteasy(commands.Cog, name='main commands '):
    def __init__(self, bot):
        self.client = bot
        print("connected to features ")

    @commands.command(aliases=["il"])
    async def invitelink(self, ctx):
        await ctx.channel.send(embed=discord.Embed(
            title="Invite Link",
            description=
            "Click link below to add me to your server.\nhttps://discord.com/api/oauth2/authorize?client_id=803611455245123625&permissions=8&scope=bot ",
            color=0x0066ff))

    @commands.command(aliases=["lc"])
    async def lettercount(self, ctx):
        info = load_database()["lettercount"]
        keys = []
        values = []
        for letter in info:
            keys.append(letter)
            values.append(info[letter])
        plt.bar(keys, values)
        plt.xlabel("letters")
        plt.ylabel("number of times used")
        plt.savefig("graph.png")
        plt.clf()
        file = discord.File("graph.png", filename='graph.png')
        await ctx.channel.send(file=file)


    @commands.command(aliases=["sc"])
    async def sourcecode(self, ctx, x=5):
        await ctx.channel.send(embed=discord.Embed(
            title="Source Code",
            description=
            "the bots code is : https://repl.it/@SaiPrabhav/using-cogs-in-discordpy",
            color=0x0066ff))

    @commands.command(aliases=["ss"])
    async def serverstatus(self, ctx, xx="0", tic=None):
        if tic:
            tic = int(tic)
        servername = ctx.message.guild.name
        serverid = str(ctx.message.guild.id)
        if xx == "online" or xx == "1":
            xx = 1
            title = f"graph of online members in {servername}"
        elif xx == "total" or xx == "0":
            xx = 0
            title = f"graph of total members in {servername}"
        await ctx.channel.send(servername)
        info = load_database()["peopleinfo"]
        serverinfo = info[serverid]
        timelist = []
        memberlist = []
        for date1 in serverinfo:
            for time1 in serverinfo[date1]:
                timelist.append(f"{date1[:-5]},{time1[:-3]}")
                memberlist.append(serverinfo[date1][time1])
        plt.plot(timelist, [member[int(xx)] for member in memberlist],
                 color="g")
        plt.title(title)
        plt.xlabel("time and date")
        plt.ylabel("number of people")
        tick = round((len(memberlist) / 6) + 0.499)
        ticklist = np.arange(0, len(memberlist), tic or tick)
        print(len(memberlist), len(memberlist) / 6)
        print(tick)
        plt.xticks(ticklist)
        plt.savefig("graph.png")
        plt.clf()
        file = discord.File("graph.png", filename='graph.png')
        await ctx.channel.send(file=file)

    @commands.command(aliases=["sl"])
    async def serverlink(self, ctx):
        await ctx.channel.send(embed=discord.Embed(
            title="Server Link",
            description=
            "to join the server use this link: https://discord.gg/CCgceGf7j9",
            color=0x0066ff))

    @commands.command()
    @commands.has_any_role("Admin", "Owner","👑CREAM_KING👑")
    async def clear(self, ctx, *, limi=5):
        time.sleep(0.5)
        await ctx.channel.purge(limit=int(limi) + 1)

    @commands.command(aliases=["dc"])
    @commands.has_permissions(administrator=True)
    async def declarechannel(self, ctx, channel: discord.TextChannel):
        serverid = str(ctx.message.guild.id)
        dat = load_database()
        dat["serverchannel"][serverid] = channel.id
        save_database(dat)


def setup(bot):
    bot.add_cog(makeiteasy(bot))
