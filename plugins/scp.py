from nonebot import on_command, CommandSession
from config import SCP_DOMAIN, SCP_DOMAIN_INDEX
from lib import get_scp_name


@on_command('scp', aliases=('scp', 'SCP'), only_to_me=False)
async def scp(session: CommandSession):
    number = session.current_arg
    message = await get_details(number)
    await session.send(message)


async def get_details(number: str) -> str:
    if 'pku' in number:
        return 'SCP-PKU-002 签到怪：\nhttps://site-871.gitee.io/scp/scp-pku-002'

    elif number == '':
        return '内容不能为空'

    else:
        number_details = number.split(' ')
        if len(number_details) == 1:
            number_details = number.split('-')
        num = ('SCP-' + '-'.join(number_details)).upper()
        name = get_scp_name(num)
        url = num + ' ' + name + ' \n' + SCP_DOMAIN[
            SCP_DOMAIN_INDEX] + num.lower()
        return url