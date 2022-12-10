import abc
import dataclasses


@dataclasses.dataclass
class CommandBusPayload(abc.ABC):
    def to_dict(self) -> dict:
        return dataclasses.asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


@dataclasses.dataclass
class HelloWorldPayload(CommandBusPayload):
    msg: str

    class Meta:
        whitelist_fields = ("msg",)
