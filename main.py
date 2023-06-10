import asyncio
import requests
from server import keep_alive

hosts = ["https://osubot.kottey.repl.co",
         "https://osubot2.kottey.repl.co",
         "https://osubot.kty788.repl.co"]

async def Monitoring():
    while True:
        for host in hosts:
            '''
            subprocess.run(["curl", host])
            print("\n")
            '''
            response = requests.get(host)
            print(response.text)
            print("\n")
        '''
        res = subprocess.run(["ping", host, "-n", "5"], stdout=subprocess.PIPE)
        '''
        await asyncio.sleep(150)


keep_alive()
asyncio.run(Monitoring())
