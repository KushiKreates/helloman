import asyncio
import json
import os
import random
from io import BytesIO
from threading import Thread
import os
import json
import discord


from io import BytesIO
from threading import Thread
import os
import json
import discord
from discord.ui import Button
import threading  
from pymongo import MongoClient
from discord.ext import tasks, commands

from flask import Flask, render_template, request, redirect, url_for, jsonify

import time


import os
import random
from discord.ext import commands
import discord


import discord
import requests
from discord.ext import tasks


from flask import Flask, jsonify, render_template
from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError
import motor.motor_asyncio

app = Flask(__name__)


def spin_wheel():
  prizes = ["Small Prize 1", "Small Prize 2", "Small Prize 3"]

  # Simulate spinning for a short duration
  time.sleep(3)

  # Return a random small prize
  return random.choice(prizes)

@app.route('/')
def hello_world():
  return 'Hello, World!!!'

def run_flask():
  app.run(host="0.0.0.0", port=5000)

global_variable = 0


intents = discord.Intents.default()
intents.typing = False

bot = discord.Bot(intents=intents)


ytdl_format_options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'extract_flat': True,
}

ffmpeg_options = {
    'options': '-vn',
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
}





######################################Commands embed list######################################################################

commands_info = [{
    'name': 'register',
    'description': 'Register yourself'
}, {
    'name': 'skin',
    'description': 'Show Minecraft skin for a user'
}, {
    'name': 'pika',
    'description': 'Get information about Top.pika.host'
}, {
    'name': 'hypixel',
    'description': 'Get information about Hypixel'
}, {
    'name': 'emote',
    'description': 'Send an emote'
}, {
    'name':
    'askforhelp',
    'description':
    'Get help with Our server, Other Minecraft issues!'
}, {
    'name': 'shop',
    'description': 'Visit the shop to buy cosmetic items'
}, {
    'name': 'buy',
    'description': 'Not open yet :('
}]


@bot.event
async def on_ready():
    print("Bot is ready!")
    update_status.start()


@tasks.loop(seconds=2)
async def update_status():
    game_names = ["Bedwars :D, With Kushi_k"]  # Add more game names as needed
    activities = [
        discord.Game(name=random.choice(game_names), type=3),
        discord.Activity(type=discord.ActivityType.watching, name="Badwars server"),
        discord.Activity(type=discord.ActivityType.watching, name="Do /help"),
        discord.Activity(type=discord.ActivityType.watching, name="/bedwarsstats"),
        discord.Activity(type=discord.ActivityType.watching, name="/pikastats"),
        discord.Activity(type=discord.ActivityType.watching, name="Made by Kushi_k")
    ]

    activity = random.choice(activities)
    statuses = [discord.Status.online, discord.Status.dnd, discord.Status.idle]

    for status in statuses:
       await bot.change_presence(status=status, activity=activity)
       await asyncio.sleep(1)

bot.event
async def on_ready():
    print("Bot Ready!")

    award_messages.start()
    change_category_name.start()

category_names = ['Talk here! 🔊🫵', 'Top tips here!', 'Bad admins!']


@tasks.loop(seconds=60)  # Change seconds to 60 for one minute
async def change_category_name():
  del user_data

@bot.event
async def on_member_join(member):
  # Create a welcome message image
  welcome_message = generate_welcome_message(member)

  # Send the welcome message as an embed
  embed = discord.Embed(title=f"Welcome to the server, {member.display_name}!",
                        color=discord.Color.green())
  file = discord.File(welcome_message, filename="welcome.png")
  embed.set_image(url="attachment://welcome.png")

  channel_id = 123456789012345678  # Replace with your channel ID
  channel = bot.get_channel(channel_id)

  await channel.send(embed=embed, file=file)


@tasks.loop(seconds=20000000)
async def hello_loop():
  channel_id = 1177332377538797679 # Replace with your channel ID
  channel = bot.get_channel(channel_id)

  if channel:
    await channel.send(
        "Hello! You are using Kushi_k's Bot! Enjoy using commands such as /register, /skin, /pika, /hypixel, /emote, and many more!"
    )
  await asyncio.sleep(2000000)

