from config import SCP_DOMAIN, SCP_DOMAIN_INDEX
from nonebot import on_command,CommandSession
from urllib.parse import quote

@on_command('tag',aliases=('tag','标签'),only_to_me=False)
async def tag(session:CommandSession):
    receive=session.current_arg
    if receive=='':
        answer='内容不能为空'
    else:
        receive_q=quote(receive)
        answer='页面标记为'+receive+':\n'+SCP_DOMAIN[SCP_DOMAIN_INDEX]+'scp/system:page-tags/tag/'+receive_q
    await session.send(answer)