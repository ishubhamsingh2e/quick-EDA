import pandas
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
    def __init__(self, data_frame: pandas.DataFrame) -> None:
        self.date_table: pandas.DataFrame = data_frame
        self.datatype_map = dict()

        try:
            for column in self.date_table.columns:
                self.datatype_map[column] = str(self.date_table[column].dtype)
        except:
            print("exception")
            return None

    def set_types(self, value_dict: dict) -> bool:

        for i in value_dict.keys():
            if i in self.datatype_map and value_dict[i] in default_types:
                self.datatype_map[i] = value_dict[i]
            else:
                return 1

    def to_nominal(self, serise_name: str) -> bool:
        if (serise_name and (serise_name in self.datatype_map.keys())):
            self.datatype_map[serise_name] = default_types[1]
            return 0
        else:
            return 1

    def to_ordinal(self, serise_name: str) -> bool:
        if (serise_name and (serise_name in self.datatype_map.keys())):
            self.datatype_map[serise_name] = default_types[2]
            return 0
        else:
            return 1

    def to_discrete(self, serise_name: str) -> bool:
        if (serise_name and (serise_name in self.datatype_map.keys())):
            self.datatype_map[serise_name] = default_types[3]
            return 0
        else:
            return 1

    def to_continuous(self, serise_name: str) -> bool:
        if (serise_name and (serise_name in self.datatype_map.keys())):
            self.datatype_map[series_name] = default_types[4]
            return 0
        else:
            return 1

    def __str__(self):
        return f"{self.datatype_map}"
