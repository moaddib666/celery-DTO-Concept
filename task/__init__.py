from celery import Task

from dto import CommandBusPayload


class DTOTask(Task):
    def publish(self, dto: CommandBusPayload):
        return self.apply_async(args=(), kwargs=dto.to_dict())

    def __call__(self, *args, **kwargs):
        dto = self.__header__(*args, **kwargs)
        result = super().__call__(dto)
        return result
