from celery import Celery

app = Celery('tasks', broker='amqp://')


@app.task(ignore_result=True)
def print_hello():
    print('hello there')


@app.task
def gen_prime(x):
    multiplies = []
    results = []
    for i in range(2, x + 1):
        results.append(i)
        for j in range(i*i, x+1, i):
            multiplies.append(j)
    return results
