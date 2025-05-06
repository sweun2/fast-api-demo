import asyncio
import httpx
import time
URL = "http://localhost:8000/api/v1/orders/"
PAYLOAD = {"item_id": 1, "quantity": 2, "user_id": 1}
CONCURRENT_REQUESTS = 300

async def create_order(client, idx):
    resp = await client.post(URL, json=PAYLOAD)
    return idx, resp.status_code, resp.text

async def main():
    times = time.time()
    async with httpx.AsyncClient(timeout=10) as client:
        tasks = [
            asyncio.create_task(create_order(client, i))
            for i in range(CONCURRENT_REQUESTS)
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)
    
    success = sum(1 for r in results if isinstance(r, tuple) and r[1] == 200)
    fail    = len(results) - success
    print(f"전체 요청: {len(results)}, 성공: {success}, 실패: {fail}")
    print(f"소요 시간: {time.time() - times:.2f}초")
    print(f"성공률: {success / len(results) * 100:.2f}%")
if __name__ == "__main__":
    asyncio.run(main())
