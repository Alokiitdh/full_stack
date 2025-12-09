import asyncio

async def process1():
    print("Process 1: Starting")
    await asyncio.sleep(3)
    print("Process 1: Completed")

async def process2():
    print("Process 2: Starting")
    await asyncio.sleep(3)
    print("Process 2: Completed")


asyncio.run(process1())

asyncio.run(process2())
