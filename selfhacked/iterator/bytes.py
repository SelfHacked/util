import gzip
from typing import Iterable, Iterator

from selfhacked.io import BytesIterableAsIO
from . import apply, Function

decode: Function[bytes, str] = apply(bytes.decode, encoding='utf-8')


def un_gzip(iterable: Iterable[bytes]) -> Iterator[str]:
    """
    Unzip a gzip byte stream into str, and split by lines.
    """
    readable = BytesIterableAsIO(iterable)
    with gzip.open(readable) as f:
        yield from f