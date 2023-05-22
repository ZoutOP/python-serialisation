import re

from src.main import DataPointer


class StoredData:
    """
    Holds the stored bytes of data.
    Uses data pointer class to point and retrieve data from the object.
    """

    def __init__(self, data: str = "", data_size: int = None) -> None:
        """
        Initialise the stored data.
        :param data: str: String representation of binary data to start the storage from.
        :param data_size: Expected data size. Pad the data with leading zeros if not same length.
        """
        self._data_len = 0
        self._data = ""
        self.add_data(data, data_size)
        self._pointer = DataPointer(0)

    def add_data(self, data: str, data_size: int = None):
        """
        Add the data string to the internal data.
        Checks whether the data follows a binary pattern.
        If a data size is provided, and the data length is smaller than size, pad the data
        with 0's
        :param data: str: Binary representation of data.
        :param data_size: int: Default None or specified number.
        :return:
        """
        if not isinstance(data, str):
            raise ValueError(f"Invalid data provided to append to stored data. Expected binary str "
                             f"representation but got: {type(data)}")
        if not re.fullmatch("[01]+", data):
            raise ValueError(f"Invalid data provided to append to stored data. Expted a binary str "
                             f"representation but got {data}")
        data_len = len(data)
        if data_len == 0:
            return
        if isinstance(data_size, int) and data_len < data_size:
            self._data += data.zfill(data_size)
            self._data_len += data_size
        else:
            self._data += data
            self._data_len += data_len

    def get_bits(self, bit_size: int = 0) -> str:
        """
        Get a string of bits from the stored data of bit_size length.
        The bits are retrieved from the pointer value. This value is effected if the pointer
        is using a temp value.
        :param bit_size: int: The requested length of the bits to return
        :return: str
        """
        start = self._pointer.value
        data = self._data[start:start + bit_size]
        self._pointer.increment(bit_size)  # Increment the pointer.
        return data

    def record_pointer(self) -> None:
        """
        Record the pointer.
        :return: None
        """
        self._pointer.record()

    def reset_pointer(self) -> None:
        """
        Reset the pointer.
        :return: None
        """
        self._pointer.reset()

    def set_pointer(self, value: int = 0) -> None:
        """
        Set the pointer value.
        :param value: int: The new value for the pointer.
        :return:
        """
        self._pointer.value = value

    def update_pointer(self) -> None:
        """
        Update pointer. Set's the new pointer value based on the temp value.
        :return:
        """
        self._pointer.update()

    def __iadd__(self, other):
        """
        __iadd__ override.
        Can use StoredData += StoredData to increment the stored data storage with new data.
        Can increment using a stored data or string of binaries.
        :param other:
        :return:
        """
        if isinstance(other, StoredData):
            self.add_data(other._data)
        else:
            self.add_data(other)
        return self