@tasks.loop(minutes=1)
async def award_messages():
    for guild in bot.guilds:
        for member in guild.members:
            # Fetch user data from MongoDB or create a new document if not exists
            user_data = collection.find_one({'user_id': str(member.id)}) or {'user_id': str(member.id), 'message_count': 0}

            # Increment message count
            user_data['message_count'] += 1

            # Save updated data to MongoDB
            collection.replace_one({'user_id': str(member.id)}, user_data, upsert=True)

            # Check for message milestones and send rewards
            if user_data['message_count'] % 100 == 0:
                await member.send(f'Congratulations! You have sent {user_data["message_count"]} messages. Claim your reward with the button.')





def generate_welcome_message(member):
  # Create a blank image
  image = Image.new("RGB", (600, 200), color=(255, 255, 255))
  draw = ImageDraw.Draw(image)

  # Load a font
  font_path = "arial.ttf"  # Replace with the path to your font file
  font = ImageFont.truetype(font_path, 30)

  # Draw the welcome message
  welcome_text = f"Welcome to the server, {member.display_name}!"
  draw.text((20, 70), welcome_text, fill=(0, 0, 0), font=font)

  # Save the image
  image.save("welcome.png")
  return "welcome.png"


# Define the path for the JSON file

mongo_uri = 'mongodb+srv://Nadhilaweb:Lapizcumpo@lumixo.w4iyuaj.mongodb.net/?retryWrites=true&w=majority'
db_name = 'Lumixo'
client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
# Initialize Firebase

# Create a reference to the root of the database
client = MongoClient(mongo_uri)
db = client[db_name]
collection = db['user_data']

json_file_path = 'stats.json'

 # Replace with your actual prefix


@bot.command(name='register', help='Register yourself')
async def register(ctx, password, minecraft_name):
    try:
        # Fetch the user's Discord ID
        user_id = str(ctx.author.id)

        # Check if the user is already registered
        with open(json_file_path, 'r') as json_file:
            user_data = json.load(json_file)

        if user_id in user_data:
            await ctx.send("You are already registered.")
        else:
            # Register the user
            user_data[user_id] = {
                'password': password,
                'minecraft_name': minecraft_name,
                'coins': 1000  # Give the user 1000 coins for the first time
            }

            with open(json_file_path, 'w') as json_file:
                json.dump(user_data, json_file, indent=2)
            del user_data

            await ctx.respond(f"You have been registered. A new user has been created for you with 1000 coins.")
    except Exception as e:
        # Handle exceptions
        print(e)
        await ctx.send("An error occurred while processing the command.")

@bot.slash_command(name='logout', help='Logout from your account')
async def logout(ctx):
    author_id = str(ctx.author.id)

    # Check if the user is registered
    if db.users.find_one({'_id': author_id}):
        # Delete user data
        db.users.delete_one({'_id': author_id})
        await ctx.send(f"You have been successfully logged out.")
    else:
        await ctx.send("You are not registered.")

@bot.slash_command(name='skin', description='Show Minecraft skin for a user')
@discord.option("username", description="Minecraft username", required=True)
async def skin(ctx: discord.ApplicationContext, username: str):
  mojang_api_url = f"https://api.mojang.com/users/profiles/minecraft/{username}"

  try:
    response = requests.get(mojang_api_url)
    response.raise_for_status()
    mojang_data = response.json()

    if 'id' in mojang_data:
      player_uuid = mojang_data['id']
      crafatar_url = f"https://crafatar.com/renders/body/{player_uuid}"

      # Download the skin texture from Crafatar
      skin_image = requests.get(crafatar_url)
      skin_image.raise_for_status()

      # Send the skin image to Discord
      await ctx.respond(
          f"Minecraft Skin for {username}:",
          files=[discord.File(BytesIO(skin_image.content), "skin.png")])
    else:
      await ctx.respond(f"User with the username {username} not found.")
  except requests.exceptions.RequestException as e:
    await ctx.respond(f"Error fetching skin: {e}")


