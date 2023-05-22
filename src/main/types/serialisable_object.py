from src.main import Serialisable, StoredData
from src.main.types import SerialisableInt


class SerialisableObject(Serialisable):
    """
      Serialisable map for the object.
      This acts as a version map where the key value is the version of the serialisable object.
      This contains an ordered list of StorageData.

    """
    version_map = {
        0: [

        ]
    }

    __VERSION__ = 0

    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def encode(cls, value: object) -> StoredData:
        return super().encode(value)

    @classmethod
    def decode(cls, data: StoredData, class_type: type = None) -> object:
        return super().decode(data, class_type)

    @classmethod
    def _encode(cls, value: object) -> StoredData:
        if not isinstance(value, SerialisableObject):
            return StoredData()
        if cls.__VERSION__ not in cls.version_map:
            return StoredData()
        data = SerialisableInt.encode(cls.__VERSION__, 8)  # Encode the version.
        for serialise_data in cls.version_map.get(cls.__VERSION__, []):
            data += serialise_data.get(value)
        return data

    @classmethod
    def _decode(cls, data: StoredData, class_type: type = None) -> object:
        class_type = class_type if class_type is not None else cls.__class__
        if not isinstance(class_type, SerialisableObject):
            raise AttributeError(
                f"Specified class {class_type} to decode is not a subclass of SerialisableObject")
        data.record_pointer()
        version = SerialisableInt.decode(data, 8)
        data.update_pointer()
        obj = class_type()
        for serialise_data in obj.version_map.get(version, []):
            serialise_data.set(obj, data)
        return obj

