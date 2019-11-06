import asyncio

import aiohttp
from aiohttp import web

SLEEP = 2


async def quote1(request):
    quote = "Wait a minute, Doc. Ah... Are you telling me that you built a time machine... out of a DeLorean?"
    print(quote)
    return web.Response(text=quote)


async def answer1(request):
    quote = "Ah, Jesus Christ! Jesus Christ, Doc, you disintegrated Einstein!"
    print(quote)
    await asyncio.sleep(SLEEP)
    try:
        async with request.app["client_session"] as session:
            async with session.get('http://emmet:8080/answer1') as resp:
                pass
    except:
        pass

    return web.Response(text=quote)


async def answer2(request):
    quote = "Then, where the hell are they?!"
    print(quote)
    await asyncio.sleep(SLEEP)
    try:
        async with request.app["client_session"] as session:
            async with session.get('http://emmet:8080/answer2') as resp:
                pass
    except:
        pass

    return web.Response(text=quote)


async def answer3(request):
    quote = "Wait a minute. Wait a minute Doc, uh, are you telling me you built a time machine... out of a DeLorean?"
    print(quote)
    await asyncio.sleep(SLEEP)
    try:
        async with request.app["client_session"] as session:
            async with session.get('http://emmet:8080/answer3') as resp:
                pass
    except:
        pass

    return web.Response(text=quote)


async def init_app(app):
    app["client_session"] = aiohttp.ClientSession()


app = web.Application()
app.on_startup.append(init_app)

app.add_routes([
    web.get("/quote1", quote1),
    web.get("/answer1", answer1),
    web.get("/answer2", answer2),
    web.get("/answer3", answer3),
])

web.run_app(app)




