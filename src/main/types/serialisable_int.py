from src.main import StoredData
from src.main.types import SerialisableValue


class SerialisableInt(SerialisableValue):
    """
    Class for serialising integers
    """

    def __init__(self, value: int, bit_size: int = 0):
        super().__init__(value, bit_size)

    def serialise(self, other: object = None) -> StoredData:
        return super().serialise(other, bit_size=self.bit_size)

    def deseralise(self, data: StoredData) -> object:
        return super().deseralise(data, bit_size=self.bit_size)

    @classmethod
    def encode(cls, value: int, bit_size: int = 0) -> StoredData:
        return super().encode(value, bit_size)

    @classmethod
    def decode(cls, data: StoredData, bit_size: int = 0) -> int:
        return super().decode(data, bit_size)

    @classmethod
    def _encode(cls, value: int, bit_size: int) -> StoredData:
        bit_value = bin(value)[2:]
        return StoredData(bit_value, bit_size)

    @classmethod
    def _decode(cls, data: StoredData, bit_size: int) -> int:
        return int(data.get_bits(bit_size), 2)