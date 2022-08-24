# import os
# from click.testing import CliRunner
# from cfn_guard_test import main
#
#
# def test_custom_set() -> None:
#     """
#     Used to load a custom test set in other projects, this is typically commented out and useful when you need to debug!
#     :return:
#     """
#
#     runner = CliRunner()
#     result = runner.invoke(main, ["--rules-path", os.path.expanduser("~/workspace/cfn-guard-cis-benchmark/rules")])
#     assert result.exit_code == 0