@bot.slash_command(name='pika-infos',
                   description='Get information about Top.pika.host')
async def pika(ctx: discord.ApplicationContext):
  message = "Join now at Top.pika.host"
  await ctx.respond(message)


@bot.slash_command(name='welcome', description='Send a welcome message with a GIF')
async def welcome(ctx, user: discord.User):
    # Replace 'your_welcome_gif_url' with the actual URL of the GIF you want to use
    welcome_gif_url = 'https://tenor.com/bMCR5.gif'

    # Create an embed with a welcome message
    embed = discord.Embed(
        title=f'Welcome to the server, {user.name}!',
        description='We are glad to have you here!',
        color=discord.Color.green()
    )

    # Add an image to the embed (the GIF)
    embed.set_image(url=welcome_gif_url)

    # Send the welcome message with the embed
    await ctx.send(embed=embed)


@bot.slash_command(name='creator', description='Get information about who made the bot!')
async def hypixel(ctx: discord.ApplicationContext):
  message = "Your Using a bot made by Kushi_K <3 🥰 SLAY!"
  await ctx.respond(message)


@bot.slash_command(name='emote', description='Send an emote')
async def emote(ctx: discord.ApplicationContext):
  # Get the user who invoked the command
  user = ctx.author

  # List of image URLs
  image_urls = [
      "https://media.giphy.com/media/TOkOM7ywZC6OI/giphy.gif",
  ]

  # Embed configuration
  embed = discord.Embed(title=f"{user.display_name} Just Emoted!",
                        description="Check out these emotes:",
                        color=discord.Colour.gold())

  # Add each image URL to the embed
  for url in image_urls:
    embed.set_image(url=url)

  # Send the embed
  await ctx.respond(embed=embed)

  # Send the embed


@bot.slash_command(
    name='askforhelp',
    description='Get help with Our server, Other minecraft issues!')
async def ask_for_help(ctx: discord.ApplicationContext):
  # URL for help
  help_url = "http://nwebworks.rf.gd/hvbot.html"

  # Respond with the help URL
  await ctx.respond(f"Need help? Visit: {help_url}")


@bot.slash_command(name="helps", description="Display available commands")
async def help(ctx: discord.ApplicationContext):
  # Create an embed for displaying commands
  embed = discord.Embed(title="Command List",
                        description="Here are the available commands:",
                        color=discord.Color.blue())

  # Add fields for each command
  for command_info in commands_info:
    embed.add_field(name=f"/{command_info['name']}",
                    value=command_info['description'],
                    inline=False)

  await ctx.send(embed=embed)


@bot.slash_command(name='serverstatus', help='Check the server status')
async def server_status(ctx, server_address):
  api_url = f'https://api.mcsrvstat.us/3/{server_address}'
  response = requests.get(api_url)
  server_data = response.json()

  if server_data.get('online', False):
    embed = discord.Embed(title=f"Server Status for {server_address}",
                          color=discord.Color.green())
    embed.add_field(name="Status", value="Online", inline=False)
    embed.add_field(name="IP",
                    value=server_data.get('ip', 'Not available'),
                    inline=False)
    embed.add_field(name="Port",
                    value=server_data.get('port', 'Not available'),
                    inline=False)
    embed.add_field(name="Version",
                    value=server_data.get('version', 'Not available'),
                    inline=False)
    embed.add_field(
        name="Players",
        value=
        f"{server_data['players']['online']}/{server_data['players']['max']}",
        inline=False)
  else:
    embed = discord.Embed(title=f"Server Status for {server_address}",
                          color=discord.Color.red())
    embed.add_field(name="Status", value="Offline", inline=False)
    embed.add_field(name="IP",
                    value=server_data.get('ip', 'Not available'),
                    inline=False)
    embed.add_field(name="Port",
                    value=server_data.get('port', 'Not available'),
                    inline=False)

  await ctx.send(embed=embed)


@bot.slash_command(name="meme", description="Make a Roll Safe meme!")
async def meme(ctx, text_input: str):
  meme_api_url = f"https://api.memegen.link/images/rollsafe/{text_input}.webp?layout=top"

  embed = discord.Embed(
      title="Roll Safe Meme has been sent as a link!, open it",
      color=discord.Color.blue())

  await ctx.send(embed=embed)
  await ctx.respond(meme_api_url)


