from nonebot import on_command, CommandSession
from random import randint
import re


@on_command('roll', aliases=('r', 'R','roll'),only_to_me=False)
async def _(session: CommandSession):
    detail=session.current_arg
    try:
        def f(x):
            roll_str=x.group()
            number2=roll_str.split('d')
            numbers=[]
            for i in range(int(number2[0])):
                numbers.append(str(randint(1,int(number2[1]))))
            # if len(numbers)==1:
            #     return numbers[0]
            # else:
            #     return '('+'+'.join(numbers)+')'
            return '('+'+'.join(numbers)+')'

        # temp=re.findall("[0-9]*d[0-9]*",detail)
        # if len(temp)==1:
        #     number2=re.findall("[0-9]*d[0-9]*",detail)[0].split('d')

        
        result_str=re.sub("[0-9]*d[0-9]*",f,detail)
        
        # def f2(x):
        #     return x+'='+str(eval(x))
        # message=detail+'='+f2(result_str)
        message=detail+'='+str(eval(result_str))
    except:
        message="roll error"
    await session.send(message)
