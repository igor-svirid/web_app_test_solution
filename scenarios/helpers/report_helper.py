class ReportHelper:
    """Class for handling reports' data"""
    @classmethod
    def get_report_column_names(cls, report: str) -> list[str]:
        """
        Gets all column names for the report
        :arg:
         - report: string representation of a report
        :returns: list of string representation of column names
        """
        return [name for name in cls.__get_lines_with_info(report)[0].split('|')]

    @classmethod
    def get_line_names(cls, report: str) -> list[str]:
        """
        Get all line names for the report
        :arg:
         - report: string representation of a report
        :returns: list of string representation of line names
        """
        lines_without_header = cls.__get_lines_with_info(report)[1:]
        return [line.split('|')[0] for line in lines_without_header]

    @staticmethod
    def __get_lines_with_info(report: str) -> list[str]:
        """
        Get all lines of the report with data
        :arg:
         - report: string representation of a report
        :returns: list of string representation of lines with data
        """
        all_lines = report.split('\n')
        return [line.replace(' ', '')[1:-1] for line in all_lines if line.startswith('|')]
