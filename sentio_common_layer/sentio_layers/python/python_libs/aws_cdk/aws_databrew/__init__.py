'''
# AWS::DataBrew Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_databrew as databrew
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DataBrew construct libraries](https://constructs.dev/search?q=databrew)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DataBrew resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DataBrew.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DataBrew](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DataBrew.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/master/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

import constructs
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnDataset(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_databrew.CfnDataset",
):
    '''A CloudFormation ``AWS::DataBrew::Dataset``.

    Specifies a new DataBrew dataset.

    :cloudformationResource: AWS::DataBrew::Dataset
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_databrew as databrew
        
        cfn_dataset = databrew.CfnDataset(self, "MyCfnDataset",
            input=databrew.CfnDataset.InputProperty(
                database_input_definition=databrew.CfnDataset.DatabaseInputDefinitionProperty(
                    glue_connection_name="glueConnectionName",
        
                    # the properties below are optional
                    database_table_name="databaseTableName",
                    query_string="queryString",
                    temp_directory=databrew.CfnDataset.S3LocationProperty(
                        bucket="bucket",
        
                        # the properties below are optional
                        key="key"
                    )
                ),
                data_catalog_input_definition=databrew.CfnDataset.DataCatalogInputDefinitionProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    table_name="tableName",
                    temp_directory=databrew.CfnDataset.S3LocationProperty(
                        bucket="bucket",
        
                        # the properties below are optional
                        key="key"
                    )
                ),
                metadata=databrew.CfnDataset.MetadataProperty(
                    source_arn="sourceArn"
                ),
                s3_input_definition=databrew.CfnDataset.S3LocationProperty(
                    bucket="bucket",
        
                    # the properties below are optional
                    key="key"
                )
            ),
            name="name",
        
            # the properties below are optional
            format="format",
            format_options=databrew.CfnDataset.FormatOptionsProperty(
                csv=databrew.CfnDataset.CsvOptionsProperty(
                    delimiter="delimiter",
                    header_row=False
                ),
                excel=databrew.CfnDataset.ExcelOptionsProperty(
                    header_row=False,
                    sheet_indexes=[123],
                    sheet_names=["sheetNames"]
                ),
                json=databrew.CfnDataset.JsonOptionsProperty(
                    multi_line=False
                )
            ),
            path_options=databrew.CfnDataset.PathOptionsProperty(
                files_limit=databrew.CfnDataset.FilesLimitProperty(
                    max_files=123,
        
                    # the properties below are optional
                    order="order",
                    ordered_by="orderedBy"
                ),
                last_modified_date_condition=databrew.CfnDataset.FilterExpressionProperty(
                    expression="expression",
                    values_map=[databrew.CfnDataset.FilterValueProperty(
                        value="value",
                        value_reference="valueReference"
                    )]
                ),
                parameters=[databrew.CfnDataset.PathParameterProperty(
                    dataset_parameter=databrew.CfnDataset.DatasetParameterProperty(
                        name="name",
                        type="type",
        
                        # the properties below are optional
                        create_column=False,
                        datetime_options=databrew.CfnDataset.DatetimeOptionsProperty(
                            format="format",
        
                            # the properties below are optional
                            locale_code="localeCode",
                            timezone_offset="timezoneOffset"
                        ),
                        filter=databrew.CfnDataset.FilterExpressionProperty(
                            expression="expression",
                            values_map=[databrew.CfnDataset.FilterValueProperty(
                                value="value",
                                value_reference="valueReference"
                            )]
                        )
                    ),
                    path_parameter_name="pathParameterName"
                )]
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        input: typing.Union["CfnDataset.InputProperty", _IResolvable_da3f097b],
        name: builtins.str,
        format: typing.Optional[builtins.str] = None,
        format_options: typing.Optional[typing.Union["CfnDataset.FormatOptionsProperty", _IResolvable_da3f097b]] = None,
        path_options: typing.Optional[typing.Union["CfnDataset.PathOptionsProperty", _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::DataBrew::Dataset``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param input: Information on how DataBrew can find the dataset, in either the AWS Glue Data Catalog or Amazon S3 .
        :param name: The unique name of the dataset.
        :param format: The file format of a dataset that is created from an Amazon S3 file or folder.
        :param format_options: A set of options that define how DataBrew interprets the data in the dataset.
        :param path_options: A set of options that defines how DataBrew interprets an Amazon S3 path of the dataset.
        :param tags: Metadata tags that have been applied to the dataset.
        '''
        props = CfnDatasetProps(
            input=input,
            name=name,
            format=format,
            format_options=format_options,
            path_options=path_options,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Metadata tags that have been applied to the dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html#cfn-databrew-dataset-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="input")
    def input(self) -> typing.Union["CfnDataset.InputProperty", _IResolvable_da3f097b]:
        '''Information on how DataBrew can find the dataset, in either the AWS Glue Data Catalog or Amazon S3 .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html#cfn-databrew-dataset-input
        '''
        return typing.cast(typing.Union["CfnDataset.InputProperty", _IResolvable_da3f097b], jsii.get(self, "input"))

    @input.setter
    def input(
        self,
        value: typing.Union["CfnDataset.InputProperty", _IResolvable_da3f097b],
    ) -> None:
        jsii.set(self, "input", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The unique name of the dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html#cfn-databrew-dataset-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="format")
    def format(self) -> typing.Optional[builtins.str]:
        '''The file format of a dataset that is created from an Amazon S3 file or folder.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html#cfn-databrew-dataset-format
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "format"))

    @format.setter
    def format(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "format", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="formatOptions")
    def format_options(
        self,
    ) -> typing.Optional[typing.Union["CfnDataset.FormatOptionsProperty", _IResolvable_da3f097b]]:
        '''A set of options that define how DataBrew interprets the data in the dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html#cfn-databrew-dataset-formatoptions
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDataset.FormatOptionsProperty", _IResolvable_da3f097b]], jsii.get(self, "formatOptions"))

    @format_options.setter
    def format_options(
        self,
        value: typing.Optional[typing.Union["CfnDataset.FormatOptionsProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "formatOptions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pathOptions")
    def path_options(
        self,
    ) -> typing.Optional[typing.Union["CfnDataset.PathOptionsProperty", _IResolvable_da3f097b]]:
        '''A set of options that defines how DataBrew interprets an Amazon S3 path of the dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html#cfn-databrew-dataset-pathoptions
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDataset.PathOptionsProperty", _IResolvable_da3f097b]], jsii.get(self, "pathOptions"))

    @path_options.setter
    def path_options(
        self,
        value: typing.Optional[typing.Union["CfnDataset.PathOptionsProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "pathOptions", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnDataset.CsvOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"delimiter": "delimiter", "header_row": "headerRow"},
    )
    class CsvOptionsProperty:
        def __init__(
            self,
            *,
            delimiter: typing.Optional[builtins.str] = None,
            header_row: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Represents a set of options that define how DataBrew will read a comma-separated value (CSV) file when creating a dataset from that file.

            :param delimiter: A single character that specifies the delimiter being used in the CSV file.
            :param header_row: A variable that specifies whether the first row in the file is parsed as the header. If this value is false, column names are auto-generated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-csvoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                csv_options_property = databrew.CfnDataset.CsvOptionsProperty(
                    delimiter="delimiter",
                    header_row=False
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if delimiter is not None:
                self._values["delimiter"] = delimiter
            if header_row is not None:
                self._values["header_row"] = header_row

        @builtins.property
        def delimiter(self) -> typing.Optional[builtins.str]:
            '''A single character that specifies the delimiter being used in the CSV file.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-csvoptions.html#cfn-databrew-dataset-csvoptions-delimiter
            '''
            result = self._values.get("delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def header_row(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A variable that specifies whether the first row in the file is parsed as the header.

            If this value is false, column names are auto-generated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-csvoptions.html#cfn-databrew-dataset-csvoptions-headerrow
            '''
            result = self._values.get("header_row")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CsvOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnDataset.DataCatalogInputDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "table_name": "tableName",
            "temp_directory": "tempDirectory",
        },
    )
    class DataCatalogInputDefinitionProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
            table_name: typing.Optional[builtins.str] = None,
            temp_directory: typing.Optional[typing.Union["CfnDataset.S3LocationProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Represents how metadata stored in the AWS Glue Data Catalog is defined in a DataBrew dataset.

            :param catalog_id: The unique identifier of the AWS account that holds the Data Catalog that stores the data.
            :param database_name: The name of a database in the Data Catalog.
            :param table_name: The name of a database table in the Data Catalog. This table corresponds to a DataBrew dataset.
            :param temp_directory: An Amazon location that AWS Glue Data Catalog can use as a temporary directory.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datacataloginputdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                data_catalog_input_definition_property = databrew.CfnDataset.DataCatalogInputDefinitionProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    table_name="tableName",
                    temp_directory=databrew.CfnDataset.S3LocationProperty(
                        bucket="bucket",
                
                        # the properties below are optional
                        key="key"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if database_name is not None:
                self._values["database_name"] = database_name
            if table_name is not None:
                self._values["table_name"] = table_name
            if temp_directory is not None:
                self._values["temp_directory"] = temp_directory

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier of the AWS account that holds the Data Catalog that stores the data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datacataloginputdefinition.html#cfn-databrew-dataset-datacataloginputdefinition-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''The name of a database in the Data Catalog.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datacataloginputdefinition.html#cfn-databrew-dataset-datacataloginputdefinition-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def table_name(self) -> typing.Optional[builtins.str]:
            '''The name of a database table in the Data Catalog.

            This table corresponds to a DataBrew dataset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datacataloginputdefinition.html#cfn-databrew-dataset-datacataloginputdefinition-tablename
            '''
            result = self._values.get("table_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def temp_directory(
            self,
        ) -> typing.Optional[typing.Union["CfnDataset.S3LocationProperty", _IResolvable_da3f097b]]:
            '''An Amazon location that AWS Glue Data Catalog can use as a temporary directory.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datacataloginputdefinition.html#cfn-databrew-dataset-datacataloginputdefinition-tempdirectory
            '''
            result = self._values.get("temp_directory")
            return typing.cast(typing.Optional[typing.Union["CfnDataset.S3LocationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataCatalogInputDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnDataset.DatabaseInputDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "glue_connection_name": "glueConnectionName",
            "database_table_name": "databaseTableName",
            "query_string": "queryString",
            "temp_directory": "tempDirectory",
        },
    )
    class DatabaseInputDefinitionProperty:
        def __init__(
            self,
            *,
            glue_connection_name: builtins.str,
            database_table_name: typing.Optional[builtins.str] = None,
            query_string: typing.Optional[builtins.str] = None,
            temp_directory: typing.Optional[typing.Union["CfnDataset.S3LocationProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Connection information for dataset input files stored in a database.

            :param glue_connection_name: The AWS Glue Connection that stores the connection information for the target database.
            :param database_table_name: The table within the target database.
            :param query_string: Custom SQL to run against the provided AWS Glue connection. This SQL will be used as the input for DataBrew projects and jobs.
            :param temp_directory: An Amazon location that AWS Glue Data Catalog can use as a temporary directory.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-databaseinputdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                database_input_definition_property = databrew.CfnDataset.DatabaseInputDefinitionProperty(
                    glue_connection_name="glueConnectionName",
                
                    # the properties below are optional
                    database_table_name="databaseTableName",
                    query_string="queryString",
                    temp_directory=databrew.CfnDataset.S3LocationProperty(
                        bucket="bucket",
                
                        # the properties below are optional
                        key="key"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "glue_connection_name": glue_connection_name,
            }
            if database_table_name is not None:
                self._values["database_table_name"] = database_table_name
            if query_string is not None:
                self._values["query_string"] = query_string
            if temp_directory is not None:
                self._values["temp_directory"] = temp_directory

        @builtins.property
        def glue_connection_name(self) -> builtins.str:
            '''The AWS Glue Connection that stores the connection information for the target database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-databaseinputdefinition.html#cfn-databrew-dataset-databaseinputdefinition-glueconnectionname
            '''
            result = self._values.get("glue_connection_name")
            assert result is not None, "Required property 'glue_connection_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_table_name(self) -> typing.Optional[builtins.str]:
            '''The table within the target database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-databaseinputdefinition.html#cfn-databrew-dataset-databaseinputdefinition-databasetablename
            '''
            result = self._values.get("database_table_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def query_string(self) -> typing.Optional[builtins.str]:
            '''Custom SQL to run against the provided AWS Glue connection.

            This SQL will be used as the input for DataBrew projects and jobs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-databaseinputdefinition.html#cfn-databrew-dataset-databaseinputdefinition-querystring
            '''
            result = self._values.get("query_string")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def temp_directory(
            self,
        ) -> typing.Optional[typing.Union["CfnDataset.S3LocationProperty", _IResolvable_da3f097b]]:
            '''An Amazon location that AWS Glue Data Catalog can use as a temporary directory.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-databaseinputdefinition.html#cfn-databrew-dataset-databaseinputdefinition-tempdirectory
            '''
            result = self._values.get("temp_directory")
            return typing.cast(typing.Optional[typing.Union["CfnDataset.S3LocationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseInputDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnDataset.DatasetParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "type": "type",
            "create_column": "createColumn",
            "datetime_options": "datetimeOptions",
            "filter": "filter",
        },
    )
    class DatasetParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            type: builtins.str,
            create_column: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            datetime_options: typing.Optional[typing.Union["CfnDataset.DatetimeOptionsProperty", _IResolvable_da3f097b]] = None,
            filter: typing.Optional[typing.Union["CfnDataset.FilterExpressionProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Represents a dataset paramater that defines type and conditions for a parameter in the Amazon S3 path of the dataset.

            :param name: The name of the parameter that is used in the dataset's Amazon S3 path.
            :param type: The type of the dataset parameter, can be one of a 'String', 'Number' or 'Datetime'.
            :param create_column: Optional boolean value that defines whether the captured value of this parameter should be loaded as an additional column in the dataset.
            :param datetime_options: Additional parameter options such as a format and a timezone. Required for datetime parameters.
            :param filter: The optional filter expression structure to apply additional matching criteria to the parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datasetparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                dataset_parameter_property = databrew.CfnDataset.DatasetParameterProperty(
                    name="name",
                    type="type",
                
                    # the properties below are optional
                    create_column=False,
                    datetime_options=databrew.CfnDataset.DatetimeOptionsProperty(
                        format="format",
                
                        # the properties below are optional
                        locale_code="localeCode",
                        timezone_offset="timezoneOffset"
                    ),
                    filter=databrew.CfnDataset.FilterExpressionProperty(
                        expression="expression",
                        values_map=[databrew.CfnDataset.FilterValueProperty(
                            value="value",
                            value_reference="valueReference"
                        )]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "type": type,
            }
            if create_column is not None:
                self._values["create_column"] = create_column
            if datetime_options is not None:
                self._values["datetime_options"] = datetime_options
            if filter is not None:
                self._values["filter"] = filter

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the parameter that is used in the dataset's Amazon S3 path.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datasetparameter.html#cfn-databrew-dataset-datasetparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the dataset parameter, can be one of a 'String', 'Number' or 'Datetime'.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datasetparameter.html#cfn-databrew-dataset-datasetparameter-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def create_column(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Optional boolean value that defines whether the captured value of this parameter should be loaded as an additional column in the dataset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datasetparameter.html#cfn-databrew-dataset-datasetparameter-createcolumn
            '''
            result = self._values.get("create_column")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def datetime_options(
            self,
        ) -> typing.Optional[typing.Union["CfnDataset.DatetimeOptionsProperty", _IResolvable_da3f097b]]:
            '''Additional parameter options such as a format and a timezone.

            Required for datetime parameters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datasetparameter.html#cfn-databrew-dataset-datasetparameter-datetimeoptions
            '''
            result = self._values.get("datetime_options")
            return typing.cast(typing.Optional[typing.Union["CfnDataset.DatetimeOptionsProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def filter(
            self,
        ) -> typing.Optional[typing.Union["CfnDataset.FilterExpressionProperty", _IResolvable_da3f097b]]:
            '''The optional filter expression structure to apply additional matching criteria to the parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datasetparameter.html#cfn-databrew-dataset-datasetparameter-filter
            '''
            result = self._values.get("filter")
            return typing.cast(typing.Optional[typing.Union["CfnDataset.FilterExpressionProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatasetParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnDataset.DatetimeOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "format": "format",
            "locale_code": "localeCode",
            "timezone_offset": "timezoneOffset",
        },
    )
    class DatetimeOptionsProperty:
        def __init__(
            self,
            *,
            format: builtins.str,
            locale_code: typing.Optional[builtins.str] = None,
            timezone_offset: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents additional options for correct interpretation of datetime parameters used in the Amazon S3 path of a dataset.

            :param format: Required option, that defines the datetime format used for a date parameter in the Amazon S3 path. Should use only supported datetime specifiers and separation characters, all litera a-z or A-Z character should be escaped with single quotes. E.g. "MM.dd.yyyy-'at'-HH:mm".
            :param locale_code: Optional value for a non-US locale code, needed for correct interpretation of some date formats.
            :param timezone_offset: Optional value for a timezone offset of the datetime parameter value in the Amazon S3 path. Shouldn't be used if Format for this parameter includes timezone fields. If no offset specified, UTC is assumed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datetimeoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                datetime_options_property = databrew.CfnDataset.DatetimeOptionsProperty(
                    format="format",
                
                    # the properties below are optional
                    locale_code="localeCode",
                    timezone_offset="timezoneOffset"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "format": format,
            }
            if locale_code is not None:
                self._values["locale_code"] = locale_code
            if timezone_offset is not None:
                self._values["timezone_offset"] = timezone_offset

        @builtins.property
        def format(self) -> builtins.str:
            '''Required option, that defines the datetime format used for a date parameter in the Amazon S3 path.

            Should use only supported datetime specifiers and separation characters, all litera a-z or A-Z character should be escaped with single quotes. E.g. "MM.dd.yyyy-'at'-HH:mm".

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datetimeoptions.html#cfn-databrew-dataset-datetimeoptions-format
            '''
            result = self._values.get("format")
            assert result is not None, "Required property 'format' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def locale_code(self) -> typing.Optional[builtins.str]:
            '''Optional value for a non-US locale code, needed for correct interpretation of some date formats.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datetimeoptions.html#cfn-databrew-dataset-datetimeoptions-localecode
            '''
            result = self._values.get("locale_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timezone_offset(self) -> typing.Optional[builtins.str]:
            '''Optional value for a timezone offset of the datetime parameter value in the Amazon S3 path.

            Shouldn't be used if Format for this parameter includes timezone fields. If no offset specified, UTC is assumed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datetimeoptions.html#cfn-databrew-dataset-datetimeoptions-timezoneoffset
            '''
            result = self._values.get("timezone_offset")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatetimeOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnDataset.ExcelOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "header_row": "headerRow",
            "sheet_indexes": "sheetIndexes",
            "sheet_names": "sheetNames",
        },
    )
    class ExcelOptionsProperty:
        def __init__(
            self,
            *,
            header_row: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            sheet_indexes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[jsii.Number]]] = None,
            sheet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Represents a set of options that define how DataBrew will interpret a Microsoft Excel file when creating a dataset from that file.

            :param header_row: A variable that specifies whether the first row in the file is parsed as the header. If this value is false, column names are auto-generated.
            :param sheet_indexes: One or more sheet numbers in the Excel file that will be included in the dataset.
            :param sheet_names: One or more named sheets in the Excel file that will be included in the dataset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-exceloptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                excel_options_property = databrew.CfnDataset.ExcelOptionsProperty(
                    header_row=False,
                    sheet_indexes=[123],
                    sheet_names=["sheetNames"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if header_row is not None:
                self._values["header_row"] = header_row
            if sheet_indexes is not None:
                self._values["sheet_indexes"] = sheet_indexes
            if sheet_names is not None:
                self._values["sheet_names"] = sheet_names

        @builtins.property
        def header_row(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A variable that specifies whether the first row in the file is parsed as the header.

            If this value is false, column names are auto-generated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-exceloptions.html#cfn-databrew-dataset-exceloptions-headerrow
            '''
            result = self._values.get("header_row")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def sheet_indexes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]]:
            '''One or more sheet numbers in the Excel file that will be included in the dataset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-exceloptions.html#cfn-databrew-dataset-exceloptions-sheetindexes
            '''
            result = self._values.get("sheet_indexes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]], result)

        @builtins.property
        def sheet_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''One or more named sheets in the Excel file that will be included in the dataset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-exceloptions.html#cfn-databrew-dataset-exceloptions-sheetnames
            '''
            result = self._values.get("sheet_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExcelOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnDataset.FilesLimitProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_files": "maxFiles",
            "order": "order",
            "ordered_by": "orderedBy",
        },
    )
    class FilesLimitProperty:
        def __init__(
            self,
            *,
            max_files: jsii.Number,
            order: typing.Optional[builtins.str] = None,
            ordered_by: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents a limit imposed on number of Amazon S3 files that should be selected for a dataset from a connected Amazon S3 path.

            :param max_files: The number of Amazon S3 files to select.
            :param order: A criteria to use for Amazon S3 files sorting before their selection. By default uses DESCENDING order, i.e. most recent files are selected first. Anotherpossible value is ASCENDING.
            :param ordered_by: A criteria to use for Amazon S3 files sorting before their selection. By default uses LAST_MODIFIED_DATE as a sorting criteria. Currently it's the only allowed value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-fileslimit.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                files_limit_property = databrew.CfnDataset.FilesLimitProperty(
                    max_files=123,
                
                    # the properties below are optional
                    order="order",
                    ordered_by="orderedBy"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_files": max_files,
            }
            if order is not None:
                self._values["order"] = order
            if ordered_by is not None:
                self._values["ordered_by"] = ordered_by

        @builtins.property
        def max_files(self) -> jsii.Number:
            '''The number of Amazon S3 files to select.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-fileslimit.html#cfn-databrew-dataset-fileslimit-maxfiles
            '''
            result = self._values.get("max_files")
            assert result is not None, "Required property 'max_files' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def order(self) -> typing.Optional[builtins.str]:
            '''A criteria to use for Amazon S3 files sorting before their selection.

            By default uses DESCENDING order, i.e. most recent files are selected first. Anotherpossible value is ASCENDING.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-fileslimit.html#cfn-databrew-dataset-fileslimit-order
            '''
            result = self._values.get("order")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ordered_by(self) -> typing.Optional[builtins.str]:
            '''A criteria to use for Amazon S3 files sorting before their selection.

            By default uses LAST_MODIFIED_DATE as a sorting criteria. Currently it's the only allowed value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-fileslimit.html#cfn-databrew-dataset-fileslimit-orderedby
            '''
            result = self._values.get("ordered_by")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilesLimitProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnDataset.FilterExpressionProperty",
        jsii_struct_bases=[],
        name_mapping={"expression": "expression", "values_map": "valuesMap"},
    )
    class FilterExpressionProperty:
        def __init__(
            self,
            *,
            expression: builtins.str,
            values_map: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataset.FilterValueProperty", _IResolvable_da3f097b]]],
        ) -> None:
            '''Represents a structure for defining parameter conditions.

            :param expression: The expression which includes condition names followed by substitution variables, possibly grouped and combined with other conditions. For example, "(starts_with :prefix1 or starts_with :prefix2) and (ends_with :suffix1 or ends_with :suffix2)". Substitution variables should start with ':' symbol.
            :param values_map: The map of substitution variable names to their values used in this filter expression.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filterexpression.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                filter_expression_property = databrew.CfnDataset.FilterExpressionProperty(
                    expression="expression",
                    values_map=[databrew.CfnDataset.FilterValueProperty(
                        value="value",
                        value_reference="valueReference"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "expression": expression,
                "values_map": values_map,
            }

        @builtins.property
        def expression(self) -> builtins.str:
            '''The expression which includes condition names followed by substitution variables, possibly grouped and combined with other conditions.

            For example, "(starts_with :prefix1 or starts_with :prefix2) and (ends_with :suffix1 or ends_with :suffix2)". Substitution variables should start with ':' symbol.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filterexpression.html#cfn-databrew-dataset-filterexpression-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values_map(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataset.FilterValueProperty", _IResolvable_da3f097b]]]:
            '''The map of substitution variable names to their values used in this filter expression.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filterexpression.html#cfn-databrew-dataset-filterexpression-valuesmap
            '''
            result = self._values.get("values_map")
            assert result is not None, "Required property 'values_map' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataset.FilterValueProperty", _IResolvable_da3f097b]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterExpressionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnDataset.FilterValueProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value", "value_reference": "valueReference"},
    )
    class FilterValueProperty:
        def __init__(
            self,
            *,
            value: builtins.str,
            value_reference: builtins.str,
        ) -> None:
            '''Represents a single entry in the ``ValuesMap`` of a ``FilterExpression`` .

            A ``FilterValue`` associates the name of a substitution variable in an expression to its value.

            :param value: The value to be associated with the substitution variable.
            :param value_reference: The substitution variable reference.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filtervalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                filter_value_property = databrew.CfnDataset.FilterValueProperty(
                    value="value",
                    value_reference="valueReference"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "value": value,
                "value_reference": value_reference,
            }

        @builtins.property
        def value(self) -> builtins.str:
            '''The value to be associated with the substitution variable.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filtervalue.html#cfn-databrew-dataset-filtervalue-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value_reference(self) -> builtins.str:
            '''The substitution variable reference.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filtervalue.html#cfn-databrew-dataset-filtervalue-valuereference
            '''
            result = self._values.get("value_reference")
            assert result is not None, "Required property 'value_reference' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnDataset.FormatOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"csv": "csv", "excel": "excel", "json": "json"},
    )
    class FormatOptionsProperty:
        def __init__(
            self,
            *,
            csv: typing.Optional[typing.Union["CfnDataset.CsvOptionsProperty", _IResolvable_da3f097b]] = None,
            excel: typing.Optional[typing.Union["CfnDataset.ExcelOptionsProperty", _IResolvable_da3f097b]] = None,
            json: typing.Optional[typing.Union["CfnDataset.JsonOptionsProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Represents a set of options that define the structure of either comma-separated value (CSV), Excel, or JSON input.

            :param csv: Options that define how CSV input is to be interpreted by DataBrew.
            :param excel: Options that define how Excel input is to be interpreted by DataBrew.
            :param json: Options that define how JSON input is to be interpreted by DataBrew.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-formatoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                format_options_property = databrew.CfnDataset.FormatOptionsProperty(
                    csv=databrew.CfnDataset.CsvOptionsProperty(
                        delimiter="delimiter",
                        header_row=False
                    ),
                    excel=databrew.CfnDataset.ExcelOptionsProperty(
                        header_row=False,
                        sheet_indexes=[123],
                        sheet_names=["sheetNames"]
                    ),
                    json=databrew.CfnDataset.JsonOptionsProperty(
                        multi_line=False
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if csv is not None:
                self._values["csv"] = csv
            if excel is not None:
                self._values["excel"] = excel
            if json is not None:
                self._values["json"] = json

        @builtins.property
        def csv(
            self,
        ) -> typing.Optional[typing.Union["CfnDataset.CsvOptionsProperty", _IResolvable_da3f097b]]:
            '''Options that define how CSV input is to be interpreted by DataBrew.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-formatoptions.html#cfn-databrew-dataset-formatoptions-csv
            '''
            result = self._values.get("csv")
            return typing.cast(typing.Optional[typing.Union["CfnDataset.CsvOptionsProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def excel(
            self,
        ) -> typing.Optional[typing.Union["CfnDataset.ExcelOptionsProperty", _IResolvable_da3f097b]]:
            '''Options that define how Excel input is to be interpreted by DataBrew.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-formatoptions.html#cfn-databrew-dataset-formatoptions-excel
            '''
            result = self._values.get("excel")
            return typing.cast(typing.Optional[typing.Union["CfnDataset.ExcelOptionsProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def json(
            self,
        ) -> typing.Optional[typing.Union["CfnDataset.JsonOptionsProperty", _IResolvable_da3f097b]]:
            '''Options that define how JSON input is to be interpreted by DataBrew.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-formatoptions.html#cfn-databrew-dataset-formatoptions-json
            '''
            result = self._values.get("json")
            return typing.cast(typing.Optional[typing.Union["CfnDataset.JsonOptionsProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FormatOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnDataset.InputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_input_definition": "databaseInputDefinition",
            "data_catalog_input_definition": "dataCatalogInputDefinition",
            "metadata": "metadata",
            "s3_input_definition": "s3InputDefinition",
        },
    )
    class InputProperty:
        def __init__(
            self,
            *,
            database_input_definition: typing.Optional[typing.Union["CfnDataset.DatabaseInputDefinitionProperty", _IResolvable_da3f097b]] = None,
            data_catalog_input_definition: typing.Optional[typing.Union["CfnDataset.DataCatalogInputDefinitionProperty", _IResolvable_da3f097b]] = None,
            metadata: typing.Optional[typing.Union["CfnDataset.MetadataProperty", _IResolvable_da3f097b]] = None,
            s3_input_definition: typing.Optional[typing.Union["CfnDataset.S3LocationProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Represents information on how DataBrew can find data, in either the AWS Glue Data Catalog or Amazon S3.

            :param database_input_definition: Connection information for dataset input files stored in a database.
            :param data_catalog_input_definition: The AWS Glue Data Catalog parameters for the data.
            :param metadata: Contains additional resource information needed for specific datasets.
            :param s3_input_definition: The Amazon S3 location where the data is stored.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-input.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                input_property = databrew.CfnDataset.InputProperty(
                    database_input_definition=databrew.CfnDataset.DatabaseInputDefinitionProperty(
                        glue_connection_name="glueConnectionName",
                
                        # the properties below are optional
                        database_table_name="databaseTableName",
                        query_string="queryString",
                        temp_directory=databrew.CfnDataset.S3LocationProperty(
                            bucket="bucket",
                
                            # the properties below are optional
                            key="key"
                        )
                    ),
                    data_catalog_input_definition=databrew.CfnDataset.DataCatalogInputDefinitionProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        table_name="tableName",
                        temp_directory=databrew.CfnDataset.S3LocationProperty(
                            bucket="bucket",
                
                            # the properties below are optional
                            key="key"
                        )
                    ),
                    metadata=databrew.CfnDataset.MetadataProperty(
                        source_arn="sourceArn"
                    ),
                    s3_input_definition=databrew.CfnDataset.S3LocationProperty(
                        bucket="bucket",
                
                        # the properties below are optional
                        key="key"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if database_input_definition is not None:
                self._values["database_input_definition"] = database_input_definition
            if data_catalog_input_definition is not None:
                self._values["data_catalog_input_definition"] = data_catalog_input_definition
            if metadata is not None:
                self._values["metadata"] = metadata
            if s3_input_definition is not None:
                self._values["s3_input_definition"] = s3_input_definition

        @builtins.property
        def database_input_definition(
            self,
        ) -> typing.Optional[typing.Union["CfnDataset.DatabaseInputDefinitionProperty", _IResolvable_da3f097b]]:
            '''Connection information for dataset input files stored in a database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-input.html#cfn-databrew-dataset-input-databaseinputdefinition
            '''
            result = self._values.get("database_input_definition")
            return typing.cast(typing.Optional[typing.Union["CfnDataset.DatabaseInputDefinitionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def data_catalog_input_definition(
            self,
        ) -> typing.Optional[typing.Union["CfnDataset.DataCatalogInputDefinitionProperty", _IResolvable_da3f097b]]:
            '''The AWS Glue Data Catalog parameters for the data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-input.html#cfn-databrew-dataset-input-datacataloginputdefinition
            '''
            result = self._values.get("data_catalog_input_definition")
            return typing.cast(typing.Optional[typing.Union["CfnDataset.DataCatalogInputDefinitionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def metadata(
            self,
        ) -> typing.Optional[typing.Union["CfnDataset.MetadataProperty", _IResolvable_da3f097b]]:
            '''Contains additional resource information needed for specific datasets.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-input.html#cfn-databrew-dataset-input-metadata
            '''
            result = self._values.get("metadata")
            return typing.cast(typing.Optional[typing.Union["CfnDataset.MetadataProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def s3_input_definition(
            self,
        ) -> typing.Optional[typing.Union["CfnDataset.S3LocationProperty", _IResolvable_da3f097b]]:
            '''The Amazon S3 location where the data is stored.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-input.html#cfn-databrew-dataset-input-s3inputdefinition
            '''
            result = self._values.get("s3_input_definition")
            return typing.cast(typing.Optional[typing.Union["CfnDataset.S3LocationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnDataset.JsonOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"multi_line": "multiLine"},
    )
    class JsonOptionsProperty:
        def __init__(
            self,
            *,
            multi_line: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Represents the JSON-specific options that define how input is to be interpreted by AWS Glue DataBrew .

            :param multi_line: A value that specifies whether JSON input contains embedded new line characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-jsonoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                json_options_property = databrew.CfnDataset.JsonOptionsProperty(
                    multi_line=False
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if multi_line is not None:
                self._values["multi_line"] = multi_line

        @builtins.property
        def multi_line(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A value that specifies whether JSON input contains embedded new line characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-jsonoptions.html#cfn-databrew-dataset-jsonoptions-multiline
            '''
            result = self._values.get("multi_line")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JsonOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnDataset.MetadataProperty",
        jsii_struct_bases=[],
        name_mapping={"source_arn": "sourceArn"},
    )
    class MetadataProperty:
        def __init__(self, *, source_arn: typing.Optional[builtins.str] = None) -> None:
            '''Contains additional resource information needed for specific datasets.

            :param source_arn: The Amazon Resource Name (ARN) associated with the dataset. Currently, DataBrew only supports ARNs from Amazon AppFlow.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-metadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                metadata_property = databrew.CfnDataset.MetadataProperty(
                    source_arn="sourceArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if source_arn is not None:
                self._values["source_arn"] = source_arn

        @builtins.property
        def source_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) associated with the dataset.

            Currently, DataBrew only supports ARNs from Amazon AppFlow.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-metadata.html#cfn-databrew-dataset-metadata-sourcearn
            '''
            result = self._values.get("source_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnDataset.PathOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "files_limit": "filesLimit",
            "last_modified_date_condition": "lastModifiedDateCondition",
            "parameters": "parameters",
        },
    )
    class PathOptionsProperty:
        def __init__(
            self,
            *,
            files_limit: typing.Optional[typing.Union["CfnDataset.FilesLimitProperty", _IResolvable_da3f097b]] = None,
            last_modified_date_condition: typing.Optional[typing.Union["CfnDataset.FilterExpressionProperty", _IResolvable_da3f097b]] = None,
            parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDataset.PathParameterProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''Represents a set of options that define how DataBrew selects files for a given Amazon S3 path in a dataset.

            :param files_limit: If provided, this structure imposes a limit on a number of files that should be selected.
            :param last_modified_date_condition: If provided, this structure defines a date range for matching Amazon S3 objects based on their LastModifiedDate attribute in Amazon S3 .
            :param parameters: A structure that maps names of parameters used in the Amazon S3 path of a dataset to their definitions.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                path_options_property = databrew.CfnDataset.PathOptionsProperty(
                    files_limit=databrew.CfnDataset.FilesLimitProperty(
                        max_files=123,
                
                        # the properties below are optional
                        order="order",
                        ordered_by="orderedBy"
                    ),
                    last_modified_date_condition=databrew.CfnDataset.FilterExpressionProperty(
                        expression="expression",
                        values_map=[databrew.CfnDataset.FilterValueProperty(
                            value="value",
                            value_reference="valueReference"
                        )]
                    ),
                    parameters=[databrew.CfnDataset.PathParameterProperty(
                        dataset_parameter=databrew.CfnDataset.DatasetParameterProperty(
                            name="name",
                            type="type",
                
                            # the properties below are optional
                            create_column=False,
                            datetime_options=databrew.CfnDataset.DatetimeOptionsProperty(
                                format="format",
                
                                # the properties below are optional
                                locale_code="localeCode",
                                timezone_offset="timezoneOffset"
                            ),
                            filter=databrew.CfnDataset.FilterExpressionProperty(
                                expression="expression",
                                values_map=[databrew.CfnDataset.FilterValueProperty(
                                    value="value",
                                    value_reference="valueReference"
                                )]
                            )
                        ),
                        path_parameter_name="pathParameterName"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if files_limit is not None:
                self._values["files_limit"] = files_limit
            if last_modified_date_condition is not None:
                self._values["last_modified_date_condition"] = last_modified_date_condition
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def files_limit(
            self,
        ) -> typing.Optional[typing.Union["CfnDataset.FilesLimitProperty", _IResolvable_da3f097b]]:
            '''If provided, this structure imposes a limit on a number of files that should be selected.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathoptions.html#cfn-databrew-dataset-pathoptions-fileslimit
            '''
            result = self._values.get("files_limit")
            return typing.cast(typing.Optional[typing.Union["CfnDataset.FilesLimitProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def last_modified_date_condition(
            self,
        ) -> typing.Optional[typing.Union["CfnDataset.FilterExpressionProperty", _IResolvable_da3f097b]]:
            '''If provided, this structure defines a date range for matching Amazon S3 objects based on their LastModifiedDate attribute in Amazon S3 .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathoptions.html#cfn-databrew-dataset-pathoptions-lastmodifieddatecondition
            '''
            result = self._values.get("last_modified_date_condition")
            return typing.cast(typing.Optional[typing.Union["CfnDataset.FilterExpressionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataset.PathParameterProperty", _IResolvable_da3f097b]]]]:
            '''A structure that maps names of parameters used in the Amazon S3 path of a dataset to their definitions.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathoptions.html#cfn-databrew-dataset-pathoptions-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDataset.PathParameterProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PathOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnDataset.PathParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dataset_parameter": "datasetParameter",
            "path_parameter_name": "pathParameterName",
        },
    )
    class PathParameterProperty:
        def __init__(
            self,
            *,
            dataset_parameter: typing.Union["CfnDataset.DatasetParameterProperty", _IResolvable_da3f097b],
            path_parameter_name: builtins.str,
        ) -> None:
            '''Represents a single entry in the path parameters of a dataset.

            Each ``PathParameter`` consists of a name and a parameter definition.

            :param dataset_parameter: The path parameter definition.
            :param path_parameter_name: The name of the path parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                path_parameter_property = databrew.CfnDataset.PathParameterProperty(
                    dataset_parameter=databrew.CfnDataset.DatasetParameterProperty(
                        name="name",
                        type="type",
                
                        # the properties below are optional
                        create_column=False,
                        datetime_options=databrew.CfnDataset.DatetimeOptionsProperty(
                            format="format",
                
                            # the properties below are optional
                            locale_code="localeCode",
                            timezone_offset="timezoneOffset"
                        ),
                        filter=databrew.CfnDataset.FilterExpressionProperty(
                            expression="expression",
                            values_map=[databrew.CfnDataset.FilterValueProperty(
                                value="value",
                                value_reference="valueReference"
                            )]
                        )
                    ),
                    path_parameter_name="pathParameterName"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "dataset_parameter": dataset_parameter,
                "path_parameter_name": path_parameter_name,
            }

        @builtins.property
        def dataset_parameter(
            self,
        ) -> typing.Union["CfnDataset.DatasetParameterProperty", _IResolvable_da3f097b]:
            '''The path parameter definition.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathparameter.html#cfn-databrew-dataset-pathparameter-datasetparameter
            '''
            result = self._values.get("dataset_parameter")
            assert result is not None, "Required property 'dataset_parameter' is missing"
            return typing.cast(typing.Union["CfnDataset.DatasetParameterProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def path_parameter_name(self) -> builtins.str:
            '''The name of the path parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathparameter.html#cfn-databrew-dataset-pathparameter-pathparametername
            '''
            result = self._values.get("path_parameter_name")
            assert result is not None, "Required property 'path_parameter_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PathParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnDataset.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key": "key"},
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents an Amazon S3 location (bucket name, bucket owner, and object key) where DataBrew can read input data, or write output from a job.

            :param bucket: The Amazon S3 bucket name.
            :param key: The unique name of the object in the bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                s3_location_property = databrew.CfnDataset.S3LocationProperty(
                    bucket="bucket",
                
                    # the properties below are optional
                    key="key"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket": bucket,
            }
            if key is not None:
                self._values["key"] = key

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The Amazon S3 bucket name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-s3location.html#cfn-databrew-dataset-s3location-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The unique name of the object in the bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-s3location.html#cfn-databrew-dataset-s3location-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_databrew.CfnDatasetProps",
    jsii_struct_bases=[],
    name_mapping={
        "input": "input",
        "name": "name",
        "format": "format",
        "format_options": "formatOptions",
        "path_options": "pathOptions",
        "tags": "tags",
    },
)
class CfnDatasetProps:
    def __init__(
        self,
        *,
        input: typing.Union[CfnDataset.InputProperty, _IResolvable_da3f097b],
        name: builtins.str,
        format: typing.Optional[builtins.str] = None,
        format_options: typing.Optional[typing.Union[CfnDataset.FormatOptionsProperty, _IResolvable_da3f097b]] = None,
        path_options: typing.Optional[typing.Union[CfnDataset.PathOptionsProperty, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataset``.

        :param input: Information on how DataBrew can find the dataset, in either the AWS Glue Data Catalog or Amazon S3 .
        :param name: The unique name of the dataset.
        :param format: The file format of a dataset that is created from an Amazon S3 file or folder.
        :param format_options: A set of options that define how DataBrew interprets the data in the dataset.
        :param path_options: A set of options that defines how DataBrew interprets an Amazon S3 path of the dataset.
        :param tags: Metadata tags that have been applied to the dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_databrew as databrew
            
            cfn_dataset_props = databrew.CfnDatasetProps(
                input=databrew.CfnDataset.InputProperty(
                    database_input_definition=databrew.CfnDataset.DatabaseInputDefinitionProperty(
                        glue_connection_name="glueConnectionName",
            
                        # the properties below are optional
                        database_table_name="databaseTableName",
                        query_string="queryString",
                        temp_directory=databrew.CfnDataset.S3LocationProperty(
                            bucket="bucket",
            
                            # the properties below are optional
                            key="key"
                        )
                    ),
                    data_catalog_input_definition=databrew.CfnDataset.DataCatalogInputDefinitionProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        table_name="tableName",
                        temp_directory=databrew.CfnDataset.S3LocationProperty(
                            bucket="bucket",
            
                            # the properties below are optional
                            key="key"
                        )
                    ),
                    metadata=databrew.CfnDataset.MetadataProperty(
                        source_arn="sourceArn"
                    ),
                    s3_input_definition=databrew.CfnDataset.S3LocationProperty(
                        bucket="bucket",
            
                        # the properties below are optional
                        key="key"
                    )
                ),
                name="name",
            
                # the properties below are optional
                format="format",
                format_options=databrew.CfnDataset.FormatOptionsProperty(
                    csv=databrew.CfnDataset.CsvOptionsProperty(
                        delimiter="delimiter",
                        header_row=False
                    ),
                    excel=databrew.CfnDataset.ExcelOptionsProperty(
                        header_row=False,
                        sheet_indexes=[123],
                        sheet_names=["sheetNames"]
                    ),
                    json=databrew.CfnDataset.JsonOptionsProperty(
                        multi_line=False
                    )
                ),
                path_options=databrew.CfnDataset.PathOptionsProperty(
                    files_limit=databrew.CfnDataset.FilesLimitProperty(
                        max_files=123,
            
                        # the properties below are optional
                        order="order",
                        ordered_by="orderedBy"
                    ),
                    last_modified_date_condition=databrew.CfnDataset.FilterExpressionProperty(
                        expression="expression",
                        values_map=[databrew.CfnDataset.FilterValueProperty(
                            value="value",
                            value_reference="valueReference"
                        )]
                    ),
                    parameters=[databrew.CfnDataset.PathParameterProperty(
                        dataset_parameter=databrew.CfnDataset.DatasetParameterProperty(
                            name="name",
                            type="type",
            
                            # the properties below are optional
                            create_column=False,
                            datetime_options=databrew.CfnDataset.DatetimeOptionsProperty(
                                format="format",
            
                                # the properties below are optional
                                locale_code="localeCode",
                                timezone_offset="timezoneOffset"
                            ),
                            filter=databrew.CfnDataset.FilterExpressionProperty(
                                expression="expression",
                                values_map=[databrew.CfnDataset.FilterValueProperty(
                                    value="value",
                                    value_reference="valueReference"
                                )]
                            )
                        ),
                        path_parameter_name="pathParameterName"
                    )]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "input": input,
            "name": name,
        }
        if format is not None:
            self._values["format"] = format
        if format_options is not None:
            self._values["format_options"] = format_options
        if path_options is not None:
            self._values["path_options"] = path_options
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def input(self) -> typing.Union[CfnDataset.InputProperty, _IResolvable_da3f097b]:
        '''Information on how DataBrew can find the dataset, in either the AWS Glue Data Catalog or Amazon S3 .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html#cfn-databrew-dataset-input
        '''
        result = self._values.get("input")
        assert result is not None, "Required property 'input' is missing"
        return typing.cast(typing.Union[CfnDataset.InputProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The unique name of the dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html#cfn-databrew-dataset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def format(self) -> typing.Optional[builtins.str]:
        '''The file format of a dataset that is created from an Amazon S3 file or folder.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html#cfn-databrew-dataset-format
        '''
        result = self._values.get("format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def format_options(
        self,
    ) -> typing.Optional[typing.Union[CfnDataset.FormatOptionsProperty, _IResolvable_da3f097b]]:
        '''A set of options that define how DataBrew interprets the data in the dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html#cfn-databrew-dataset-formatoptions
        '''
        result = self._values.get("format_options")
        return typing.cast(typing.Optional[typing.Union[CfnDataset.FormatOptionsProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def path_options(
        self,
    ) -> typing.Optional[typing.Union[CfnDataset.PathOptionsProperty, _IResolvable_da3f097b]]:
        '''A set of options that defines how DataBrew interprets an Amazon S3 path of the dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html#cfn-databrew-dataset-pathoptions
        '''
        result = self._values.get("path_options")
        return typing.cast(typing.Optional[typing.Union[CfnDataset.PathOptionsProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata tags that have been applied to the dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html#cfn-databrew-dataset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatasetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnJob(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_databrew.CfnJob",
):
    '''A CloudFormation ``AWS::DataBrew::Job``.

    Specifies a new DataBrew job.

    :cloudformationResource: AWS::DataBrew::Job
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_databrew as databrew
        
        # parameters: Any
        
        cfn_job = databrew.CfnJob(self, "MyCfnJob",
            name="name",
            role_arn="roleArn",
            type="type",
        
            # the properties below are optional
            database_outputs=[databrew.CfnJob.DatabaseOutputProperty(
                database_options=databrew.CfnJob.DatabaseTableOutputOptionsProperty(
                    table_name="tableName",
        
                    # the properties below are optional
                    temp_directory=databrew.CfnJob.S3LocationProperty(
                        bucket="bucket",
        
                        # the properties below are optional
                        bucket_owner="bucketOwner",
                        key="key"
                    )
                ),
                glue_connection_name="glueConnectionName",
        
                # the properties below are optional
                database_output_mode="databaseOutputMode"
            )],
            data_catalog_outputs=[databrew.CfnJob.DataCatalogOutputProperty(
                database_name="databaseName",
                table_name="tableName",
        
                # the properties below are optional
                catalog_id="catalogId",
                database_options=databrew.CfnJob.DatabaseTableOutputOptionsProperty(
                    table_name="tableName",
        
                    # the properties below are optional
                    temp_directory=databrew.CfnJob.S3LocationProperty(
                        bucket="bucket",
        
                        # the properties below are optional
                        bucket_owner="bucketOwner",
                        key="key"
                    )
                ),
                overwrite=False,
                s3_options=databrew.CfnJob.S3TableOutputOptionsProperty(
                    location=databrew.CfnJob.S3LocationProperty(
                        bucket="bucket",
        
                        # the properties below are optional
                        bucket_owner="bucketOwner",
                        key="key"
                    )
                )
            )],
            dataset_name="datasetName",
            encryption_key_arn="encryptionKeyArn",
            encryption_mode="encryptionMode",
            job_sample=databrew.CfnJob.JobSampleProperty(
                mode="mode",
                size=123
            ),
            log_subscription="logSubscription",
            max_capacity=123,
            max_retries=123,
            output_location=databrew.CfnJob.OutputLocationProperty(
                bucket="bucket",
        
                # the properties below are optional
                bucket_owner="bucketOwner",
                key="key"
            ),
            outputs=[databrew.CfnJob.OutputProperty(
                location=databrew.CfnJob.S3LocationProperty(
                    bucket="bucket",
        
                    # the properties below are optional
                    bucket_owner="bucketOwner",
                    key="key"
                ),
        
                # the properties below are optional
                compression_format="compressionFormat",
                format="format",
                format_options=databrew.CfnJob.OutputFormatOptionsProperty(
                    csv=databrew.CfnJob.CsvOutputOptionsProperty(
                        delimiter="delimiter"
                    )
                ),
                max_output_files=123,
                overwrite=False,
                partition_columns=["partitionColumns"]
            )],
            profile_configuration=databrew.CfnJob.ProfileConfigurationProperty(
                column_statistics_configurations=[databrew.CfnJob.ColumnStatisticsConfigurationProperty(
                    statistics=databrew.CfnJob.StatisticsConfigurationProperty(
                        included_statistics=["includedStatistics"],
                        overrides=[databrew.CfnJob.StatisticOverrideProperty(
                            parameters=parameters,
                            statistic="statistic"
                        )]
                    ),
        
                    # the properties below are optional
                    selectors=[databrew.CfnJob.ColumnSelectorProperty(
                        name="name",
                        regex="regex"
                    )]
                )],
                dataset_statistics_configuration=databrew.CfnJob.StatisticsConfigurationProperty(
                    included_statistics=["includedStatistics"],
                    overrides=[databrew.CfnJob.StatisticOverrideProperty(
                        parameters=parameters,
                        statistic="statistic"
                    )]
                ),
                entity_detector_configuration=databrew.CfnJob.EntityDetectorConfigurationProperty(
                    entity_types=["entityTypes"],
        
                    # the properties below are optional
                    allowed_statistics=databrew.CfnJob.AllowedStatisticsProperty(
                        statistics=["statistics"]
                    )
                ),
                profile_columns=[databrew.CfnJob.ColumnSelectorProperty(
                    name="name",
                    regex="regex"
                )]
            ),
            project_name="projectName",
            recipe=databrew.CfnJob.RecipeProperty(
                name="name",
        
                # the properties below are optional
                version="version"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            timeout=123,
            validation_configurations=[databrew.CfnJob.ValidationConfigurationProperty(
                ruleset_arn="rulesetArn",
        
                # the properties below are optional
                validation_mode="validationMode"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        role_arn: builtins.str,
        type: builtins.str,
        database_outputs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnJob.DatabaseOutputProperty", _IResolvable_da3f097b]]]] = None,
        data_catalog_outputs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnJob.DataCatalogOutputProperty", _IResolvable_da3f097b]]]] = None,
        dataset_name: typing.Optional[builtins.str] = None,
        encryption_key_arn: typing.Optional[builtins.str] = None,
        encryption_mode: typing.Optional[builtins.str] = None,
        job_sample: typing.Optional[typing.Union["CfnJob.JobSampleProperty", _IResolvable_da3f097b]] = None,
        log_subscription: typing.Optional[builtins.str] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        output_location: typing.Optional[typing.Union["CfnJob.OutputLocationProperty", _IResolvable_da3f097b]] = None,
        outputs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnJob.OutputProperty", _IResolvable_da3f097b]]]] = None,
        profile_configuration: typing.Optional[typing.Union["CfnJob.ProfileConfigurationProperty", _IResolvable_da3f097b]] = None,
        project_name: typing.Optional[builtins.str] = None,
        recipe: typing.Optional[typing.Union["CfnJob.RecipeProperty", _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        timeout: typing.Optional[jsii.Number] = None,
        validation_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnJob.ValidationConfigurationProperty", _IResolvable_da3f097b]]]] = None,
    ) -> None:
        '''Create a new ``AWS::DataBrew::Job``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The unique name of the job.
        :param role_arn: The Amazon Resource Name (ARN) of the role to be assumed for this job.
        :param type: The job type of the job, which must be one of the following:. - ``PROFILE`` - A job to analyze a dataset, to determine its size, data types, data distribution, and more. - ``RECIPE`` - A job to apply one or more transformations to a dataset.
        :param database_outputs: Represents a list of JDBC database output objects which defines the output destination for a DataBrew recipe job to write into.
        :param data_catalog_outputs: One or more artifacts that represent the AWS Glue Data Catalog output from running the job.
        :param dataset_name: A dataset that the job is to process.
        :param encryption_key_arn: The Amazon Resource Name (ARN) of an encryption key that is used to protect the job output. For more information, see `Encrypting data written by DataBrew jobs <https://docs.aws.amazon.com/databrew/latest/dg/encryption-security-configuration.html>`_
        :param encryption_mode: The encryption mode for the job, which can be one of the following:. - ``SSE-KMS`` - Server-side encryption with keys managed by AWS KMS . - ``SSE-S3`` - Server-side encryption with keys managed by Amazon S3.
        :param job_sample: A sample configuration for profile jobs only, which determines the number of rows on which the profile job is run. If a ``JobSample`` value isn't provided, the default value is used. The default value is CUSTOM_ROWS for the mode parameter and 20,000 for the size parameter.
        :param log_subscription: The current status of Amazon CloudWatch logging for the job.
        :param max_capacity: The maximum number of nodes that can be consumed when the job processes data.
        :param max_retries: The maximum number of times to retry the job after a job run fails.
        :param output_location: ``AWS::DataBrew::Job.OutputLocation``.
        :param outputs: One or more artifacts that represent output from running the job.
        :param profile_configuration: Configuration for profile jobs. Configuration can be used to select columns, do evaluations, and override default parameters of evaluations. When configuration is undefined, the profile job will apply default settings to all supported columns.
        :param project_name: The name of the project that the job is associated with.
        :param recipe: A series of data transformation steps that the job runs.
        :param tags: Metadata tags that have been applied to the job.
        :param timeout: The job's timeout in minutes. A job that attempts to run longer than this timeout period ends with a status of ``TIMEOUT`` .
        :param validation_configurations: List of validation configurations that are applied to the profile job.
        '''
        props = CfnJobProps(
            name=name,
            role_arn=role_arn,
            type=type,
            database_outputs=database_outputs,
            data_catalog_outputs=data_catalog_outputs,
            dataset_name=dataset_name,
            encryption_key_arn=encryption_key_arn,
            encryption_mode=encryption_mode,
            job_sample=job_sample,
            log_subscription=log_subscription,
            max_capacity=max_capacity,
            max_retries=max_retries,
            output_location=output_location,
            outputs=outputs,
            profile_configuration=profile_configuration,
            project_name=project_name,
            recipe=recipe,
            tags=tags,
            timeout=timeout,
            validation_configurations=validation_configurations,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Metadata tags that have been applied to the job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The unique name of the job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the role to be assumed for this job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The job type of the job, which must be one of the following:.

        - ``PROFILE`` - A job to analyze a dataset, to determine its size, data types, data distribution, and more.
        - ``RECIPE`` - A job to apply one or more transformations to a dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="databaseOutputs")
    def database_outputs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.DatabaseOutputProperty", _IResolvable_da3f097b]]]]:
        '''Represents a list of JDBC database output objects which defines the output destination for a DataBrew recipe job to write into.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-databaseoutputs
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.DatabaseOutputProperty", _IResolvable_da3f097b]]]], jsii.get(self, "databaseOutputs"))

    @database_outputs.setter
    def database_outputs(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.DatabaseOutputProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "databaseOutputs", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataCatalogOutputs")
    def data_catalog_outputs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.DataCatalogOutputProperty", _IResolvable_da3f097b]]]]:
        '''One or more artifacts that represent the AWS Glue Data Catalog output from running the job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-datacatalogoutputs
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.DataCatalogOutputProperty", _IResolvable_da3f097b]]]], jsii.get(self, "dataCatalogOutputs"))

    @data_catalog_outputs.setter
    def data_catalog_outputs(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.DataCatalogOutputProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "dataCatalogOutputs", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="datasetName")
    def dataset_name(self) -> typing.Optional[builtins.str]:
        '''A dataset that the job is to process.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-datasetname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetName"))

    @dataset_name.setter
    def dataset_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "datasetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionKeyArn")
    def encryption_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an encryption key that is used to protect the job output.

        For more information, see `Encrypting data written by DataBrew jobs <https://docs.aws.amazon.com/databrew/latest/dg/encryption-security-configuration.html>`_

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-encryptionkeyarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKeyArn"))

    @encryption_key_arn.setter
    def encryption_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "encryptionKeyArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionMode")
    def encryption_mode(self) -> typing.Optional[builtins.str]:
        '''The encryption mode for the job, which can be one of the following:.

        - ``SSE-KMS`` - Server-side encryption with keys managed by AWS KMS .
        - ``SSE-S3`` - Server-side encryption with keys managed by Amazon S3.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-encryptionmode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionMode"))

    @encryption_mode.setter
    def encryption_mode(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "encryptionMode", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobSample")
    def job_sample(
        self,
    ) -> typing.Optional[typing.Union["CfnJob.JobSampleProperty", _IResolvable_da3f097b]]:
        '''A sample configuration for profile jobs only, which determines the number of rows on which the profile job is run.

        If a ``JobSample`` value isn't provided, the default value is used. The default value is CUSTOM_ROWS for the mode parameter and 20,000 for the size parameter.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-jobsample
        '''
        return typing.cast(typing.Optional[typing.Union["CfnJob.JobSampleProperty", _IResolvable_da3f097b]], jsii.get(self, "jobSample"))

    @job_sample.setter
    def job_sample(
        self,
        value: typing.Optional[typing.Union["CfnJob.JobSampleProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "jobSample", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logSubscription")
    def log_subscription(self) -> typing.Optional[builtins.str]:
        '''The current status of Amazon CloudWatch logging for the job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-logsubscription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logSubscription"))

    @log_subscription.setter
    def log_subscription(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "logSubscription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of nodes that can be consumed when the job processes data.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-maxcapacity
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxCapacity"))

    @max_capacity.setter
    def max_capacity(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "maxCapacity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxRetries")
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry the job after a job run fails.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-maxretries
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetries"))

    @max_retries.setter
    def max_retries(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "maxRetries", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outputLocation")
    def output_location(
        self,
    ) -> typing.Optional[typing.Union["CfnJob.OutputLocationProperty", _IResolvable_da3f097b]]:
        '''``AWS::DataBrew::Job.OutputLocation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-outputlocation
        '''
        return typing.cast(typing.Optional[typing.Union["CfnJob.OutputLocationProperty", _IResolvable_da3f097b]], jsii.get(self, "outputLocation"))

    @output_location.setter
    def output_location(
        self,
        value: typing.Optional[typing.Union["CfnJob.OutputLocationProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "outputLocation", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outputs")
    def outputs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.OutputProperty", _IResolvable_da3f097b]]]]:
        '''One or more artifacts that represent output from running the job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-outputs
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.OutputProperty", _IResolvable_da3f097b]]]], jsii.get(self, "outputs"))

    @outputs.setter
    def outputs(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.OutputProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "outputs", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="profileConfiguration")
    def profile_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnJob.ProfileConfigurationProperty", _IResolvable_da3f097b]]:
        '''Configuration for profile jobs.

        Configuration can be used to select columns, do evaluations, and override default parameters of evaluations. When configuration is undefined, the profile job will apply default settings to all supported columns.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-profileconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnJob.ProfileConfigurationProperty", _IResolvable_da3f097b]], jsii.get(self, "profileConfiguration"))

    @profile_configuration.setter
    def profile_configuration(
        self,
        value: typing.Optional[typing.Union["CfnJob.ProfileConfigurationProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "profileConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="projectName")
    def project_name(self) -> typing.Optional[builtins.str]:
        '''The name of the project that the job is associated with.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-projectname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectName"))

    @project_name.setter
    def project_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "projectName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="recipe")
    def recipe(
        self,
    ) -> typing.Optional[typing.Union["CfnJob.RecipeProperty", _IResolvable_da3f097b]]:
        '''A series of data transformation steps that the job runs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-recipe
        '''
        return typing.cast(typing.Optional[typing.Union["CfnJob.RecipeProperty", _IResolvable_da3f097b]], jsii.get(self, "recipe"))

    @recipe.setter
    def recipe(
        self,
        value: typing.Optional[typing.Union["CfnJob.RecipeProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "recipe", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''The job's timeout in minutes.

        A job that attempts to run longer than this timeout period ends with a status of ``TIMEOUT`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-timeout
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "timeout", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="validationConfigurations")
    def validation_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.ValidationConfigurationProperty", _IResolvable_da3f097b]]]]:
        '''List of validation configurations that are applied to the profile job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-validationconfigurations
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.ValidationConfigurationProperty", _IResolvable_da3f097b]]]], jsii.get(self, "validationConfigurations"))

    @validation_configurations.setter
    def validation_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.ValidationConfigurationProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "validationConfigurations", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.AllowedStatisticsProperty",
        jsii_struct_bases=[],
        name_mapping={"statistics": "statistics"},
    )
    class AllowedStatisticsProperty:
        def __init__(self, *, statistics: typing.Sequence[builtins.str]) -> None:
            '''Configuration of statistics that are allowed to be run on columns that contain detected entities.

            When undefined, no statistics will be computed on columns that contain detected entities.

            :param statistics: One or more column statistics to allow for columns that contain detected entities.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-allowedstatistics.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                allowed_statistics_property = databrew.CfnJob.AllowedStatisticsProperty(
                    statistics=["statistics"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "statistics": statistics,
            }

        @builtins.property
        def statistics(self) -> typing.List[builtins.str]:
            '''One or more column statistics to allow for columns that contain detected entities.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-allowedstatistics.html#cfn-databrew-job-allowedstatistics-statistics
            '''
            result = self._values.get("statistics")
            assert result is not None, "Required property 'statistics' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AllowedStatisticsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.ColumnSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "regex": "regex"},
    )
    class ColumnSelectorProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            regex: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Selector of a column from a dataset for profile job configuration.

            One selector includes either a column name or a regular expression.

            :param name: The name of a column from a dataset.
            :param regex: A regular expression for selecting a column from a dataset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnselector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                column_selector_property = databrew.CfnJob.ColumnSelectorProperty(
                    name="name",
                    regex="regex"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if regex is not None:
                self._values["regex"] = regex

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of a column from a dataset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnselector.html#cfn-databrew-job-columnselector-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def regex(self) -> typing.Optional[builtins.str]:
            '''A regular expression for selecting a column from a dataset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnselector.html#cfn-databrew-job-columnselector-regex
            '''
            result = self._values.get("regex")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.ColumnStatisticsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"statistics": "statistics", "selectors": "selectors"},
    )
    class ColumnStatisticsConfigurationProperty:
        def __init__(
            self,
            *,
            statistics: typing.Union["CfnJob.StatisticsConfigurationProperty", _IResolvable_da3f097b],
            selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnJob.ColumnSelectorProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''Configuration for column evaluations for a profile job.

            ColumnStatisticsConfiguration can be used to select evaluations and override parameters of evaluations for particular columns.

            :param statistics: Configuration for evaluations. Statistics can be used to select evaluations and override parameters of evaluations.
            :param selectors: List of column selectors. Selectors can be used to select columns from the dataset. When selectors are undefined, configuration will be applied to all supported columns.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnstatisticsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                # parameters: Any
                
                column_statistics_configuration_property = databrew.CfnJob.ColumnStatisticsConfigurationProperty(
                    statistics=databrew.CfnJob.StatisticsConfigurationProperty(
                        included_statistics=["includedStatistics"],
                        overrides=[databrew.CfnJob.StatisticOverrideProperty(
                            parameters=parameters,
                            statistic="statistic"
                        )]
                    ),
                
                    # the properties below are optional
                    selectors=[databrew.CfnJob.ColumnSelectorProperty(
                        name="name",
                        regex="regex"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "statistics": statistics,
            }
            if selectors is not None:
                self._values["selectors"] = selectors

        @builtins.property
        def statistics(
            self,
        ) -> typing.Union["CfnJob.StatisticsConfigurationProperty", _IResolvable_da3f097b]:
            '''Configuration for evaluations.

            Statistics can be used to select evaluations and override parameters of evaluations.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnstatisticsconfiguration.html#cfn-databrew-job-columnstatisticsconfiguration-statistics
            '''
            result = self._values.get("statistics")
            assert result is not None, "Required property 'statistics' is missing"
            return typing.cast(typing.Union["CfnJob.StatisticsConfigurationProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def selectors(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.ColumnSelectorProperty", _IResolvable_da3f097b]]]]:
            '''List of column selectors.

            Selectors can be used to select columns from the dataset. When selectors are undefined, configuration will be applied to all supported columns.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnstatisticsconfiguration.html#cfn-databrew-job-columnstatisticsconfiguration-selectors
            '''
            result = self._values.get("selectors")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.ColumnSelectorProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnStatisticsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.CsvOutputOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"delimiter": "delimiter"},
    )
    class CsvOutputOptionsProperty:
        def __init__(self, *, delimiter: typing.Optional[builtins.str] = None) -> None:
            '''Represents a set of options that define how DataBrew will write a comma-separated value (CSV) file.

            :param delimiter: A single character that specifies the delimiter used to create CSV job output.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-csvoutputoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                csv_output_options_property = databrew.CfnJob.CsvOutputOptionsProperty(
                    delimiter="delimiter"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if delimiter is not None:
                self._values["delimiter"] = delimiter

        @builtins.property
        def delimiter(self) -> typing.Optional[builtins.str]:
            '''A single character that specifies the delimiter used to create CSV job output.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-csvoutputoptions.html#cfn-databrew-job-csvoutputoptions-delimiter
            '''
            result = self._values.get("delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CsvOutputOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.DataCatalogOutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_name": "databaseName",
            "table_name": "tableName",
            "catalog_id": "catalogId",
            "database_options": "databaseOptions",
            "overwrite": "overwrite",
            "s3_options": "s3Options",
        },
    )
    class DataCatalogOutputProperty:
        def __init__(
            self,
            *,
            database_name: builtins.str,
            table_name: builtins.str,
            catalog_id: typing.Optional[builtins.str] = None,
            database_options: typing.Optional[typing.Union["CfnJob.DatabaseTableOutputOptionsProperty", _IResolvable_da3f097b]] = None,
            overwrite: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            s3_options: typing.Optional[typing.Union["CfnJob.S3TableOutputOptionsProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Represents options that specify how and where in the AWS Glue Data Catalog DataBrew writes the output generated by recipe jobs.

            :param database_name: The name of a database in the Data Catalog.
            :param table_name: The name of a table in the Data Catalog.
            :param catalog_id: The unique identifier of the AWS account that holds the Data Catalog that stores the data.
            :param database_options: Represents options that specify how and where DataBrew writes the database output generated by recipe jobs.
            :param overwrite: A value that, if true, means that any data in the location specified for output is overwritten with new output. Not supported with DatabaseOptions.
            :param s3_options: Represents options that specify how and where DataBrew writes the Amazon S3 output generated by recipe jobs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                data_catalog_output_property = databrew.CfnJob.DataCatalogOutputProperty(
                    database_name="databaseName",
                    table_name="tableName",
                
                    # the properties below are optional
                    catalog_id="catalogId",
                    database_options=databrew.CfnJob.DatabaseTableOutputOptionsProperty(
                        table_name="tableName",
                
                        # the properties below are optional
                        temp_directory=databrew.CfnJob.S3LocationProperty(
                            bucket="bucket",
                
                            # the properties below are optional
                            bucket_owner="bucketOwner",
                            key="key"
                        )
                    ),
                    overwrite=False,
                    s3_options=databrew.CfnJob.S3TableOutputOptionsProperty(
                        location=databrew.CfnJob.S3LocationProperty(
                            bucket="bucket",
                
                            # the properties below are optional
                            bucket_owner="bucketOwner",
                            key="key"
                        )
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "database_name": database_name,
                "table_name": table_name,
            }
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if database_options is not None:
                self._values["database_options"] = database_options
            if overwrite is not None:
                self._values["overwrite"] = overwrite
            if s3_options is not None:
                self._values["s3_options"] = s3_options

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The name of a database in the Data Catalog.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html#cfn-databrew-job-datacatalogoutput-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The name of a table in the Data Catalog.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html#cfn-databrew-job-datacatalogoutput-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier of the AWS account that holds the Data Catalog that stores the data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html#cfn-databrew-job-datacatalogoutput-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_options(
            self,
        ) -> typing.Optional[typing.Union["CfnJob.DatabaseTableOutputOptionsProperty", _IResolvable_da3f097b]]:
            '''Represents options that specify how and where DataBrew writes the database output generated by recipe jobs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html#cfn-databrew-job-datacatalogoutput-databaseoptions
            '''
            result = self._values.get("database_options")
            return typing.cast(typing.Optional[typing.Union["CfnJob.DatabaseTableOutputOptionsProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def overwrite(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A value that, if true, means that any data in the location specified for output is overwritten with new output.

            Not supported with DatabaseOptions.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html#cfn-databrew-job-datacatalogoutput-overwrite
            '''
            result = self._values.get("overwrite")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def s3_options(
            self,
        ) -> typing.Optional[typing.Union["CfnJob.S3TableOutputOptionsProperty", _IResolvable_da3f097b]]:
            '''Represents options that specify how and where DataBrew writes the Amazon S3 output generated by recipe jobs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html#cfn-databrew-job-datacatalogoutput-s3options
            '''
            result = self._values.get("s3_options")
            return typing.cast(typing.Optional[typing.Union["CfnJob.S3TableOutputOptionsProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataCatalogOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.DatabaseOutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_options": "databaseOptions",
            "glue_connection_name": "glueConnectionName",
            "database_output_mode": "databaseOutputMode",
        },
    )
    class DatabaseOutputProperty:
        def __init__(
            self,
            *,
            database_options: typing.Union["CfnJob.DatabaseTableOutputOptionsProperty", _IResolvable_da3f097b],
            glue_connection_name: builtins.str,
            database_output_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents a JDBC database output object which defines the output destination for a DataBrew recipe job to write into.

            :param database_options: Represents options that specify how and where DataBrew writes the database output generated by recipe jobs.
            :param glue_connection_name: The AWS Glue connection that stores the connection information for the target database.
            :param database_output_mode: The output mode to write into the database. Currently supported option: NEW_TABLE.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databaseoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                database_output_property = databrew.CfnJob.DatabaseOutputProperty(
                    database_options=databrew.CfnJob.DatabaseTableOutputOptionsProperty(
                        table_name="tableName",
                
                        # the properties below are optional
                        temp_directory=databrew.CfnJob.S3LocationProperty(
                            bucket="bucket",
                
                            # the properties below are optional
                            bucket_owner="bucketOwner",
                            key="key"
                        )
                    ),
                    glue_connection_name="glueConnectionName",
                
                    # the properties below are optional
                    database_output_mode="databaseOutputMode"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "database_options": database_options,
                "glue_connection_name": glue_connection_name,
            }
            if database_output_mode is not None:
                self._values["database_output_mode"] = database_output_mode

        @builtins.property
        def database_options(
            self,
        ) -> typing.Union["CfnJob.DatabaseTableOutputOptionsProperty", _IResolvable_da3f097b]:
            '''Represents options that specify how and where DataBrew writes the database output generated by recipe jobs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databaseoutput.html#cfn-databrew-job-databaseoutput-databaseoptions
            '''
            result = self._values.get("database_options")
            assert result is not None, "Required property 'database_options' is missing"
            return typing.cast(typing.Union["CfnJob.DatabaseTableOutputOptionsProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def glue_connection_name(self) -> builtins.str:
            '''The AWS Glue connection that stores the connection information for the target database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databaseoutput.html#cfn-databrew-job-databaseoutput-glueconnectionname
            '''
            result = self._values.get("glue_connection_name")
            assert result is not None, "Required property 'glue_connection_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_output_mode(self) -> typing.Optional[builtins.str]:
            '''The output mode to write into the database.

            Currently supported option: NEW_TABLE.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databaseoutput.html#cfn-databrew-job-databaseoutput-databaseoutputmode
            '''
            result = self._values.get("database_output_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.DatabaseTableOutputOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"table_name": "tableName", "temp_directory": "tempDirectory"},
    )
    class DatabaseTableOutputOptionsProperty:
        def __init__(
            self,
            *,
            table_name: builtins.str,
            temp_directory: typing.Optional[typing.Union["CfnJob.S3LocationProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Represents options that specify how and where DataBrew writes the database output generated by recipe jobs.

            :param table_name: A prefix for the name of a table DataBrew will create in the database.
            :param temp_directory: Represents an Amazon S3 location (bucket name and object key) where DataBrew can store intermediate results.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databasetableoutputoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                database_table_output_options_property = databrew.CfnJob.DatabaseTableOutputOptionsProperty(
                    table_name="tableName",
                
                    # the properties below are optional
                    temp_directory=databrew.CfnJob.S3LocationProperty(
                        bucket="bucket",
                
                        # the properties below are optional
                        bucket_owner="bucketOwner",
                        key="key"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "table_name": table_name,
            }
            if temp_directory is not None:
                self._values["temp_directory"] = temp_directory

        @builtins.property
        def table_name(self) -> builtins.str:
            '''A prefix for the name of a table DataBrew will create in the database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databasetableoutputoptions.html#cfn-databrew-job-databasetableoutputoptions-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def temp_directory(
            self,
        ) -> typing.Optional[typing.Union["CfnJob.S3LocationProperty", _IResolvable_da3f097b]]:
            '''Represents an Amazon S3 location (bucket name and object key) where DataBrew can store intermediate results.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databasetableoutputoptions.html#cfn-databrew-job-databasetableoutputoptions-tempdirectory
            '''
            result = self._values.get("temp_directory")
            return typing.cast(typing.Optional[typing.Union["CfnJob.S3LocationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseTableOutputOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.EntityDetectorConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "entity_types": "entityTypes",
            "allowed_statistics": "allowedStatistics",
        },
    )
    class EntityDetectorConfigurationProperty:
        def __init__(
            self,
            *,
            entity_types: typing.Sequence[builtins.str],
            allowed_statistics: typing.Optional[typing.Union["CfnJob.AllowedStatisticsProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Configuration of entity detection for a profile job.

            When undefined, entity detection is disabled.

            :param entity_types: Entity types to detect. Can be any of the following:. - USA_SSN - EMAIL - USA_ITIN - USA_PASSPORT_NUMBER - PHONE_NUMBER - USA_DRIVING_LICENSE - BANK_ACCOUNT - CREDIT_CARD - IP_ADDRESS - MAC_ADDRESS - USA_DEA_NUMBER - USA_HCPCS_CODE - USA_NATIONAL_PROVIDER_IDENTIFIER - USA_NATIONAL_DRUG_CODE - USA_HEALTH_INSURANCE_CLAIM_NUMBER - USA_MEDICARE_BENEFICIARY_IDENTIFIER - USA_CPT_CODE - PERSON_NAME - DATE The Entity type group USA_ALL is also supported, and includes all of the above entity types except PERSON_NAME and DATE.
            :param allowed_statistics: Configuration of statistics that are allowed to be run on columns that contain detected entities. When undefined, no statistics will be computed on columns that contain detected entities.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-entitydetectorconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                entity_detector_configuration_property = databrew.CfnJob.EntityDetectorConfigurationProperty(
                    entity_types=["entityTypes"],
                
                    # the properties below are optional
                    allowed_statistics=databrew.CfnJob.AllowedStatisticsProperty(
                        statistics=["statistics"]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "entity_types": entity_types,
            }
            if allowed_statistics is not None:
                self._values["allowed_statistics"] = allowed_statistics

        @builtins.property
        def entity_types(self) -> typing.List[builtins.str]:
            '''Entity types to detect. Can be any of the following:.

            - USA_SSN
            - EMAIL
            - USA_ITIN
            - USA_PASSPORT_NUMBER
            - PHONE_NUMBER
            - USA_DRIVING_LICENSE
            - BANK_ACCOUNT
            - CREDIT_CARD
            - IP_ADDRESS
            - MAC_ADDRESS
            - USA_DEA_NUMBER
            - USA_HCPCS_CODE
            - USA_NATIONAL_PROVIDER_IDENTIFIER
            - USA_NATIONAL_DRUG_CODE
            - USA_HEALTH_INSURANCE_CLAIM_NUMBER
            - USA_MEDICARE_BENEFICIARY_IDENTIFIER
            - USA_CPT_CODE
            - PERSON_NAME
            - DATE

            The Entity type group USA_ALL is also supported, and includes all of the above entity types except PERSON_NAME and DATE.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-entitydetectorconfiguration.html#cfn-databrew-job-entitydetectorconfiguration-entitytypes
            '''
            result = self._values.get("entity_types")
            assert result is not None, "Required property 'entity_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def allowed_statistics(
            self,
        ) -> typing.Optional[typing.Union["CfnJob.AllowedStatisticsProperty", _IResolvable_da3f097b]]:
            '''Configuration of statistics that are allowed to be run on columns that contain detected entities.

            When undefined, no statistics will be computed on columns that contain detected entities.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-entitydetectorconfiguration.html#cfn-databrew-job-entitydetectorconfiguration-allowedstatistics
            '''
            result = self._values.get("allowed_statistics")
            return typing.cast(typing.Optional[typing.Union["CfnJob.AllowedStatisticsProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EntityDetectorConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.JobSampleProperty",
        jsii_struct_bases=[],
        name_mapping={"mode": "mode", "size": "size"},
    )
    class JobSampleProperty:
        def __init__(
            self,
            *,
            mode: typing.Optional[builtins.str] = None,
            size: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''A sample configuration for profile jobs only, which determines the number of rows on which the profile job is run.

            If a ``JobSample`` value isn't provided, the default is used. The default value is CUSTOM_ROWS for the mode parameter and 20,000 for the size parameter.

            :param mode: A value that determines whether the profile job is run on the entire dataset or a specified number of rows. This value must be one of the following: - FULL_DATASET - The profile job is run on the entire dataset. - CUSTOM_ROWS - The profile job is run on the number of rows specified in the ``Size`` parameter.
            :param size: The ``Size`` parameter is only required when the mode is CUSTOM_ROWS. The profile job is run on the specified number of rows. The maximum value for size is Long.MAX_VALUE. Long.MAX_VALUE = 9223372036854775807

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-jobsample.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                job_sample_property = databrew.CfnJob.JobSampleProperty(
                    mode="mode",
                    size=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if mode is not None:
                self._values["mode"] = mode
            if size is not None:
                self._values["size"] = size

        @builtins.property
        def mode(self) -> typing.Optional[builtins.str]:
            '''A value that determines whether the profile job is run on the entire dataset or a specified number of rows.

            This value must be one of the following:

            - FULL_DATASET - The profile job is run on the entire dataset.
            - CUSTOM_ROWS - The profile job is run on the number of rows specified in the ``Size`` parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-jobsample.html#cfn-databrew-job-jobsample-mode
            '''
            result = self._values.get("mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def size(self) -> typing.Optional[jsii.Number]:
            '''The ``Size`` parameter is only required when the mode is CUSTOM_ROWS.

            The profile job is run on the specified number of rows. The maximum value for size is Long.MAX_VALUE.

            Long.MAX_VALUE = 9223372036854775807

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-jobsample.html#cfn-databrew-job-jobsample-size
            '''
            result = self._values.get("size")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JobSampleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.OutputFormatOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"csv": "csv"},
    )
    class OutputFormatOptionsProperty:
        def __init__(
            self,
            *,
            csv: typing.Optional[typing.Union["CfnJob.CsvOutputOptionsProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Represents a set of options that define the structure of comma-separated (CSV) job output.

            :param csv: Represents a set of options that define the structure of comma-separated value (CSV) job output.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputformatoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                output_format_options_property = databrew.CfnJob.OutputFormatOptionsProperty(
                    csv=databrew.CfnJob.CsvOutputOptionsProperty(
                        delimiter="delimiter"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if csv is not None:
                self._values["csv"] = csv

        @builtins.property
        def csv(
            self,
        ) -> typing.Optional[typing.Union["CfnJob.CsvOutputOptionsProperty", _IResolvable_da3f097b]]:
            '''Represents a set of options that define the structure of comma-separated value (CSV) job output.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputformatoptions.html#cfn-databrew-job-outputformatoptions-csv
            '''
            result = self._values.get("csv")
            return typing.cast(typing.Optional[typing.Union["CfnJob.CsvOutputOptionsProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputFormatOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.OutputLocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "bucket_owner": "bucketOwner", "key": "key"},
    )
    class OutputLocationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            bucket_owner: typing.Optional[builtins.str] = None,
            key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The location in Amazon S3 or AWS Glue Data Catalog where the job writes its output.

            :param bucket: The Amazon S3 bucket name.
            :param bucket_owner: ``CfnJob.OutputLocationProperty.BucketOwner``.
            :param key: The unique name of the object in the bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputlocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                output_location_property = databrew.CfnJob.OutputLocationProperty(
                    bucket="bucket",
                
                    # the properties below are optional
                    bucket_owner="bucketOwner",
                    key="key"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket": bucket,
            }
            if bucket_owner is not None:
                self._values["bucket_owner"] = bucket_owner
            if key is not None:
                self._values["key"] = key

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The Amazon S3 bucket name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputlocation.html#cfn-databrew-job-outputlocation-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bucket_owner(self) -> typing.Optional[builtins.str]:
            '''``CfnJob.OutputLocationProperty.BucketOwner``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputlocation.html#cfn-databrew-job-outputlocation-bucketowner
            '''
            result = self._values.get("bucket_owner")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The unique name of the object in the bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputlocation.html#cfn-databrew-job-outputlocation-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "location": "location",
            "compression_format": "compressionFormat",
            "format": "format",
            "format_options": "formatOptions",
            "max_output_files": "maxOutputFiles",
            "overwrite": "overwrite",
            "partition_columns": "partitionColumns",
        },
    )
    class OutputProperty:
        def __init__(
            self,
            *,
            location: typing.Union["CfnJob.S3LocationProperty", _IResolvable_da3f097b],
            compression_format: typing.Optional[builtins.str] = None,
            format: typing.Optional[builtins.str] = None,
            format_options: typing.Optional[typing.Union["CfnJob.OutputFormatOptionsProperty", _IResolvable_da3f097b]] = None,
            max_output_files: typing.Optional[jsii.Number] = None,
            overwrite: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            partition_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Represents options that specify how and where in Amazon S3 DataBrew writes the output generated by recipe jobs or profile jobs.

            :param location: The location in Amazon S3 where the job writes its output.
            :param compression_format: The compression algorithm used to compress the output text of the job.
            :param format: The data format of the output of the job.
            :param format_options: Represents options that define how DataBrew formats job output files.
            :param max_output_files: The maximum number of files to be generated by the job and written to the output folder.
            :param overwrite: A value that, if true, means that any data in the location specified for output is overwritten with new output.
            :param partition_columns: The names of one or more partition columns for the output of the job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                output_property = databrew.CfnJob.OutputProperty(
                    location=databrew.CfnJob.S3LocationProperty(
                        bucket="bucket",
                
                        # the properties below are optional
                        bucket_owner="bucketOwner",
                        key="key"
                    ),
                
                    # the properties below are optional
                    compression_format="compressionFormat",
                    format="format",
                    format_options=databrew.CfnJob.OutputFormatOptionsProperty(
                        csv=databrew.CfnJob.CsvOutputOptionsProperty(
                            delimiter="delimiter"
                        )
                    ),
                    max_output_files=123,
                    overwrite=False,
                    partition_columns=["partitionColumns"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "location": location,
            }
            if compression_format is not None:
                self._values["compression_format"] = compression_format
            if format is not None:
                self._values["format"] = format
            if format_options is not None:
                self._values["format_options"] = format_options
            if max_output_files is not None:
                self._values["max_output_files"] = max_output_files
            if overwrite is not None:
                self._values["overwrite"] = overwrite
            if partition_columns is not None:
                self._values["partition_columns"] = partition_columns

        @builtins.property
        def location(
            self,
        ) -> typing.Union["CfnJob.S3LocationProperty", _IResolvable_da3f097b]:
            '''The location in Amazon S3 where the job writes its output.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html#cfn-databrew-job-output-location
            '''
            result = self._values.get("location")
            assert result is not None, "Required property 'location' is missing"
            return typing.cast(typing.Union["CfnJob.S3LocationProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def compression_format(self) -> typing.Optional[builtins.str]:
            '''The compression algorithm used to compress the output text of the job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html#cfn-databrew-job-output-compressionformat
            '''
            result = self._values.get("compression_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def format(self) -> typing.Optional[builtins.str]:
            '''The data format of the output of the job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html#cfn-databrew-job-output-format
            '''
            result = self._values.get("format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def format_options(
            self,
        ) -> typing.Optional[typing.Union["CfnJob.OutputFormatOptionsProperty", _IResolvable_da3f097b]]:
            '''Represents options that define how DataBrew formats job output files.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html#cfn-databrew-job-output-formatoptions
            '''
            result = self._values.get("format_options")
            return typing.cast(typing.Optional[typing.Union["CfnJob.OutputFormatOptionsProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def max_output_files(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of files to be generated by the job and written to the output folder.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html#cfn-databrew-job-output-maxoutputfiles
            '''
            result = self._values.get("max_output_files")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def overwrite(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A value that, if true, means that any data in the location specified for output is overwritten with new output.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html#cfn-databrew-job-output-overwrite
            '''
            result = self._values.get("overwrite")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def partition_columns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The names of one or more partition columns for the output of the job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html#cfn-databrew-job-output-partitioncolumns
            '''
            result = self._values.get("partition_columns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.ProfileConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "column_statistics_configurations": "columnStatisticsConfigurations",
            "dataset_statistics_configuration": "datasetStatisticsConfiguration",
            "entity_detector_configuration": "entityDetectorConfiguration",
            "profile_columns": "profileColumns",
        },
    )
    class ProfileConfigurationProperty:
        def __init__(
            self,
            *,
            column_statistics_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnJob.ColumnStatisticsConfigurationProperty", _IResolvable_da3f097b]]]] = None,
            dataset_statistics_configuration: typing.Optional[typing.Union["CfnJob.StatisticsConfigurationProperty", _IResolvable_da3f097b]] = None,
            entity_detector_configuration: typing.Optional[typing.Union["CfnJob.EntityDetectorConfigurationProperty", _IResolvable_da3f097b]] = None,
            profile_columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnJob.ColumnSelectorProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''Configuration for profile jobs.

            Configuration can be used to select columns, do evaluations, and override default parameters of evaluations. When configuration is undefined, the profile job will apply default settings to all supported columns.

            :param column_statistics_configurations: List of configurations for column evaluations. ColumnStatisticsConfigurations are used to select evaluations and override parameters of evaluations for particular columns. When ColumnStatisticsConfigurations is undefined, the profile job will profile all supported columns and run all supported evaluations.
            :param dataset_statistics_configuration: Configuration for inter-column evaluations. Configuration can be used to select evaluations and override parameters of evaluations. When configuration is undefined, the profile job will run all supported inter-column evaluations.
            :param entity_detector_configuration: Configuration of entity detection for a profile job. When undefined, entity detection is disabled.
            :param profile_columns: List of column selectors. ProfileColumns can be used to select columns from the dataset. When ProfileColumns is undefined, the profile job will profile all supported columns.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-profileconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                # parameters: Any
                
                profile_configuration_property = databrew.CfnJob.ProfileConfigurationProperty(
                    column_statistics_configurations=[databrew.CfnJob.ColumnStatisticsConfigurationProperty(
                        statistics=databrew.CfnJob.StatisticsConfigurationProperty(
                            included_statistics=["includedStatistics"],
                            overrides=[databrew.CfnJob.StatisticOverrideProperty(
                                parameters=parameters,
                                statistic="statistic"
                            )]
                        ),
                
                        # the properties below are optional
                        selectors=[databrew.CfnJob.ColumnSelectorProperty(
                            name="name",
                            regex="regex"
                        )]
                    )],
                    dataset_statistics_configuration=databrew.CfnJob.StatisticsConfigurationProperty(
                        included_statistics=["includedStatistics"],
                        overrides=[databrew.CfnJob.StatisticOverrideProperty(
                            parameters=parameters,
                            statistic="statistic"
                        )]
                    ),
                    entity_detector_configuration=databrew.CfnJob.EntityDetectorConfigurationProperty(
                        entity_types=["entityTypes"],
                
                        # the properties below are optional
                        allowed_statistics=databrew.CfnJob.AllowedStatisticsProperty(
                            statistics=["statistics"]
                        )
                    ),
                    profile_columns=[databrew.CfnJob.ColumnSelectorProperty(
                        name="name",
                        regex="regex"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if column_statistics_configurations is not None:
                self._values["column_statistics_configurations"] = column_statistics_configurations
            if dataset_statistics_configuration is not None:
                self._values["dataset_statistics_configuration"] = dataset_statistics_configuration
            if entity_detector_configuration is not None:
                self._values["entity_detector_configuration"] = entity_detector_configuration
            if profile_columns is not None:
                self._values["profile_columns"] = profile_columns

        @builtins.property
        def column_statistics_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.ColumnStatisticsConfigurationProperty", _IResolvable_da3f097b]]]]:
            '''List of configurations for column evaluations.

            ColumnStatisticsConfigurations are used to select evaluations and override parameters of evaluations for particular columns. When ColumnStatisticsConfigurations is undefined, the profile job will profile all supported columns and run all supported evaluations.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-profileconfiguration.html#cfn-databrew-job-profileconfiguration-columnstatisticsconfigurations
            '''
            result = self._values.get("column_statistics_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.ColumnStatisticsConfigurationProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def dataset_statistics_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnJob.StatisticsConfigurationProperty", _IResolvable_da3f097b]]:
            '''Configuration for inter-column evaluations.

            Configuration can be used to select evaluations and override parameters of evaluations. When configuration is undefined, the profile job will run all supported inter-column evaluations.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-profileconfiguration.html#cfn-databrew-job-profileconfiguration-datasetstatisticsconfiguration
            '''
            result = self._values.get("dataset_statistics_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnJob.StatisticsConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def entity_detector_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnJob.EntityDetectorConfigurationProperty", _IResolvable_da3f097b]]:
            '''Configuration of entity detection for a profile job.

            When undefined, entity detection is disabled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-profileconfiguration.html#cfn-databrew-job-profileconfiguration-entitydetectorconfiguration
            '''
            result = self._values.get("entity_detector_configuration")
            return typing.cast(typing.Optional[typing.Union["CfnJob.EntityDetectorConfigurationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def profile_columns(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.ColumnSelectorProperty", _IResolvable_da3f097b]]]]:
            '''List of column selectors.

            ProfileColumns can be used to select columns from the dataset. When ProfileColumns is undefined, the profile job will profile all supported columns.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-profileconfiguration.html#cfn-databrew-job-profileconfiguration-profilecolumns
            '''
            result = self._values.get("profile_columns")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.ColumnSelectorProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProfileConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.RecipeProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "version": "version"},
    )
    class RecipeProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents one or more actions to be performed on a DataBrew dataset.

            :param name: The unique name for the recipe.
            :param version: The identifier for the version for the recipe.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-recipe.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                recipe_property = databrew.CfnJob.RecipeProperty(
                    name="name",
                
                    # the properties below are optional
                    version="version"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def name(self) -> builtins.str:
            '''The unique name for the recipe.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-recipe.html#cfn-databrew-job-recipe-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''The identifier for the version for the recipe.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-recipe.html#cfn-databrew-job-recipe-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecipeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "bucket_owner": "bucketOwner", "key": "key"},
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            bucket_owner: typing.Optional[builtins.str] = None,
            key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents an Amazon S3 location (bucket name, bucket owner, and object key) where DataBrew can read input data, or write output from a job.

            :param bucket: The Amazon S3 bucket name.
            :param bucket_owner: The AWS account ID of the bucket owner.
            :param key: The unique name of the object in the bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                s3_location_property = databrew.CfnJob.S3LocationProperty(
                    bucket="bucket",
                
                    # the properties below are optional
                    bucket_owner="bucketOwner",
                    key="key"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket": bucket,
            }
            if bucket_owner is not None:
                self._values["bucket_owner"] = bucket_owner
            if key is not None:
                self._values["key"] = key

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The Amazon S3 bucket name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3location.html#cfn-databrew-job-s3location-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bucket_owner(self) -> typing.Optional[builtins.str]:
            '''The AWS account ID of the bucket owner.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3location.html#cfn-databrew-job-s3location-bucketowner
            '''
            result = self._values.get("bucket_owner")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The unique name of the object in the bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3location.html#cfn-databrew-job-s3location-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.S3TableOutputOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"location": "location"},
    )
    class S3TableOutputOptionsProperty:
        def __init__(
            self,
            *,
            location: typing.Union["CfnJob.S3LocationProperty", _IResolvable_da3f097b],
        ) -> None:
            '''Represents options that specify how and where DataBrew writes the Amazon S3 output generated by recipe jobs.

            :param location: Represents an Amazon S3 location (bucket name and object key) where DataBrew can write output from a job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3tableoutputoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                s3_table_output_options_property = databrew.CfnJob.S3TableOutputOptionsProperty(
                    location=databrew.CfnJob.S3LocationProperty(
                        bucket="bucket",
                
                        # the properties below are optional
                        bucket_owner="bucketOwner",
                        key="key"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "location": location,
            }

        @builtins.property
        def location(
            self,
        ) -> typing.Union["CfnJob.S3LocationProperty", _IResolvable_da3f097b]:
            '''Represents an Amazon S3 location (bucket name and object key) where DataBrew can write output from a job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3tableoutputoptions.html#cfn-databrew-job-s3tableoutputoptions-location
            '''
            result = self._values.get("location")
            assert result is not None, "Required property 'location' is missing"
            return typing.cast(typing.Union["CfnJob.S3LocationProperty", _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3TableOutputOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.StatisticOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={"parameters": "parameters", "statistic": "statistic"},
    )
    class StatisticOverrideProperty:
        def __init__(self, *, parameters: typing.Any, statistic: builtins.str) -> None:
            '''Override of a particular evaluation for a profile job.

            :param parameters: A map that includes overrides of an evaluation’s parameters.
            :param statistic: The name of an evaluation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                # parameters: Any
                
                statistic_override_property = databrew.CfnJob.StatisticOverrideProperty(
                    parameters=parameters,
                    statistic="statistic"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "parameters": parameters,
                "statistic": statistic,
            }

        @builtins.property
        def parameters(self) -> typing.Any:
            '''A map that includes overrides of an evaluation’s parameters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticoverride.html#cfn-databrew-job-statisticoverride-parameters
            '''
            result = self._values.get("parameters")
            assert result is not None, "Required property 'parameters' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def statistic(self) -> builtins.str:
            '''The name of an evaluation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticoverride.html#cfn-databrew-job-statisticoverride-statistic
            '''
            result = self._values.get("statistic")
            assert result is not None, "Required property 'statistic' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatisticOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.StatisticsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "included_statistics": "includedStatistics",
            "overrides": "overrides",
        },
    )
    class StatisticsConfigurationProperty:
        def __init__(
            self,
            *,
            included_statistics: typing.Optional[typing.Sequence[builtins.str]] = None,
            overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnJob.StatisticOverrideProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''Configuration of evaluations for a profile job.

            This configuration can be used to select evaluations and override the parameters of selected evaluations.

            :param included_statistics: List of included evaluations. When the list is undefined, all supported evaluations will be included.
            :param overrides: List of overrides for evaluations.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                # parameters: Any
                
                statistics_configuration_property = databrew.CfnJob.StatisticsConfigurationProperty(
                    included_statistics=["includedStatistics"],
                    overrides=[databrew.CfnJob.StatisticOverrideProperty(
                        parameters=parameters,
                        statistic="statistic"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if included_statistics is not None:
                self._values["included_statistics"] = included_statistics
            if overrides is not None:
                self._values["overrides"] = overrides

        @builtins.property
        def included_statistics(self) -> typing.Optional[typing.List[builtins.str]]:
            '''List of included evaluations.

            When the list is undefined, all supported evaluations will be included.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticsconfiguration.html#cfn-databrew-job-statisticsconfiguration-includedstatistics
            '''
            result = self._values.get("included_statistics")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def overrides(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.StatisticOverrideProperty", _IResolvable_da3f097b]]]]:
            '''List of overrides for evaluations.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticsconfiguration.html#cfn-databrew-job-statisticsconfiguration-overrides
            '''
            result = self._values.get("overrides")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnJob.StatisticOverrideProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatisticsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnJob.ValidationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ruleset_arn": "rulesetArn",
            "validation_mode": "validationMode",
        },
    )
    class ValidationConfigurationProperty:
        def __init__(
            self,
            *,
            ruleset_arn: builtins.str,
            validation_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration for data quality validation.

            Used to select the Rulesets and Validation Mode to be used in the profile job. When ValidationConfiguration is null, the profile job will run without data quality validation.

            :param ruleset_arn: The Amazon Resource Name (ARN) for the ruleset to be validated in the profile job. The TargetArn of the selected ruleset should be the same as the Amazon Resource Name (ARN) of the dataset that is associated with the profile job.
            :param validation_mode: Mode of data quality validation. Default mode is “CHECK_ALL” which verifies all rules defined in the selected ruleset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-validationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                validation_configuration_property = databrew.CfnJob.ValidationConfigurationProperty(
                    ruleset_arn="rulesetArn",
                
                    # the properties below are optional
                    validation_mode="validationMode"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "ruleset_arn": ruleset_arn,
            }
            if validation_mode is not None:
                self._values["validation_mode"] = validation_mode

        @builtins.property
        def ruleset_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) for the ruleset to be validated in the profile job.

            The TargetArn of the selected ruleset should be the same as the Amazon Resource Name (ARN) of the dataset that is associated with the profile job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-validationconfiguration.html#cfn-databrew-job-validationconfiguration-rulesetarn
            '''
            result = self._values.get("ruleset_arn")
            assert result is not None, "Required property 'ruleset_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def validation_mode(self) -> typing.Optional[builtins.str]:
            '''Mode of data quality validation.

            Default mode is “CHECK_ALL” which verifies all rules defined in the selected ruleset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-validationconfiguration.html#cfn-databrew-job-validationconfiguration-validationmode
            '''
            result = self._values.get("validation_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ValidationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_databrew.CfnJobProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "role_arn": "roleArn",
        "type": "type",
        "database_outputs": "databaseOutputs",
        "data_catalog_outputs": "dataCatalogOutputs",
        "dataset_name": "datasetName",
        "encryption_key_arn": "encryptionKeyArn",
        "encryption_mode": "encryptionMode",
        "job_sample": "jobSample",
        "log_subscription": "logSubscription",
        "max_capacity": "maxCapacity",
        "max_retries": "maxRetries",
        "output_location": "outputLocation",
        "outputs": "outputs",
        "profile_configuration": "profileConfiguration",
        "project_name": "projectName",
        "recipe": "recipe",
        "tags": "tags",
        "timeout": "timeout",
        "validation_configurations": "validationConfigurations",
    },
)
class CfnJobProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        role_arn: builtins.str,
        type: builtins.str,
        database_outputs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnJob.DatabaseOutputProperty, _IResolvable_da3f097b]]]] = None,
        data_catalog_outputs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnJob.DataCatalogOutputProperty, _IResolvable_da3f097b]]]] = None,
        dataset_name: typing.Optional[builtins.str] = None,
        encryption_key_arn: typing.Optional[builtins.str] = None,
        encryption_mode: typing.Optional[builtins.str] = None,
        job_sample: typing.Optional[typing.Union[CfnJob.JobSampleProperty, _IResolvable_da3f097b]] = None,
        log_subscription: typing.Optional[builtins.str] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        output_location: typing.Optional[typing.Union[CfnJob.OutputLocationProperty, _IResolvable_da3f097b]] = None,
        outputs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnJob.OutputProperty, _IResolvable_da3f097b]]]] = None,
        profile_configuration: typing.Optional[typing.Union[CfnJob.ProfileConfigurationProperty, _IResolvable_da3f097b]] = None,
        project_name: typing.Optional[builtins.str] = None,
        recipe: typing.Optional[typing.Union[CfnJob.RecipeProperty, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        timeout: typing.Optional[jsii.Number] = None,
        validation_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnJob.ValidationConfigurationProperty, _IResolvable_da3f097b]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnJob``.

        :param name: The unique name of the job.
        :param role_arn: The Amazon Resource Name (ARN) of the role to be assumed for this job.
        :param type: The job type of the job, which must be one of the following:. - ``PROFILE`` - A job to analyze a dataset, to determine its size, data types, data distribution, and more. - ``RECIPE`` - A job to apply one or more transformations to a dataset.
        :param database_outputs: Represents a list of JDBC database output objects which defines the output destination for a DataBrew recipe job to write into.
        :param data_catalog_outputs: One or more artifacts that represent the AWS Glue Data Catalog output from running the job.
        :param dataset_name: A dataset that the job is to process.
        :param encryption_key_arn: The Amazon Resource Name (ARN) of an encryption key that is used to protect the job output. For more information, see `Encrypting data written by DataBrew jobs <https://docs.aws.amazon.com/databrew/latest/dg/encryption-security-configuration.html>`_
        :param encryption_mode: The encryption mode for the job, which can be one of the following:. - ``SSE-KMS`` - Server-side encryption with keys managed by AWS KMS . - ``SSE-S3`` - Server-side encryption with keys managed by Amazon S3.
        :param job_sample: A sample configuration for profile jobs only, which determines the number of rows on which the profile job is run. If a ``JobSample`` value isn't provided, the default value is used. The default value is CUSTOM_ROWS for the mode parameter and 20,000 for the size parameter.
        :param log_subscription: The current status of Amazon CloudWatch logging for the job.
        :param max_capacity: The maximum number of nodes that can be consumed when the job processes data.
        :param max_retries: The maximum number of times to retry the job after a job run fails.
        :param output_location: ``AWS::DataBrew::Job.OutputLocation``.
        :param outputs: One or more artifacts that represent output from running the job.
        :param profile_configuration: Configuration for profile jobs. Configuration can be used to select columns, do evaluations, and override default parameters of evaluations. When configuration is undefined, the profile job will apply default settings to all supported columns.
        :param project_name: The name of the project that the job is associated with.
        :param recipe: A series of data transformation steps that the job runs.
        :param tags: Metadata tags that have been applied to the job.
        :param timeout: The job's timeout in minutes. A job that attempts to run longer than this timeout period ends with a status of ``TIMEOUT`` .
        :param validation_configurations: List of validation configurations that are applied to the profile job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_databrew as databrew
            
            # parameters: Any
            
            cfn_job_props = databrew.CfnJobProps(
                name="name",
                role_arn="roleArn",
                type="type",
            
                # the properties below are optional
                database_outputs=[databrew.CfnJob.DatabaseOutputProperty(
                    database_options=databrew.CfnJob.DatabaseTableOutputOptionsProperty(
                        table_name="tableName",
            
                        # the properties below are optional
                        temp_directory=databrew.CfnJob.S3LocationProperty(
                            bucket="bucket",
            
                            # the properties below are optional
                            bucket_owner="bucketOwner",
                            key="key"
                        )
                    ),
                    glue_connection_name="glueConnectionName",
            
                    # the properties below are optional
                    database_output_mode="databaseOutputMode"
                )],
                data_catalog_outputs=[databrew.CfnJob.DataCatalogOutputProperty(
                    database_name="databaseName",
                    table_name="tableName",
            
                    # the properties below are optional
                    catalog_id="catalogId",
                    database_options=databrew.CfnJob.DatabaseTableOutputOptionsProperty(
                        table_name="tableName",
            
                        # the properties below are optional
                        temp_directory=databrew.CfnJob.S3LocationProperty(
                            bucket="bucket",
            
                            # the properties below are optional
                            bucket_owner="bucketOwner",
                            key="key"
                        )
                    ),
                    overwrite=False,
                    s3_options=databrew.CfnJob.S3TableOutputOptionsProperty(
                        location=databrew.CfnJob.S3LocationProperty(
                            bucket="bucket",
            
                            # the properties below are optional
                            bucket_owner="bucketOwner",
                            key="key"
                        )
                    )
                )],
                dataset_name="datasetName",
                encryption_key_arn="encryptionKeyArn",
                encryption_mode="encryptionMode",
                job_sample=databrew.CfnJob.JobSampleProperty(
                    mode="mode",
                    size=123
                ),
                log_subscription="logSubscription",
                max_capacity=123,
                max_retries=123,
                output_location=databrew.CfnJob.OutputLocationProperty(
                    bucket="bucket",
            
                    # the properties below are optional
                    bucket_owner="bucketOwner",
                    key="key"
                ),
                outputs=[databrew.CfnJob.OutputProperty(
                    location=databrew.CfnJob.S3LocationProperty(
                        bucket="bucket",
            
                        # the properties below are optional
                        bucket_owner="bucketOwner",
                        key="key"
                    ),
            
                    # the properties below are optional
                    compression_format="compressionFormat",
                    format="format",
                    format_options=databrew.CfnJob.OutputFormatOptionsProperty(
                        csv=databrew.CfnJob.CsvOutputOptionsProperty(
                            delimiter="delimiter"
                        )
                    ),
                    max_output_files=123,
                    overwrite=False,
                    partition_columns=["partitionColumns"]
                )],
                profile_configuration=databrew.CfnJob.ProfileConfigurationProperty(
                    column_statistics_configurations=[databrew.CfnJob.ColumnStatisticsConfigurationProperty(
                        statistics=databrew.CfnJob.StatisticsConfigurationProperty(
                            included_statistics=["includedStatistics"],
                            overrides=[databrew.CfnJob.StatisticOverrideProperty(
                                parameters=parameters,
                                statistic="statistic"
                            )]
                        ),
            
                        # the properties below are optional
                        selectors=[databrew.CfnJob.ColumnSelectorProperty(
                            name="name",
                            regex="regex"
                        )]
                    )],
                    dataset_statistics_configuration=databrew.CfnJob.StatisticsConfigurationProperty(
                        included_statistics=["includedStatistics"],
                        overrides=[databrew.CfnJob.StatisticOverrideProperty(
                            parameters=parameters,
                            statistic="statistic"
                        )]
                    ),
                    entity_detector_configuration=databrew.CfnJob.EntityDetectorConfigurationProperty(
                        entity_types=["entityTypes"],
            
                        # the properties below are optional
                        allowed_statistics=databrew.CfnJob.AllowedStatisticsProperty(
                            statistics=["statistics"]
                        )
                    ),
                    profile_columns=[databrew.CfnJob.ColumnSelectorProperty(
                        name="name",
                        regex="regex"
                    )]
                ),
                project_name="projectName",
                recipe=databrew.CfnJob.RecipeProperty(
                    name="name",
            
                    # the properties below are optional
                    version="version"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                timeout=123,
                validation_configurations=[databrew.CfnJob.ValidationConfigurationProperty(
                    ruleset_arn="rulesetArn",
            
                    # the properties below are optional
                    validation_mode="validationMode"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "role_arn": role_arn,
            "type": type,
        }
        if database_outputs is not None:
            self._values["database_outputs"] = database_outputs
        if data_catalog_outputs is not None:
            self._values["data_catalog_outputs"] = data_catalog_outputs
        if dataset_name is not None:
            self._values["dataset_name"] = dataset_name
        if encryption_key_arn is not None:
            self._values["encryption_key_arn"] = encryption_key_arn
        if encryption_mode is not None:
            self._values["encryption_mode"] = encryption_mode
        if job_sample is not None:
            self._values["job_sample"] = job_sample
        if log_subscription is not None:
            self._values["log_subscription"] = log_subscription
        if max_capacity is not None:
            self._values["max_capacity"] = max_capacity
        if max_retries is not None:
            self._values["max_retries"] = max_retries
        if output_location is not None:
            self._values["output_location"] = output_location
        if outputs is not None:
            self._values["outputs"] = outputs
        if profile_configuration is not None:
            self._values["profile_configuration"] = profile_configuration
        if project_name is not None:
            self._values["project_name"] = project_name
        if recipe is not None:
            self._values["recipe"] = recipe
        if tags is not None:
            self._values["tags"] = tags
        if timeout is not None:
            self._values["timeout"] = timeout
        if validation_configurations is not None:
            self._values["validation_configurations"] = validation_configurations

    @builtins.property
    def name(self) -> builtins.str:
        '''The unique name of the job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the role to be assumed for this job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The job type of the job, which must be one of the following:.

        - ``PROFILE`` - A job to analyze a dataset, to determine its size, data types, data distribution, and more.
        - ``RECIPE`` - A job to apply one or more transformations to a dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database_outputs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnJob.DatabaseOutputProperty, _IResolvable_da3f097b]]]]:
        '''Represents a list of JDBC database output objects which defines the output destination for a DataBrew recipe job to write into.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-databaseoutputs
        '''
        result = self._values.get("database_outputs")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnJob.DatabaseOutputProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def data_catalog_outputs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnJob.DataCatalogOutputProperty, _IResolvable_da3f097b]]]]:
        '''One or more artifacts that represent the AWS Glue Data Catalog output from running the job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-datacatalogoutputs
        '''
        result = self._values.get("data_catalog_outputs")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnJob.DataCatalogOutputProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def dataset_name(self) -> typing.Optional[builtins.str]:
        '''A dataset that the job is to process.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-datasetname
        '''
        result = self._values.get("dataset_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an encryption key that is used to protect the job output.

        For more information, see `Encrypting data written by DataBrew jobs <https://docs.aws.amazon.com/databrew/latest/dg/encryption-security-configuration.html>`_

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-encryptionkeyarn
        '''
        result = self._values.get("encryption_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_mode(self) -> typing.Optional[builtins.str]:
        '''The encryption mode for the job, which can be one of the following:.

        - ``SSE-KMS`` - Server-side encryption with keys managed by AWS KMS .
        - ``SSE-S3`` - Server-side encryption with keys managed by Amazon S3.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-encryptionmode
        '''
        result = self._values.get("encryption_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_sample(
        self,
    ) -> typing.Optional[typing.Union[CfnJob.JobSampleProperty, _IResolvable_da3f097b]]:
        '''A sample configuration for profile jobs only, which determines the number of rows on which the profile job is run.

        If a ``JobSample`` value isn't provided, the default value is used. The default value is CUSTOM_ROWS for the mode parameter and 20,000 for the size parameter.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-jobsample
        '''
        result = self._values.get("job_sample")
        return typing.cast(typing.Optional[typing.Union[CfnJob.JobSampleProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def log_subscription(self) -> typing.Optional[builtins.str]:
        '''The current status of Amazon CloudWatch logging for the job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-logsubscription
        '''
        result = self._values.get("log_subscription")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of nodes that can be consumed when the job processes data.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-maxcapacity
        '''
        result = self._values.get("max_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry the job after a job run fails.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-maxretries
        '''
        result = self._values.get("max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def output_location(
        self,
    ) -> typing.Optional[typing.Union[CfnJob.OutputLocationProperty, _IResolvable_da3f097b]]:
        '''``AWS::DataBrew::Job.OutputLocation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-outputlocation
        '''
        result = self._values.get("output_location")
        return typing.cast(typing.Optional[typing.Union[CfnJob.OutputLocationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def outputs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnJob.OutputProperty, _IResolvable_da3f097b]]]]:
        '''One or more artifacts that represent output from running the job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-outputs
        '''
        result = self._values.get("outputs")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnJob.OutputProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def profile_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnJob.ProfileConfigurationProperty, _IResolvable_da3f097b]]:
        '''Configuration for profile jobs.

        Configuration can be used to select columns, do evaluations, and override default parameters of evaluations. When configuration is undefined, the profile job will apply default settings to all supported columns.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-profileconfiguration
        '''
        result = self._values.get("profile_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnJob.ProfileConfigurationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def project_name(self) -> typing.Optional[builtins.str]:
        '''The name of the project that the job is associated with.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-projectname
        '''
        result = self._values.get("project_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recipe(
        self,
    ) -> typing.Optional[typing.Union[CfnJob.RecipeProperty, _IResolvable_da3f097b]]:
        '''A series of data transformation steps that the job runs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-recipe
        '''
        result = self._values.get("recipe")
        return typing.cast(typing.Optional[typing.Union[CfnJob.RecipeProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata tags that have been applied to the job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''The job's timeout in minutes.

        A job that attempts to run longer than this timeout period ends with a status of ``TIMEOUT`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def validation_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnJob.ValidationConfigurationProperty, _IResolvable_da3f097b]]]]:
        '''List of validation configurations that are applied to the profile job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-validationconfigurations
        '''
        result = self._values.get("validation_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnJob.ValidationConfigurationProperty, _IResolvable_da3f097b]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnJobProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnProject(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_databrew.CfnProject",
):
    '''A CloudFormation ``AWS::DataBrew::Project``.

    Specifies a new AWS Glue DataBrew project.

    :cloudformationResource: AWS::DataBrew::Project
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_databrew as databrew
        
        cfn_project = databrew.CfnProject(self, "MyCfnProject",
            dataset_name="datasetName",
            name="name",
            recipe_name="recipeName",
            role_arn="roleArn",
        
            # the properties below are optional
            sample=databrew.CfnProject.SampleProperty(
                type="type",
        
                # the properties below are optional
                size=123
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        dataset_name: builtins.str,
        name: builtins.str,
        recipe_name: builtins.str,
        role_arn: builtins.str,
        sample: typing.Optional[typing.Union["CfnProject.SampleProperty", _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::DataBrew::Project``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param dataset_name: The dataset that the project is to act upon.
        :param name: The unique name of a project.
        :param recipe_name: The name of a recipe that will be developed during a project session.
        :param role_arn: The Amazon Resource Name (ARN) of the role that will be assumed for this project.
        :param sample: The sample size and sampling type to apply to the data. If this parameter isn't specified, then the sample consists of the first 500 rows from the dataset.
        :param tags: Metadata tags that have been applied to the project.
        '''
        props = CfnProjectProps(
            dataset_name=dataset_name,
            name=name,
            recipe_name=recipe_name,
            role_arn=role_arn,
            sample=sample,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Metadata tags that have been applied to the project.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html#cfn-databrew-project-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="datasetName")
    def dataset_name(self) -> builtins.str:
        '''The dataset that the project is to act upon.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html#cfn-databrew-project-datasetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "datasetName"))

    @dataset_name.setter
    def dataset_name(self, value: builtins.str) -> None:
        jsii.set(self, "datasetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The unique name of a project.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html#cfn-databrew-project-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="recipeName")
    def recipe_name(self) -> builtins.str:
        '''The name of a recipe that will be developed during a project session.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html#cfn-databrew-project-recipename
        '''
        return typing.cast(builtins.str, jsii.get(self, "recipeName"))

    @recipe_name.setter
    def recipe_name(self, value: builtins.str) -> None:
        jsii.set(self, "recipeName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the role that will be assumed for this project.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html#cfn-databrew-project-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sample")
    def sample(
        self,
    ) -> typing.Optional[typing.Union["CfnProject.SampleProperty", _IResolvable_da3f097b]]:
        '''The sample size and sampling type to apply to the data.

        If this parameter isn't specified, then the sample consists of the first 500 rows from the dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html#cfn-databrew-project-sample
        '''
        return typing.cast(typing.Optional[typing.Union["CfnProject.SampleProperty", _IResolvable_da3f097b]], jsii.get(self, "sample"))

    @sample.setter
    def sample(
        self,
        value: typing.Optional[typing.Union["CfnProject.SampleProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "sample", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnProject.SampleProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "size": "size"},
    )
    class SampleProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            size: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Represents the sample size and sampling type for DataBrew to use for interactive data analysis.

            :param type: The way in which DataBrew obtains rows from a dataset.
            :param size: The number of rows in the sample.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-project-sample.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                sample_property = databrew.CfnProject.SampleProperty(
                    type="type",
                
                    # the properties below are optional
                    size=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
            }
            if size is not None:
                self._values["size"] = size

        @builtins.property
        def type(self) -> builtins.str:
            '''The way in which DataBrew obtains rows from a dataset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-project-sample.html#cfn-databrew-project-sample-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def size(self) -> typing.Optional[jsii.Number]:
            '''The number of rows in the sample.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-project-sample.html#cfn-databrew-project-sample-size
            '''
            result = self._values.get("size")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SampleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_databrew.CfnProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "dataset_name": "datasetName",
        "name": "name",
        "recipe_name": "recipeName",
        "role_arn": "roleArn",
        "sample": "sample",
        "tags": "tags",
    },
)
class CfnProjectProps:
    def __init__(
        self,
        *,
        dataset_name: builtins.str,
        name: builtins.str,
        recipe_name: builtins.str,
        role_arn: builtins.str,
        sample: typing.Optional[typing.Union[CfnProject.SampleProperty, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnProject``.

        :param dataset_name: The dataset that the project is to act upon.
        :param name: The unique name of a project.
        :param recipe_name: The name of a recipe that will be developed during a project session.
        :param role_arn: The Amazon Resource Name (ARN) of the role that will be assumed for this project.
        :param sample: The sample size and sampling type to apply to the data. If this parameter isn't specified, then the sample consists of the first 500 rows from the dataset.
        :param tags: Metadata tags that have been applied to the project.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_databrew as databrew
            
            cfn_project_props = databrew.CfnProjectProps(
                dataset_name="datasetName",
                name="name",
                recipe_name="recipeName",
                role_arn="roleArn",
            
                # the properties below are optional
                sample=databrew.CfnProject.SampleProperty(
                    type="type",
            
                    # the properties below are optional
                    size=123
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "dataset_name": dataset_name,
            "name": name,
            "recipe_name": recipe_name,
            "role_arn": role_arn,
        }
        if sample is not None:
            self._values["sample"] = sample
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def dataset_name(self) -> builtins.str:
        '''The dataset that the project is to act upon.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html#cfn-databrew-project-datasetname
        '''
        result = self._values.get("dataset_name")
        assert result is not None, "Required property 'dataset_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The unique name of a project.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html#cfn-databrew-project-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recipe_name(self) -> builtins.str:
        '''The name of a recipe that will be developed during a project session.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html#cfn-databrew-project-recipename
        '''
        result = self._values.get("recipe_name")
        assert result is not None, "Required property 'recipe_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the role that will be assumed for this project.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html#cfn-databrew-project-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sample(
        self,
    ) -> typing.Optional[typing.Union[CfnProject.SampleProperty, _IResolvable_da3f097b]]:
        '''The sample size and sampling type to apply to the data.

        If this parameter isn't specified, then the sample consists of the first 500 rows from the dataset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html#cfn-databrew-project-sample
        '''
        result = self._values.get("sample")
        return typing.cast(typing.Optional[typing.Union[CfnProject.SampleProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata tags that have been applied to the project.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html#cfn-databrew-project-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnRecipe(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_databrew.CfnRecipe",
):
    '''A CloudFormation ``AWS::DataBrew::Recipe``.

    Specifies a new AWS Glue DataBrew transformation recipe.

    :cloudformationResource: AWS::DataBrew::Recipe
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_databrew as databrew
        
        cfn_recipe = databrew.CfnRecipe(self, "MyCfnRecipe",
            name="name",
            steps=[databrew.CfnRecipe.RecipeStepProperty(
                action=databrew.CfnRecipe.ActionProperty(
                    operation="operation",
        
                    # the properties below are optional
                    parameters={
                        "parameters_key": "parameters"
                    }
                ),
        
                # the properties below are optional
                condition_expressions=[databrew.CfnRecipe.ConditionExpressionProperty(
                    condition="condition",
                    target_column="targetColumn",
        
                    # the properties below are optional
                    value="value"
                )]
            )],
        
            # the properties below are optional
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        steps: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnRecipe.RecipeStepProperty", _IResolvable_da3f097b]]],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::DataBrew::Recipe``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The unique name for the recipe.
        :param steps: A list of steps that are defined by the recipe.
        :param description: The description of the recipe.
        :param tags: Metadata tags that have been applied to the recipe.
        '''
        props = CfnRecipeProps(
            name=name, steps=steps, description=description, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Metadata tags that have been applied to the recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html#cfn-databrew-recipe-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The unique name for the recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html#cfn-databrew-recipe-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="steps")
    def steps(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnRecipe.RecipeStepProperty", _IResolvable_da3f097b]]]:
        '''A list of steps that are defined by the recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html#cfn-databrew-recipe-steps
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnRecipe.RecipeStepProperty", _IResolvable_da3f097b]]], jsii.get(self, "steps"))

    @steps.setter
    def steps(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnRecipe.RecipeStepProperty", _IResolvable_da3f097b]]],
    ) -> None:
        jsii.set(self, "steps", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html#cfn-databrew-recipe-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnRecipe.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={"operation": "operation", "parameters": "parameters"},
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            operation: builtins.str,
            parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''Represents a transformation and associated parameters that are used to apply a change to an AWS Glue DataBrew dataset.

            :param operation: The name of a valid DataBrew transformation to be performed on the data.
            :param parameters: Contextual parameters for the transformation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                action_property = databrew.CfnRecipe.ActionProperty(
                    operation="operation",
                
                    # the properties below are optional
                    parameters={
                        "parameters_key": "parameters"
                    }
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "operation": operation,
            }
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def operation(self) -> builtins.str:
            '''The name of a valid DataBrew transformation to be performed on the data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-action.html#cfn-databrew-recipe-action-operation
            '''
            result = self._values.get("operation")
            assert result is not None, "Required property 'operation' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''Contextual parameters for the transformation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-action.html#cfn-databrew-recipe-action-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnRecipe.ConditionExpressionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "condition": "condition",
            "target_column": "targetColumn",
            "value": "value",
        },
    )
    class ConditionExpressionProperty:
        def __init__(
            self,
            *,
            condition: builtins.str,
            target_column: builtins.str,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents an individual condition that evaluates to true or false.

            Conditions are used with recipe actions. The action is only performed for column values where the condition evaluates to true.

            If a recipe requires more than one condition, then the recipe must specify multiple ``ConditionExpression`` elements. Each condition is applied to the rows in a dataset first, before the recipe action is performed.

            :param condition: A specific condition to apply to a recipe action. For more information, see `Recipe structure <https://docs.aws.amazon.com/databrew/latest/dg/recipe-structure.html>`_ in the *AWS Glue DataBrew Developer Guide* .
            :param target_column: A column to apply this condition to.
            :param value: A value that the condition must evaluate to for the condition to succeed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-conditionexpression.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                condition_expression_property = databrew.CfnRecipe.ConditionExpressionProperty(
                    condition="condition",
                    target_column="targetColumn",
                
                    # the properties below are optional
                    value="value"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "condition": condition,
                "target_column": target_column,
            }
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def condition(self) -> builtins.str:
            '''A specific condition to apply to a recipe action.

            For more information, see `Recipe structure <https://docs.aws.amazon.com/databrew/latest/dg/recipe-structure.html>`_ in the *AWS Glue DataBrew Developer Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-conditionexpression.html#cfn-databrew-recipe-conditionexpression-condition
            '''
            result = self._values.get("condition")
            assert result is not None, "Required property 'condition' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target_column(self) -> builtins.str:
            '''A column to apply this condition to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-conditionexpression.html#cfn-databrew-recipe-conditionexpression-targetcolumn
            '''
            result = self._values.get("target_column")
            assert result is not None, "Required property 'target_column' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''A value that the condition must evaluate to for the condition to succeed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-conditionexpression.html#cfn-databrew-recipe-conditionexpression-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionExpressionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnRecipe.DataCatalogInputDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "table_name": "tableName",
            "temp_directory": "tempDirectory",
        },
    )
    class DataCatalogInputDefinitionProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
            table_name: typing.Optional[builtins.str] = None,
            temp_directory: typing.Optional[typing.Union["CfnRecipe.S3LocationProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Represents how metadata stored in the AWS Glue Data Catalog is defined in a DataBrew dataset.

            :param catalog_id: The unique identifier of the AWS account that holds the Data Catalog that stores the data.
            :param database_name: The name of a database in the Data Catalog.
            :param table_name: The name of a database table in the Data Catalog. This table corresponds to a DataBrew dataset.
            :param temp_directory: Represents an Amazon location where DataBrew can store intermediate results.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-datacataloginputdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                data_catalog_input_definition_property = databrew.CfnRecipe.DataCatalogInputDefinitionProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    table_name="tableName",
                    temp_directory=databrew.CfnRecipe.S3LocationProperty(
                        bucket="bucket",
                
                        # the properties below are optional
                        key="key"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if database_name is not None:
                self._values["database_name"] = database_name
            if table_name is not None:
                self._values["table_name"] = table_name
            if temp_directory is not None:
                self._values["temp_directory"] = temp_directory

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier of the AWS account that holds the Data Catalog that stores the data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-datacataloginputdefinition.html#cfn-databrew-recipe-datacataloginputdefinition-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''The name of a database in the Data Catalog.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-datacataloginputdefinition.html#cfn-databrew-recipe-datacataloginputdefinition-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def table_name(self) -> typing.Optional[builtins.str]:
            '''The name of a database table in the Data Catalog.

            This table corresponds to a DataBrew dataset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-datacataloginputdefinition.html#cfn-databrew-recipe-datacataloginputdefinition-tablename
            '''
            result = self._values.get("table_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def temp_directory(
            self,
        ) -> typing.Optional[typing.Union["CfnRecipe.S3LocationProperty", _IResolvable_da3f097b]]:
            '''Represents an Amazon location where DataBrew can store intermediate results.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-datacataloginputdefinition.html#cfn-databrew-recipe-datacataloginputdefinition-tempdirectory
            '''
            result = self._values.get("temp_directory")
            return typing.cast(typing.Optional[typing.Union["CfnRecipe.S3LocationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataCatalogInputDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnRecipe.RecipeParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aggregate_function": "aggregateFunction",
            "base": "base",
            "case_statement": "caseStatement",
            "category_map": "categoryMap",
            "chars_to_remove": "charsToRemove",
            "collapse_consecutive_whitespace": "collapseConsecutiveWhitespace",
            "column_data_type": "columnDataType",
            "column_range": "columnRange",
            "count": "count",
            "custom_characters": "customCharacters",
            "custom_stop_words": "customStopWords",
            "custom_value": "customValue",
            "datasets_columns": "datasetsColumns",
            "date_add_value": "dateAddValue",
            "date_time_format": "dateTimeFormat",
            "date_time_parameters": "dateTimeParameters",
            "delete_other_rows": "deleteOtherRows",
            "delimiter": "delimiter",
            "end_pattern": "endPattern",
            "end_position": "endPosition",
            "end_value": "endValue",
            "expand_contractions": "expandContractions",
            "exponent": "exponent",
            "false_string": "falseString",
            "group_by_agg_function_options": "groupByAggFunctionOptions",
            "group_by_columns": "groupByColumns",
            "hidden_columns": "hiddenColumns",
            "ignore_case": "ignoreCase",
            "include_in_split": "includeInSplit",
            "input": "input",
            "interval": "interval",
            "is_text": "isText",
            "join_keys": "joinKeys",
            "join_type": "joinType",
            "left_columns": "leftColumns",
            "limit": "limit",
            "lower_bound": "lowerBound",
            "map_type": "mapType",
            "mode_type": "modeType",
            "multi_line": "multiLine",
            "num_rows": "numRows",
            "num_rows_after": "numRowsAfter",
            "num_rows_before": "numRowsBefore",
            "order_by_column": "orderByColumn",
            "order_by_columns": "orderByColumns",
            "other": "other",
            "pattern": "pattern",
            "pattern_option1": "patternOption1",
            "pattern_option2": "patternOption2",
            "pattern_options": "patternOptions",
            "period": "period",
            "position": "position",
            "remove_all_punctuation": "removeAllPunctuation",
            "remove_all_quotes": "removeAllQuotes",
            "remove_all_whitespace": "removeAllWhitespace",
            "remove_custom_characters": "removeCustomCharacters",
            "remove_custom_value": "removeCustomValue",
            "remove_leading_and_trailing_punctuation": "removeLeadingAndTrailingPunctuation",
            "remove_leading_and_trailing_quotes": "removeLeadingAndTrailingQuotes",
            "remove_leading_and_trailing_whitespace": "removeLeadingAndTrailingWhitespace",
            "remove_letters": "removeLetters",
            "remove_numbers": "removeNumbers",
            "remove_source_column": "removeSourceColumn",
            "remove_special_characters": "removeSpecialCharacters",
            "right_columns": "rightColumns",
            "sample_size": "sampleSize",
            "sample_type": "sampleType",
            "secondary_inputs": "secondaryInputs",
            "second_input": "secondInput",
            "sheet_indexes": "sheetIndexes",
            "sheet_names": "sheetNames",
            "source_column": "sourceColumn",
            "source_column1": "sourceColumn1",
            "source_column2": "sourceColumn2",
            "source_columns": "sourceColumns",
            "start_column_index": "startColumnIndex",
            "start_pattern": "startPattern",
            "start_position": "startPosition",
            "start_value": "startValue",
            "stemming_mode": "stemmingMode",
            "step_count": "stepCount",
            "step_index": "stepIndex",
            "stop_words_mode": "stopWordsMode",
            "strategy": "strategy",
            "target_column": "targetColumn",
            "target_column_names": "targetColumnNames",
            "target_date_format": "targetDateFormat",
            "target_index": "targetIndex",
            "time_zone": "timeZone",
            "tokenizer_pattern": "tokenizerPattern",
            "true_string": "trueString",
            "udf_lang": "udfLang",
            "units": "units",
            "unpivot_column": "unpivotColumn",
            "upper_bound": "upperBound",
            "use_new_data_frame": "useNewDataFrame",
            "value": "value",
            "value1": "value1",
            "value2": "value2",
            "value_column": "valueColumn",
            "view_frame": "viewFrame",
        },
    )
    class RecipeParametersProperty:
        def __init__(
            self,
            *,
            aggregate_function: typing.Optional[builtins.str] = None,
            base: typing.Optional[builtins.str] = None,
            case_statement: typing.Optional[builtins.str] = None,
            category_map: typing.Optional[builtins.str] = None,
            chars_to_remove: typing.Optional[builtins.str] = None,
            collapse_consecutive_whitespace: typing.Optional[builtins.str] = None,
            column_data_type: typing.Optional[builtins.str] = None,
            column_range: typing.Optional[builtins.str] = None,
            count: typing.Optional[builtins.str] = None,
            custom_characters: typing.Optional[builtins.str] = None,
            custom_stop_words: typing.Optional[builtins.str] = None,
            custom_value: typing.Optional[builtins.str] = None,
            datasets_columns: typing.Optional[builtins.str] = None,
            date_add_value: typing.Optional[builtins.str] = None,
            date_time_format: typing.Optional[builtins.str] = None,
            date_time_parameters: typing.Optional[builtins.str] = None,
            delete_other_rows: typing.Optional[builtins.str] = None,
            delimiter: typing.Optional[builtins.str] = None,
            end_pattern: typing.Optional[builtins.str] = None,
            end_position: typing.Optional[builtins.str] = None,
            end_value: typing.Optional[builtins.str] = None,
            expand_contractions: typing.Optional[builtins.str] = None,
            exponent: typing.Optional[builtins.str] = None,
            false_string: typing.Optional[builtins.str] = None,
            group_by_agg_function_options: typing.Optional[builtins.str] = None,
            group_by_columns: typing.Optional[builtins.str] = None,
            hidden_columns: typing.Optional[builtins.str] = None,
            ignore_case: typing.Optional[builtins.str] = None,
            include_in_split: typing.Optional[builtins.str] = None,
            input: typing.Any = None,
            interval: typing.Optional[builtins.str] = None,
            is_text: typing.Optional[builtins.str] = None,
            join_keys: typing.Optional[builtins.str] = None,
            join_type: typing.Optional[builtins.str] = None,
            left_columns: typing.Optional[builtins.str] = None,
            limit: typing.Optional[builtins.str] = None,
            lower_bound: typing.Optional[builtins.str] = None,
            map_type: typing.Optional[builtins.str] = None,
            mode_type: typing.Optional[builtins.str] = None,
            multi_line: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            num_rows: typing.Optional[builtins.str] = None,
            num_rows_after: typing.Optional[builtins.str] = None,
            num_rows_before: typing.Optional[builtins.str] = None,
            order_by_column: typing.Optional[builtins.str] = None,
            order_by_columns: typing.Optional[builtins.str] = None,
            other: typing.Optional[builtins.str] = None,
            pattern: typing.Optional[builtins.str] = None,
            pattern_option1: typing.Optional[builtins.str] = None,
            pattern_option2: typing.Optional[builtins.str] = None,
            pattern_options: typing.Optional[builtins.str] = None,
            period: typing.Optional[builtins.str] = None,
            position: typing.Optional[builtins.str] = None,
            remove_all_punctuation: typing.Optional[builtins.str] = None,
            remove_all_quotes: typing.Optional[builtins.str] = None,
            remove_all_whitespace: typing.Optional[builtins.str] = None,
            remove_custom_characters: typing.Optional[builtins.str] = None,
            remove_custom_value: typing.Optional[builtins.str] = None,
            remove_leading_and_trailing_punctuation: typing.Optional[builtins.str] = None,
            remove_leading_and_trailing_quotes: typing.Optional[builtins.str] = None,
            remove_leading_and_trailing_whitespace: typing.Optional[builtins.str] = None,
            remove_letters: typing.Optional[builtins.str] = None,
            remove_numbers: typing.Optional[builtins.str] = None,
            remove_source_column: typing.Optional[builtins.str] = None,
            remove_special_characters: typing.Optional[builtins.str] = None,
            right_columns: typing.Optional[builtins.str] = None,
            sample_size: typing.Optional[builtins.str] = None,
            sample_type: typing.Optional[builtins.str] = None,
            secondary_inputs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnRecipe.SecondaryInputProperty", _IResolvable_da3f097b]]]] = None,
            second_input: typing.Optional[builtins.str] = None,
            sheet_indexes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[jsii.Number]]] = None,
            sheet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            source_column: typing.Optional[builtins.str] = None,
            source_column1: typing.Optional[builtins.str] = None,
            source_column2: typing.Optional[builtins.str] = None,
            source_columns: typing.Optional[builtins.str] = None,
            start_column_index: typing.Optional[builtins.str] = None,
            start_pattern: typing.Optional[builtins.str] = None,
            start_position: typing.Optional[builtins.str] = None,
            start_value: typing.Optional[builtins.str] = None,
            stemming_mode: typing.Optional[builtins.str] = None,
            step_count: typing.Optional[builtins.str] = None,
            step_index: typing.Optional[builtins.str] = None,
            stop_words_mode: typing.Optional[builtins.str] = None,
            strategy: typing.Optional[builtins.str] = None,
            target_column: typing.Optional[builtins.str] = None,
            target_column_names: typing.Optional[builtins.str] = None,
            target_date_format: typing.Optional[builtins.str] = None,
            target_index: typing.Optional[builtins.str] = None,
            time_zone: typing.Optional[builtins.str] = None,
            tokenizer_pattern: typing.Optional[builtins.str] = None,
            true_string: typing.Optional[builtins.str] = None,
            udf_lang: typing.Optional[builtins.str] = None,
            units: typing.Optional[builtins.str] = None,
            unpivot_column: typing.Optional[builtins.str] = None,
            upper_bound: typing.Optional[builtins.str] = None,
            use_new_data_frame: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
            value1: typing.Optional[builtins.str] = None,
            value2: typing.Optional[builtins.str] = None,
            value_column: typing.Optional[builtins.str] = None,
            view_frame: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Parameters that are used as inputs for various recipe actions.

            The parameters are specific to the context in which they're used.

            :param aggregate_function: The name of an aggregation function to apply.
            :param base: The number of digits used in a counting system.
            :param case_statement: A case statement associated with a recipe.
            :param category_map: A category map used for one-hot encoding.
            :param chars_to_remove: Characters to remove from a step that applies one-hot encoding or tokenization.
            :param collapse_consecutive_whitespace: Remove any non-word non-punctuation character.
            :param column_data_type: The data type of the column.
            :param column_range: A range of columns to which a step is applied.
            :param count: The number of times a string needs to be repeated.
            :param custom_characters: One or more characters that can be substituted or removed, depending on the context.
            :param custom_stop_words: A list of words to ignore in a step that applies word tokenization.
            :param custom_value: A list of custom values to use in a step that requires that you provide a value to finish the operation.
            :param datasets_columns: A list of the dataset columns included in a project.
            :param date_add_value: A value that specifies how many units of time to add or subtract for a date math operation.
            :param date_time_format: A date format to apply to a date.
            :param date_time_parameters: A set of parameters associated with a datetime.
            :param delete_other_rows: Determines whether unmapped rows in a categorical mapping should be deleted.
            :param delimiter: The delimiter to use when parsing separated values in a text file.
            :param end_pattern: The end pattern to locate.
            :param end_position: The end position to locate.
            :param end_value: The end value to locate.
            :param expand_contractions: A list of word contractions and what they expand to. For eample: *can't* ; *cannot* ; *can not* .
            :param exponent: The exponent to apply in an exponential operation.
            :param false_string: A value that represents ``FALSE`` .
            :param group_by_agg_function_options: Specifies options to apply to the ``GROUP BY`` used in an aggregation.
            :param group_by_columns: The columns to use in the ``GROUP BY`` clause.
            :param hidden_columns: A list of columns to hide.
            :param ignore_case: Indicates that lower and upper case letters are treated equally.
            :param include_in_split: Indicates if this column is participating in a split transform.
            :param input: The input location to load the dataset from - Amazon S3 or AWS Glue Data Catalog .
            :param interval: The number of characters to split by.
            :param is_text: Indicates if the content is text.
            :param join_keys: The keys or columns involved in a join.
            :param join_type: The type of join to use, for example, ``INNER JOIN`` , ``OUTER JOIN`` , and so on.
            :param left_columns: The columns on the left side of the join.
            :param limit: The number of times to perform ``split`` or ``replaceBy`` in a string.
            :param lower_bound: The lower boundary for a value.
            :param map_type: The type of mappings to apply to construct a new dynamic frame.
            :param mode_type: Determines the manner in which mode value is calculated, in case there is more than one mode value. Valid values: ``NONE`` | ``AVERAGE`` | ``MINIMUM`` | ``MAXIMUM``
            :param multi_line: Specifies whether JSON input contains embedded new line characters.
            :param num_rows: The number of rows to consider in a window.
            :param num_rows_after: The number of rows to consider after the current row in a window.
            :param num_rows_before: The number of rows to consider before the current row in a window.
            :param order_by_column: A column to sort the results by.
            :param order_by_columns: The columns to sort the results by.
            :param other: The value to assign to unmapped cells, in categorical mapping.
            :param pattern: The pattern to locate.
            :param pattern_option1: The starting pattern to split between.
            :param pattern_option2: The ending pattern to split between.
            :param pattern_options: For splitting by multiple delimiters: A JSON-encoded string that lists the patterns in the format. For example: ``[{\\"pattern\\":\\"1\\",\\"includeInSplit\\":true}]``
            :param period: The size of the rolling window.
            :param position: The character index within a string.
            :param remove_all_punctuation: If ``true`` , removes all of the following characters: ``.`` ``.!`` ``.,`` ``.?``.
            :param remove_all_quotes: If ``true`` , removes all single quotes and double quotes.
            :param remove_all_whitespace: If ``true`` , removes all whitespaces from the value.
            :param remove_custom_characters: If ``true`` , removes all chraracters specified by ``CustomCharacters`` .
            :param remove_custom_value: If ``true`` , removes all chraracters specified by ``CustomValue`` .
            :param remove_leading_and_trailing_punctuation: If ``true`` , removes the following characters if they occur at the start or end of the value: ``.`` ``!`` ``,`` ``?``.
            :param remove_leading_and_trailing_quotes: If ``true`` , removes single quotes and double quotes from the beginning and end of the value.
            :param remove_leading_and_trailing_whitespace: If ``true`` , removes all whitespaces from the beginning and end of the value.
            :param remove_letters: If ``true`` , removes all uppercase and lowercase alphabetic characters (A through Z; a through z).
            :param remove_numbers: If ``true`` , removes all numeric characters (0 through 9).
            :param remove_source_column: If ``true`` , the source column will be removed after un-nesting that column. (Used with nested column types, such as Map, Struct, or Array.)
            :param remove_special_characters: If ``true`` , removes all of the following characters: `! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \\ ] ^ _ `` { | } ~``
            :param right_columns: The columns on the right side of a join.
            :param sample_size: The number of rows in the sample.
            :param sample_type: The sampling type to apply to the dataset. Valid values: ``FIRST_N`` | ``LAST_N`` | ``RANDOM``
            :param secondary_inputs: A list of secondary inputs in a UNION transform.
            :param second_input: A object value to indicate the second dataset used in a join.
            :param sheet_indexes: One or more sheet numbers in the Excel file, which will be included in a dataset.
            :param sheet_names: Oone or more named sheets in the Excel file, which will be included in a dataset.
            :param source_column: A source column needed for an operation, step, or transform.
            :param source_column1: A source column needed for an operation, step, or transform.
            :param source_column2: A source column needed for an operation, step, or transform.
            :param source_columns: A list of source columns needed for an operation, step, or transform.
            :param start_column_index: The index number of the first column used by an operation, step, or transform.
            :param start_pattern: The starting pattern to locate.
            :param start_position: The starting position to locate.
            :param start_value: The starting value to locate.
            :param stemming_mode: Indicates this operation uses stems and lemmas (base words) for word tokenization.
            :param step_count: The total number of transforms in this recipe.
            :param step_index: The index ID of a step.
            :param stop_words_mode: Indicates this operation uses stop words as part of word tokenization.
            :param strategy: The resolution strategy to apply in resolving ambiguities.
            :param target_column: The column targeted by this operation.
            :param target_column_names: The names to give columns altered by this operation.
            :param target_date_format: The date format to convert to.
            :param target_index: The index number of an object that is targeted by this operation.
            :param time_zone: The current timezone that you want to use for dates.
            :param tokenizer_pattern: A regex expression to use when splitting text into terms, also called words or tokens.
            :param true_string: A value to use to represent ``TRUE`` .
            :param udf_lang: The language that's used in the user-defined function.
            :param units: Specifies a unit of time. For example: ``MINUTES`` ; ``SECONDS`` ; ``HOURS`` ; etc.
            :param unpivot_column: Cast columns as rows, so that each value is a different row in a single column.
            :param upper_bound: The upper boundary for a value.
            :param use_new_data_frame: Create a new container to hold a dataset.
            :param value: A static value that can be used in a comparison, a substitution, or in another context-specific way. A ``Value`` can be a number, string, or other datatype, depending on the recipe action in which it's used.
            :param value1: A value that's used by this operation.
            :param value2: A value that's used by this operation.
            :param value_column: The column that is provided as a value that's used by this operation.
            :param view_frame: The subset of rows currently available for viewing.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                # input: Any
                
                recipe_parameters_property = databrew.CfnRecipe.RecipeParametersProperty(
                    aggregate_function="aggregateFunction",
                    base="base",
                    case_statement="caseStatement",
                    category_map="categoryMap",
                    chars_to_remove="charsToRemove",
                    collapse_consecutive_whitespace="collapseConsecutiveWhitespace",
                    column_data_type="columnDataType",
                    column_range="columnRange",
                    count="count",
                    custom_characters="customCharacters",
                    custom_stop_words="customStopWords",
                    custom_value="customValue",
                    datasets_columns="datasetsColumns",
                    date_add_value="dateAddValue",
                    date_time_format="dateTimeFormat",
                    date_time_parameters="dateTimeParameters",
                    delete_other_rows="deleteOtherRows",
                    delimiter="delimiter",
                    end_pattern="endPattern",
                    end_position="endPosition",
                    end_value="endValue",
                    expand_contractions="expandContractions",
                    exponent="exponent",
                    false_string="falseString",
                    group_by_agg_function_options="groupByAggFunctionOptions",
                    group_by_columns="groupByColumns",
                    hidden_columns="hiddenColumns",
                    ignore_case="ignoreCase",
                    include_in_split="includeInSplit",
                    input=input,
                    interval="interval",
                    is_text="isText",
                    join_keys="joinKeys",
                    join_type="joinType",
                    left_columns="leftColumns",
                    limit="limit",
                    lower_bound="lowerBound",
                    map_type="mapType",
                    mode_type="modeType",
                    multi_line=False,
                    num_rows="numRows",
                    num_rows_after="numRowsAfter",
                    num_rows_before="numRowsBefore",
                    order_by_column="orderByColumn",
                    order_by_columns="orderByColumns",
                    other="other",
                    pattern="pattern",
                    pattern_option1="patternOption1",
                    pattern_option2="patternOption2",
                    pattern_options="patternOptions",
                    period="period",
                    position="position",
                    remove_all_punctuation="removeAllPunctuation",
                    remove_all_quotes="removeAllQuotes",
                    remove_all_whitespace="removeAllWhitespace",
                    remove_custom_characters="removeCustomCharacters",
                    remove_custom_value="removeCustomValue",
                    remove_leading_and_trailing_punctuation="removeLeadingAndTrailingPunctuation",
                    remove_leading_and_trailing_quotes="removeLeadingAndTrailingQuotes",
                    remove_leading_and_trailing_whitespace="removeLeadingAndTrailingWhitespace",
                    remove_letters="removeLetters",
                    remove_numbers="removeNumbers",
                    remove_source_column="removeSourceColumn",
                    remove_special_characters="removeSpecialCharacters",
                    right_columns="rightColumns",
                    sample_size="sampleSize",
                    sample_type="sampleType",
                    secondary_inputs=[databrew.CfnRecipe.SecondaryInputProperty(
                        data_catalog_input_definition=databrew.CfnRecipe.DataCatalogInputDefinitionProperty(
                            catalog_id="catalogId",
                            database_name="databaseName",
                            table_name="tableName",
                            temp_directory=databrew.CfnRecipe.S3LocationProperty(
                                bucket="bucket",
                
                                # the properties below are optional
                                key="key"
                            )
                        ),
                        s3_input_definition=databrew.CfnRecipe.S3LocationProperty(
                            bucket="bucket",
                
                            # the properties below are optional
                            key="key"
                        )
                    )],
                    second_input="secondInput",
                    sheet_indexes=[123],
                    sheet_names=["sheetNames"],
                    source_column="sourceColumn",
                    source_column1="sourceColumn1",
                    source_column2="sourceColumn2",
                    source_columns="sourceColumns",
                    start_column_index="startColumnIndex",
                    start_pattern="startPattern",
                    start_position="startPosition",
                    start_value="startValue",
                    stemming_mode="stemmingMode",
                    step_count="stepCount",
                    step_index="stepIndex",
                    stop_words_mode="stopWordsMode",
                    strategy="strategy",
                    target_column="targetColumn",
                    target_column_names="targetColumnNames",
                    target_date_format="targetDateFormat",
                    target_index="targetIndex",
                    time_zone="timeZone",
                    tokenizer_pattern="tokenizerPattern",
                    true_string="trueString",
                    udf_lang="udfLang",
                    units="units",
                    unpivot_column="unpivotColumn",
                    upper_bound="upperBound",
                    use_new_data_frame="useNewDataFrame",
                    value="value",
                    value1="value1",
                    value2="value2",
                    value_column="valueColumn",
                    view_frame="viewFrame"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if aggregate_function is not None:
                self._values["aggregate_function"] = aggregate_function
            if base is not None:
                self._values["base"] = base
            if case_statement is not None:
                self._values["case_statement"] = case_statement
            if category_map is not None:
                self._values["category_map"] = category_map
            if chars_to_remove is not None:
                self._values["chars_to_remove"] = chars_to_remove
            if collapse_consecutive_whitespace is not None:
                self._values["collapse_consecutive_whitespace"] = collapse_consecutive_whitespace
            if column_data_type is not None:
                self._values["column_data_type"] = column_data_type
            if column_range is not None:
                self._values["column_range"] = column_range
            if count is not None:
                self._values["count"] = count
            if custom_characters is not None:
                self._values["custom_characters"] = custom_characters
            if custom_stop_words is not None:
                self._values["custom_stop_words"] = custom_stop_words
            if custom_value is not None:
                self._values["custom_value"] = custom_value
            if datasets_columns is not None:
                self._values["datasets_columns"] = datasets_columns
            if date_add_value is not None:
                self._values["date_add_value"] = date_add_value
            if date_time_format is not None:
                self._values["date_time_format"] = date_time_format
            if date_time_parameters is not None:
                self._values["date_time_parameters"] = date_time_parameters
            if delete_other_rows is not None:
                self._values["delete_other_rows"] = delete_other_rows
            if delimiter is not None:
                self._values["delimiter"] = delimiter
            if end_pattern is not None:
                self._values["end_pattern"] = end_pattern
            if end_position is not None:
                self._values["end_position"] = end_position
            if end_value is not None:
                self._values["end_value"] = end_value
            if expand_contractions is not None:
                self._values["expand_contractions"] = expand_contractions
            if exponent is not None:
                self._values["exponent"] = exponent
            if false_string is not None:
                self._values["false_string"] = false_string
            if group_by_agg_function_options is not None:
                self._values["group_by_agg_function_options"] = group_by_agg_function_options
            if group_by_columns is not None:
                self._values["group_by_columns"] = group_by_columns
            if hidden_columns is not None:
                self._values["hidden_columns"] = hidden_columns
            if ignore_case is not None:
                self._values["ignore_case"] = ignore_case
            if include_in_split is not None:
                self._values["include_in_split"] = include_in_split
            if input is not None:
                self._values["input"] = input
            if interval is not None:
                self._values["interval"] = interval
            if is_text is not None:
                self._values["is_text"] = is_text
            if join_keys is not None:
                self._values["join_keys"] = join_keys
            if join_type is not None:
                self._values["join_type"] = join_type
            if left_columns is not None:
                self._values["left_columns"] = left_columns
            if limit is not None:
                self._values["limit"] = limit
            if lower_bound is not None:
                self._values["lower_bound"] = lower_bound
            if map_type is not None:
                self._values["map_type"] = map_type
            if mode_type is not None:
                self._values["mode_type"] = mode_type
            if multi_line is not None:
                self._values["multi_line"] = multi_line
            if num_rows is not None:
                self._values["num_rows"] = num_rows
            if num_rows_after is not None:
                self._values["num_rows_after"] = num_rows_after
            if num_rows_before is not None:
                self._values["num_rows_before"] = num_rows_before
            if order_by_column is not None:
                self._values["order_by_column"] = order_by_column
            if order_by_columns is not None:
                self._values["order_by_columns"] = order_by_columns
            if other is not None:
                self._values["other"] = other
            if pattern is not None:
                self._values["pattern"] = pattern
            if pattern_option1 is not None:
                self._values["pattern_option1"] = pattern_option1
            if pattern_option2 is not None:
                self._values["pattern_option2"] = pattern_option2
            if pattern_options is not None:
                self._values["pattern_options"] = pattern_options
            if period is not None:
                self._values["period"] = period
            if position is not None:
                self._values["position"] = position
            if remove_all_punctuation is not None:
                self._values["remove_all_punctuation"] = remove_all_punctuation
            if remove_all_quotes is not None:
                self._values["remove_all_quotes"] = remove_all_quotes
            if remove_all_whitespace is not None:
                self._values["remove_all_whitespace"] = remove_all_whitespace
            if remove_custom_characters is not None:
                self._values["remove_custom_characters"] = remove_custom_characters
            if remove_custom_value is not None:
                self._values["remove_custom_value"] = remove_custom_value
            if remove_leading_and_trailing_punctuation is not None:
                self._values["remove_leading_and_trailing_punctuation"] = remove_leading_and_trailing_punctuation
            if remove_leading_and_trailing_quotes is not None:
                self._values["remove_leading_and_trailing_quotes"] = remove_leading_and_trailing_quotes
            if remove_leading_and_trailing_whitespace is not None:
                self._values["remove_leading_and_trailing_whitespace"] = remove_leading_and_trailing_whitespace
            if remove_letters is not None:
                self._values["remove_letters"] = remove_letters
            if remove_numbers is not None:
                self._values["remove_numbers"] = remove_numbers
            if remove_source_column is not None:
                self._values["remove_source_column"] = remove_source_column
            if remove_special_characters is not None:
                self._values["remove_special_characters"] = remove_special_characters
            if right_columns is not None:
                self._values["right_columns"] = right_columns
            if sample_size is not None:
                self._values["sample_size"] = sample_size
            if sample_type is not None:
                self._values["sample_type"] = sample_type
            if secondary_inputs is not None:
                self._values["secondary_inputs"] = secondary_inputs
            if second_input is not None:
                self._values["second_input"] = second_input
            if sheet_indexes is not None:
                self._values["sheet_indexes"] = sheet_indexes
            if sheet_names is not None:
                self._values["sheet_names"] = sheet_names
            if source_column is not None:
                self._values["source_column"] = source_column
            if source_column1 is not None:
                self._values["source_column1"] = source_column1
            if source_column2 is not None:
                self._values["source_column2"] = source_column2
            if source_columns is not None:
                self._values["source_columns"] = source_columns
            if start_column_index is not None:
                self._values["start_column_index"] = start_column_index
            if start_pattern is not None:
                self._values["start_pattern"] = start_pattern
            if start_position is not None:
                self._values["start_position"] = start_position
            if start_value is not None:
                self._values["start_value"] = start_value
            if stemming_mode is not None:
                self._values["stemming_mode"] = stemming_mode
            if step_count is not None:
                self._values["step_count"] = step_count
            if step_index is not None:
                self._values["step_index"] = step_index
            if stop_words_mode is not None:
                self._values["stop_words_mode"] = stop_words_mode
            if strategy is not None:
                self._values["strategy"] = strategy
            if target_column is not None:
                self._values["target_column"] = target_column
            if target_column_names is not None:
                self._values["target_column_names"] = target_column_names
            if target_date_format is not None:
                self._values["target_date_format"] = target_date_format
            if target_index is not None:
                self._values["target_index"] = target_index
            if time_zone is not None:
                self._values["time_zone"] = time_zone
            if tokenizer_pattern is not None:
                self._values["tokenizer_pattern"] = tokenizer_pattern
            if true_string is not None:
                self._values["true_string"] = true_string
            if udf_lang is not None:
                self._values["udf_lang"] = udf_lang
            if units is not None:
                self._values["units"] = units
            if unpivot_column is not None:
                self._values["unpivot_column"] = unpivot_column
            if upper_bound is not None:
                self._values["upper_bound"] = upper_bound
            if use_new_data_frame is not None:
                self._values["use_new_data_frame"] = use_new_data_frame
            if value is not None:
                self._values["value"] = value
            if value1 is not None:
                self._values["value1"] = value1
            if value2 is not None:
                self._values["value2"] = value2
            if value_column is not None:
                self._values["value_column"] = value_column
            if view_frame is not None:
                self._values["view_frame"] = view_frame

        @builtins.property
        def aggregate_function(self) -> typing.Optional[builtins.str]:
            '''The name of an aggregation function to apply.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-aggregatefunction
            '''
            result = self._values.get("aggregate_function")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def base(self) -> typing.Optional[builtins.str]:
            '''The number of digits used in a counting system.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-base
            '''
            result = self._values.get("base")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def case_statement(self) -> typing.Optional[builtins.str]:
            '''A case statement associated with a recipe.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-casestatement
            '''
            result = self._values.get("case_statement")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def category_map(self) -> typing.Optional[builtins.str]:
            '''A category map used for one-hot encoding.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-categorymap
            '''
            result = self._values.get("category_map")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def chars_to_remove(self) -> typing.Optional[builtins.str]:
            '''Characters to remove from a step that applies one-hot encoding or tokenization.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-charstoremove
            '''
            result = self._values.get("chars_to_remove")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def collapse_consecutive_whitespace(self) -> typing.Optional[builtins.str]:
            '''Remove any non-word non-punctuation character.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-collapseconsecutivewhitespace
            '''
            result = self._values.get("collapse_consecutive_whitespace")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def column_data_type(self) -> typing.Optional[builtins.str]:
            '''The data type of the column.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-columndatatype
            '''
            result = self._values.get("column_data_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def column_range(self) -> typing.Optional[builtins.str]:
            '''A range of columns to which a step is applied.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-columnrange
            '''
            result = self._values.get("column_range")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def count(self) -> typing.Optional[builtins.str]:
            '''The number of times a string needs to be repeated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-count
            '''
            result = self._values.get("count")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def custom_characters(self) -> typing.Optional[builtins.str]:
            '''One or more characters that can be substituted or removed, depending on the context.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-customcharacters
            '''
            result = self._values.get("custom_characters")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def custom_stop_words(self) -> typing.Optional[builtins.str]:
            '''A list of words to ignore in a step that applies word tokenization.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-customstopwords
            '''
            result = self._values.get("custom_stop_words")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def custom_value(self) -> typing.Optional[builtins.str]:
            '''A list of custom values to use in a step that requires that you provide a value to finish the operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-customvalue
            '''
            result = self._values.get("custom_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def datasets_columns(self) -> typing.Optional[builtins.str]:
            '''A list of the dataset columns included in a project.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-datasetscolumns
            '''
            result = self._values.get("datasets_columns")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def date_add_value(self) -> typing.Optional[builtins.str]:
            '''A value that specifies how many units of time to add or subtract for a date math operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-dateaddvalue
            '''
            result = self._values.get("date_add_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def date_time_format(self) -> typing.Optional[builtins.str]:
            '''A date format to apply to a date.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-datetimeformat
            '''
            result = self._values.get("date_time_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def date_time_parameters(self) -> typing.Optional[builtins.str]:
            '''A set of parameters associated with a datetime.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-datetimeparameters
            '''
            result = self._values.get("date_time_parameters")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def delete_other_rows(self) -> typing.Optional[builtins.str]:
            '''Determines whether unmapped rows in a categorical mapping should be deleted.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-deleteotherrows
            '''
            result = self._values.get("delete_other_rows")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def delimiter(self) -> typing.Optional[builtins.str]:
            '''The delimiter to use when parsing separated values in a text file.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-delimiter
            '''
            result = self._values.get("delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def end_pattern(self) -> typing.Optional[builtins.str]:
            '''The end pattern to locate.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-endpattern
            '''
            result = self._values.get("end_pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def end_position(self) -> typing.Optional[builtins.str]:
            '''The end position to locate.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-endposition
            '''
            result = self._values.get("end_position")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def end_value(self) -> typing.Optional[builtins.str]:
            '''The end value to locate.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-endvalue
            '''
            result = self._values.get("end_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def expand_contractions(self) -> typing.Optional[builtins.str]:
            '''A list of word contractions and what they expand to.

            For eample: *can't* ; *cannot* ; *can not* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-expandcontractions
            '''
            result = self._values.get("expand_contractions")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def exponent(self) -> typing.Optional[builtins.str]:
            '''The exponent to apply in an exponential operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-exponent
            '''
            result = self._values.get("exponent")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def false_string(self) -> typing.Optional[builtins.str]:
            '''A value that represents ``FALSE`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-falsestring
            '''
            result = self._values.get("false_string")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def group_by_agg_function_options(self) -> typing.Optional[builtins.str]:
            '''Specifies options to apply to the ``GROUP BY`` used in an aggregation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-groupbyaggfunctionoptions
            '''
            result = self._values.get("group_by_agg_function_options")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def group_by_columns(self) -> typing.Optional[builtins.str]:
            '''The columns to use in the ``GROUP BY`` clause.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-groupbycolumns
            '''
            result = self._values.get("group_by_columns")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def hidden_columns(self) -> typing.Optional[builtins.str]:
            '''A list of columns to hide.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-hiddencolumns
            '''
            result = self._values.get("hidden_columns")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ignore_case(self) -> typing.Optional[builtins.str]:
            '''Indicates that lower and upper case letters are treated equally.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-ignorecase
            '''
            result = self._values.get("ignore_case")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def include_in_split(self) -> typing.Optional[builtins.str]:
            '''Indicates if this column is participating in a split transform.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-includeinsplit
            '''
            result = self._values.get("include_in_split")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input(self) -> typing.Any:
            '''The input location to load the dataset from - Amazon S3 or AWS Glue Data Catalog .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-input
            '''
            result = self._values.get("input")
            return typing.cast(typing.Any, result)

        @builtins.property
        def interval(self) -> typing.Optional[builtins.str]:
            '''The number of characters to split by.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-interval
            '''
            result = self._values.get("interval")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def is_text(self) -> typing.Optional[builtins.str]:
            '''Indicates if the content is text.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-istext
            '''
            result = self._values.get("is_text")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def join_keys(self) -> typing.Optional[builtins.str]:
            '''The keys or columns involved in a join.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-joinkeys
            '''
            result = self._values.get("join_keys")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def join_type(self) -> typing.Optional[builtins.str]:
            '''The type of join to use, for example, ``INNER JOIN`` , ``OUTER JOIN`` , and so on.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-jointype
            '''
            result = self._values.get("join_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def left_columns(self) -> typing.Optional[builtins.str]:
            '''The columns on the left side of the join.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-leftcolumns
            '''
            result = self._values.get("left_columns")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def limit(self) -> typing.Optional[builtins.str]:
            '''The number of times to perform ``split`` or ``replaceBy`` in a string.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-limit
            '''
            result = self._values.get("limit")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def lower_bound(self) -> typing.Optional[builtins.str]:
            '''The lower boundary for a value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-lowerbound
            '''
            result = self._values.get("lower_bound")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def map_type(self) -> typing.Optional[builtins.str]:
            '''The type of mappings to apply to construct a new dynamic frame.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-maptype
            '''
            result = self._values.get("map_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mode_type(self) -> typing.Optional[builtins.str]:
            '''Determines the manner in which mode value is calculated, in case there is more than one mode value.

            Valid values: ``NONE`` | ``AVERAGE`` | ``MINIMUM`` | ``MAXIMUM``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-modetype
            '''
            result = self._values.get("mode_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def multi_line(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether JSON input contains embedded new line characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-multiline
            '''
            result = self._values.get("multi_line")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def num_rows(self) -> typing.Optional[builtins.str]:
            '''The number of rows to consider in a window.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-numrows
            '''
            result = self._values.get("num_rows")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def num_rows_after(self) -> typing.Optional[builtins.str]:
            '''The number of rows to consider after the current row in a window.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-numrowsafter
            '''
            result = self._values.get("num_rows_after")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def num_rows_before(self) -> typing.Optional[builtins.str]:
            '''The number of rows to consider before the current row in a window.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-numrowsbefore
            '''
            result = self._values.get("num_rows_before")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def order_by_column(self) -> typing.Optional[builtins.str]:
            '''A column to sort the results by.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-orderbycolumn
            '''
            result = self._values.get("order_by_column")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def order_by_columns(self) -> typing.Optional[builtins.str]:
            '''The columns to sort the results by.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-orderbycolumns
            '''
            result = self._values.get("order_by_columns")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def other(self) -> typing.Optional[builtins.str]:
            '''The value to assign to unmapped cells, in categorical mapping.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-other
            '''
            result = self._values.get("other")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pattern(self) -> typing.Optional[builtins.str]:
            '''The pattern to locate.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-pattern
            '''
            result = self._values.get("pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pattern_option1(self) -> typing.Optional[builtins.str]:
            '''The starting pattern to split between.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-patternoption1
            '''
            result = self._values.get("pattern_option1")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pattern_option2(self) -> typing.Optional[builtins.str]:
            '''The ending pattern to split between.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-patternoption2
            '''
            result = self._values.get("pattern_option2")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pattern_options(self) -> typing.Optional[builtins.str]:
            '''For splitting by multiple delimiters: A JSON-encoded string that lists the patterns in the format.

            For example: ``[{\\"pattern\\":\\"1\\",\\"includeInSplit\\":true}]``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-patternoptions
            '''
            result = self._values.get("pattern_options")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def period(self) -> typing.Optional[builtins.str]:
            '''The size of the rolling window.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-period
            '''
            result = self._values.get("period")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def position(self) -> typing.Optional[builtins.str]:
            '''The character index within a string.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-position
            '''
            result = self._values.get("position")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def remove_all_punctuation(self) -> typing.Optional[builtins.str]:
            '''If ``true`` , removes all of the following characters: ``.`` ``.!`` ``.,`` ``.?``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removeallpunctuation
            '''
            result = self._values.get("remove_all_punctuation")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def remove_all_quotes(self) -> typing.Optional[builtins.str]:
            '''If ``true`` , removes all single quotes and double quotes.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removeallquotes
            '''
            result = self._values.get("remove_all_quotes")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def remove_all_whitespace(self) -> typing.Optional[builtins.str]:
            '''If ``true`` , removes all whitespaces from the value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removeallwhitespace
            '''
            result = self._values.get("remove_all_whitespace")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def remove_custom_characters(self) -> typing.Optional[builtins.str]:
            '''If ``true`` , removes all chraracters specified by ``CustomCharacters`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removecustomcharacters
            '''
            result = self._values.get("remove_custom_characters")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def remove_custom_value(self) -> typing.Optional[builtins.str]:
            '''If ``true`` , removes all chraracters specified by ``CustomValue`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removecustomvalue
            '''
            result = self._values.get("remove_custom_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def remove_leading_and_trailing_punctuation(
            self,
        ) -> typing.Optional[builtins.str]:
            '''If ``true`` , removes the following characters if they occur at the start or end of the value: ``.`` ``!`` ``,`` ``?``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removeleadingandtrailingpunctuation
            '''
            result = self._values.get("remove_leading_and_trailing_punctuation")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def remove_leading_and_trailing_quotes(self) -> typing.Optional[builtins.str]:
            '''If ``true`` , removes single quotes and double quotes from the beginning and end of the value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removeleadingandtrailingquotes
            '''
            result = self._values.get("remove_leading_and_trailing_quotes")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def remove_leading_and_trailing_whitespace(
            self,
        ) -> typing.Optional[builtins.str]:
            '''If ``true`` , removes all whitespaces from the beginning and end of the value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removeleadingandtrailingwhitespace
            '''
            result = self._values.get("remove_leading_and_trailing_whitespace")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def remove_letters(self) -> typing.Optional[builtins.str]:
            '''If ``true`` , removes all uppercase and lowercase alphabetic characters (A through Z;

            a through z).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removeletters
            '''
            result = self._values.get("remove_letters")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def remove_numbers(self) -> typing.Optional[builtins.str]:
            '''If ``true`` , removes all numeric characters (0 through 9).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removenumbers
            '''
            result = self._values.get("remove_numbers")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def remove_source_column(self) -> typing.Optional[builtins.str]:
            '''If ``true`` , the source column will be removed after un-nesting that column.

            (Used with nested column types, such as Map, Struct, or Array.)

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removesourcecolumn
            '''
            result = self._values.get("remove_source_column")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def remove_special_characters(self) -> typing.Optional[builtins.str]:
            '''If ``true`` , removes all of the following characters: `!

            " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \\ ] ^ _ `` { | } ~``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removespecialcharacters
            '''
            result = self._values.get("remove_special_characters")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def right_columns(self) -> typing.Optional[builtins.str]:
            '''The columns on the right side of a join.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-rightcolumns
            '''
            result = self._values.get("right_columns")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sample_size(self) -> typing.Optional[builtins.str]:
            '''The number of rows in the sample.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-samplesize
            '''
            result = self._values.get("sample_size")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sample_type(self) -> typing.Optional[builtins.str]:
            '''The sampling type to apply to the dataset.

            Valid values: ``FIRST_N`` | ``LAST_N`` | ``RANDOM``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-sampletype
            '''
            result = self._values.get("sample_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secondary_inputs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnRecipe.SecondaryInputProperty", _IResolvable_da3f097b]]]]:
            '''A list of secondary inputs in a UNION transform.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-secondaryinputs
            '''
            result = self._values.get("secondary_inputs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnRecipe.SecondaryInputProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def second_input(self) -> typing.Optional[builtins.str]:
            '''A object value to indicate the second dataset used in a join.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-secondinput
            '''
            result = self._values.get("second_input")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sheet_indexes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]]:
            '''One or more sheet numbers in the Excel file, which will be included in a dataset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-sheetindexes
            '''
            result = self._values.get("sheet_indexes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]], result)

        @builtins.property
        def sheet_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Oone or more named sheets in the Excel file, which will be included in a dataset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-sheetnames
            '''
            result = self._values.get("sheet_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def source_column(self) -> typing.Optional[builtins.str]:
            '''A source column needed for an operation, step, or transform.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-sourcecolumn
            '''
            result = self._values.get("source_column")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_column1(self) -> typing.Optional[builtins.str]:
            '''A source column needed for an operation, step, or transform.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-sourcecolumn1
            '''
            result = self._values.get("source_column1")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_column2(self) -> typing.Optional[builtins.str]:
            '''A source column needed for an operation, step, or transform.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-sourcecolumn2
            '''
            result = self._values.get("source_column2")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_columns(self) -> typing.Optional[builtins.str]:
            '''A list of source columns needed for an operation, step, or transform.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-sourcecolumns
            '''
            result = self._values.get("source_columns")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start_column_index(self) -> typing.Optional[builtins.str]:
            '''The index number of the first column used by an operation, step, or transform.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-startcolumnindex
            '''
            result = self._values.get("start_column_index")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start_pattern(self) -> typing.Optional[builtins.str]:
            '''The starting pattern to locate.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-startpattern
            '''
            result = self._values.get("start_pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start_position(self) -> typing.Optional[builtins.str]:
            '''The starting position to locate.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-startposition
            '''
            result = self._values.get("start_position")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start_value(self) -> typing.Optional[builtins.str]:
            '''The starting value to locate.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-startvalue
            '''
            result = self._values.get("start_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stemming_mode(self) -> typing.Optional[builtins.str]:
            '''Indicates this operation uses stems and lemmas (base words) for word tokenization.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-stemmingmode
            '''
            result = self._values.get("stemming_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def step_count(self) -> typing.Optional[builtins.str]:
            '''The total number of transforms in this recipe.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-stepcount
            '''
            result = self._values.get("step_count")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def step_index(self) -> typing.Optional[builtins.str]:
            '''The index ID of a step.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-stepindex
            '''
            result = self._values.get("step_index")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stop_words_mode(self) -> typing.Optional[builtins.str]:
            '''Indicates this operation uses stop words as part of word tokenization.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-stopwordsmode
            '''
            result = self._values.get("stop_words_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def strategy(self) -> typing.Optional[builtins.str]:
            '''The resolution strategy to apply in resolving ambiguities.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-strategy
            '''
            result = self._values.get("strategy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_column(self) -> typing.Optional[builtins.str]:
            '''The column targeted by this operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-targetcolumn
            '''
            result = self._values.get("target_column")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_column_names(self) -> typing.Optional[builtins.str]:
            '''The names to give columns altered by this operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-targetcolumnnames
            '''
            result = self._values.get("target_column_names")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_date_format(self) -> typing.Optional[builtins.str]:
            '''The date format to convert to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-targetdateformat
            '''
            result = self._values.get("target_date_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_index(self) -> typing.Optional[builtins.str]:
            '''The index number of an object that is targeted by this operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-targetindex
            '''
            result = self._values.get("target_index")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def time_zone(self) -> typing.Optional[builtins.str]:
            '''The current timezone that you want to use for dates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-timezone
            '''
            result = self._values.get("time_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tokenizer_pattern(self) -> typing.Optional[builtins.str]:
            '''A regex expression to use when splitting text into terms, also called words or tokens.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-tokenizerpattern
            '''
            result = self._values.get("tokenizer_pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def true_string(self) -> typing.Optional[builtins.str]:
            '''A value to use to represent ``TRUE`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-truestring
            '''
            result = self._values.get("true_string")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def udf_lang(self) -> typing.Optional[builtins.str]:
            '''The language that's used in the user-defined function.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-udflang
            '''
            result = self._values.get("udf_lang")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def units(self) -> typing.Optional[builtins.str]:
            '''Specifies a unit of time.

            For example: ``MINUTES`` ; ``SECONDS`` ; ``HOURS`` ; etc.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-units
            '''
            result = self._values.get("units")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unpivot_column(self) -> typing.Optional[builtins.str]:
            '''Cast columns as rows, so that each value is a different row in a single column.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-unpivotcolumn
            '''
            result = self._values.get("unpivot_column")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def upper_bound(self) -> typing.Optional[builtins.str]:
            '''The upper boundary for a value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-upperbound
            '''
            result = self._values.get("upper_bound")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def use_new_data_frame(self) -> typing.Optional[builtins.str]:
            '''Create a new container to hold a dataset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-usenewdataframe
            '''
            result = self._values.get("use_new_data_frame")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''A static value that can be used in a comparison, a substitution, or in another context-specific way.

            A ``Value`` can be a number, string, or other datatype, depending on the recipe action in which it's used.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value1(self) -> typing.Optional[builtins.str]:
            '''A value that's used by this operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-value1
            '''
            result = self._values.get("value1")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value2(self) -> typing.Optional[builtins.str]:
            '''A value that's used by this operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-value2
            '''
            result = self._values.get("value2")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value_column(self) -> typing.Optional[builtins.str]:
            '''The column that is provided as a value that's used by this operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-valuecolumn
            '''
            result = self._values.get("value_column")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def view_frame(self) -> typing.Optional[builtins.str]:
            '''The subset of rows currently available for viewing.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-viewframe
            '''
            result = self._values.get("view_frame")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecipeParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnRecipe.RecipeStepProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "condition_expressions": "conditionExpressions",
        },
    )
    class RecipeStepProperty:
        def __init__(
            self,
            *,
            action: typing.Union["CfnRecipe.ActionProperty", _IResolvable_da3f097b],
            condition_expressions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnRecipe.ConditionExpressionProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''Represents a single step from a DataBrew recipe to be performed.

            :param action: The particular action to be performed in the recipe step.
            :param condition_expressions: One or more conditions that must be met for the recipe step to succeed. .. epigraph:: All of the conditions in the array must be met. In other words, all of the conditions must be combined using a logical AND operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipestep.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                recipe_step_property = databrew.CfnRecipe.RecipeStepProperty(
                    action=databrew.CfnRecipe.ActionProperty(
                        operation="operation",
                
                        # the properties below are optional
                        parameters={
                            "parameters_key": "parameters"
                        }
                    ),
                
                    # the properties below are optional
                    condition_expressions=[databrew.CfnRecipe.ConditionExpressionProperty(
                        condition="condition",
                        target_column="targetColumn",
                
                        # the properties below are optional
                        value="value"
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "action": action,
            }
            if condition_expressions is not None:
                self._values["condition_expressions"] = condition_expressions

        @builtins.property
        def action(
            self,
        ) -> typing.Union["CfnRecipe.ActionProperty", _IResolvable_da3f097b]:
            '''The particular action to be performed in the recipe step.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipestep.html#cfn-databrew-recipe-recipestep-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(typing.Union["CfnRecipe.ActionProperty", _IResolvable_da3f097b], result)

        @builtins.property
        def condition_expressions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnRecipe.ConditionExpressionProperty", _IResolvable_da3f097b]]]]:
            '''One or more conditions that must be met for the recipe step to succeed.

            .. epigraph::

               All of the conditions in the array must be met. In other words, all of the conditions must be combined using a logical AND operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipestep.html#cfn-databrew-recipe-recipestep-conditionexpressions
            '''
            result = self._values.get("condition_expressions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnRecipe.ConditionExpressionProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecipeStepProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnRecipe.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key": "key"},
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents an Amazon S3 location (bucket name, bucket owner, and object key) where DataBrew can read input data, or write output from a job.

            :param bucket: The Amazon S3 bucket name.
            :param key: The unique name of the object in the bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                s3_location_property = databrew.CfnRecipe.S3LocationProperty(
                    bucket="bucket",
                
                    # the properties below are optional
                    key="key"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket": bucket,
            }
            if key is not None:
                self._values["key"] = key

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The Amazon S3 bucket name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-s3location.html#cfn-databrew-recipe-s3location-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The unique name of the object in the bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-s3location.html#cfn-databrew-recipe-s3location-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnRecipe.SecondaryInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_catalog_input_definition": "dataCatalogInputDefinition",
            "s3_input_definition": "s3InputDefinition",
        },
    )
    class SecondaryInputProperty:
        def __init__(
            self,
            *,
            data_catalog_input_definition: typing.Optional[typing.Union["CfnRecipe.DataCatalogInputDefinitionProperty", _IResolvable_da3f097b]] = None,
            s3_input_definition: typing.Optional[typing.Union["CfnRecipe.S3LocationProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Represents secondary inputs in a UNION transform.

            :param data_catalog_input_definition: The AWS Glue Data Catalog parameters for the data.
            :param s3_input_definition: The Amazon S3 location where the data is stored.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-secondaryinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                secondary_input_property = databrew.CfnRecipe.SecondaryInputProperty(
                    data_catalog_input_definition=databrew.CfnRecipe.DataCatalogInputDefinitionProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        table_name="tableName",
                        temp_directory=databrew.CfnRecipe.S3LocationProperty(
                            bucket="bucket",
                
                            # the properties below are optional
                            key="key"
                        )
                    ),
                    s3_input_definition=databrew.CfnRecipe.S3LocationProperty(
                        bucket="bucket",
                
                        # the properties below are optional
                        key="key"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if data_catalog_input_definition is not None:
                self._values["data_catalog_input_definition"] = data_catalog_input_definition
            if s3_input_definition is not None:
                self._values["s3_input_definition"] = s3_input_definition

        @builtins.property
        def data_catalog_input_definition(
            self,
        ) -> typing.Optional[typing.Union["CfnRecipe.DataCatalogInputDefinitionProperty", _IResolvable_da3f097b]]:
            '''The AWS Glue Data Catalog parameters for the data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-secondaryinput.html#cfn-databrew-recipe-secondaryinput-datacataloginputdefinition
            '''
            result = self._values.get("data_catalog_input_definition")
            return typing.cast(typing.Optional[typing.Union["CfnRecipe.DataCatalogInputDefinitionProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def s3_input_definition(
            self,
        ) -> typing.Optional[typing.Union["CfnRecipe.S3LocationProperty", _IResolvable_da3f097b]]:
            '''The Amazon S3 location where the data is stored.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-secondaryinput.html#cfn-databrew-recipe-secondaryinput-s3inputdefinition
            '''
            result = self._values.get("s3_input_definition")
            return typing.cast(typing.Optional[typing.Union["CfnRecipe.S3LocationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecondaryInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_databrew.CfnRecipeProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "steps": "steps",
        "description": "description",
        "tags": "tags",
    },
)
class CfnRecipeProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        steps: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnRecipe.RecipeStepProperty, _IResolvable_da3f097b]]],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRecipe``.

        :param name: The unique name for the recipe.
        :param steps: A list of steps that are defined by the recipe.
        :param description: The description of the recipe.
        :param tags: Metadata tags that have been applied to the recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_databrew as databrew
            
            cfn_recipe_props = databrew.CfnRecipeProps(
                name="name",
                steps=[databrew.CfnRecipe.RecipeStepProperty(
                    action=databrew.CfnRecipe.ActionProperty(
                        operation="operation",
            
                        # the properties below are optional
                        parameters={
                            "parameters_key": "parameters"
                        }
                    ),
            
                    # the properties below are optional
                    condition_expressions=[databrew.CfnRecipe.ConditionExpressionProperty(
                        condition="condition",
                        target_column="targetColumn",
            
                        # the properties below are optional
                        value="value"
                    )]
                )],
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "steps": steps,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The unique name for the recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html#cfn-databrew-recipe-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def steps(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnRecipe.RecipeStepProperty, _IResolvable_da3f097b]]]:
        '''A list of steps that are defined by the recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html#cfn-databrew-recipe-steps
        '''
        result = self._values.get("steps")
        assert result is not None, "Required property 'steps' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnRecipe.RecipeStepProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html#cfn-databrew-recipe-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata tags that have been applied to the recipe.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html#cfn-databrew-recipe-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRecipeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnRuleset(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_databrew.CfnRuleset",
):
    '''A CloudFormation ``AWS::DataBrew::Ruleset``.

    Specifies a new ruleset that can be used in a profile job to validate the data quality of a dataset.

    :cloudformationResource: AWS::DataBrew::Ruleset
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_databrew as databrew
        
        cfn_ruleset = databrew.CfnRuleset(self, "MyCfnRuleset",
            name="name",
            rules=[databrew.CfnRuleset.RuleProperty(
                check_expression="checkExpression",
                name="name",
        
                # the properties below are optional
                column_selectors=[databrew.CfnRuleset.ColumnSelectorProperty(
                    name="name",
                    regex="regex"
                )],
                disabled=False,
                substitution_map=[databrew.CfnRuleset.SubstitutionValueProperty(
                    value="value",
                    value_reference="valueReference"
                )],
                threshold=databrew.CfnRuleset.ThresholdProperty(
                    value=123,
        
                    # the properties below are optional
                    type="type",
                    unit="unit"
                )
            )],
            target_arn="targetArn",
        
            # the properties below are optional
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnRuleset.RuleProperty", _IResolvable_da3f097b]]],
        target_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::DataBrew::Ruleset``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of the ruleset.
        :param rules: Contains metadata about the ruleset.
        :param target_arn: The Amazon Resource Name (ARN) of a resource (dataset) that the ruleset is associated with.
        :param description: The description of the ruleset.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        props = CfnRulesetProps(
            name=name,
            rules=rules,
            target_arn=target_arn,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html#cfn-databrew-ruleset-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the ruleset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html#cfn-databrew-ruleset-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rules")
    def rules(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnRuleset.RuleProperty", _IResolvable_da3f097b]]]:
        '''Contains metadata about the ruleset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html#cfn-databrew-ruleset-rules
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnRuleset.RuleProperty", _IResolvable_da3f097b]]], jsii.get(self, "rules"))

    @rules.setter
    def rules(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnRuleset.RuleProperty", _IResolvable_da3f097b]]],
    ) -> None:
        jsii.set(self, "rules", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targetArn")
    def target_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of a resource (dataset) that the ruleset is associated with.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html#cfn-databrew-ruleset-targetarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "targetArn"))

    @target_arn.setter
    def target_arn(self, value: builtins.str) -> None:
        jsii.set(self, "targetArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the ruleset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html#cfn-databrew-ruleset-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnRuleset.ColumnSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "regex": "regex"},
    )
    class ColumnSelectorProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            regex: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Selector of a column from a dataset for profile job configuration.

            One selector includes either a column name or a regular expression.

            :param name: The name of a column from a dataset.
            :param regex: A regular expression for selecting a column from a dataset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-columnselector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                column_selector_property = databrew.CfnRuleset.ColumnSelectorProperty(
                    name="name",
                    regex="regex"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if regex is not None:
                self._values["regex"] = regex

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of a column from a dataset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-columnselector.html#cfn-databrew-ruleset-columnselector-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def regex(self) -> typing.Optional[builtins.str]:
            '''A regular expression for selecting a column from a dataset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-columnselector.html#cfn-databrew-ruleset-columnselector-regex
            '''
            result = self._values.get("regex")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnRuleset.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "check_expression": "checkExpression",
            "name": "name",
            "column_selectors": "columnSelectors",
            "disabled": "disabled",
            "substitution_map": "substitutionMap",
            "threshold": "threshold",
        },
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            check_expression: builtins.str,
            name: builtins.str,
            column_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnRuleset.ColumnSelectorProperty", _IResolvable_da3f097b]]]] = None,
            disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            substitution_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnRuleset.SubstitutionValueProperty", _IResolvable_da3f097b]]]] = None,
            threshold: typing.Optional[typing.Union["CfnRuleset.ThresholdProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Represents a single data quality requirement that should be validated in the scope of this dataset.

            :param check_expression: The expression which includes column references, condition names followed by variable references, possibly grouped and combined with other conditions. For example, ``(:col1 starts_with :prefix1 or :col1 starts_with :prefix2) and (:col1 ends_with :suffix1 or :col1 ends_with :suffix2)`` . Column and value references are substitution variables that should start with the ':' symbol. Depending on the context, substitution variables' values can be either an actual value or a column name. These values are defined in the SubstitutionMap. If a CheckExpression starts with a column reference, then ColumnSelectors in the rule should be null. If ColumnSelectors has been defined, then there should be no columnn reference in the left side of a condition, for example, ``is_between :val1 and :val2`` .
            :param name: The name of the rule.
            :param column_selectors: List of column selectors. Selectors can be used to select columns using a name or regular expression from the dataset. Rule will be applied to selected columns.
            :param disabled: A value that specifies whether the rule is disabled. Once a rule is disabled, a profile job will not validate it during a job run. Default value is false.
            :param substitution_map: The map of substitution variable names to their values used in a check expression. Variable names should start with a ':' (colon). Variable values can either be actual values or column names. To differentiate between the two, column names should be enclosed in backticks, for example, ``":col1": "``Column A``".``
            :param threshold: The threshold used with a non-aggregate check expression. Non-aggregate check expressions will be applied to each row in a specific column, and the threshold will be used to determine whether the validation succeeds.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-rule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                rule_property = databrew.CfnRuleset.RuleProperty(
                    check_expression="checkExpression",
                    name="name",
                
                    # the properties below are optional
                    column_selectors=[databrew.CfnRuleset.ColumnSelectorProperty(
                        name="name",
                        regex="regex"
                    )],
                    disabled=False,
                    substitution_map=[databrew.CfnRuleset.SubstitutionValueProperty(
                        value="value",
                        value_reference="valueReference"
                    )],
                    threshold=databrew.CfnRuleset.ThresholdProperty(
                        value=123,
                
                        # the properties below are optional
                        type="type",
                        unit="unit"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "check_expression": check_expression,
                "name": name,
            }
            if column_selectors is not None:
                self._values["column_selectors"] = column_selectors
            if disabled is not None:
                self._values["disabled"] = disabled
            if substitution_map is not None:
                self._values["substitution_map"] = substitution_map
            if threshold is not None:
                self._values["threshold"] = threshold

        @builtins.property
        def check_expression(self) -> builtins.str:
            '''The expression which includes column references, condition names followed by variable references, possibly grouped and combined with other conditions.

            For example, ``(:col1 starts_with :prefix1 or :col1 starts_with :prefix2) and (:col1 ends_with :suffix1 or :col1 ends_with :suffix2)`` . Column and value references are substitution variables that should start with the ':' symbol. Depending on the context, substitution variables' values can be either an actual value or a column name. These values are defined in the SubstitutionMap. If a CheckExpression starts with a column reference, then ColumnSelectors in the rule should be null. If ColumnSelectors has been defined, then there should be no columnn reference in the left side of a condition, for example, ``is_between :val1 and :val2`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-rule.html#cfn-databrew-ruleset-rule-checkexpression
            '''
            result = self._values.get("check_expression")
            assert result is not None, "Required property 'check_expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the rule.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-rule.html#cfn-databrew-ruleset-rule-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def column_selectors(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnRuleset.ColumnSelectorProperty", _IResolvable_da3f097b]]]]:
            '''List of column selectors.

            Selectors can be used to select columns using a name or regular expression from the dataset. Rule will be applied to selected columns.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-rule.html#cfn-databrew-ruleset-rule-columnselectors
            '''
            result = self._values.get("column_selectors")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnRuleset.ColumnSelectorProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def disabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A value that specifies whether the rule is disabled.

            Once a rule is disabled, a profile job will not validate it during a job run. Default value is false.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-rule.html#cfn-databrew-ruleset-rule-disabled
            '''
            result = self._values.get("disabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def substitution_map(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnRuleset.SubstitutionValueProperty", _IResolvable_da3f097b]]]]:
            '''The map of substitution variable names to their values used in a check expression.

            Variable names should start with a ':' (colon). Variable values can either be actual values or column names. To differentiate between the two, column names should be enclosed in backticks, for example, ``":col1": "``Column A``".``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-rule.html#cfn-databrew-ruleset-rule-substitutionmap
            '''
            result = self._values.get("substitution_map")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnRuleset.SubstitutionValueProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def threshold(
            self,
        ) -> typing.Optional[typing.Union["CfnRuleset.ThresholdProperty", _IResolvable_da3f097b]]:
            '''The threshold used with a non-aggregate check expression.

            Non-aggregate check expressions will be applied to each row in a specific column, and the threshold will be used to determine whether the validation succeeds.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-rule.html#cfn-databrew-ruleset-rule-threshold
            '''
            result = self._values.get("threshold")
            return typing.cast(typing.Optional[typing.Union["CfnRuleset.ThresholdProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnRuleset.SubstitutionValueProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value", "value_reference": "valueReference"},
    )
    class SubstitutionValueProperty:
        def __init__(
            self,
            *,
            value: builtins.str,
            value_reference: builtins.str,
        ) -> None:
            '''A key-value pair to associate an expression's substitution variable names with their values.

            :param value: Value or column name.
            :param value_reference: Variable name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-substitutionvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                substitution_value_property = databrew.CfnRuleset.SubstitutionValueProperty(
                    value="value",
                    value_reference="valueReference"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "value": value,
                "value_reference": value_reference,
            }

        @builtins.property
        def value(self) -> builtins.str:
            '''Value or column name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-substitutionvalue.html#cfn-databrew-ruleset-substitutionvalue-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value_reference(self) -> builtins.str:
            '''Variable name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-substitutionvalue.html#cfn-databrew-ruleset-substitutionvalue-valuereference
            '''
            result = self._values.get("value_reference")
            assert result is not None, "Required property 'value_reference' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubstitutionValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_databrew.CfnRuleset.ThresholdProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value", "type": "type", "unit": "unit"},
    )
    class ThresholdProperty:
        def __init__(
            self,
            *,
            value: jsii.Number,
            type: typing.Optional[builtins.str] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The threshold used with a non-aggregate check expression.

            The non-aggregate check expression will be applied to each row in a specific column. Then the threshold will be used to determine whether the validation succeeds.

            :param value: The value of a threshold.
            :param type: The type of a threshold. Used for comparison of an actual count of rows that satisfy the rule to the threshold value.
            :param unit: Unit of threshold value. Can be either a COUNT or PERCENTAGE of the full sample size used for validation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-threshold.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_databrew as databrew
                
                threshold_property = databrew.CfnRuleset.ThresholdProperty(
                    value=123,
                
                    # the properties below are optional
                    type="type",
                    unit="unit"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "value": value,
            }
            if type is not None:
                self._values["type"] = type
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def value(self) -> jsii.Number:
            '''The value of a threshold.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-threshold.html#cfn-databrew-ruleset-threshold-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of a threshold.

            Used for comparison of an actual count of rows that satisfy the rule to the threshold value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-threshold.html#cfn-databrew-ruleset-threshold-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''Unit of threshold value.

            Can be either a COUNT or PERCENTAGE of the full sample size used for validation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-threshold.html#cfn-databrew-ruleset-threshold-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ThresholdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_databrew.CfnRulesetProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "rules": "rules",
        "target_arn": "targetArn",
        "description": "description",
        "tags": "tags",
    },
)
class CfnRulesetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnRuleset.RuleProperty, _IResolvable_da3f097b]]],
        target_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRuleset``.

        :param name: The name of the ruleset.
        :param rules: Contains metadata about the ruleset.
        :param target_arn: The Amazon Resource Name (ARN) of a resource (dataset) that the ruleset is associated with.
        :param description: The description of the ruleset.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_databrew as databrew
            
            cfn_ruleset_props = databrew.CfnRulesetProps(
                name="name",
                rules=[databrew.CfnRuleset.RuleProperty(
                    check_expression="checkExpression",
                    name="name",
            
                    # the properties below are optional
                    column_selectors=[databrew.CfnRuleset.ColumnSelectorProperty(
                        name="name",
                        regex="regex"
                    )],
                    disabled=False,
                    substitution_map=[databrew.CfnRuleset.SubstitutionValueProperty(
                        value="value",
                        value_reference="valueReference"
                    )],
                    threshold=databrew.CfnRuleset.ThresholdProperty(
                        value=123,
            
                        # the properties below are optional
                        type="type",
                        unit="unit"
                    )
                )],
                target_arn="targetArn",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "rules": rules,
            "target_arn": target_arn,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the ruleset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html#cfn-databrew-ruleset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rules(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnRuleset.RuleProperty, _IResolvable_da3f097b]]]:
        '''Contains metadata about the ruleset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html#cfn-databrew-ruleset-rules
        '''
        result = self._values.get("rules")
        assert result is not None, "Required property 'rules' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnRuleset.RuleProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def target_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of a resource (dataset) that the ruleset is associated with.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html#cfn-databrew-ruleset-targetarn
        '''
        result = self._values.get("target_arn")
        assert result is not None, "Required property 'target_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the ruleset.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html#cfn-databrew-ruleset-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html#cfn-databrew-ruleset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRulesetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSchedule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_databrew.CfnSchedule",
):
    '''A CloudFormation ``AWS::DataBrew::Schedule``.

    Specifies a new schedule for one or more AWS Glue DataBrew jobs. Jobs can be run at a specific date and time, or at regular intervals.

    :cloudformationResource: AWS::DataBrew::Schedule
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_databrew as databrew
        
        cfn_schedule = databrew.CfnSchedule(self, "MyCfnSchedule",
            cron_expression="cronExpression",
            name="name",
        
            # the properties below are optional
            job_names=["jobNames"],
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        cron_expression: builtins.str,
        name: builtins.str,
        job_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::DataBrew::Schedule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cron_expression: The dates and times when the job is to run. For more information, see `Working with cron expressions for recipe jobs <https://docs.aws.amazon.com/databrew/latest/dg/jobs.recipe.html#jobs.cron>`_ in the *AWS Glue DataBrew Developer Guide* .
        :param name: The name of the schedule.
        :param job_names: A list of jobs to be run, according to the schedule.
        :param tags: Metadata tags that have been applied to the schedule.
        '''
        props = CfnScheduleProps(
            cron_expression=cron_expression, name=name, job_names=job_names, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Metadata tags that have been applied to the schedule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html#cfn-databrew-schedule-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cronExpression")
    def cron_expression(self) -> builtins.str:
        '''The dates and times when the job is to run.

        For more information, see `Working with cron expressions for recipe jobs <https://docs.aws.amazon.com/databrew/latest/dg/jobs.recipe.html#jobs.cron>`_ in the *AWS Glue DataBrew Developer Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html#cfn-databrew-schedule-cronexpression
        '''
        return typing.cast(builtins.str, jsii.get(self, "cronExpression"))

    @cron_expression.setter
    def cron_expression(self, value: builtins.str) -> None:
        jsii.set(self, "cronExpression", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the schedule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html#cfn-databrew-schedule-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobNames")
    def job_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of jobs to be run, according to the schedule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html#cfn-databrew-schedule-jobnames
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jobNames"))

    @job_names.setter
    def job_names(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "jobNames", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_databrew.CfnScheduleProps",
    jsii_struct_bases=[],
    name_mapping={
        "cron_expression": "cronExpression",
        "name": "name",
        "job_names": "jobNames",
        "tags": "tags",
    },
)
class CfnScheduleProps:
    def __init__(
        self,
        *,
        cron_expression: builtins.str,
        name: builtins.str,
        job_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSchedule``.

        :param cron_expression: The dates and times when the job is to run. For more information, see `Working with cron expressions for recipe jobs <https://docs.aws.amazon.com/databrew/latest/dg/jobs.recipe.html#jobs.cron>`_ in the *AWS Glue DataBrew Developer Guide* .
        :param name: The name of the schedule.
        :param job_names: A list of jobs to be run, according to the schedule.
        :param tags: Metadata tags that have been applied to the schedule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_databrew as databrew
            
            cfn_schedule_props = databrew.CfnScheduleProps(
                cron_expression="cronExpression",
                name="name",
            
                # the properties below are optional
                job_names=["jobNames"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "cron_expression": cron_expression,
            "name": name,
        }
        if job_names is not None:
            self._values["job_names"] = job_names
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cron_expression(self) -> builtins.str:
        '''The dates and times when the job is to run.

        For more information, see `Working with cron expressions for recipe jobs <https://docs.aws.amazon.com/databrew/latest/dg/jobs.recipe.html#jobs.cron>`_ in the *AWS Glue DataBrew Developer Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html#cfn-databrew-schedule-cronexpression
        '''
        result = self._values.get("cron_expression")
        assert result is not None, "Required property 'cron_expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the schedule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html#cfn-databrew-schedule-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def job_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of jobs to be run, according to the schedule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html#cfn-databrew-schedule-jobnames
        '''
        result = self._values.get("job_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata tags that have been applied to the schedule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html#cfn-databrew-schedule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScheduleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataset",
    "CfnDatasetProps",
    "CfnJob",
    "CfnJobProps",
    "CfnProject",
    "CfnProjectProps",
    "CfnRecipe",
    "CfnRecipeProps",
    "CfnRuleset",
    "CfnRulesetProps",
    "CfnSchedule",
    "CfnScheduleProps",
]

publication.publish()
