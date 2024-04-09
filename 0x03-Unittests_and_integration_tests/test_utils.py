#!/usr/bin/env python3
"""Testing the utils file"""
from unittest import TestCase, main
from unittest.mock import Mock, patch
from parameterized import parameterized_class, parameterized
from utils import access_nested_map, get_json, memoize, requests
from typing import Mapping, Sequence, Any, Dict


class TestAccessNestedMap(TestCase):
    """Unittest class for testing the function
    access_nested_map from utils.py

    Args:
        TestCase (unittest): The base Unittest
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, result: Any) -> None:
        """Tests the access_nested_map function of
        utils.py

        Args:
            nested_map (Mapping): the dit to check
            path (Sequence): the path representing the no of
            depths to travel
            result (Any): the result
        """
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, result)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence, key: str) -> None:
        """Test that a key error is raised when the
        key in the path is not in the dict
        Args:
            nested_map (Mapping): the map in question
            path (Sequence): the path representing the no of
            depths to travel
            key (Str): the expected Error message
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        message = str(context.exception).strip("\'")
        self.assertEqual(message, key)


class TestGetJson(TestCase):
    """Tests the get_json function

    Args:
        unittest (_type_): base unittest class
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str,
                      test_payload: Dict[str, bool], mock_get: Mock) -> None:
        """Tests the get_json function

        Args:
            test_url (str): the url
            test_payload (dict): the return value
            mock_get (Mock): the mocked function
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(TestCase):
    """Tests the memoize function

    Args:
        TestCase (unittest): the base Test class
    """

    def test_memoize(self) -> None:
        """Tests the memoize function
        """
        class TestClass:
            """A test class for the purposes of this test
            """

            def a_method(self) -> int:
                """A simple test method

                Returns:
                    int: 42
                """
                return 42

            @memoize
            def a_property(self) -> int:
                """A getter to test the memoize function

                Returns:
                    int: a_method()
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            v = TestClass()
            result = v.a_property
            x = v.a_property
            mock_method.assert_called_once()


if __name__ == '__main__':
    main()