@bot.slash_command(name='config', help='Configure the Bot simply!')
async def configure_loop_channel(ctx):
  global loop_channel_id
  loop_channel_id = ctx.channel.id
  await ctx.send(f"Loop channel configured to {ctx.channel.mention}")



# Add more commands and event handlers as needed


# Run the bot


class MyView(discord.ui.View):
    def __init__(self, username, pika_data):
        super().__init__()

        self.username = username
        self.pika_data = pika_data
        self.page_number = 0

    @discord.ui.button(label="General Stats", style=discord.ButtonStyle.primary)
    async def general_stats_button(self, button, interaction):
        self.page_number = 0
        await self.update_embed(interaction)

    @discord.ui.button(label="Clan Info", style=discord.ButtonStyle.primary)
    async def clan_info_button(self, button, interaction):
        self.page_number = 1
        await self.update_embed(interaction)

    async def update_embed(self, interaction):
        embed = discord.Embed(title="Pika Network Stats", color=discord.Color.blurple())

        if self.page_number == 0:
            embed.add_field(name="Username", value=self.username)
            embed.add_field(name="Rank Level", value=self.pika_data.get("rank", {}).get("level", "N/A"))

            # Generate skin render URL
            skin_render_url = f"https://starlightskins.lunareclipse.studio/skin-render/ultimate/{self.username}/full"

            try:
                # Fetch the skin image from the URL
                skin_image_response = requests.get(skin_render_url)
                skin_image_response.raise_for_status()

                # Load the skin image and add it to the embed
                skin_image = Image.open(BytesIO(skin_image_response.content)).convert("RGBA")
                skin_image_path = f"skin_{self.username}.png"
                skin_image.save(skin_image_path, format="PNG")

                with open(skin_image_path, 'rb') as skin_file:
                    embed.set_image(url=f"attachment://skin_{self.username}.png")
                    await interaction.response.send_message(file=discord.File(skin_file, f"skin_{self.username}.png"), embed=embed, view=self)
            except requests.exceptions.HTTPError:
                # Ignore errors when fetching skin
                pass
            except UnidentifiedImageError:
                # Handle UnidentifiedImageError (cannot identify image file)
                pass

        elif self.page_number == 1:
            clan_data = self.pika_data.get('clan', {})
            if clan_data:
                embed.add_field(name="Clan Name", value=clan_data.get('name', 'N/A'))
                embed.add_field(name="Clan Role", value=clan_data.get('role', 'N/A'))
            else:
                embed.add_field(name="Clan Information", value="Not available")

        if interaction.message:
            await interaction.message.edit(content=None, embed=embed, view=self)
            a
        else:
            await interaction.response.send_message(embed=embed, view=self)

@bot.slash_command(name='pikastat', description='Pika-network stats')
async def pikastats(ctx, username: str):
    try:
        # Fetch player information from Pika stats API
        pika_stats_url = f"https://stats.pika-network.net/api/profile/{username}"
        pika_stats_response = requests.get(pika_stats_url)
        pika_stats_response.raise_for_status()
        pika_data = pika_stats_response.json()

        # Create a view with buttons and send the initial embed
        view = MyView(username, pika_data)
        await view.update_embed(ctx)

    except discord.errors.NotFound as not_found_error:
        # Handle the specific NotFound exception
        await ctx.respond("Error: The interaction is not found. Please try the command again.")

    except requests.exceptions.HTTPError as http_error:
        # Handle HTTP errors
        if http_error.response.status_code == 400:
            await ctx.respond("Error: The player is not registered in the PikaNetwork database. Please recheck the details.", ephemeral=True)
        elif http_error.response.status_code == 404:
            await ctx.respond("Error: There was a mistake in the link. Please recheck the details.", ephemeral=True)
        else:
            await ctx.respond(f"An error occurred: {http_error.response.status_code}", ephemeral=True)

    

