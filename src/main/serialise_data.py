from src.main import Serialisable, StoredData


class SerialiseData:
    """
    Serialisable data class.
    Acts as a third party class that holds a property value and serialisable object which it will
    be able to encode or decode when called with a parent object that contains the property.
    This class is used for denoting data in a serialisable object.
    """

    def __init__(self, property_name: str, serialisable: Serialisable):
        super().__init__()
        self.property_name = property_name
        self.serialisable = serialisable

    def get(self, parent: object) -> StoredData:
        """ Returns the serialised value of the parent and property value."""
        if not hasattr(parent, self.property_name):
            raise ValueError(f"Unable to instantiate serialisable object. Parent does not has specified property. \
                             property: {self.property_name}. class: {parent}")
        return self.serialisable.encode(getattr(parent, self.property_name))

    def set(self, parent: object, data: StoredData) -> None:
        """ Set the parent property value based on the decoded data. Updates pointer."""
        if not hasattr(parent, self.property_name):
            raise ValueError(f"Unable to instantiate serialisable object. Parent does not has specified property. \
                             property: {self.property_name}. class: {parent}")
        data.record_pointer()
        value = self.serialisable.decode(data)
        data.update_pointer()
        setattr(parent, self.property_name, value)

