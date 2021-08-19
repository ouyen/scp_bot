from requests.sessions import session
from config import SCP_DOMAIN, SCP_DOMAIN_INDEX
from nonebot import on_command, CommandSession
from requests import get
from urllib.parse import quote
import re

@on_command('search', aliases=('search', '寻找','搜索'),only_to_me=False)
async def search(session: CommandSession):
    keyword = session.current_arg
    message = await get_message(keyword)
    # await session.send(message)
    for i in message:
        await session.send(i)
async def get_message(keyword: str) -> str:
    if keyword=='起义':
        mes='起义：\n%sinsurrection\n不过鸢娓Iris提供了更为精彩的译文：\nhttps://www.bilibili.com/read/cv5317774'%SCP_DOMAIN[SCP_DOMAIN_INDEX]
        return mes
    elif keyword=='':
        return '内容不能为空'
    else:
        url='http://scp-wiki-cn.wikidot.com/search:site/q/'+keyword
        try:
            r=get(url,timeout=10)
            r.raise_for_status()
            r.encoding='utf-8'
            
            temp=re.search(r'<div class="search-results">.+?</a>',r.text,re.S)
            message=re.search(r'http://scp-wiki-cn.wikidot.com/(.+?)"',temp.group(0),re.S)
            realurl=r'https'+message.group(0)[:-1][4:]
            title_temp=re.search(r'<a href.+?</a>',temp.group(0)).group(0)
            title=re.sub(r'<.+?>','',title_temp)
            return [title+':\n'+realurl.replace("https://scp-wiki-cn.wikidot.com/",SCP_DOMAIN[SCP_DOMAIN_INDEX])]
        except:
            return ['scp网站的搜索功能大概无法使用，请使用searchx搜索引擎提供的结果：（请复制到浏览器打开）',r"https://searx.bar/search?q="+quote(keyword)+r"site%3Ahttp%3A%2F%2Fscp-wiki-cn.wikidot.com"]