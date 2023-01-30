import datetime
from django.test import TestCase
from .models import Bulletin

class BulletinModelTests(TestCase):

    def test_save_and_retrieve(self):
        """
        日記データの保存と取得を確認
        """
        Bulletin.objects.create(title='test_title', text='test_text')
        actual_bulletin = Bulletin.objects.get(title='test_title')
        self.assertEqual(actual_bulletin.title, 'test_title')