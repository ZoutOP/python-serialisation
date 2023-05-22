from src.main import Serialisable, StoredData


class SerialisableValue(Serialisable):
    """
    Single value serialisation class for simple objects.
    This is only an interface for subclasses to implement.
    """

    def __init__(self, value: object, bit_size: int = 0):
        """
        Initialise the serialisable value.
        :param value: object: Any value to be encoded.
        :param bit_size: int = 0: The numbers of bits the encoded string should be.
        """
        super().__init__()
        self.value = value
        self.bit_size = bit_size

    def serialise(self, other: object = None, *args, **kwargs) -> StoredData:
        """
        Override serialise to provide the value instead of self to be encoded.
        """
        return super().serialise(other if other is not None else self.value, *args, **kwargs)