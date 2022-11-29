from enum import Enum


class ParameterUnits(Enum):
    """Enum class to match pin parameters with their units"""
    FREQUENCY = 'Hz'
    DUTY = '%'
