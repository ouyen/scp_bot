from config import SETU_API_KEY
from nonebot import permission,on_command,CommandSession
import requests
import json

@on_command('setu',aliases=('setu','色图'),permission=permission.SUPERUSER)
async  def get_setu(session:CommandSession):
    receive=session.current_arg
    if receive=='':
        pic=requests.get(url='https://api.lolicon.app/setu',params={'apikey':SETU_API_KEY,'r18':0})
        setu_dic=json.loads(pic.content)
        message="[CQ:image,file="+setu_dic['data'][0]['url']+"]"
        await session.send(message)