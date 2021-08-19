from nonebot import on_command, CommandSession

@on_command('fun', aliases=('你是谁'))
async def _(session: CommandSession):
    await session.send('我是一台烤面包机')