class BedwarsStatsView(discord.ui.View):

    def __init__(self, username):
        super().__init__()
        self.username = username
        self.skin_render_url = f"https://starlightskins.lunareclipse.studio/skin-render/ultimate/{self.username}/full"

    @discord.ui.button(label="Solo", style=discord.ButtonStyle.primary)
    async def solos_button_callback(self, button, interaction):
        await self.send_stats("SOLO", interaction)

    @discord.ui.button(label="Doubles", style=discord.ButtonStyle.primary)
    async def doubles_button_callback(self, button, interaction):
        await self.send_stats("DOUBLES", interaction)

    @discord.ui.button(label="Quads", style=discord.ButtonStyle.primary)
    async def quads_button_callback(self, button, interaction):
        await self.send_stats("QUAD", interaction)

    async def send_stats(self, mode, interaction):
        try:
            pika_stats_url = f"https://stats.pika-network.net/api/profile/{self.username}/leaderboard?type=bedwars&interval=yearly&mode={mode}"
            pika_stats_response = requests.get(pika_stats_url)

            if pika_stats_response.status_code == 200:
                pika_data = pika_stats_response.json()

                embed = discord.Embed(title=f"Pika-network Bed Wars Stats - {self.username}", color=discord.Color.blurple())
                embed.set_thumbnail(url=self.skin_render_url)  # Set the player's skin as the thumbnail

                for stat_name, stat_data in pika_data.items():
                    if stat_data and 'entries' in stat_data and stat_data['entries']:
                        stat_value = stat_data['entries'][0].get('value', 'N/A')
                        embed.add_field(name=stat_name, value=stat_value, inline=True)

                # Edit the original message with the updated embed
                await interaction.response.edit_message(embed=embed, view=self)
                
            else:
                await interaction.response.send_message("Failed to fetch Bed Wars stats. Please try again later.", ephemeral=True)
        except Exception as e:
            print(e)
            await interaction.response.send_message("An error occurred while processing the command.", ephemeral=True)

@bot.command(name='bedwarsstats', description='Pika-network Bed Wars stats')
async def bedwars_stats(ctx, username: str):
    
        # Creating an instance of the view with the username
        view = BedwarsStatsView(username)
        loading_embed = discord.Embed(title="Select mode please", color=0x3498db)

        # Send the initial message with the view
        await ctx.respond("Choose Bed Wars mode:", view=view)
        
        
    
        




@bot.command(name='notifys', help='Notify server members about a tournament')
async def notify(ctx, date):
    # Get the server members
    server_members = ctx.guild.members

    # Create the tournament message with the entered date
    tournament_message = (
        "# 🚀 **Attention Squaddies! 🎮✨**\n\n"
        f"Yo, what's poppin', gamers! It's your main squeeze, {ctx.author.mention}, here to drop a bomb announcement! 🕹️💣\n\n"
        "## 🏆 **Get Hyped for the Ultimate Throwdown!** 🏆\n\n"
        "We're cooking up a tourney hotter than your KD ratio, and YOU are invited! If you're down to flex your gaming skills, hit us up with a vibe check in the replies! 🚀🔥\n\n"
        "**Prizes? Oh, you bet!** 🤑\n"
        "- Like, I'm broke, but we're making it rain with mystery goodies! 🌧️💰\n\n"
        "**Game Plan:**\n"
        "- Solo, doubles, quads – we're serving it all up. It's a Bedwars buffet, baby! 🛌🍽️\n\n"
        "**Grading Criteria:**\n"
        "- Most finals, most beds obliterated, most wins – if you're not aiming for the stars, you're doing it wrong. 🌟🛏️💔\n\n"
        "**FKDR? We're getting mathematical, fam!** 🔢\n\n"
        "**Spread the Word:**\n"
        "- Tell your squad, tell your grandma, tell your cat – it's gonna be lit! 🗣️👵🐱\n\n"
        f"**Save the Date:** {date} - Mark it in your swag calendar! 📆🔥\n\n"
        "Let's make this tourney the talk of the town! RSVP below if you're ready to slay, fam! 💪🎮\n\n"
        f"# Date to Remember: {date} – The Day We Make Gaming History! 🌐💫"
    )

    # Send private messages to all server members
    for member in server_members:
        try:
            await member.send(tournament_message)
        except discord.Forbidden:
            # Handle cases where the bot is not allowed to send a private message
            print(f"Cannot send a message to {member.display_name} ({member.id})")
        except Exception as e:
            # Handle other exceptions
            print(f"An error occurred while sending a message to {member.display_name} ({member.id}): {e}")

    await ctx.send("Tournament notification sent to all server members!")


