import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="+", intents=intents)

@bot.event
async def on_ready():
print(f"Connecté en tant que {bot.user}")

@bot.command()
async def ping(ctx):
await ctx.send("🏓 Pong !")

# Embed

@bot.command()
async def embed(ctx, titre, *, description):
em = discord.Embed(
title=titre,
description=description,
color=discord.Color.blue()
)
await ctx.send(embed=em)

# Effacer des messages

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, nombre: int):
await ctx.channel.purge(limit=nombre + 1)
msg = await ctx.send(f"✅ {nombre} messages supprimés.")
await asyncio.sleep(3)
await msg.delete()

# Bannir

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, membre: discord.Member, *, raison="Aucune raison"):
await membre.ban(reason=raison)
await ctx.send(f"🔨 {membre} a été banni. Raison : {raison}")

# Expulser

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, membre: discord.Member, *, raison="Aucune raison"):
await membre.kick(reason=raison)
await ctx.send(f"👢 {membre} a été expulsé. Raison : {raison}")

# Bannissement temporaire

@bot.command()
@commands.has_permissions(ban_members=True)
async def tempban(ctx, membre: discord.Member, secondes: int, *, raison="Aucune raison"):
await membre.ban(reason=raison)
await ctx.send(
f"⏳ {membre} est banni pendant {secondes} seconde(s)."
)

```
await asyncio.sleep(secondes)

await ctx.guild.unban(
    discord.Object(id=membre.id),
    reason="Fin du bannissement temporaire"
)

await ctx.send(f"✅ {membre} a été débanni automatiquement.")
```

bot.run(TOKEN)
