import my_work12_2

import unittest

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run1 = my_work12_2.Runner('Усэйн', 10)
        self.run2 = my_work12_2.Runner('Андрей', 9)
        self.run3 = my_work12_2.Runner('Ник', 3)

    def tearDownClass():
        list = {}
        for key, value in TournamentTest.all_results.items():
            list.update({key: str(value)})
        return list

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run1(self):
        Tournament = my_work12_2.Tournament(90, self.run1, self.run3)
        TournamentTest.all_results.update(Tournament.start())
        print(TournamentTest.tearDownClass())
        key_val = max(list(TournamentTest.all_results.items()))
        self.assertTrue(key_val[1], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run2(self):
        Tournament = my_work12_2.Tournament(90, self.run2, self.run3)
        TournamentTest.all_results.update(Tournament.start())
        print(TournamentTest.tearDownClass())
        key_val = max(list(TournamentTest.all_results.items()))
        self.assertTrue(key_val[1], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run3(self):
        Tournament = my_work12_2.Tournament(90, self.run2, self.run1, self.run3)
        TournamentTest.all_results.update(Tournament.start())
        print(TournamentTest.tearDownClass())
        key_val = max(list(TournamentTest.all_results.items()))
        self.assertTrue(key_val[1], 'Ник')


if __name__ == '__main__':
    unittest.main()