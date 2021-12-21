# from cfn_guard_test.test_suite import CfnGuardTestSuite
# from junit_xml import TestCase, TestSuite
#
#
# class CfnGuardReport:
#     """
#     Understands how to create reports
#     """
#
#     def __init__(self, suite: CfnGuardTestSuite):
#         pass
#
#     def write(self, path: str):
#         pass
#
#
#
#
# def validate_writable_path(
#     ctx: click.Context, _: click.Option, value: Optional[str]
# ) -> Optional[str]:
#     # TODO: Check if we can write to the given path
#     return value
#
# @click.option("--junit-path", callback=validate_writable_path)
#
#
#
#     if junit_path:
#         CfnGuardReport(suite).write(junit_path)
