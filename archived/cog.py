import discord
from discord.ext import commands
# from libs import notice
class mordrate(commands.Cog, name='Admin commands'):
    '''These are the developer commands'''
    def __init__(self, bot):
        self.client = bot
        print("connected")

    @commands.command()
    @commands.has_any_role("Admin", "Owner")
    async def kick(self, ctx, man: discord.Member, *, reson):
        channel = self.client.get_channel(807532505137545217)
    	await  notice(self.client,"Notice: Kick",f"<@{str(man.id)}> has been kicked by <@{str(ctx.id)}>\nchannel: { str(ctx.channel)}\nreason: {reson}")
		await notice(self.client,"Notice: Kick",f"<@{str(man.id)}> has been kicked by <@{str(ctx.id)}>\nchannel: { str(ctx.channel)}\nreason: {reson}", ctx.channel.id)
        
		
        await man.kick()

    @commands.command()
    @commands.has_any_role("Admin", "Owner")
    async def mute(self, ctx, man: discord.Member, *, reson="none"):
        await notice(self.client,"Notice:muted",f"<@{man.id}> has been muted by <@{ctx.author.id}>\n reason: {reson}")
        await notice(self.client,"Notice:muted",f"<@{man.id}> has been muted by <@{ctx.author.id}>\n reason: {reson}",ctx.channel.id)
        await man.add_roles(discord.utils.get(ctx.guild.roles, name='muted'))

    @commands.command()
    @commands.has_any_role("Admin", "Owner")
    async def unmute(self, ctx, man: discord.Member, *, reson="none"):
        await notice(self.client,"Notice:unmuted",f"<@{man.id}> has been unmuted by <@{ctx.author.id}>\n reason: {reson}")
        await notice(self.client,"Notice:unmuted",f"<@{man.id}> has been unmuted by <@{ctx.author.id}>\n reason: {reson}",ctx.channel.id)
        await man.remove_roles(discord.utils.get( ctx.guild.roles, name='muted'))

    @commands.command()
    @commands.has_any_role("Admin", "Owner")
    async def addrole(self, ctx, man: discord.Member, role):
        role = discord.utils.get(ctx.guild.roles, name=role)
        await man.add_roles(role)
        await notice(self.client,"Role added",f"{str(man.mention)} has been given the role of  {str(role.name)}")
        await notice(self.client,"Role added",f"{str(man.mention)} has been given the role of  {str(role.name)}",ctx.channel.id)
        await ctx.channel.send(
            f"{str(man.mention)} has been given the role of  {str(role.name)}")
		

    @commands.command()
    @commands.has_any_role("Admin", "Owner")
    async def removerole(self, ctx, man: discord.Member, role):
        role = discord.utils.get(ctx.guild.roles, name=role)
        await man.remove_roles(role)
        await notice(self.client,"Role removed",f"{str(man.mention)} has been deprived the role of  {str(role.name)}")
        await notice(self.client,"Role removed",f"{str(man.mention)} has been deprived the role of  {str(role.name)}",ctx.channel.id)
        await ctx.channel.send(
            f"{str(man.mention)} has been deprived of the role {str(role.name)}"
        )
    @commands.command(aliases=["s"])
        async def spam(self, ctx, man: discord.Member, x, *, msg):
            if ctx.message.author.id == 792707663850635274:
                for _ in range(int(x)):
                    await man.send(msg)
            await ctx.message.author.send("done")
            print("i am done")

def setup(bot):
    bot.add_cog(mordrate(bot))


def notice(client,title,disc,channel=807532505137545217):
	channel = client.get_channel(channel)
	embed = discord.Embed( title=title,description=disc,color=0x0066ff)
	return channel.send(embed=embed)

	