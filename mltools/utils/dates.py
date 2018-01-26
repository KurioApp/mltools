import datetime
import logging

import iso8601
import pytz

_logger = logging.getLogger(__name__)

utc = pytz.UTC
jakarta_tz = pytz.timezone("Asia/Jakarta")


def datetime_to_posix(dt):
    """
    Convert Python's datetime to POSIX time (a.k.a. UNIX epoch).

    Args:
        dt (datetime.datetime): Python's datetime

    Returns:
        float: POSIX time of the Python's datetime

    """
    if dt.tzinfo is None:
        _logger.warning("datetime has no tzinfo. using it as UTC")
        dt = utc.localize(dt)
    return dt.timestamp()


def posix_to_datetime(t, timezone=utc):
    """
    Convert POSIX time (a.k.a. UNIX epoch) to Python's datetime.

    Args:
        t (int|float): POSIX time
        timezone (datetime.tzinfo): Timezone to be included in Python's
            datetime.

    Returns:
        datetime.datetime: Python's datetime of the POSIX time

    """
    dt = utc.localize(datetime.datetime.utcfromtimestamp(t))
    return dt.astimezone(timezone)


def datetime_to_string(dt):
    """
    Convert Python's datetime to string.
    To make sure the behavior is correct, simply specify tzinfo in Python's
    datetime.

    Args:
        dt (datetime.datetime): Python's datetime

    Returns:
        str: The string representation of Python's datetime.
            In the case of datetime(2016, 1, 2, 15, 4, 5, 999999, tzinfo=utc),
            this function will return: '2016-01-02T15:04:05.999999+00:00'

    """
    if not isinstance(dt, datetime.datetime):
        raise ValueError("dt must be datetime.datetime")
    if dt.tzinfo is None:
        _logger.warning("datetime has no tzinfo. using it as UTC")
        dt = utc.localize(dt)
    return dt.isoformat()


def string_to_datetime(s, timezone=None):
    """
    Convert a string to Python's datetime

    Args:
        s (str): The datetime string with one of these formats:
            - 2016-01-02T08:04:05.999999Z
            - 2016-01-02T15:04:05.999999+07:00
            - 2016-01-02T08:04:05.999999+00:00
            - 2016-01-02T12:04:05.999999+04:00
            - 2016-01-02T01:04:05.999999-07:00
            - 2016-01-02 08:04:05.999999Z
            - 2016-01-02 15:04:05.999999+07:00
            - 2016-01-02 08:04:05.999999+00:00
            - 2016-01-02 12:04:05.999999+04:00
            - 2016-01-02 01:04:05.999999-07:00
            - 2016-01-02T08:04:05Z
            - 2016-01-02T15:04:05+07:00
            - 2016-01-02T08:04:05+00:00
            - 2016-01-02T12:04:05+04:00
            - 2016-01-02T01:04:05-07:00
            - 2016-01-02 08:04:05Z
            - 2016-01-02 15:04:05+07:00
            - 2016-01-02 08:04:05+00:00
            - 2016-01-02 12:04:05+04:00
            - 2016-01-02 01:04:05-07:00
        timezone (datetime.tzinfo|None): Timezone to be included in Python's
            datetime.

    Returns:
        datetime.datetime: Python's datetime of the string

    Raises:
        ValueError: input is not a valid datetime

    """
    try:
        dt = iso8601.parse_date(s)
        if timezone is None:
            return dt
        print(timezone)
        return dt.astimezone(timezone)
    except iso8601.ParseError:
        raise ValueError("not a valid datetime")
