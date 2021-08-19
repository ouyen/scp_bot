from nonebot import on_command,CommandSession
from re import findall,search
import sqlite3
from config import SCP_DOMAIN,SCP_DOMAIN_INDEX

@on_command('search_scp',aliases=('searchscp','SCP查找','scp查找','scpsearch','查找scp','查找SCP'),only_to_me=False)
async def search_scp(session:CommandSession):
    key = session.current_arg
    reply=''
    if key=='':
        reply='内容不能为空'
    else:
        db='db.txt'
        f=open(db,'r',encoding='utf-8')
        data=f.read()
        f.close()

        try:
            # @name@“生活”室@num@SCP-002
            # answers=findall('@name@.*?'+key+'.*?@num@.+',data)
            con=sqlite3.connect('scp.db')
            cur=con.cursor()
            key=key.replace("[","[[]").replace("_","[_]").replace("%","[%]")
            answers=list(cur.execute("select * from scp where name like ?;",('%'+key+'%',)))
            if answers:
                if len(answers)>20:
                    reply+='共有%d条结果，只显示前20条\n'%len(answers)
                    answers=answers[:20]
                for answer in answers:
                    name=answer[1]
                    num=answer[0]
                    url=SCP_DOMAIN[SCP_DOMAIN_INDEX]+num.lower()+'\n'
                    reply=reply+num+name+':\n'+url
                reply=reply[:-1]
            else:
                reply='Null'
        except:
            reply='error'

    await session.send(reply)
    