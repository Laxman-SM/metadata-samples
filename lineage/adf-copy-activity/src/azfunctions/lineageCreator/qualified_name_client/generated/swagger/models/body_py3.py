# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Body(Model):
    """Body.

    :param uri:
    :type uri: str
    :param azure_storage_uri:
    :type azure_storage_uri: str
    :param filesystem_name:
    :type filesystem_name: str
    :param resource_set_path:
    :type resource_set_path: str
    :param azure_sql_server_uri:
    :type azure_sql_server_uri: str
    :param database_name:
    :type database_name: str
    :param azure_sql_table_name:
    :type azure_sql_table_name: str
    :param azure_sql_column_name:
    :type azure_sql_column_name: str
    :param hostname:
    :type hostname: str
    :param file_path:
    :type file_path: str
    :param cosmosdb_uri:
    :type cosmosdb_uri: str
    :param cosmosdb_database:
    :type cosmosdb_database: str
    :param container_name:
    :type container_name: str
    :param datafactory_name:
    :type datafactory_name: str
    :param pipeline_name:
    :type pipeline_name: str
    :param activity_name:
    :type activity_name: str
    :param spark_activity_name:
    :type spark_activity_name: str
    """

    _attribute_map = {
        'uri': {'key': 'uri', 'type': 'str'},
        'azure_storage_uri': {'key': 'azure_storage_uri', 'type': 'str'},
        'filesystem_name': {'key': 'filesystem_name', 'type': 'str'},
        'resource_set_path': {'key': 'resource_set_path', 'type': 'str'},
        'azure_sql_server_uri': {'key': 'azure_sql_server_uri', 'type': 'str'},
        'database_name': {'key': 'database_name', 'type': 'str'},
        'azure_sql_table_name': {'key': 'azure_sql_table_name', 'type': 'str'},
        'azure_sql_column_name': {'key': 'azure_sql_column_name', 'type': 'str'},
        'hostname': {'key': 'hostname', 'type': 'str'},
        'file_path': {'key': 'file_path', 'type': 'str'},
        'cosmosdb_uri': {'key': 'cosmosdb_uri', 'type': 'str'},
        'cosmosdb_database': {'key': 'cosmosdb_database', 'type': 'str'},
        'container_name': {'key': 'container_name', 'type': 'str'},
        'datafactory_name': {'key': 'datafactory_name', 'type': 'str'},
        'pipeline_name': {'key': 'pipeline_name', 'type': 'str'},
        'activity_name': {'key': 'activity_name', 'type': 'str'},
        'spark_activity_name': {'key': 'spark_activity_name', 'type': 'str'},
    }

    def __init__(self, *, uri: str=None, azure_storage_uri: str=None, filesystem_name: str=None, resource_set_path: str=None, azure_sql_server_uri: str=None, database_name: str=None, azure_sql_table_name: str=None, azure_sql_column_name: str=None, hostname: str=None, file_path: str=None, cosmosdb_uri: str=None, cosmosdb_database: str=None, container_name: str=None, datafactory_name: str=None, pipeline_name: str=None, activity_name: str=None, spark_activity_name: str=None, **kwargs) -> None:
        super(Body, self).__init__(**kwargs)
        self.uri = uri
        self.azure_storage_uri = azure_storage_uri
        self.filesystem_name = filesystem_name
        self.resource_set_path = resource_set_path
        self.azure_sql_server_uri = azure_sql_server_uri
        self.database_name = database_name
        self.azure_sql_table_name = azure_sql_table_name
        self.azure_sql_column_name = azure_sql_column_name
        self.hostname = hostname
        self.file_path = file_path
        self.cosmosdb_uri = cosmosdb_uri
        self.cosmosdb_database = cosmosdb_database
        self.container_name = container_name
        self.datafactory_name = datafactory_name
        self.pipeline_name = pipeline_name
        self.activity_name = activity_name
        self.spark_activity_name = spark_activity_name
