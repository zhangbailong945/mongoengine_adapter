from tests.test_adapter import TestConfig
import unittest

#test
if __name__ == "__main__":
    #suite
    suite=unittest.TestSuite()
    suite.addTest(TestConfig("test_enforcer_basic"))
    suite.addTest(TestConfig("test_add_policy"))
    suite.addTest(TestConfig("test_save_policy"))
    suite.addTest(TestConfig("test_str"))
    suite.addTest(TestConfig("test_repr"))
    #run test
    runner=unittest.TextTestRunner()
    runner.run(suite)
    