from common.base import Base
from common.read_yml import ReadYaml
testelement = ReadYaml("news_page.yml").get_yaml_data()

class NewsPage(Base):
    new1 = tuple(testelement["test_add_new"][0]) # 新闻管理
    new2 = tuple(testelement["test_add_new"][1]) # 新增新闻
    new3 = tuple(testelement["test_add_new"][2]) # 输入标题
    new4 = tuple(testelement["test_add_new"][3]) # 自定义作者
    new5 = tuple(testelement["test_add_new"][4]) # 输入作者名
    new6 = tuple(testelement["test_add_new"][5]) # 选择TMT(一级)频道
    new7 = tuple(testelement["test_add_new"][6]) # 选择原创类型输入框
    new8 = tuple(testelement["test_add_new"][7]) # 选择原创类型
    new9 = tuple(testelement["test_add_new"][8]) # 选择同步首页
    new10 = tuple(testelement["test_add_new"][9]) # 选择摘要

    # 判断元素
    # loc4 = tuple(testelement["test_login_element"][3])#登录成功断言
    # loc5 = tuple(testelement["test_login_element"][4])#登录失败断言

    def come_news(self):
        '''进入新闻管理模块'''
        self.click(self.new1)

    def add_news(self):
        '''进入新增新闻'''
        self.click(self.new2)

    def input_title(self, text):
        '''输入新闻标题'''
        self.input(self.new3, text)

    def click_CustomAuthor(self):
        '''点击自定义作者'''
        self.click(self.new4)

    def input_author(self, text):
        '''输入作者名'''
        self.input(self.new5, text)

    def input_channel(self):
        '''选择频道'''
        self.click(self.new6)

    def input_type(self):
        '''点击新闻类型框'''
        self.click(self.new7)

    def select_tpye(self):
        '''选择新闻类型'''
        self.click(self.new8)

    def select_homePage(self):
        '''选择新闻类型'''
        self.click(self.new9)

    def input_abstract(self, text):
        '''填写摘要'''
        self.input(self.new10, text)


    def click_button(self):
        '''点击登录按钮'''
        self.click(self.loc3)

    def login(self, user="admin", password="123456"):
        '''登录'''
        self.driver.get(self.base_url)
        self.input_username(user)
        self.input_password(password)
        self.click_button()

    def is_login_success(self, expect_text='后台页面'):
        text = self.get_text(self.loc4)
        self.log.info("获取到断言元素的文本内容：%s"%text)
        return expect_text == text

    def is_login_fail(self, expect_text='错误'):
        text = self.get_text(self.loc5)
        self.log.info("获取到断言元素的文本内容：%s"%text)
        return expect_text in text


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    web = LoginPage(driver)
    web.login()
    result = web.is_login_fail()
    print("登录结果：", result)
    assert result
    driver.quit()
