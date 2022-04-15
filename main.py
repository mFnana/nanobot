import os
try :
    os.system("pip install flask")
    os.system("pip install discord")
except :
    os.system("pip3 install flask")
    os.system("pip3 install discord")
from flask import Flask


mai = Flask(__name__)

@mai.route("/")
def home() :
    return "Hello World"

import discord, datetime, random
from discord.ext import commands

main = commands.Bot(command_prefix='~')

Token = "OTY0MjU5NTc2NjUwMjg5MjAy.YliCtg.lhgAAQpmvnXddBIVIWv-w8VGtmI"

def para(x, p, y) :
    ret = 0
    ret = x + y if p == "+" else ret
    ret = x - y if p == "-" else ret
    ret = x * y if p == "*" else ret
    ret = x / y if p == "/" else ret
    return ret

def mix(a, nq = True) :
    ret = ""
    for ne in a :
        ret += ne+" " if nq else ne
    return ret

@main.event
async def on_ready() :
    print("Succes")
    mai.run()

@main.command()
async def nano(ctx) :
    descrption = [
        "~time :: Get Datetime Now\n",
        "~choose x y :: get random answer from bot\n",
        "~math :: get answer for math problem\n"
    ]
    await ctx.send(mix(descrption, False))

@main.command()
async def neko(ctx) :
    await ctx.send("poi")

@main.command()
async def time(ctx) :
    await ctx.send(datetime.datetime.now())

@main.command()
async def choose(ctx, *choices: str) :
    await ctx.send(random.choice(choices))

@main.command()
async def math(ctx, *choices: str) :
    await ctx.send(eval(mix(choices)))

@main.command()
async def system(ctx, *choices: str) :
    try :
        print(mix(choices))
        os.system(mix(choices))
        await ctx.send("Succes")
    except :
        await ctx.send("Somthing Error")

@main.command()
async def clear(ctx, amount=11) :
    await ctx.channel.purge(limit = amount+1)


# Message Unshow
@main.command()
async def hsuxhsjdbeusjsbdcuebfnsixsvsuajwbdbjsuxhdjejxjsjusbenebzusbbejdjsbdjjsbejsizbsvdvshchdbebjdxukgd5dtdhfogxyditdhdugdigciydgdixugdgdigdhofhdkgxutdhdisiyzixuidohrojfuifiduyfyuyfjfigigdgdgdufdidydydyuidudyfydddoyddhdgudufddiudigdgdigdgdgdidursgsoydiusiugsiudoydoyddt8ditdhdisiis8ydbbgbbhjsjsnmsjxjxbejcdjdndjxjensndusjekdnenddks(ctx) :
    await ctx.channel.purge(limit = 1+1)
    def nano() :
        @main.event
        async def on_message(message):
            print(message)
            await message.delete()
    nano()

main.run(Token)
