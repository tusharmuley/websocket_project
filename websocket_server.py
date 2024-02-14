import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(f"Received message from client: {message}")
        await websocket.send(f"Echoing back: {message}")

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        print("WebSocket server started")
        await asyncio.Future()  # Run forever

asyncio.run(main())
