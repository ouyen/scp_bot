from nonebot import on_command, CommandSession


@on_command('help', aliases=('help', '帮助'),only_to_me=False)
async def _(session: CommandSession):
    with open('help.txt','r',encoding='utf-8') as f:
        message=f.read()
    await session.send(message)
