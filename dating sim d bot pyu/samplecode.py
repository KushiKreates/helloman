import discord
import os
from dotenv import load_dotenv
import json
from discord import option


global_variable = 0

load_dotenv()
intents = discord.Intents.default()
intents.typing = False

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

# Define the path for the JSON file
json_file_path = "user_data.json"

# Initialize the user_name variable with a default value
user_name = ""

import discord

class Myoiew(discord.ui.View):
    @discord.ui.button(label="Love me right?", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        # Create an embed
        embed = discord.Embed(
            title="Here's a Kiss!",
            description="You just got a kiss!",
            color=discord.Colour.blue()
        )
        embed.set_image(url="https://media.giphy.com/media/jR22gdcPiOLaE/giphy.gif")

        # Send the embed
        await interaction.response.send_message(embed=embed)

    @discord.ui.button(label="Not now, we are not in that stage!", row=1, style=discord.ButtonStyle.danger)
    async def second_button_callback(self, button, interaction):
        # Create a sad embed
        embed = discord.Embed(
            title="oKAY ;(",
            description="WARNING, YOUR GIRLFRIEND HAS GOT SAD!",
            color=discord.Colour.red()
        )
        embed.set_image(url="https://media.giphy.com/media/cxTOMfjEyMwNmu6de5/giphy.gif")

        # Send the sad embed
        await interaction.response.send_message(embed=embed)

@bot.slash_command(name='date', description='Your girlfriend')
@discord.option("name", description="Your girlfriend", required=False, default='')
async def date(ctx: discord.ApplicationContext, name: str):
    global global_variable
    global user_name
    
    # Load user data from the JSON file
    user_data = {}
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as json_file:
            user_data = json.load(json_file)

    author_id = str(ctx.author.id)
    
    if author_id in user_data:
        # User already has a girlfriend, get the girlfriend's name from the data
        chosen_name = user_data[author_id]['name']
        await ctx.respond(f"You already have a girlfriend: {chosen_name}.", view=Myoiew())
    else:
        # User hasn't chosen a girlfriend, allow the choice
        await ctx.respond(f"You chose: {name} to be your Girlfriend!", view=Myoiew())

        # Update the user data in the JSON file
        user_data[author_id] = {
            'name': name,
            'username': ctx.author.display_name,
            'coins': 100  # Initialize with 100 coins
        }
        with open(json_file_path, 'w') as json_file:
            json.dump(user_data, json_file)

        # Update the user_name variable
        user_name = name
def get_user_data():
    user_data = {}
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as json_file:
            user_data = json.load(json_file)
    return user_data

@bot.slash_command(name='stats', description='Display your stats, Lets find out more things!')
async def stats_command(ctx: discord.ApplicationContext):
    user_id = str(ctx.author.id)
    user_data = get_user_data()

    if user_id in user_data:
        # Retrieve the user's data from the JSON
        user_stats = user_data[user_id]

        # Create an embed to display the stats
        embed = discord.Embed(
            title="Your Stats",
            color=discord.Colour.blue()
        )
        embed.add_field(name="🌸Your Girlfriend🌸", value=user_stats['name'])
        embed.add_field(name="✅Your Username✅", value=user_stats['username'])
        embed.add_field(name="🪙Coins🪙", value=user_stats['coins'])
        embed.set_image(url="https://images-ext-2.discordapp.net/external/-yhjgE6vtmJRQSViNLWOMoneQ-G_G35H6FOfUpdXZ-Q/%3Fpid%3DImgDet%26rs%3D1/https/th.bing.com/th/id/OIP.74NCX_IHbwi7p6dNwnJ9YwHaEK")
        embed.set_footer(text="VNB or Visual novel Bot, By Nadhilaweb bots (Lumixo)")

        await ctx.respond("Here are your stats:", embed=embed)
    else:
        await ctx.respond("You need to start dating first. Use `/date` to start a date.")


bot.run(os.getenv('TOKEN'))
