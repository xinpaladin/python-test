from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest


# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')

# # assert 'Django' in browser.title
# assert 'To-Do' in browser.title, 'Browser title was %s' % browser.title

# browser.quit()

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_adn_retrieve_it_later(self):
        # 听说一个很酷的在线待办事项应用
        # 看首页
        self.browser.get('http://localhost:8000')

        # 注意到 标题和头部都包含"To-Do"这个词
        self.assertIn('To-Do', self.browser.title)
        headers_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', headers_text)

        # 输入待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )
        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
    # unittest.main()