class ToyCommandsView(discord.ui.View):
    def __init__(self, target_user):
        super().__init__()
        self.target_user = target_user

    async def send_action_message(self, action_name, gif_url, interaction, additional_message=""):
        embed = discord.Embed(description=f"{self.target_user.mention} {action_name} by {interaction.user.mention} {additional_message}", color=discord.Color.blurple())
        embed.set_image(url=gif_url)

        await interaction.response.send_message(embed=embed, view=self)

    @discord.ui.button(label="Kidnap", style=discord.ButtonStyle.primary, custom_id="kidnap_button")
    async def kidnap_button_callback(self, button, interaction):
        gif_url = "https://media.giphy.com/media/ViIh8qu8Y08swHV7dX/giphy.gif"
        await self.send_action_message("was kidnapped", gif_url, interaction)

    @discord.ui.button(label="Kill", style=discord.ButtonStyle.danger, custom_id="kill_button")
    async def kill_button_callback(self, button, interaction):
        gif_url = "https://media.giphy.com/media/37WzogMvUjAaiRXtMA/giphy.gif"
        await self.send_action_message("was killed", gif_url, interaction)

@bot.command(name='toy', description='Interact with a user using various actions')
async def toy(ctx, user: discord.User):
    try:
        # Creating an instance of the view with the target user
        view = ToyCommandsView(user)

        # Send the message with the view
        await ctx.send(f"Choose an action for {user.mention}:", view=view)
    except Exception as e:
        # Handle exceptions
        print(e)
        await ctx.send("An error occurred while processing the command.")







@bot.command(name='les', help='Ls ur friends Costs 50 coins!')
async def call_loser(ctx, another_person: discord.User):
    try:
        # Fetch the caller's user ID
        caller_user_id = str(ctx.author.id)

        # Fetch the user's data
        with open(json_file_path, 'r') as json_file:
            user_data = json.load(json_file)

        # Get the caller's data
        caller_data = user_data.get(caller_user_id, {})

        if not caller_data:
            await ctx.send("You are not registered. Please use /register to register yourself.")
            return

        # Check if the user has enough coins
        if caller_data.get('coins', 0) < 50:
            await ctx.respond("You don't have enough coins to use this command.")
            return

        # Deduct 50 coins
        caller_data['coins'] -= 50

        # Save the updated user data
        with open(json_file_path, 'w') as json_file:
            json.dump(user_data, json_file, indent=2)


        # Randomly choose a message
        messages = [
            f"## {ctx.author.mention} Just led that kid called {another_person.mention}",
            f"## {ctx.author.mention} Just beat that child called {another_person.mention}",
            f"## Today on news 📺 {another_person.mention}'s dad has gone to buy the milk. This news broadcast is delivered to you by {ctx.author.mention}",
            f"## {another_person.mention} Just found out that he can't live, So {ctx.author.mention} helped him out!, to kill himself ",
            f"## {ctx.author.mention} Are you going mad? Ask the handsome warrior called {ctx.author.mention}"
        ]

        # Choose a message with a higher chance for the first two
        weights = [0.15, 0.15, 0.05, 0.15, 0.15]
        chosen_message = random.choices(messages, weights=weights)[0]

        # Send the message
        await ctx.respond(chosen_message)

    except Exception as e:
        # Handle exceptions
        print(e)
        await ctx.send("An error occurred while processing the command.")



@bot.command(name='modmsg', help='Send a custom message to a user')
async def modmsg(ctx, target_user: discord.User, *, message):
    await target_user.send(message)
    await ctx.respond(f'Message sent to {target_user.mention}')


