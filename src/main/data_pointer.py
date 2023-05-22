

class DataPointer:
    """
    Data Pointer class.
    Holds a pointer value and a temporary pointer value to aid pointing to current
    value for the data storage.
    """

    def __init__(self, value: int = 0):
        """
        Initialise the data pointer class.
        :param value: int Default value for the pointer.
        """
        self._value = value
        self._temp_value = 0
        self._use_temp_value = 0

    @property
    def value(self) -> int:
        """
        Calculates and returns the pointer value.
        :return: int: pointer value. If temporary value is more than 0, return pointer and temp
        """
        if self._use_temp_value > 0:
            return self._value + self._temp_value
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        """
        Pointer value setter. The pointer class must not be using a temp value.
        :param value: int: Value to set the pointer at.
        :return: None
        """
        if self._use_temp_value > 0:
            raise AttributeError("Unable to set pointer while using temp value. "
                                 "Please call update or reset pointer.")
        self._value = value

    def increment(self, value: int) -> None:
        """
        Increment the pointer value. If the pointer is currently using a temporary value,
        add the value to the temporary value. Otherwise update the actual pointer value with
        the given integer value.
        :param value: int: The value to add or subtract (if negative) from the temp or pointer value
        :return: None
        """
        if self._use_temp_value > 0:
            self._temp_value += value
        else:
            self.value = self._value + value

    def record(self):
        """
        Record temporary value. Increments the temp value by one.
        """
        self._use_temp_value += 1

    def reset(self):
        """
        Reset the temporary value. Decrements the temp value by one. If the use temp value will be 0
        after reset, reset the temp value to 0. Decrement the use temp value by one each time this
        is called.
        :return: None
        """
        if self._use_temp_value <= 1:
            self._temp_value = 0
        if self._use_temp_value > 0:
            self._use_temp_value -= 1

    def update(self):
        """
        Update the pointer value based on temp value. Reset the temp value data.
        :return: None
        """
        self._use_temp_value = 0
        self.value = self._value + self._temp_value
        self._temp_value = 0