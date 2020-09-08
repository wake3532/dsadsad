import discord
import asyncio
from captcha.image import ImageCaptcha

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.id}')

@client.event
async def on_guild_join(guild):
    category=await guild.create_category(name="[홍보서버]")
    text = await category.create_text_channel(name="【:gear:】ㅣwasekay")
    embed = discord.Embed(title="WaseKay", description="봇이 요청 없는 서버에 봇이 초대되었습니다.",
    colour = discord.Colour.gold()
    )
    await text.send(embed=embed)

@client.event
async def on_message(message):
    if message.content == "!인증":
        Image_captcha = ImageCaptcha()
        msg = ""
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))

        name = "Captcha.png"
        Image_captcha.write(a, name)

        await message.channel.send(file=discord.File(name))
        embed = discord.Embed(title="어서오세요 여기는 wasekay입니다!", description = message.author.mention + ", 코드가 10초뒤 만료됩니다. 정확히 입력하십시오.", timestamp=message.created_at,
        colour=discord.Colour.blurple()
    )
        embed.set_footer(text="WELCOME TO SERVER LIST", icon_url="https://media.discordapp.net/attachments/731412060541288518/752696344384372816/unknown.png?width=783&height=612")
        await message.channel.send(embed=embed)

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            embed = discord.Embed(title="실패!", description = message.author.mention + ", __**수고하셨어요. 하지만 시간 **10초**가 지났어요 :( ", timestamp=message.created_at,
            colour=discord.Colour.orange()
    )
            embed.set_footer(text="welcome to wasekay", icon_url="https://media.discordapp.net/attachments/731412060541288518/752696344384372816/unknown.png?width=783&height=612")
            await message.channel.send(embed=embed)

        if msg.content == a:
            embed = discord.Embed(title="welcome", description = message.author.mention + ", __**Captcha**__인증코드가 정확합니다 여기는 wasekay입니다 !", timestamp=message.created_at,
            colour=discord.Colour.green()
    )
            embed.set_footer(text="축하드려요 !", icon_url="https://media.discordapp.net/attachments/731412060541288518/752696344384372816/unknown.png?width=783&height=612")
            await message.channel.send(embed=embed)
            role = discord.utils.get(message.author.guild.roles, name='유저')
            await message.author.add_roles(role)
        
        else:
            embed = discord.Embed(title="다시 도전 !", description = message.author.mention + ", __**Captcha**__ 수고하셨어요 하지만 코드가 정확하지 않네요 :(", timestamp=message.created_at,
            colour=discord.Colour.red()
    )
            embed.set_footer(text="welcome to wasekay", icon_url="https://media.discordapp.net/attachments/731412060541288518/752696344384372816/unknown.png?width=783&height=612")
            await message.channel.send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
