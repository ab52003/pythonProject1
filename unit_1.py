import my_work12

import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        run1 = my_work12.Runner('runner1')
        distance = 0
        for i in range(10):
            distance = run1.walk()
            return distance
        self.assertEqual(distance, 50)

    def test_run(self):
        run2 = my_work12.Runner('runner2')
        distance = 0
        for i in range(10):
            distance = run2.run()
            return distance
        self.assertEqual(distance, 100)

    def test_challenge(self):
        run3 = my_work12.Runner('runner3')
        run4 = my_work12.Runner('runner4')
        distance1 = 0
        distance2 = 0
        for i in range(10):
            distance1 = run3.run()
            distance2 = run4.run()
            return distance1, distance2
        self.assertNotEqual(distance1, distance2)

if __name__ == '__main__':
    unittest.main()