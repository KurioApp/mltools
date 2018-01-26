import datetime

from mltools.utils.dates import datetime_to_posix, utc, posix_to_datetime, \
    jakarta_tz, datetime_to_string, string_to_datetime


def test_datetime_to_posix():
    dt = datetime.datetime(2016, 1, 2, 15, 4, 5, 999999, tzinfo=utc)
    t = datetime_to_posix(dt)

    assert t == 1451747045.999999

    dt = datetime.datetime(2016, 1, 2, 15, 4, 5, 999999)
    t = datetime_to_posix(dt)

    assert t == 1451747045.999999


def test_posix_to_datetime():
    t = 1451747045.999999
    dt = posix_to_datetime(t)
    assert dt == datetime.datetime(2016, 1, 2, 15, 4, 5, 999999, tzinfo=utc)
    assert dt.tzinfo.utcoffset(dt) == datetime.timedelta(hours=0)

    dt = posix_to_datetime(t, utc)
    assert dt == datetime.datetime(2016, 1, 2, 15, 4, 5, 999999, tzinfo=utc)
    assert dt.tzinfo.utcoffset(dt) == datetime.timedelta(hours=0)

    dt = posix_to_datetime(t, jakarta_tz)
    assert dt == jakarta_tz.localize(
        datetime.datetime(2016, 1, 2, 22, 4, 5, 999999)
    )
    assert dt.tzinfo.utcoffset(dt) == datetime.timedelta(hours=7)


def test_datetime_to_string():
    dt = datetime.datetime(2016, 1, 2, 15, 4, 5, 999999, tzinfo=utc)
    assert datetime_to_string(dt) == '2016-01-02T15:04:05.999999+00:00'

    dt = jakarta_tz.localize(datetime.datetime(2016, 1, 2, 15, 4, 5, 999999))
    assert datetime_to_string(dt) == '2016-01-02T15:04:05.999999+07:00'

    dt = datetime.datetime(2016, 1, 2, 15, 4, 5, 999999,
                           tzinfo=utc).astimezone(jakarta_tz)
    assert datetime_to_string(dt) == '2016-01-02T22:04:05.999999+07:00'

    dt = datetime.datetime(2016, 1, 2, 15, 4, 5, 999999)
    assert datetime_to_string(dt) == '2016-01-02T15:04:05.999999+00:00'


def test_string_to_datetime():
    s = '2016-01-02T15:04:05.999999+00:00'
    dt = string_to_datetime(s)
    assert dt == datetime.datetime(2016, 1, 2, 15, 4, 5, 999999, tzinfo=utc)
    assert dt.tzinfo.utcoffset(dt) == datetime.timedelta(hours=0)

    s = '2016-01-02T15:04:05.999999+00:00'
    dt = string_to_datetime(s, utc)
    assert dt == datetime.datetime(2016, 1, 2, 15, 4, 5, 999999, tzinfo=utc)
    assert dt.tzinfo.utcoffset(dt) == datetime.timedelta(hours=0)

    s = '2016-01-02T15:04:05.999999+00:00'
    dt = string_to_datetime(s, jakarta_tz)
    assert dt == datetime.datetime(2016, 1, 2, 15, 4, 5, 999999, tzinfo=utc)
    assert dt.tzinfo.utcoffset(dt) == datetime.timedelta(hours=7)
