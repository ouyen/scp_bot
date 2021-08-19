from config import SCP_DOMAIN, SCP_DOMAIN_INDEX
from nonebot import on_command, CommandSession
from requests import get

@on_command('wanders', aliases=('wanders', 'wander','图书馆','被放逐者之图书馆','tsg'),only_to_me=False)
async def wanders(session: CommandSession):
    receive = session.current_arg
    message = await get_wanders(receive)
    await session.send(message)
async def get_wanders(receive: str) -> str:
    if receive=='':
        return SCP_DOMAIN[SCP_DOMAIN_INDEX]+f'wanderers:start'
    else:
        a=receive.split(' ')
        temp='-'.join(a)
        url=SCP_DOMAIN[SCP_DOMAIN_INDEX]+'wanderers:'+temp
        return url
        # try:
        #     r=get(url,timeout=30)
        #     r.raise_for_status()
        #     return url
        # except:
        #     try:
        #         url='https://wanderers-library.wikidot.com/'+temp
        #         r=get(url,timrout=30)
        #         r.raise_for_status()
        #         return f'此页面尚未翻译，英文页面如下：\n'+url
        #     except:
        #         return f'此页面不存在'

