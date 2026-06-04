import discord
from discord.ext import commands
import asyncio
import os

TOKEN = os.getenv("TOKEN")
PREFIX = "+"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} est connecté !")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def embed(ctx, titre, *, description):
    embed = discord.Embed(
        title=titre,
        description=description,
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, nombre: int):
    await ctx.channel.purge(limit=nombre + 1)
    msg = await ctx.send(f"✅ {nombre} messages supprimés.")
    await asyncio.sleep(3)
    await msg.delete()

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, membre: discord.Member, *, raison="Aucune raison"):
    await membre.ban(reason=raison)
    await ctx.send(f"🔨 {membre.mention} a été banni.\nRaison : {raison}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def tempban(ctx, membre: discord.Member, temps: int, *, raison="Aucune raison"):
    await membre.ban(reason=raison)

    await ctx.send(f"⏳ {membre.mention} a été banni pendant {temps} seconde(s).")

    await asyncio.sleep(temps)

    await ctx.guild.unban(discord.Object(id=membre.id))
    await ctx.send(f"✅ {membre.mention} a été débanni automatiquement.")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, membre: discord.Member, *, raison="Aucune raison"):
    await membre.kick(reason=raison)
    await ctx.send(f"👢 {membre.mention} a été expulsé.\nRaison : {raison}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Vous n'avez pas les permissions nécessaires.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Arguments manquants.")
    else:
        print(error)

bot.run(TOKEN)
