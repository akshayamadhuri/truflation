from typing import Callable

import pandas
from truflation.data.connector import Connector


class SourceDetails:
    """
    SourceDetails is a class that encapsulates the details for a data source.
    These details include the name of the source, the type of the source, the
    specific source, the connector used to connect to the source, and a parser
    function to process the data from the source.

    This class serves as a configuration object, providing all necessary details
    required to read from a particular data source.

    Parameters
    ----------
    name: str
        A string that represents the name of the data source.

    source_type: str
        A string that indicates the type of the data source. For example, this
        could be 'override', 'csv', etc.

    source: str
        A string that specifies the particular source of data. The interpretation
        of this string depends on the source_type. For a CSV file, for example,
        this would be the file path.

    connector: Connector (default = None)
        An instance of a Connector class or its subclass used to establish a
        connection with the data source. This is optional and if not provided,
        a default connector may be used.

    parser: Callable[[pandas.DataFrame], pandas.DataFrame] (default = lambda x: x)
        A function that takes a pandas DataFrame as input and returns a
        pandas DataFrame as output. This is used to perform any necessary
        transformations or preprocessing on the data read from the source.
        By default, this is an identity function that returns the input as is.

    Attributes
    ----------
    name: str
        Name of the data source.

    source_type: str
        Type of the data source.

    source: str
        Specific source of data.

    connector: Connector
        Connector instance used to connect to the data source.

    parser: Callable
        Parser function used to process the data from the source.
    """

    def __init__(self, name: str, source_type: str, source: str,  *args, connector: Connector = None,
                 parser: Callable[[pandas.DataFrame], pandas.DataFrame] = None,  **kwargs):
        self.name = name
        # options: override, csv,
        self.source_type = source_type
        self.source = source
        self.connector = connector # instance of overriden class
        self.parser = parser # parser is run on the dataframe that is returned
        self.args = args
        self.kwargs = kwargs

