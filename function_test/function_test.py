from selenium import webdriver
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
        self.browser.get('http://localhost:8000')

        #
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')


if __name__ == '__main__':
    # unittest.main(warnings='ignore')
    unittest.main()
