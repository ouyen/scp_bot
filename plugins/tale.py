from config import SCP_DOMAIN, SCP_DOMAIN_INDEX
from nonebot import on_command, CommandSession
from requests import get
from re import search
from lib import get_page_title

@on_command('wd', aliases=('故事','gs','tale','Tale'),only_to_me=False)
async def wd(session: CommandSession):
    received = session.current_arg
    message = await get_details(received)
    await session.send(message)

async def get_details(received: str) -> str:
    if received=='insurrection':
        mes='http://scp-wiki-cn.wikidot.com/insurrection\n不过鸢娓Iris提供了更为精彩的译文：\nhttps://www.bilibili.com/read/cv5317774'
        return mes
    elif received=='':
        return f'内容不能为空'
    else:
        a=received.split(' ')
        realurl='http://scp-wiki-cn.wikidot.com/'+'-'.join(a)
        title = get_page_title(realurl)
            
        return title+':\n'+SCP_DOMAIN[SCP_DOMAIN_INDEX]+'-'.join(a)
