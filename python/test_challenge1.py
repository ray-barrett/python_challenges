#!/bin/python3

import pytest

import challenge1


@pytest.mark.parametrize(
    "date_pairs, expected",
    [
        (
            [
                "Sun 10 May 2015 13:54:36 -0700",
                "Sun 10 May 2015 13:54:36 -0000",
                "Sat 02 May 2015 19:54:36 +0530",
                "Fri 01 May 2015 13:54:36 -0000",
            ],
            [25200, 88200],
        )
    ],
)
def test_time_differences(date_pairs, expected):
    assert challenge1.time_differences(date_pairs) == expected


@pytest.mark.parametrize(
    "date_pairs, expected",
    [
        (
            [
                "Sun 10 May 2015 13:54:36 -0700",
                "Sun 10 May 2015 13:54:36 -0000",
                "Sat 02 May 2015 19:54:36 +0530",
            ],
            [25200],
        )
    ],
)
def test_uneven_pairs(date_pairs, expected):
    with pytest.raises(IndexError):
        challenge1.time_differences(date_pairs)


def test_wrong_format():
    pair = ["2019/10/10 20:20:20", "2019/10/11 20:20:20"]
    with pytest.raises(ValueError):
        challenge1.time_differences(pair)
