import discord
from discord.ext import commands
from sympy import Symbol, solve
import os

bot = commands.Bot(command_prefix=">")

@bot.command()
async def eq(ctx, *, eqs):
    equations = eqs.split(" ")
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    a = Symbol('a')
    b = Symbol('b')
    c = Symbol('c')
    n = Symbol('n')
    try:
        eql = []
        for equation in equations:
           eql.append(eval(equation))
        res = solve(eql, dict=True)
        if (len(res) > 0):
            await ctx.send(f"결과 : `{res}`")
        else:
            await ctx.send("식에 문제가 있습니다.")
            
    except Exception as e:
        await ctx.send(f"오류 발생\n{e}")

bot.run(os.getenv("token"))