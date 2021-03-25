import unittest
from function_testing.ex1.name import get_full_name


class NameTest(unittest.TestCase):
    def test_ism(self):
        name = get_full_name('alijon', 'Valiyev')
        self.assertEqual(name, 'Alijon Valiyev')

    def test_otasi(self):
        name = get_full_name('alijon', 'valiyev', 'ikromovich')
        self.assertEqual(name, 'Alijon Valiyev Ikromovich')


unittest.main()
