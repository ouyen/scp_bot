# from nonebot import on_command, CommandSession
from nonebot import permission,on_command,CommandSession
import re
import requests
import os
import sqlite3
import time

@on_command('update',aliases=('update','更新'),permission=permission.SUPERUSER)
async def update(session:CommandSession):
    receive = session.current_arg
    if receive=='':
        urls=[
            'http://scp-wiki-cn.wikidot.com/scp-series',
            'http://scp-wiki-cn.wikidot.com/scp-series-2',
            'http://scp-wiki-cn.wikidot.com/scp-series-3',
            'http://scp-wiki-cn.wikidot.com/scp-series-4',
            'http://scp-wiki-cn.wikidot.com/scp-series-5',
            'http://scp-wiki-cn.wikidot.com/scp-series-6',
            'http://scp-wiki-cn.wikidot.com/scp-series-7',
            'http://scp-wiki-cn.wikidot.com/joke-scps',
            'http://scp-wiki-cn.wikidot.com/scp-ex',
            'http://scp-wiki-cn.wikidot.com/scp-series-cn',
            'http://scp-wiki-cn.wikidot.com/scp-series-cn-2',
            'http://scp-wiki-cn.wikidot.com/scp-series-cn-3',
            'http://scp-wiki-cn.wikidot.com/joke-scps-cn',
            'http://scp-wiki-cn.wikidot.com/scp-ex-cn'
            ]
    else:
        urls=receive.split('')
    global con
    con=sqlite3.connect('scp.db')
    for url in urls:
        print('doing '+url)
        await session.send('doing '+url)
        await getSCPlist(await getHtml(url))
        time.sleep(0.5)
    print('all done')
    con.close()
    await session.send('all done')

async def getHtml(url):
    try:
        r=requests.get(url,timeout=10)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
    except:
        print(url+'error')
        await CommandSession.send(url)
        return ''

async def getSCPlist(text):
    scp_messages=re.findall(r'>SCP-.+?</a> - .+?</li>',text)
    scp_list=''
    cur=con.cursor()
    for scp_message in scp_messages:
        scp_num=re.findall(r'SCP-.+?</a>',scp_message)[0][:-4]
        scp_name_temp=re.findall(r'</a> - .+?</li>',scp_message)[0]
        scp_name=re.sub(r'<.+?>','',scp_name_temp)[3:]#滤掉名称的格式
        # scp_name=''.join(scp_name.split(' '))#滤掉空格
        if scp_name!='[禁止访问]' and scp_name!='[拒绝访问]':
            if(list(cur.execute("select * from SCP where NUM=?;",(scp_num,)))):
                cur.execute('update scp set name=? where num=?',(scp_name,scp_num))
            else:
                cur.execute('insert into scp values(?,?)',(scp_num,scp_name))
    con.commit()
    return scp_list
