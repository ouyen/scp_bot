from config import SCP_DOMAIN, SCP_DOMAIN_INDEX
from nonebot import on_command, CommandSession
from requests import get
from random import random
from re import search
from lib import get_scp_name,get_page_title


@on_command('random', aliases=('randomscp', 'random', '随机'), only_to_me=False)
async def rand(session: CommandSession):
    try:
        tag = session.current_arg
    except:
        await session.send('error')
    scplist = ['scp', 'SCP', '']
    talelist = ['故事', 'gs', 'tale', 'Tale']
    if tag in scplist:
        judge = random()
        if judge < 0.25:
            url = 'http://scp-wiki-cn.wikidot.com/random:random-scp-cn'
        else:
            url = 'http://scp-wiki-cn.wikidot.com/random:random-scp'
    elif tag in talelist:
        judge = random()
        if judge < 0.25:
            url = 'http://scp-wiki-cn.wikidot.com/random:random-tale-cn'
        else:
            url = 'http://scp-wiki-cn.wikidot.com/random:random-tale'
    try:
        r = get(url, timeout=20)
        r.raise_for_status()
        r.encoding = 'utf-8'
    except:
        await session.send('error')
    temp = search(
        r'<p><iframe src="https://snippets.wdfiles.com/local--code/code:iframe-redirect#.+?"', r.text).group(0)
    # realurl=search(r'http://scp-wiki-cn.wikidot.com/(.+?)"',temp).group(0)[:-1]
    message = search(r'http://scp-wiki-cn.wikidot.com/(.+?)"', temp)
    realurl = r'http'+message.group(0)[:-1][4:]
    title = message.group(1)
    if title[:4] == 'scp-':
        try:
            num=message.group(1).upper()
            name=get_scp_name(num)
            title = num+':'+name
        except:
            pass
    else:
        title=get_page_title(realurl)

    reply = title+':\n'+realurl
    await session.send(reply.replace("http://scp-wiki-cn.wikidot.com/",SCP_DOMAIN[SCP_DOMAIN_INDEX]))
