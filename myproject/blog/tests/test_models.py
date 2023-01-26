from django.test import TestCase
from datetime import datetime
from blog.models import Author,Blog,Comment

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name = 'Sardar Patel',about_author = 'Vallabhbhai Jhaverbhai Patel, commonly known as Sardar Patel, was an Indian lawyer, influential political leader, barrister and statesman who served as the first Deputy Prime Minister and Home Minister of India from 1947 to 1950')

    def test_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEqual(field_label,'name')

    def test_about_author_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('about_author').verbose_name
        self.assertEqual(field_label,'about author')

    def test_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEqual(max_length,100)

    def test_object_name_is_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.name}'
        self.assertEqual(str(author),expected_object_name)

class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(name = 'Sardar Patel',about_author = 'Vallabhbhai Jhaverbhai Patel, commonly known as Sardar Patel, was an Indian lawyer, influential political leader, barrister and statesman who served as the first Deputy Prime Minister and Home Minister of India from 1947 to 1950')
        Blog.objects.create(title='India won world cup',posted_date = datetime.now(),content = 'The Indian cricket team are two times World Champions. In addition to winning the 1983 Cricket World Cup, India was also first country to win Cricket World Cup on home soil in 2011. They were also runners-up at the 2003 Cricket World Cup, and semifinalists four times (1987, 1996, 2015, 2019).',author = author )

    def test_title_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('title').verbose_name
        self.assertEqual(field_label,'title')

    def test_about_author_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('content').verbose_name
        self.assertEqual(field_label,'content')

    def test_name_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('title').max_length
        self.assertEqual(max_length,100)

    def test_object_name_is_title(self):
        blog = Blog.objects.get(id=1)
        get_object_name = f'{blog.title}'
        self.assertEqual(str(blog),get_object_name)

class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(name = 'Sardar Patel',about_author = 'Vallabhbhai Jhaverbhai Patel, commonly known as Sardar Patel, was an Indian lawyer, influential political leader, barrister and statesman who served as the first Deputy Prime Minister and Home Minister of India from 1947 to 1950')
        blog = Blog.objects.create(title='India won world cup',posted_date = datetime.now(),content = 'The Indian cricket team are two times World Champions. In addition to winning the 1983 Cricket World Cup, India was also first country to win Cricket World Cup on home soil in 2011. They were also runners-up at the 2003 Cricket World Cup, and semifinalists four times (1987, 1996, 2015, 2019).',author = author )
        Comment.objects.create(comment_content = 'GoodGood Good Good Godd good good good hdkjkjhdnbkj askjhkjashdkk',commented_date = datetime.now(),blog = blog)

    def test_comment_content_label(self):        
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('comment_content').verbose_name
        self.assertEqual(field_label,'comment content')

    def test_object_name_is_comment(self):
        comment = Comment.objects.get(id=1)
        get_object_name = f'{comment.comment_content}'
        self.assertEqual(str(comment),get_object_name)
