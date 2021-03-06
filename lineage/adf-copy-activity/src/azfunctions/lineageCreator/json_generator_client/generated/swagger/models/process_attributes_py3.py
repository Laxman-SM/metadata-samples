# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ProcessAttributes(Model):
    """ProcessAttributes.

    :param attr_name:
    :type attr_name: str
    :param attr_value:
    :type attr_value: str
    :param is_entityref:
    :type is_entityref: bool
    """

    _attribute_map = {
        'attr_name': {'key': 'attr_name', 'type': 'str'},
        'attr_value': {'key': 'attr_value', 'type': 'str'},
        'is_entityref': {'key': 'is_entityref', 'type': 'bool'},
    }

    def __init__(self, *, attr_name: str=None, attr_value: str=None, is_entityref: bool=None, **kwargs) -> None:
        super(ProcessAttributes, self).__init__(**kwargs)
        self.attr_name = attr_name
        self.attr_value = attr_value
        self.is_entityref = is_entityref
