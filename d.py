import discord
import asyncio
from captcha.image import ImageCaptcha

client = discord.Client()

owner = ['724769557759393837']
@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))
    
@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))
    while True:
        user = len(client.users)
        server = len(client.guilds)
        messages = ["제 접두사는 * 입니다!", "∑」FOR#1234님이 제작했어요!" , "TEAM MB" , str(user) + "분이 제 봇을 이용중입니다.", str(server) + "개의 서버에 있습니다."]
        for (m) in range(5):
            await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=messages[(m)], type=discord.ActivityType.watching))
            await asyncio.sleep(4)

@client.event
async def on_member_join(member):
    syschannel = member.guild.system_channel.id 
    try:
        embed=discord.Embed(
            title=f'welcome to wasekay !',
            description=f'{member}님{member.guild}에 오신것을 환영해요! !인증 이라고 말해보세요 \n현재 서버 인원수: {str(len(member.guild.members))}명',
            colour=0x00ff00
        )
        embed.set_thumbnail(url=member.avatar_url)
        await client.get_channel(syschannel).send(embed=embed)
    except:
        return None
@client.event
async def on_member_remove(member):
    syschannel = member.guild.system_channel.id 
    try:
        embed=discord.Embed(
            title=f'멤버 퇴장',
            description=f'{member}님이{member.guild}에 퇴장 했습니다.\n현재 서버 인원수: {str(len(member.guild.members))}명',
            colour=discord.Colour.red()
        )
        embed.set_thumbnail(url=member.avatar_url)
        await client.get_channel(syschannel).send(embed=embed)
    except:
        return None

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
