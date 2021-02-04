import discord
import asyncio, openpyxl
import time
import datetime
import os
#모듈값 불러오기

from discord.ext import commands
from discord.utils import get

client = discord.Client()

command_prefix="."  # 명령어 접두사


@client.event
async def on_ready():
    print("")
    print("")
    print(" ======================================================================= ")
    print("")
    print(" System : 봇 실행중..... ")
    print("")
    print(" ======================================================================= ")
    await client.change_presence(activity=discord.Game(".도움"), status=discord.Status.online)
    print("")
    print(" System : 상태 표시 완료! ")
    print("")
    print(" System : 성공적으로 봇이 시작되었습니다. ")
    print("")
    print(" ======================================================================= ")
    print("")
    print(" System : 디스코드 봇 로그인이 완료되었습니다.")
    print("")
    print(" System : 디스코드봇 이름 : " + client.user.name)
    print("")
    print(" System : 디스코드봇 ID : " + str(client.user.id))
    print("")
    print(" System : 디스코드봇 버전 : " + str(discord.__version__))
    print("")
    print(" ======================================================================= ")
    print("")
    print("")

@client.event
async def on_message(message):
    if message.content.startswith(f'{command_prefix}자기소개'):
        await message.channel.send("안녕! 나는 얄룽님이 개발해주신! 포인트봇(V3)야! 반가워~ 채팅창에 **`.도움`** 를 쳐봐!")

    #명령어 도움말 페이지 임베드
    if message.content.startswith(f'{command_prefix}도움'):
        embed = discord.Embed(title="도움말", description="**이 봇은 `LeeSin#5693 - 얄룽` 님에 의해 개발 되었습니다.**", color=0xffffff)
        embed.add_field(name="**도움**", value="**이 메시지를 보여줍니다.**", inline=False)
        embed.add_field(name="**정보**", value="**`각자의 정보를 보여줍니다.`**", inline=False)
        embed.add_field(name="**서버 초대하기**", value="**[클릭!](https://discord.com/invite/D7chQKTxTA)**", inline=False)
        embed.add_field(name="**포인트봇(V3) 초대하기**",value="**[바로가기](https://discord.com/api/oauth2/authorize?client_id=805064278469115905&permissions=8&scope=bot)**", inline=False)
        embed.add_field(name='**참고**', value='**포인트봇(V3) Ver 3.0\n명령어: `.`**', inline=False)
        embed.set_author(name="포인트봇(V3) 도움말",icon_url="https://i.imgur.com/uLDnDU3.png")
        embed.set_thumbnail(url="https://i.imgur.com/uLDnDU3.png")
        await message.channel.send(embed=embed)

    #관리자 전용 명령어 도움말 페이지 임베드
    if message.content.startswith(f'{command_prefix}어드민'):
        embed = discord.Embed(title="(운영위원회 전용) 도움말", description="**이 봇은 `LeeSin#5693 - 얄룽` 님에 의해 개발 되었습니다.**", color=0xffffff)
        embed.add_field(name="**킥**", value="**`서버에서 해당 유저를 킥합니다.`**", inline=False)
        embed.add_field(name="**청소**", value="**`청소 (갯수)만큼 채팅이 삭제됩니다.`**", inline=False)
        embed.add_field(name="**뮤트**", value="**`뮤트 (userid)를 입력할 경우, 해당 유저는 뮤트 됩니다.`**", inline=False)
        embed.add_field(name="**뮤트해제**", value="**`뮤트해제 (userid) 를 입력할 경우, (userid)는 뮤트 해제 됩니다.`**", inline=False)
        embed.add_field(name="**정보**", value="**`각자의 정보를 보여줍니다.`**", inline=False)
        embed.add_field(name="**---> **", value="**`정보(가입일, 이름, 아이디, 닉네임, 온(오프)라인상태)를 보여줍니다.`**", inline=False)
        embed.add_field(name="**---> **", value="**[자리비움,다른용무중은 오프라인으로 인식됩니다.]**")
        embed.add_field(name="**서버정보**", value="**`서버의 정보를 보여줍니다.`**", inline=False)
        embed.add_field(name="**유저정보**", value="**`서버 내의 유저정보를 보여줍니다.`**", inline=False)
        embed.add_field(name="**업타임(개발중)**", value="**`어머나 개발중이넹?`**", inline=False)
        embed.add_field(name="**벤(개발중)**", value="**`어머나 개발중이넹?`**", inline=False)
        embed.add_field(name="**경고(개발중)**", value="**`어머나 개발중이넹?`**", inline=False)
        embed.add_field(name="**서버 초대링크**", value="**[클릭!](https://discord.com/invite/D7chQKTxTA)**", inline=False)
        embed.add_field(name="**포인트봇(V3) 초대하기**",value="**[바로가기](https://discord.com/api/oauth2/authorize?client_id=805064278469115905&permissions=8&scope=bot)**", inline=False)
        embed.add_field(name='**참고**', value='**포인트봇(V3) Ver 3.0\n명령어: `.`**', inline=False)
        embed.set_author(name="포인트봇(V3) 도움말",icon_url="https://i.imgur.com/uLDnDU3.png")
        embed.set_thumbnail(url="https://i.imgur.com/uLDnDU3.png")
        await message.channel.send(embed=embed)

    #킥 명령어 구문
    if(message.content.split(" ")[0] == f'{command_prefix}킥'):
        if(message.author.guild_permissions.kick_members):
            try:
                user=message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                reason=message.content[25:]
                if(len(message.content.split(" ")) == 10):
                    reason="None"
                await user.send(embed=discord.Embed(title="킥", description=f'당신은 {message.guild.name} 서버에서 킥당했습니다. 사유는 다음과 같습니다. ```{reason}```', color=0xff0000))
                await user.kick(reason=reason)
                await message.channel.send(embed=discord.Embed(title="✅ 킥 성공!", description=f"{message.author.mention} 님은 해당 서버에서 킥당하셨습니다. 사유:```{reason}```", color=0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="🛑 (킥)처리 도중 에러 발생", description=str(e), color=0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="💢 권한 부족", description=message.author.mention + "님은 유저를 킥할 수 있는 권한이 없습니다.", color=0xff0000))
            return

    #뮤트 명령어 구문
    if(message.content.split(" ")[0] == f'{command_prefix}뮤트'):
        if(message.author.guild_permissions.manage_channels):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                await message.guild.get_channel(message.channel.category_id).set_permissions(user, send_messages=False)
                await message.channel.send(embed=discord.Embed(title="✅ 뮤트 성공!", color=0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="🛑 (뮤트)처리 도중 에러 발생", description=str(e), color=0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="💢 권한 부족", description=message.author.mention + "님은 채널을 관리 할 수 있는 권한이 없습니다.", color=0xff0000))
            return

    #뮤트해제 명령어 구문
    if(message.content.split(" ")[0] == f'{command_prefix}뮤트해제'):
        if(message.author.guild_permissions.manage_channels):
            try:
                user = message.guild.get_member(
                    int(message.content.split(' ')[1][3:21]))
                await message.guild.get_channel(message.channel.category_id).set_permissions(user, overwrite=None)
                await message.channel.send(embed=discord.Embed(title="✅ 뮤트해제 성공!", color=0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="🛑 (뮤트해제)처리 도중 에러 발생", description=str(e), color=0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="💢 권한 부족", description=message.author.mention + "님은 채널을 관리 할 수 있는 권한이 없습니다.", color=0xff0000))
            return
    #청소 명령어 구문
    if message.content.startswith(f'{command_prefix}청소'):
        num = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=num)
        await message.channel.send(f"✅ {num}개의 메시지를 정상적으로 삭제 완료!")

    #정보 명령어 구문
    if message.content.startswith(f'{command_prefix}정보'):
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention} 의 디스코드 가입일 : {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention} 의 이름 / 아이디 / 닉네임: {user.name} / {user.id} / {user.display_name}")
        await message.channel.send(user.status) #온라인, 오프라인
        #await message.channel.send(message.author.avatar)

    if message.content.startswith(f'{command_prefix}서버정보'):
        await message.channel.send(len(message.guild.members))

    if message.content.startswith(f'{command_prefix}유저정보'):
        await message.channel.send(message.author.status)


    #업타임 명령어 구문
    if message.content.startswith(f'{command_prefix}업타임'):
        uptime = str(uptime.uptime()).split(":")
        hours = uptime[0]
        minitues = uptime[1]
        seconds = uptime[2].split(".")[0]
        await message.channel.send(f"| {hours}시간 {minitues}분 {seconds}초 | 동안 작동되었어요!")



client.run("ODA1MDY0Mjc4NDY5MTE1OTA1.YBVciQ.varrK4j1Mh6eaHV6TY7TsGnTfCs")
