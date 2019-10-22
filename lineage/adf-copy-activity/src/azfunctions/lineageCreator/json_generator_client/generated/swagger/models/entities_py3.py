# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Entities(Model):
    """Entities.

    :param type_name:
    :type type_name: str
    :param guid:
    :type guid: int
    :param created_by:
    :type created_by: str
    :param attributes:
    :type attributes: ~swagger.models.Attributes
    """

    _attribute_map = {
        'type_name': {'key': 'typeName', 'type': 'str'},
        'guid': {'key': 'guid', 'type': 'int'},
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'Attributes'},
    }

    def __init__(self, *, type_name: str=None, guid: int=None, created_by: str=None, attributes=None, **kwargs) -> None:
        super(Entities, self).__init__(**kwargs)
        self.type_name = type_name
        self.guid = guid
        self.created_by = created_by
        self.attributes = attributes