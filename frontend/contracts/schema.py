from typing import Union, Dict

GenericSchema = Dict[str, Union[str, float, int]]

CompraSchema: GenericSchema = {
    "ean": str,
    "prince": float,
    "store": int,
    "dateTime": str

}