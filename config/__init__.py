import dataclasses


@dataclasses.dataclass
class CeleryConfig:
    task_always_eager = True
    task_eager_propagates = True
    task_store_eager_result = True
