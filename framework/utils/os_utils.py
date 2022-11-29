import os


class OsUtils:
    @staticmethod
    def create_directory_if_not_exist(path_to_directory: str) -> None:
        """
        Creates directory if it doesn't exist
        :arg:
         - path_to_directory: full path for directory that is required
        """
        if not os.path.exists(path_to_directory):
            os.makedirs(path_to_directory)

    @staticmethod
    def get_current_work_dir() -> str:
        """
        Gets current working directory for the solution
        :returns: base directory for the solution
        """
        return os.getcwd()
