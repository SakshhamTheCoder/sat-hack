from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from threading import Lock
import time
import asyncio

app = FastAPI()

ml_data = None
lock = Lock()
clients = set()


def run_ml_model():
    print("Running ML model...")
    return {"data": "Predicted results", "timestamp": time.time()}


async def refresh_ml_model():
    global ml_data
    while True:
        with lock:
            ml_data = run_ml_model()

        await broadcast_to_clients(ml_data)
        await asyncio.sleep(10)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(refresh_ml_model())


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()
    clients.add(websocket)
    try:
        while True:

            await websocket.receive_text()
    except WebSocketDisconnect:

        clients.remove(websocket)


async def broadcast_to_clients(data):

    disconnected_clients = []
    for client in clients:
        try:
            await client.send_json(data)
        except WebSocketDisconnect:
            disconnected_clients.append(client)

    for client in disconnected_clients:
        clients.remove(client)
