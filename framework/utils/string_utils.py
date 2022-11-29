class StringUtils:
    @staticmethod
    def get_ints_from_string(string: str) -> int:
        """
        Get all integers from string and returns as one integer
        :arg:
         - string: string with integers
        :returns: all integers from string joined into one integer
        """
        return int(''.join([character for character in string if character.isdigit()]))
