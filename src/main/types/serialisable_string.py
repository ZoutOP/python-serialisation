from src.main import StoredData
from src.main.types import SerialisableValue, SerialisableInt


class SerialisableString(SerialisableValue):
    """
    Class responsible for serialising a string value.
    """

    def __init__(self, value: str = "", str_length: int = 64, encoding: str = "utf-8",
                 char_size: int = 8):
        super().__init__(value, str_length * char_size)
        self.str_length = str_length
        self.encoding = encoding
        self.char_size = char_size

    def serialise(self, other: object = None) -> StoredData:
        return super().serialise(other, str_length=self.str_length, encoding=self.encoding,
                                 char_size=self.char_size)

    def deseralise(self, data: StoredData) -> object:
        return super().deseralise(data, str_length=self.str_length, encoding=self.encoding,
                                  char_size=self.char_size)

    @classmethod
    def encode(cls, value: str, str_length: int = 64, encoding: str = 'utf-8',
               char_size: int = 8) -> StoredData:
        return super().encode(value, str_length, encoding, char_size)

    @classmethod
    def decode(cls, data: StoredData, str_length: int = 64, encoding: str = 'utf-8',
               char_size: int = 8) -> str:
        return super().decode(data, str_length, encoding, char_size)

    @classmethod
    def _encode(cls, value: str, str_length: int, encoding: str, char_size: int) -> StoredData:
        data = StoredData()
        trimmed_value = value[:str_length].encode(encoding)
        for _ in range(str_length - len(trimmed_value)):
            data += SerialisableInt.encode(0, char_size)  # Add none value.
        for character in trimmed_value:
            data += SerialisableInt.encode(character, char_size)
        return data

    @classmethod
    def _decode(cls, data: StoredData, str_length: int, encoding: str, char_size: int) -> str:
        string = ""
        for _ in range(str_length):
            string += chr(SerialisableInt.decode(data, char_size))
        return string.lstrip('\0')  # Remove leading null values.

