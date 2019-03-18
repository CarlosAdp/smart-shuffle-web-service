
def force_type(cls : type) -> type:
    """
    Decorators that forces types to class attributes
    """
    def generate_getter_and_setter(attribute_name: str, attribute_type: type) -> property:
        """ 
        Generates a getter and a setter according to defined type of attribute
        """
        def getter(self):
            return getattr(self, "__" + attribute_name)
        def setter(self, value):
            if value is not None and not isinstance(value, attribute_type):
                raise TypeError("{} attribute must be set to an instance of {}".format(attribute_name, attribute_type))
            setattr(self, "__" + attribute_name, value)
        return property(getter, setter)

    cls_dict = dict()
    for key, value in cls.__dict__.items():
        if isinstance(value, type):
            value = generate_getter_and_setter(attribute_name=key, attribute_type=value)
        cls_dict.update({ key : value })

    return type(cls)(cls.__name__, cls.__bases__, cls_dict)
