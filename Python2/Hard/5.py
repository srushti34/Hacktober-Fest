def countdown(n):
   while n > 0:
     yield n
     n -= 1

async def main():
    try:
     gen = countdown(5)
     print(await gen.__next__()) 
    except StopIteration:
     print("Countdown finished")

import asyncio
asyncio.run(main())