import asyncio
import time


async def coroutine():
    print(f"Waiting 1 seconds")
    await asyncio.sleep(1)


async def main_without_tasks(n_times:int):
    for i in range(n_times):
        await coroutine()

async def main_with_tasks(n_times:int):
    for i in range(n_times):
        task = asyncio.create_task(coroutine())
    
    await task #waiting only for last task
    

if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main_without_tasks(5))

    print(f"Without task time {time.perf_counter()-start:2f}")

    start = time.perf_counter()
    asyncio.run(main_with_tasks(5))

    print(f"With task time {time.perf_counter()-start:2f}")
