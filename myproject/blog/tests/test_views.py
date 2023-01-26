from django.urls import reverse
from django.test import TestCase
from blog.models import Blog,Author


class BlogViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_blogs = 20
        for blog in range(1,number_of_blogs):
            author = Author.objects.create(
                name = f'Sardar Patel {blog}',
                about_author = f'Vallabhbhai Jhaverbhai Patel,{blog} commonly known as Sardar Patel, was an Indian lawyer, influential political leader, barrister and statesman who served as the first Deputy Prime Minister and Home Minister of India from 1947 to 1950'
            )
            Blog.objects.create(
                title = f"{blog} lorem {blog} is lorem The BlogLis is accessible at the expected blogs {blog}",
                content = f"{blog} The Indian team was led by off spinner Srinivasaraghavan Venkataraghavan and included leading batsmen Sunil Gavaskar, Gundappa Vishwanath, and Farokh Engineer as well as Venkataraghavan's teammate from the Indian spin quartet, Bishen Singh Bedi. The team was relatively inexperienced at one-day cricket, having played . ",
                author = author
            )
    
    def test_view_url_exists_at_given_url(self):
        response = self.client.get('/blog/blogs/')
        self.assertEqual(response.status_code,200)

    def test_view_url_exists_at_given_url_name(self):
        response = self.client.get(reverse('blog:bloglistview'))
        self.assertEqual(response.status_code,200)

    def test_view_with_expected_template(self):
        response = self.client.get(reverse('blog:bloglistview'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'blog/bloglistpage.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('blog:bloglistview'))
        self.assertEqual(response.status_code,200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['object_list']),5)