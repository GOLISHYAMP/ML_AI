from flask import Flask, jsonify
import time
import threading
from multiprocessing import Process
import asyncio

app = Flask(__name__)





# processes = []
# for i in range(4):
#     p = Process(target=compute)
#     processes.append(p)
#     p.start()

# for p in processes:
#     p.join()

def compute():
    time.sleep(10)
    print('done')
p = None
@app.route("/")
def home():
    # th = threading.Thread(target=compute)
    # th.start()
    global p
    p = Process(target=compute)
    p.start()
    return "<h1>Hello shyam</h1>"

# Define the asynchronous function
async def my_async_function():
    # Simulate an asynchronous I/O-bound task
    print('started')
    await asyncio.sleep(10)
    print("done")
    # return "Async task completed"

@app.route('/async')
async def async_route():
    # Simulate an asynchronous I/O-bound task
    # await asyncio.create_subprocess_exec(compute)
    # my_async_function()
    # await asyncio.run(my_async_function())
    # print('done')
    asyncio.create_task(my_async_function())
    # await asyncio.gather(task1)
    return jsonify(message="This is an async route")

if __name__ == "__main__":
    app.run(debug=True)
    # p.join()

