import dataclasses
from celery.utils import functional, abstract


@dataclasses.dataclass
class TypeChecker:
    fun: callable
    bound: bool
    debug: bool = False

    class InvalidArgsKwargs(Exception):
        pass

    def __call__(self, *args, **kwargs):
        _annotations = {
            k: v
            for k, v in self.fun.__annotations__.items()
            if not issubclass(v, abstract.CallableTask)
        }
        if len(_annotations) > 1:
            raise self.InvalidArgsKwargs(
                f"Only dto styled function allowed please use `{self.fun.__name__}(dto: DtoCls)`"
            )
        _, dto_cls = _annotations.popitem()
        return dto_cls(*args, **kwargs)


# Monkey patch
functional.head_from_fun = TypeChecker
