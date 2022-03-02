import pandas
import pprint
from colorama import Fore

# don't change order
default_types = (
    "object",
    "nominal",
    "ordianal",
    "discrete",
    "continuous",
    "int64",
    "float64",
    "bool",
    "datetime64"
)


class base:
    """Base class for DataFrame and Type initialization
    """

    def __init__(self, data_frame: pandas.DataFrame) -> None:
        """datatabel is dataframe,
           __datatype_map is structure storing datatypes
           nominaldata map is data

        Args:
            data_frame (pandas.DataFrame): _description_

        Returns:
            _type_: _description_
        """
        self.__date_table: pandas.DataFrame = data_frame
        self.__datatype_map = dict()
        self.nominal_dataMap = dict()
        self.__queue = set()

        try:
            for column in self.__date_table.columns:
                self.__datatype_map[column] = str(
                    self.__date_table[column].dtype)
        except:
            return None

    def set_types(self, value_dict: dict, to_num: bool = False) -> bool:
        """Set the Type for DataFrame Series.

        Args:
            value_dict (dict): dict for data types.
            to_num (bool): to change character data to numrical, data change to numirical can be found in `nominal_dataMap` class variable.

        Returns:
            bool: Success = 0, Failure = 1
        """
        # for nominal conversion
        for i in value_dict.keys():
            if i in self.__datatype_map:
                if value_dict[i] == "nominal":
                    self.to_nominal(i, to_num)
                    self.__datatype_map[i] = value_dict[i]

                elif value_dict[i] == "ordinal":
                    self.to_ordinal(i, order, to_num)
                    self.__datatype_map[i] = value_dict[i]

                elif value_dict[i] == "discrete":
                    self.to_discrete(i)
                    self.__datatype_map[i] = value_dict[i]

                elif value_dict[i] == "continus":
                    self.to_continuous(i)
                    self.__datatype_map[i] = value_dict[i]

                else:
                    print(Fore.RED + "ERROR: " +
                          Fore.WHITE + f"Not a Valid Type {i}")
            else:
                return 1

        return 0

    def to_nominal(self, serise_name: str, to_num: bool = False) -> bool:
        """conver a seriese to nominal data type

        Args:
            serise_name (str): column name

        Returns:
            bool: Success = 0, Failure = 1
        """
        if (serise_name and (serise_name in self.__datatype_map.keys())):
            self.__datatype_map[serise_name] = default_types[1]
            unique = self.__date_table[serise_name].unique()
            if to_num:
                counter = 0
                for unique_value in unique:
                    self.nominal_dataMap[unique_value] = counter
                    self.__date_table[serise_name].replace({
                        unique_value: counter
                    }, inplace=True)
                    counter += 1
                return 0
        else:
            return 1

    def to_ordinal(self, serise_name: str, order: set, to_num=False) -> bool:
        """converts a series to ordinal data type

        Args:
            serise_name (str): column name

        Returns:
            bool: Success = 0, Failure = 1
        """

        if order:
            if to_num:
                counter = 0
                for value in order:
                    self.__date_table[serise_name].replace({
                        value: counter
                    })
                    counter += 1
            else:
                self.__queue = order
            return 0

        else:
            return 1

        if (serise_name and (serise_name in self.__datatype_map.keys())):
            self.__datatype_map[serise_name] = default_types[2]
            return 0
        else:
            return 1

    def to_discrete(self, serise_name: str) -> bool:
        """converts data to discrete

        Args:
            serise_name (str): column name

        Returns:
            bool: Success = 0, Failure = 1
        """

        if (serise_name and (serise_name in self.__datatype_map.keys())):
            print(Fore.RED + 'Warning: ', end="")
            conf = input(
                Fore.WHITE + "data loss is possible, to conform press (y or n) > ")

            if (conf == "y" or conf == "Y"):
                self.__date_table[serise_name] = self.__date_table[serise_name].astype(
                    int)
                self.__datatype_map[serise_name] = default_types[3]
                print(Fore.GREEN + "Conversion Sucess\n", Fore.WHITE)
                return 0
            elif (conf == "n" or conf == "N"):
                return 0
            else:
                print(Fore.RED + "ERROR OCCURRED" + Fore.WHITE)
                return 0
            return 0
        else:
            return 1

    def to_continuous(self, serise_name: str) -> bool:
        """converts series to continuous

        Args:
            serise_name (str): column name

        Returns:
            bool: Success = 0, Failure = 1
        """
        if (serise_name and (serise_name in self.__datatype_map.keys())):
            try:
                self.__date_table[serise_name] = self.__date_table[serise_name].astype(
                    float)
                self.__datatype_map[serise_name] = default_types[4]
            except:
                print(
                    Fore.RED + f"Not able to conver data to {default_types[4]}\n" + Fore.WHITE)
                return 0
        else:
            return 1

    def info(self, nominal: bool = False):
        """outputs data information in stdout

        Args:
            nominal (bool): to show nomial data

        Returns:
            bool: Success = 0, Failure = 1
        """
        if self.__datatype_map.keys() != 0:
            print("dtyps: ")
            pprint.pprint(self.__datatype_map)
            print()

        if self.nominal_dataMap.keys() != 0 and nominal:
            print("nominal: ")
            pprint.pprint(self.nominal_dataMap)
            print()

    def __str__(self):
        return f"{self.__date_table}"
