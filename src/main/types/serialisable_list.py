from src.main import Serialisable, StoredData
from src.main.types import SerialisableValue, SerialisableInt


class SerialisableList(SerialisableValue):
    """
    Class for serialising a list of serialisable objects.
    Sets a max list length. The specified value for the maximum list length will be converted
    to binary length. Then the first part of the encoded list will contain the number of elements
    based on the length. Default is a list of max size 1023 which is 10 bits long.
    Can be List of Lists using this class inside of this class.
    """

    def __init__(self, value: list = None, list_type: Serialisable = None,
                 max_list_length: int = 1023) -> None:
        super().__init__(value if value is not None else [], len(bin(max_list_length)) - 2)
        self.list_type = list_type

    def serialise(self, other: object = None) -> StoredData:
        return super().serialise(other, list_type=self.list_type, bit_size=self.bit_size)

    def deseralise(self, data: StoredData) -> object:
        return super().deseralise(data, list_type=self.list_type, bit_size=self.bit_size)

    @classmethod
    def encode(cls, value: list, list_type: Serialisable, max_list_length: int = 1023,
               bit_size: int = None) -> StoredData:
        return super().encode(value, list_type, max_list_length, bit_size)

    @classmethod
    def decode(cls, data: StoredData, list_type: Serialisable, max_list_length: int = 1023,
               bit_size: int = None) -> list:
        return super().decode(data, list_type, max_list_length, bit_size)

    @classmethod
    def _encode(cls, value: list, list_type: Serialisable, max_list_length: int,
                bit_size: int) -> StoredData:
        bit_size = bit_size if bit_size is not None else len(bin(max_list_length)) - 2
        list_length = len(value)
        data = SerialisableInt.encode(list_length, bit_size)
        for item in value:
            print(list_type, item)
            data += list_type.serialise(item)
        return data

    @classmethod
    def _decode(cls, data: str, list_type: Serialisable, max_list_length: int,
                bit_size: int) -> list:
        bit_size = bit_size if bit_size is not None else len(bin(max_list_length)) - 2
        list_length = SerialisableInt.decode(data, bit_size)
        data_list = []  # Return value
        for _ in range(list_length):
            data_list.append(list_type.deseralise(data))
        return data_list
