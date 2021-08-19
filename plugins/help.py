from config import HELP_MESSAGE
from nonebot import on_command, CommandSession


@on_command('help', aliases=('help', '帮助'),only_to_me=False)
async def _(session: CommandSession):
    await session.send(HELP_MESSAGE)
