from nonebot import on_command, CommandSession

@on_command('sb', aliases=('sb','SB','zz','ZZ','Sb','cnm','nmsl','[脏话]','憨批'))
async def _(session: CommandSession):
    # print('我是一台烤面包机')
    # return f'我是一台烤面包机'
    await session.send('你这肥[脏话]，你[脏话]想干啥？')