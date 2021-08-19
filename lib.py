import sqlite3
from requests import get
from re import search

def get_scp_name(scp_num:str):
    #like SCP-001
    try:
        con=sqlite3.connect('scp.db')
        cur=con.cursor()
        names=list(cur.execute("select * from scp where NUM==?;",(scp_num,)))
        con.close()
        if(len(names)!=0):
            return names[0][1]
        else:
            return ""
    except:
        return ""

def get_page_title(url:str):
    try:
        r = get(url, timeout=10)
        r.raise_for_status()
        r.encoding = 'utf-8'
        title = search(r'<title>(.+) - SCP基金会</title>', r.text).group(1)
    except:
        title=url[31:]
        # len('http://scp-wiki-cn.wikidot.com/')=31
    return title