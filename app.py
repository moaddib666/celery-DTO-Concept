# Monkey Patch for Celery as not supported by upstream yet
import celery_patch  # noqa
from celery import Celery
from config import CeleryConfig
from dto import HelloWorldPayload
from task import DTOTask

app = Celery("hello", broker="amqp://guest@localhost//")
app.config_from_object(CeleryConfig)
app.task_cls = DTOTask


@app.task(bind=True)
def hello(task: DTOTask, dto: HelloWorldPayload):
    print("This is DTO Based Task")
    print("task", task, "dto", dto)
    return "result"


@app.task
def world(dto: HelloWorldPayload):
    print("This is DTO Based Task")
    print("dto", dto)
    return "result"


if __name__ == "__main__":
    data = HelloWorldPayload(msg="TestMessage")
    async_result = hello.publish(data)
    print("AsyncResult", type(async_result), async_result)
    print("=" * 6)

    async_result = hello.delay("this is message for dto in args")
    print("AsyncResult", type(async_result), async_result)
    print("=" * 6)

    async_result = hello.delay(msg="this is message for dto in kwargs")
    print("AsyncResult", type(async_result), async_result)
    print("=" * 6)

    async_result = hello.apply_async(
        args=("this is message for dto in kwargs",), MessageGroupId=123
    )
    print("AsyncResult", type(async_result), async_result)
    print("=" * 6)

    async_result = world.delay(msg="this is message for dto in kwargs")
    print("AsyncResult", type(async_result), async_result)
    print("=" * 6)
