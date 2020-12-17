import time

import allure
import pytest
from common.log import Log
from common.read_yml import ReadYaml
from pages.login_page import LoginPage
from pages.news_page import NewsPage
from selenium import webdriver

testdata = ReadYaml('news_page.yml').get_yaml_data()  # 读取数据


class Test_news():
    log = Log()

    @allure.feature("功能点：添加新闻")
    @allure.story("用例：用户新添加新闻")
    @pytest.mark.parametrize("title,author,abstract", testdata["test_add_news_data"], ids=["正常添加"])
    # @pytest.mark.skip('跳过该成功用例')
    def test_add_new(self, login_fixtrue, title, author, abstract):
        driver = login_fixtrue
        new = NewsPage(driver)
        with allure.step("点击进入新闻管理模块"):
            new.come_news()
            time.sleep(2)
        with allure.step("点击进入新增新闻页面"):
            new.add_news()
        with allure.step("输入新闻标题"):
            new.input_title(title)
        with allure.step("点击自定义作者"):
            new.click_CustomAuthor()
        with allure.step("输入自定义作者名"):
            new.input_author(author)
            time.sleep(2)
        with allure.step("选择TMT(一级)频道"):
            new.input_channel()
        with allure.step("选择原创类型"):
            new.input_type()
            new.select_tpye()
            time.sleep(7)
        with allure.step("选择同步首页"):
            new.select_homePage()
        with allure.step("填写摘要"):
            new.input_abstract(abstract)
        time.sleep(5)
        # assert result
        # web.is_quit()

    # @allure.feature("功能点：用户登录页面")
    # @allure.story("用例：用户登录")
    # @pytest.mark.parametrize("username,password,msg", testdata["test_login_fail_data"],
    #                          ids=["正确用户名错误密码登录",
    #                               "错误用户名正确密码登录"])
    # # @pytest.mark.skip('跳过')
    # def test_fail_login(self, username, password, msg):
    #     driver = webdriver.Chrome()
    #     web = LoginPage(driver)
    #     web.login(user=username, password=password)
    #     result = web.is_login_fail(expect_text=msg)
    #     self.log.info("登录结果:%s" % result)
    #     assert result
    #     # web.is_quit()
