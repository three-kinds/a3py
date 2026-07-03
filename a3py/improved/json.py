# -*- coding: utf-8 -*-
from typing import Union, List, Dict

import ujson

JsonType = Union[None, bool, int, float, str, List["JsonType"], Dict[str, "JsonType"]]


def fast_loads(str_json: str) -> JsonType:
    return ujson.loads(str_json)


def fast_dumps(obj: JsonType, ensure_ascii: bool = False, **kwargs) -> str:
    return ujson.dumps(obj, ensure_ascii=ensure_ascii, **kwargs)