@bot.command(name='curseme', help='Get cursed memes from meme-api.com')
async def curseme(ctx):
    # Fetch JSON data from the API
    response = requests.get('https://meme-api.com/gimme/memes').json()

    if 'preview' in response:
        preview_images = response['preview']
        last_preview = preview_images[-1]

        embed = discord.Embed(title=response['title'], url=response['postLink'])
        embed.set_author(name=response['author'])
        embed.set_image(url=last_preview)

        await ctx.respond(embed=embed)
    else:
        await ctx.send("No preview images found.")

@bot.command(name='transmemes', help='Send an embed with a link to a YouTube video')
async def transmeme(ctx):
    file_path = 'send.mp4'

    # Send the file
    await ctx.respond(file=discord.File(file_path))

@bot.command(name='warn', help='Warn a user about their behavior')
async def warn(ctx, user: discord.User, *, reason=None):
    # Check if the command sender has the necessary permissions
    if ctx.author.guild_permissions.kick_members:
        # Send a warning message to the specified user
        await user.send(f'You have been warned in {ctx.guild.name} for the following reason: {reason or "No reason specified."}')
        await ctx.send(f'{user.mention} has been warned by {ctx.author.mention} for: {reason or "No reason specified."}', ephemeral=True)
    else:
        await ctx.respond("You don't have the necessary permissions to use this command.", ephemeral=True)

@bot.command(name='claim', help='Claim your message reward')
async def claim_reward(ctx):
    # Fetch user data from MongoDB
    user_data = collection.find_one({'user_id': str(ctx.author.id)})

    if user_data and user_data['message_count'] % 100 == 0:
        # Send reward in DM
        await ctx.author.send('Congratulations! You have claimed your message reward.', ephemeral=True)
    else:
        await ctx.send(f'{ctx.author.mention}, your reward is waiting! Open your DMs.', ephemeral=True)

owner_ids = [745271907754180678, 876543210987654321]

@bot.command(name='nuke', help='Nuke the channel (Owners only)')
async def nuke_channel(ctx):
      # Check if the command user is an owner
      if ctx.author.id not in owner_ids:
          return await ctx.respond('You do not have permission to use this command.', ephemeral=True)

      # Create a new channel with the same name as the original channel
      new_channel = await ctx.channel.clone()

      # Delete the original channel
      await ctx.channel.delete()

      # Send a message to the new channel
      await new_channel.send('This channel has been nuked!')
@bot.command(name='bye', help='Say goodbye to a user. Costs 100 coins!')
async def say_goodbye(ctx, target_user: discord.User):
    try:
        # Fetch the caller's user ID
        caller_user_id = str(ctx.author.id)

        # Fetch the user's data
        with open(json_file_path, 'r') as json_file:
            user_data = json.load(json_file)


        # Get the caller's data
        caller_data = user_data.get(caller_user_id, {})

        if not caller_data:
            await ctx.send("You are not registered. Please use /register to register yourself.")
            return

        # Check if the user has enough coins
        if caller_data.get('coins', 0) < 100:
            await ctx.respond("You don't have enough coins to use this command.")
            return

        # Deduct 100 coins
        caller_data['coins'] -= 100

        # Save the updated user data
        with open(json_file_path, 'w') as json_file:
            json.dump(user_data, json_file, indent=2)

        # Randomly choose a goodbye message
        goodbye_messages = [
            f"## {target_user.mention} Sit tight and relax for a while until we meet back again.",
            f"## Farewell, {target_user.mention}! May our paths cross again in the future.",
            f"## Goodbye, {target_user.mention}! Take care on your journey.",
            f"## See you later, {target_user.mention}! Until our next encounter.",
            f"## Adieu, {target_user.mention}! Wishing you the best until we meet again."
        ]

        # Choose a message with equal chance
        chosen_goodbye_message = random.choice(goodbye_messages)

        # Send the message
        await ctx.respond(chosen_goodbye_message)


    except Exception as e:
        # Handle exceptions
        print(e)
        await ctx.send("An error occurred while processing the command.")
