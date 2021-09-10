from nonebot import on_command, CommandSession
import re,json

@on_command('minigram', patterns=(r".+CQ:json,data=.+"),only_to_me=False)
async def _(session: CommandSession):
    x=session.current_arg
    if '"prompt":"&amp;#91;QQ小程序&amp' in x:
        pattern=re.compile(".+CQ:json,data=(.+)\]")
        tmp=pattern.match(x)

        

        x_json=(re.sub('&#44;',',',tmp.group(1)).replace('&amp;#44;',','))
        x_dict=json.loads(x_json)
        x_url=x_dict['meta']['detail_1']['qqdocurl']

        if x_url.find('?')!=-1:
            reply=x_url[:x_url.find('?')]
        else:
            reply=x_url
        await session.send(reply)

