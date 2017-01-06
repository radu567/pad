import asyncio
from proxy.main import run_proxy

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    run_proxy(loop)
