??? solution "Challenge 1: Read-Only Descriptor"
    ```python
    class ReadOnly:
        def __init__(self, value):
            self._value = value

        def __get__(self, instance, owner):
            # If accessed via an instance (instance is not None), return the stored value.
            # If accessed via the class (instance is None), return the descriptor itself.
            # For a simple read-only constant, directly returning _value is fine.
            return self._value

        def __set__(self, instance, value):
            raise AttributeError("Read-only attribute")

        def __delete__(self, instance):
            raise AttributeError("Cannot delete read-only attribute")

    class MyClass:
        const = ReadOnly(42)

    # Example Usage and Verification:
    # obj = MyClass()
    # assert obj.const == 42
    # try:
    #     obj.const = 10
    # except AttributeError as e:
    #     print(f"Successfully caught expected error: {e}")
    # else:
    #     print("Failed to catch expected AttributeError on assignment.")
    #
    # try:
    #     del obj.const
    # except AttributeError as e:
    #     print(f"Successfully caught expected error: {e}")
    # else:
    #     print("Failed to catch expected AttributeError on deletion.")
    ```