from requests import Response

from framework.utils.random_utils import RandomUtils


class Device:
    """Class to describe a device"""
    ADDRESS: str = "address"
    NAME: str = "name"
    PIN_1_DUTY: str = "pin_1_pwm_d"
    PIN_1_FREQUENCY: str = "pin_1_pwm_f"
    PIN_2_DUTY: str = "pin_2_pwm_d"
    PIN_2_FREQUENCY: str = "pin_2_pwm_f"
    TYPE: str = "type"
    AVAILABLE_FREQUENCIES: list[int] = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    MAX_DUTY: int = 100
    FIELD_NAMES: list[str] = [ADDRESS, NAME, TYPE, PIN_1_DUTY, PIN_1_FREQUENCY, PIN_2_DUTY, PIN_2_FREQUENCY]

    def __init__(self, **kwargs):
        """
        Initializes device
        :arg:
         - kwargs: any of ADDRESS, NAME, TYPE, PIN_1_DUTY, PIN_1_FREQUENCY, PIN_2_DUTY, PIN_2_FREQUENCY
        """
        self.address = kwargs[self.ADDRESS]
        self.name = kwargs[self.NAME]
        self.pin_1_pwm_d = kwargs[self.PIN_1_DUTY]
        self.pin_1_pwm_f = kwargs[self.PIN_1_FREQUENCY]
        self.pin_2_pwm_d = kwargs[self.PIN_2_DUTY]
        self.pin_2_pwm_f = kwargs[self.PIN_2_FREQUENCY]
        self.type = kwargs[self.TYPE]

    def __eq__(self, other) -> bool:
        """
        Describes equality of 2 devices
        :returns: True if devices are equal
        """
        return other.__dict__ == self.__dict__

    def __str__(self) -> str:
        """
        Describes string representation of device parameters
        :returns: string representation of device parameters
        """
        return f'Name: {self.name}. Address: {self.address}. Type: {self.type}. ' \
               f'Pin 1 - duty: {self.pin_1_pwm_d}, frequency: {self.pin_1_pwm_f} '\
               f'Pin 2 - duty: {self.pin_2_pwm_d}, frequency: {self.pin_2_pwm_f}'

    def get_duty_for_pin(self, pin_number: int) -> int:
        """
        Get duty by number of pin
        :arg:
         - pin_number: number of pin to access duty
        :returns: value of duty in %
        """
        key = f'pin_{pin_number - 1}_pwm_d'
        return self.__dict__[key]

    def get_frequency_by_pin(self, pin_number: int) -> int:
        """
        Get frequency by number of pin
        :arg:
         - pin_number: number of pin to access frequency
        :returns: value of frequency in Hz
        """
        key = f'pin_{pin_number - 1}_pwm_f'
        return self.__dict__[key]

    def generate_new_random_parameters(self) -> None:
        """Generates new random values for pin parameters not equal to the current"""
        self.pin_1_pwm_d = self.generate_random_duty_not_equal_to(self.pin_1_pwm_d)
        self.pin_1_pwm_f = self.generate_random_frequency_not_equal_to(self.pin_1_pwm_f)
        self.pin_2_pwm_d = self.generate_random_duty_not_equal_to(self.pin_1_pwm_d)
        self.pin_2_pwm_f = self.generate_random_frequency_not_equal_to(self.pin_1_pwm_f)

    @classmethod
    def get_list_of_devices_from_response(cls, response: Response) -> list['Device']:
        """
        Generates list of devices from provided api response
        :arg:
         - response: response from api for get devices request
        :returns: list of devices generate from response
        """
        return [cls(**device) for device in response.json()]

    @classmethod
    def generate_random_frequency_not_equal_to(cls, not_equal_value: int, frequency_list=None) -> int:
        """
        Returns new randomly generated frequency
        :arg:
         -not_equal_value: frequency value that should not be generated
        :optional arg:
         -frequency_list: list[int] -> list of frequencies available for generation. If None gets list from TestData
        :returns: randomly generated new integer value of frequency in Hz
        """
        return RandomUtils.get_random_value_from_sequence_not_in(
            cls.AVAILABLE_FREQUENCIES if not frequency_list else frequency_list, [not_equal_value])

    @classmethod
    def generate_random_duty_not_equal_to(cls, not_equal_value: int) -> int:
        """
        Returns new randomly generated duty from 0 to 100%
        :args:
         -not_equal_value: duty value that should not be generated
        :returns: randomly generated new integer value of duty in %
        """
        return RandomUtils.get_random_int_value_not_in(cls.MAX_DUTY, [not_equal_value])
