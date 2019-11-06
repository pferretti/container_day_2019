import asyncio

import aiohttp
from aiohttp import web

SLEEP = 2


async def quote1(request):
    quote = "Roads? Where we're going we don't need... roads!"
    print(quote)
    return web.Response(text=quote)


async def question1(request):
    quote = "Ha! What did I tell you?! 88 MILES PER HOUR! The temporal displacement occurred exactly 1:20 A.M. and zero seconds!"
    print(quote)
    await asyncio.sleep(SLEEP)
    try:
        async with request.app["client_session"] as session:
            async with session.get('http://marty:8080/answer1') as resp:
                pass
    except:
        pass

    return web.Response(text=quote)


async def answer1(request):
    quote = "Calm down, Marty! I didn't disintegrate anything! The molecular structure of both Einstein and the car are completely intact."
    print(quote)
    await asyncio.sleep(SLEEP)
    try:
        async with request.app["client_session"] as session:
            async with session.get('http://marty:8080/answer2') as resp:
                pass
    except:
        pass

    return web.Response(text=quote)


async def answer2(request):
    quote = (
        "The appropriate question is, \"When the hell are they?\"! You see, "
        "Einstein has just become the world's first time traveler! I sent "
        "him into the future. One minute into the future to be exact. And "
        "at precisely 1:21 A.M. and zero seconds, we shall catch up with him "
        "and the time machine!"
    )
    print(quote)
    await asyncio.sleep(SLEEP)
    try:
        async with request.app["client_session"] as session:
            async with session.get('http://marty:8080/answer3') as resp:
                pass
    except:
        pass

    return web.Response(text=quote)


async def answer3(request):
    quote = (
        "The way I see it, if you're going to build a time machine into a car, "
        "why not do it with some style? Besides, the stainless steel construction "
        "made the flux dispersal. Look out!"
    )
    print(quote)
    await asyncio.sleep(SLEEP)
    return web.Response(text=quote)


async def init_app(app):
    app["client_session"] = aiohttp.ClientSession()


app = web.Application()
app.on_startup.append(init_app)

app.add_routes([
    web.get("/quote1", quote1),
    web.get("/question1", question1),
    web.get("/answer1", answer1),
    web.get("/answer2", answer2),
    web.get("/answer3", answer3),
])

web.run_app(app)
