# -*- coding: utf-8 -*-
"""client.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rVmYRq9f-L5NhEJUeey-HXC-wLh_mTAV
"""

import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:40000"
    async with websockets.connect(uri) as websocket:
        message = input("Enter message to send: ")
        await websocket.send(f"send:{message}")
        result = await websocket.recv()
        print(result)

async def receive_messages():
    uri = "ws://localhost:40000"
    async with websockets.connect(uri) as websocket:
        await websocket.send("receive")
        messages = await websocket.recv()
        print("\nReceived Messages:")
        print(messages)

if __name__ == '__main__':
    while True:
        choice = input("Choose an action (s/r/e): ").lower()

        if choice == "s":
            asyncio.get_event_loop().run_until_complete(send_message())
        elif choice == "r":
            asyncio.get_event_loop().run_until_complete(receive_messages())
        elif choice == "e":
            break
        else:
            print("Invalid choice. Please try again.")