@bot.command(name='coin', help='Check your coin balance.')
async def check_coins(ctx):
    try:
        # Fetch the caller's user ID
        caller_user_id = str(ctx.author.id)

        # Fetch the user's data
        with open(json_file_path, 'r') as json_file:
            user_data = json.load(json_file)


        # Get the caller's data
        caller_data = user_data.get(caller_user_id, {})

        if not caller_data:
            await ctx.send("You are not registered. Please use /register to register yourself.", ephemeral=True)
            return

        # Check if the user has enough coins
        coins = caller_data.get('coins', 0)

        # Display the user's coin balance
        await ctx.respond(f"### You currently have {coins} coins.🪙")

        # Check if the user has over 10,000 coins
        if coins > 10000:
            # Get the "Hella rich" role or create it if it doesn't exist
            hella_rich_role = discord.utils.get(ctx.guild.roles, name="Hella rich")

            if not hella_rich_role:
                # Create the role with gold color
                hella_rich_role = await ctx.guild.create_role(name="Hella rich", color=discord.Color.gold())

            # Add the role to the user
            await ctx.author.add_roles(hella_rich_role)
            await ctx.respond(f"Congratulations! You are now a member of the exclusive 'Hella rich' club!", ephemeral=True)


    except Exception as e:
        # Handle exceptions
        print(e)
        await ctx.send("An error occurred while processing the command.")
@bot.command(name='dox', help='Fake Dox a person')
async def show_options(ctx, user: discord.User):
    # Construct the text message
    text_message = f"# {user.mention} here are your results"

    # Send the text message to the channel
    await ctx.send(text_message)

    file_path1 = 'send1.mp4'
    await ctx.respond(file=discord.File(file_path1))

import time
import requests
from discord.ext import commands

API_KEY = 'AIzaSyBLRvuu6vFZ2VsWTEjjelvZ7lTD8abdVL0'

def generate_gemini_content(prompt):
    url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'
    headers = {'Content-Type': 'application/json'}
    params = {'key': API_KEY}

    my_additional_text = "Make the response thinking Your a ai called Zumi developed by Kushi_k "
    modified_prompt = my_additional_text + prompt

    data = {
        'contents': [{
            'parts': [{
                'text': modified_prompt
            }]
        }]
    }
    response = requests.post(url, headers=headers, params=params, json=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        response_data = response.json()

        # Check if 'candidates' is present in the response
        if 'candidates' in response_data and response_data['candidates']:
            # Extracting the generated content
            generated_text = response_data['candidates'][0]['content']['parts'][0]['text']

            # Truncate to 1999 characters if it exceeds the limit
            generated_text = generated_text[:1999]

            return generated_text
        else:
            raise Exception('Unexpected response format from Gemini API')
    else:
        raise Exception(f'Error in Gemini API request. Status code: {response.status_code}')

@bot.command(name='ai', description='Generate content using Gemini AI')
async def ai_command(ctx, *, prompt):
    try:
        # Create a loading embed
        loading_embed = discord.Embed(title="Zumi is thinking 🤔", color=0x3498db)
        await ctx.respond(content="Welcome to Zumi bot Ai, Let zumi take the back!, You can handle the front", ephemeral=True)
        msg = await ctx.send(embed=loading_embed)

        # Introduce a delay (adjust the sleep time as needed)
        await asyncio.sleep(5)  # 5 seconds delay (for example)

        # Generate content
        generated_text = generate_gemini_content(prompt)

        # Send the generated content as a new message
        result_embed = discord.Embed(title="Zumi's response 🤖🔊™️", color=0x2ecc71, description=f"```\n{generated_text}\n```")
        

        # Delete the loading message
        await msg.edit(embed=result_embed)

    except Exception as e:
        # Handle exceptions
        print(e)
        await ctx.send("An error occurred while processing the command.")


flask_thread = threading.Thread(target=run_flask)
flask_thread.start()
bot.run("MTE5Mzg2NDMyODc5ODAxMTM5Mg.Gtz8Gu.lVjFFBAna5c3fHfpR3jA-Clw51qgRZBQDQCkws")



