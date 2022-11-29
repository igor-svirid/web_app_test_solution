class ErrorMessage:
    """Class with possible error messages"""
    REPORT_MISSING_ERROR_MESSAGE: str = "Report is not exist"
    INVALID_TYPE_MESSAGE_TEMPLATE: str = "Invalid type of '{}' value"
    INVALID_FREQUENCY_VALUE_TEMPLATE: str =\
        "Invalid value of '{}' value. Valid values (Hz) are 1, 2, 5, 10, 20, 50, 100, 200, 500"
    INVALID_DUTY_VALUE_TEMPLATE: str = "Invalid value of '{}' value. Valid diapason is 0 - 100 (%)"
    SPECIFY_PARAMETERS_MESSAGE = "Please specify one of values: 'duty1', 'freq1', 'duty2', 'freq2'"
    SPECIFY_PARAMETER_MESSAGE_TEMPLATE = "Please specify '{}' value"
    INVALID_ADDRESS_API_MESSAGE = "Invalid value of address"
