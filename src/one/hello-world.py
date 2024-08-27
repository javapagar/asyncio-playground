import asyncio
import random

async def hello_world() ->None:
    wait_time = random.randint(1,10)
    await asyncio.sleep(wait_time)
    print(f"hello world before {wait_time} seconds")



if __name__ == "__main__":
    asyncio.run(hello_world())