# To make a discord app you need to download discord.py with pip
#-*- coding: utf-8 -*-
import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.id}')

@client.event
async def on_guild_join(guild):
    category=await guild.create_category(name="[홍보서버]")
    text = await category.create_text_channel(name="【⚙】ㅣwasekay")
    embed = discord.Embed(title="WaseKay", description="다양한 장르의 서버를 찾고, 다른 유저와 놀아보세요! \n ※ 해당 채널에서 잡담은 자제해주세요. \n 서포트 서버에서 서버 신청을 하실 수 있습니다. [서포트 서버](https://discord.gg/QJyQZkM)",
    colour = discord.Colour.gold()
    )
    await text.send(embed=embed)

@client.event
async def on_message(message):
    if message.content == 'wa홍보방법':
        embed = discord.Embed(title="Wasekay 홍보방법!", description="Wasekay 홍보는 굉장히 쉬워요!\n\n먼저 봇을 초대해보세요!\nㄴ 서버가 인식되면 Wasekay 홍보가 자동으로 시작해요.\nㄴ채널 이동은 상관없지만, **홍보 메시지는 절대로 지우지 마세요!**\n\n채널이 생기면 자동으로 홍보를 해요!\nㄴ만약 누군가 당신의 홍보 채널에서 괴롭힌다구요? 바로 관리자를 불러보세요! 바로 달려올거에요!\n\n[봇 초대하기](https://discord.com/oauth2/authorize?client_id=746384600112038014&permissions=8&scope=bot)",
        colour = discord.Colour.purple()    
    )
        await message.channel.send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
