import discord
from discord.ext import commands
from discord import app_commands

from dotenv import load_dotenv
import os

import aiohttp
import asyncio

import json

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

header={"User-Agent": "Opium Lyric Lounge (adityanarayanr3@gmail.com)"}

client = commands.Bot(command_prefix="!", intents=intents)

with open("playlist.json", 'r') as f:
    playlists = json.load(f)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    await client.tree.sync() 
    print("Slash commands synced!")

@client.tree.command(name="track", description="Provides detailed information on track")
@app_commands.describe(track="Name of the song", artist="Artist name")
async def track(interaction: discord.Interaction, track: str, artist: str):
    query = f'recording:"{track}" AND artist:"{artist}"'
    url = f'https://musicbrainz.org/ws/2/recording/?query={query}&fmt=json'

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=header, timeout=20) as resp:
                data = await resp.json()
    except asyncio.TimeoutError:
        await interaction.response.send_message("API timed out. Try again later!")
        return
            
    data = data["recordings"][0]
    track = data["title"]
    artist= data["artist-credit"][0]["name"]

    time = data["length"] /60000
    minute = int(time//1)
    seconds = int(time%1 * 60)

    album_cover_url = f"https://coverartarchive.org/release/{data["releases"][0]["id"]}/front"

    embed = discord.Embed(
        title=track,
        description=artist,
        color=discord.Color.blue()
    )
    embed.add_field(name="Album", value=data["releases"][0]["title"], inline=True)
    embed.add_field(name="Duration", value=f"{minute}:{seconds}", inline=True)
    embed.set_thumbnail(url=album_cover_url)

    await interaction.response.send_message(embed=embed)


@client.tree.command(name="lyrics", description="Provides lyrics")
@app_commands.describe(query="Search query with artist and song")
async def lyrics(interaction: discord.Interaction, query: str):
    try: 
        async with aiohttp.ClientSession() as session:
            async with session.get(url=f"https://lrclib.net/api/search?q={query}", timeout=20) as resp:
                    data = await resp.json()
                    data = data[0]
    except asyncio.TimeoutError:
        await interaction.response.send_message("API timed out. Try again later!")
        return

    embed = discord.Embed(
        title=f"{data["trackName"]} by {data["artistName"]}",
        description=data["plainLyrics"][:4096],
        color=discord.Color.purple()
    )

    await interaction.response.send_message(embed=embed)

@client.tree.command(name="playlist", description="Make a playlist")
@app_commands.describe(
    action="Choose an action for your playlist",
    song="Name of the song (required for add/remove)"
)
@app_commands.choices(
    action=[
        app_commands.Choice(name="Add", value="add"),
        app_commands.Choice(name="Remove", value="remove"),
        app_commands.Choice(name="View", value="view"),
        app_commands.Choice(name="Clear", value="clear")
    ]
)
async def playlist(interaction: discord.Interaction, action: app_commands.Choice[str], song: str = None):
    await interaction.response.defer()
    user_id = str(interaction.user.id)
    
    if user_id not in playlists:
        playlists[user_id] = []
    
    if action.value=="add" or action.value=="remove":
        try: 
            async with aiohttp.ClientSession() as session:
                async with session.get(url=f"https://lrclib.net/api/search?q={song}", timeout=20) as resp:
                    if resp.status != 200:
                        await interaction.followup.send(f"API error: {resp.status}")
                        return
                    data = await resp.json()
                    data = data[0]
            track = data["trackName"]
            artist =data["artistName"]

            song = track+" - "+artist
        except asyncio.TimeoutError:
            await interaction.followup.send("API timed out. Try again later!")
            return
    if action.value=="add":
        playlists[user_id].append(song)
        await interaction.followup.send(f"Added {song} to your playlist!")
    elif action.value=="remove":
        playlists[user_id].remove(song)
        await interaction.followup.send(f"Removed {song} from your playlist!")
    elif action.value=="clear":
        await interaction.followup.send(f"Cleared {len(playlists[user_id])} songs from your playlist!")
        playlists[user_id]=[]
        
    elif action.value=="view":
        embed = discord.Embed(
            title="Liked Songs",
            description=interaction.user,
            color=discord.Color.og_blurple()
        )
        embed.set_thumbnail(url=interaction.user.display_avatar)

        for i in playlists[user_id]:
            name,value = i.split(" - ", 1)
            print(name, value)
            embed.add_field(name=name, value= value, inline=False)
        
        await interaction.followup.send(embed=embed)
    
    with open("playlist.json", "w") as f:
        json.dump(playlists, f, indent=4)



@client.tree.command(name="help", description="Shows all bot commands")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Bot Commands",
        description="List of available slash commands:",
        color=discord.Color.green()
    )

    # Loop through all registered slash commands
    for cmd in client.tree.get_commands():
        if isinstance(cmd, app_commands.Command):
            embed.add_field(
                name=f"/{cmd.name}",
                value=cmd.description or "No description",
                inline=False
            )

    await interaction.response.send_message(embed=embed)
    
    

    






client.run(token) 