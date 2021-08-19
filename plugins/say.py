from nonebot import on_command,CommandSession

@on_command('say',aliases=('say'),only_to_me=False)
async def _(session:CommandSession):
    receive=session.current_arg
    await session.send(receive)