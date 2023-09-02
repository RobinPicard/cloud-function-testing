import pytest

from cloud_function_test.functions import create_tests
from cloud_function_test.functions import EventFunctionTest
from cloud_function_test.functions import HttpFunctionTest


def test_create_tests():

    class DummyHttpClass:
        data = {}

    class DummyEventClass:
        event = {}

    # Test with http type
    classes = [DummyHttpClass, DummyHttpClass]
    tests, class_name = create_tests(classes)
    assert len(tests) == 2
    for test in tests:
        assert isinstance(test, HttpFunctionTest)
        assert class_name == HttpFunctionTest

    # Test with event type
    classes = [DummyEventClass, DummyEventClass]
    tests, class_name = create_tests(classes)
    assert len(tests) == 2
    for test in tests:
        assert isinstance(test, EventFunctionTest)
        assert class_name == EventFunctionTest
