# content of test_sample.py

import icedtools


def test_ping():
    res = icedtools.ping("hi")
    assert res == "hi"
