from typing import Any


class Asserts:

    @staticmethod
    def soft_assert(checks: list[tuple[bool, str]]) -> None:
        """
        Soft assertion for different kinds of comparative functions
        :arg:
         - checks: list of tuples [(expression, error_message)]
        :raises: AssertionError if any check is False
        :using:
         when there is a need to assert some different results without failing test upon first failed check:

         soft_assert([(a == b, 'a is not equal b'), (a != b, 'a equals b')])
        """
        errors = [check[1] for check in checks if not check[0]]

        if errors:
            raise AssertionError('\n'.join(errors))

    @staticmethod
    def assert_true(expression: bool, check_parameter: str) -> None:
        """
        Assertion of result to be True
        :args:
         - expression: function that returns bool value
         - check_parameter: string representation of what expects to be True. Will be part of error message
        """
        assert expression, f'Expected [{check_parameter}] to be True, but was False'

    @staticmethod
    def assert_equal(expected_value: Any, actual_value: Any) -> None:
        """
        Assertion of two values to be equal
        :args:
         - expected_value: value that is expected
         - actual_value: value that should be equal to expected_value
        """
        assert expected_value == actual_value, f'Expected: {expected_value}. Actual: {actual_value}'

    @staticmethod
    def soft_are_equal(expected_values: dict[str: Any], actual_values: dict[str: Any]) -> None:
        """
        Soft assertion for comparing values of two dictionaries to be equal
        :args:
         - expected_values: dict with values that are expected
         - actual_values: value that should be equal to expected_values
        :raises: AssertionError any of actual_value is not equal to its expected_value
        """
        message = '{} -> Expected: {}. Actual: {}'
        errors = []

        for key in expected_values:
            if expected_values[key] != actual_values[key]:
                errors.append(message.format(key, expected_values[key], actual_values[key]))

        if errors:
            raise AssertionError('\n'.join(errors))

    @staticmethod
    def not_empty(value: Any, value_name: str) -> None:
        """
        Assertion for checking value to be not empty
        :args:
         - value: value that expects to be not empty
         - value_name: name of the checking value. Will be a part of the error message
        """
        assert value, f"{value_name} is empty"

    @staticmethod
    def not_equal(expected_value: Any, actual_value: Any, value_name: str) -> None:
        """
        Assertion of two values to be not equal
        :args:
         - expected_value: value that is not expected
         - actual_value: value that should be not equal to expected_value
        """
        assert expected_value != actual_value, f"Expected {value_name} to be not equal to {expected_value}"
