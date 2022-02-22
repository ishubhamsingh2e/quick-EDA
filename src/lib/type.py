subtypes = ("nominal", "ordianal", "discrete", "continuous")


class nominal:
    def __init__(self, data) -> None:
        self.data: pandas.Series = data
        self.subtype = subtypes[0]

    def __str__(self):
        return f"[Name: {self.data.name}, Lenght: {self.data.size}, dtype: {self.data.dtype}, subtype: { self.subtype}]"


class ordinal:
    def __init__(self, data) -> None:
        self.data: pandas.Series = data
        self.subtype = subtypes[1]

    def __str__(self):
        return f"[Name: {self.data.name}, Lenght: {self.data.size}, dtype: {self.data.dtype}, subtype: { self.subtype}]"


class discrete:
    def __init__(self, data) -> None:
        self.data: pandas.Series = data
        self.subtype = subtypes[2]

    def __str__(self):
        return f"[Name: {self.data.name}, Lenght: {self.data.size}, dtype: {self.data.dtype}, subtype: { self.subtype}]"


class continuous:
    def __init__(self, data) -> None:
        self.data: pandas.Series = data
        self.subtype = subtypes[3]

    def __str__(self):
        return f"[Name: {self.data.name}, Lenght: {self.data.size}, dtype: {self.data.dtype}, subtype: { self.subtype}]"


if __name__ == "__main__":
    import pandas
    df = pandas.read_csv(
        "C:/Users/shubham/Downloads/State Pregnancy-Birth-Abortion Rates.csv")
    obj0 = discrete(df["State"])
    print(obj0)
