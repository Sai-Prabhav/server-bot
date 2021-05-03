import discord

def notice(client,title,disc):
	channel = client.get_channel(807532505137545217)
	embed = discord.Embed(
	title=title,
	description=disc,
	color=0x0066ff)
	await channel.send(embed=embed)
