# To make a discord app you need to download discord.py with pip
#-- coding: utf-8 --
import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.id}')

@client.event
async def on_guild_join(guild):
    category=await guild.create_category(name="[홍보서버]")
    text = await category.create_text_channel(name="【:gear:】ㅣwasekay")
    embed = discord.Embed(title="WaseKay", description="워스키는 봇 초대 형식 홍보하는곳입니다 ! \n ※ 이 모든걸 4학년이 제작했어요 !  \n 사이트 워스키.홈페이지.한국 들어가는 사이트 : WASEKAY.KRO.KR 또는 들어가기로 들어와보세요! [서포트 서버](https://discord.gg/QJyQZkM)",
    colour = discord.Colour.gold()
    )
    await text.send(embed=embed)

@client.event
async def on_message(message):
    if message.content == 'wa홍보방법':
        embed = discord.Embed(title="Wasekay 홍보방법!", description="Wasekay 홍보는 굉장히 쉬워요!\n\n먼저 봇을 초대해보세요!\nㄴ 서버가 인식되면 Wasekay 홍보가 자동으로 시작해요.\nㄴ채널 이동은 상관없지만, 홍보 메시지는 절대로 지우지 마세요!\n\n채널이 생기면 자동으로 홍보를 해요!\nㄴ만약 누군가 당신의 홍보 채널에서 괴롭힌다구요? 바로 관리자를 불러보세요! 바로 달려올거에요!\n\n[봇 초대하기](https://discord.com/oauth2/authorize?client_id=746384600112038014&permissions=8&scope=bot)",
        colour = discord.Colour.purple()
    )
        await message.channel.send(embed=embed)

    if message.content == '&서버신청':
        servername = message.guild.name
        serverid = message.guild.id
        print(f'{servername} - {serverid}')

    if message.content == '&서버등록':
        guild = client.get_guild(742180737910046830)
        servername = message.guild.name
        category = discord.utils.get(message.guild.categories, id=(752061799217758219))
        text = await guild.create_text_channel(name=f"【:gear:】ㅣ{servername}", category=category)
        invite = await message.channel.create_invite(reason="Wasekay 서버등록에 의해 자동으로 생성된 초대링크입니다.")
        await text.send(invite)

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
