import pytest
import logging
import allure

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('testmodel')


def setup_module():
    log.debug('xianzhixing')
    print('xianzhixing')


def teardown_module():
    log.debug('houzhixing')
    print('houzhixing')

@allure.feature("模型测试模块")
class TestModel:
    def setup_method(self):
        print('setupmethod')

    def teardown_method(self):
        print('teardownmethod')

    @allure.story("测试test_tt")
    def test_tt(self):
        print('ssssss')

    @allure.story("测试test_mm")
    def test_mm(self):
        print('test mm')

    @allure.story("测试test_ff")
    def test_ff(self):
        print('test ff')
