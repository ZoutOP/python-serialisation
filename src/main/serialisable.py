from src.main import StoredData


class Serialisable:
    """
    Serialisable parent class.
    All child classes should implement the _encode and _decode methods for encoding.
    the serialise and deserialise methods should be overridden too to accompany different
    variables for serialisable objects.
    """

    def __init__(self) -> None:
        """
        Initialise the serialisable.
        """
        pass

    def serialise(self, other: object = None, *args, **kwargs) -> StoredData:
        """
        Serialise this class.
        Encodes the class based on set arguments and kwargs.
        If other is provided, the class will encode the provided object as it was self.
        :param other: object: A different value or object to encode instead of self.
        :param args: List of arguments to pass to the encoder.
        :param kwargs: List of keyword arguments to pass to the encoder.
        :return: StoredData item containing the serialised class object.
        """
        return self.encode(self if other is None else other, *args, **kwargs)

    def deseralise(self, data: StoredData, *args, **kwargs) -> object:
        """
        Deserialise the provided stored data into this class.
        Decodes the class based on this class properties.
        :param data: StoredData: The data to read this class's information from.
        :param args: List of arguments to pass to decoder
        :param kwargs: List of key word arguments to pass to decoder
        :return: object: This class with variables set from the stored data.
        """
        data.record_pointer()
        value = self.decode(data, *args, **kwargs)
        data.update_pointer()
        return value

    @classmethod
    def encode(cls, value: object, *args, **kwargs) -> StoredData:
        """
        Class Method to encode the provided object.
        :param value: object: Encodes this object to the stored data object it returns.
        :param args: Arguments to help the encoder encode this.
        :param kwargs: Keyword arguments to help the encoder encode this.
        :return: StoredData: Binary data of the provided value.
        """
        return cls._encode(value, *args, **kwargs)

    @classmethod
    def _encode(cls, value: object, *args, **kwargs) -> StoredData:
        """
        Children must implement this method to correctly encode their classes.
        :param value: object: The object to encode into binary data.
        :param args: Arguments to help the encoder encode this.
        :param kwargs: Keyword arguments to help the encoder encode this
        :return: StoredData: Binary data of the provided value.
        """
        return StoredData()

    @classmethod
    def decode(cls, data: StoredData, *args, **kwargs) -> object:
        """
        Decode the provided data into a new object of this class.
        Decoding is a classmethod and will not update the pointer value of the stored data object
        that is given. After the object is decoded, the pointer will reset to the original position
        before it was iterated.
        :param data: StoredData: The binary data to read and decode from.
        :param args: List of arguments to pass to decoder
        :param kwargs: List of key word arguments to pass to decoder
        :return: object: Serialisable object that is decoded.
        """
        data.record_pointer()
        result = cls._decode(data, *args, **kwargs)
        data.reset_pointer()
        return result

    @classmethod
    def _decode(cls, data: StoredData, *args, **kwargs) -> object:
        """
        The decode method to be implemented by subclasses.
        :param data: StoredData: The data to read this class's information from.
        :param args: List of arguments to pass to decoder
        :param kwargs: List of key word arguments to pass to decoder
        :return: object: Serialisable object with variables set from the stored data.
        """
        return None
