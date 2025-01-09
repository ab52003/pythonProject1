import my_work12_4
import unittest
import logging

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            run1 = my_work12_4.Runner('runner1', -10)
            distance = 0
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                distance = run1.walk()
                return distance
            self.assertEqual(distance, 50)
        except:
            logging.warning('Неверная скорость для Runner')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            run2 = my_work12_4.Runner('runner2', g)
            distance = 0
            logging.info('"test_run" выполнен успешно')
            for i in range(10):
                distance = run2.run()
                return distance
            self.assertEqual(distance, 100)
        except:
            logging.warning('Неверный тип данных для объекта Runner')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run3 = my_work12_4.Runner('runner3')
        run4 = my_work12_4.Runner('runner4')
        distance1 = 0
        distance2 = 0
        for i in range(10):
            distance1 = run3.run()
            distance2 = run4.run()
            return distance1, distance2
        self.assertNotEqual(distance1, distance2)

if __name__ == '__main__':
    unittest.main()

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8', format='%(asctime)s | %(levelname)s | %(message)s')