import asyncio
from loguru import logger
import time

async def coroutine(i:int):
    logger.info(f"Executing coroutine {i} for {i} seconds")
    await asyncio.sleep(i)

async def main(n_coroutines:int):

    tasks = [asyncio.create_task(coroutine(i)) for i in range(1,n_coroutines + 1)]
    logger.info(f"treating {len(tasks)} tasks")
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    start = time.perf_counter()
    while len(pending) > 0:
        logger.info(f"Tasks done: {len(done)} in {time.perf_counter() - start:2f} seconds")
        await asyncio.sleep(1)
        done = [task for task in tasks if task.done()]
        pending = [task for task in tasks if not task.done()]
    
    logger.info(f"Number Tasks done: {len(done)}")
    logger.success("Tasks finished")

if __name__ == "__main__":

    asyncio.run(main(10))