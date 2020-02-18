import urllib.parse
from queue import Empty, Queue
from typing import Any
from urllib.request import unquote

queue = Queue
queue_empty = Empty
urldecode = unquote
urlsplit: Any
parse_qs: Any
bytes = str
builtin_range = range
range = xrange
builtin_str = str
str = unicode
basestring = basestring
queue = Queue
queue_empty = Empty
urldecode = unquote
parse_qs = urllib.parse.parse_qs
builtin_range = range
builtin_str = str
long = int
bytes = bytes
range = range
str = str
numeric_types: Any

def urlencode(resource: Any): ...
def queryencode(query: Any): ...
