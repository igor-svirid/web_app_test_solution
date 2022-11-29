import allure

from framework.utils.assert_utils import Asserts
from scenarios.helpers.report_helper import ReportHelper
from scenarios.pages.diagnostics_page import DiagnosticsPage


class DiagnosticsPageSteps:
    """Class to describe steps on the Diagnostics page"""

    REPORT_NAMES: list[str] = ['header names', 'line names']

    def __init__(self, diagnostics_page: DiagnosticsPage):
        """Initialize steps class instance"""
        self.page = diagnostics_page

    def load_report_by_name(self, report_name=None) -> None:
        """
        Selects report if specified and clicks Load Report button
        :optional arg:
         - report_name: Union[str, int] -> name of the report to select
        """
        with allure.step(f"Loading [{report_name}] report"):
            if report_name:
                self.page.select_report(report_name)
            self.page.load_report()

    @allure.step("Asserting report values")
    def assert_report_with_correct_info_loaded(self, expected_report: str) -> None:
        """
        Asserts loaded report equals to the expected_report
        :arg:
         - expected_report: report that is expected to display
        """
        self.__assert_report_loaded()
        Asserts.assert_equal(expected_report, self.page.get_report())

    @allure.step("Asserting displayed report has required columns and lines")
    def assert_correct_report_type_loaded(self, expected_report: str) -> None:
        """
        Asserts loaded report has the same column and line names as the expected_report
        :arg:
         - expected_report: report that is expected to display
        """
        self.__assert_report_loaded()
        actual_report = self.page.get_report()

        expected_report_names = dict(zip(
            self.REPORT_NAMES,
            [ReportHelper.get_report_column_names(expected_report), ReportHelper.get_line_names(expected_report)]))
        actual_report_names = dict(zip(
            self.REPORT_NAMES,
            [ReportHelper.get_report_column_names(actual_report), ReportHelper.get_line_names(actual_report)]
        ))

        Asserts.soft_are_equal(expected_report_names, actual_report_names)

    def assert_error_message_displayed(self, expected_error: str) -> None:
        """
        Asserts error message displayed instead of report
        :arg:
         - expected_error: string representation of error message that should be displayed
        """
        with allure.step(f"Asserting [{expected_error}] message displayed"):
            Asserts.assert_equal(expected_error, self.page.get_report())

    @allure.step("Asserting a report is displayed")
    def __assert_report_loaded(self) -> None:
        """Asserts report displayed on the page"""
        Asserts.assert_true(self.page.is_report_loaded(), 'report loaded')
