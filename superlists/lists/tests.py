from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.models import Item
from lists.views import home_page

# Create your tests here.


class SmokeTest(TestCase):

    # def test_bad_maths(self):
    #     self.assertEqual(1+1, 3)

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     html = response.content.decode('utf8')
    #     # self.assertTrue(html.startswith('<html>'))
    #     # self.assertIn('<title>To-Do lists</title>', html)
    #     # self.assertTrue(html.endswith('</html>'))
    #     expected_html = render_to_string('home.html')
    #     self.assertEqual(html, expected_html)

    def test_django_home_page_returns_correct_html(self):

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_Post_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):
    def test_saving_amd_retriving_items(self):
        first_item = Item()
        first_item.text = 'the first item'
        first_item.save()

        second_item = Item()
        second_item.text = 'the second item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual('the first item', first_saved_item.text)
        self.assertEqual('the second item', second_saved_item.text)
