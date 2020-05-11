from abc import ABC, abstractmethod


class SerializeMixin(ABC):
    """
    Mixin for serializing and deserializing.
    """

    @abstractmethod
    def to_bytes(self) -> bytes:
        ...

    @staticmethod
    @abstractmethod
    def from_bytes(blob: bytes):
        ...


class TrainMixin(ABC):
    """
    Mixin for adding a training method.
    """

    @abstractmethod
    def train(self, data):
        ...


class Parser(ABC):
    """
    A parser runs on a certain input type and does some kind of parsing.

    An example could be a regex based intent parser which when called on a
    string returns a list of intents matched.
    """

    @abstractmethod
    def __call__(self):
        pass
