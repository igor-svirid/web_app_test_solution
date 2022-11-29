from typing import Any

from scenarios.enums.device_table_columns import TableColumn
from scenarios.models.device import Device


class TestData:
    """Class with tests data"""
    PIN_NUMBERS: list[int] = [2, 3]
    INVALID_PARAMETER_VALUES: list[Any] = [-1, 0.5, 101, "parameter", "!@#$%", ""]
    AVAILABLE_REPORT_TYPES: list[int] = [100, 200, 300, 400]
    DEVICE_PATCH_PARAMETERS: list[str] = ['freq1', 'freq2', 'duty1', 'duty2']
    DEVICE_INVALID_ADDRESSES: list[Any] = [0, "parameter", "!@#$%", ""]
    DEVICE_PAGE_BUTTON_COLUMNS: list[TableColumn] = [TableColumn.MONITORING, TableColumn.DIAGNOSTICS]
    REPORT_ID_PARAMETER_NAME: str = "repId"
    ADDRESS_PARAMETER_NAME: str = "address"
    WEBSOCKET_MESSAGES_PARAMS = [('duties', [Device.PIN_1_DUTY, Device.PIN_2_DUTY]),
                                 ('freqs', [Device.PIN_1_FREQUENCY, Device.PIN_2_FREQUENCY])]
