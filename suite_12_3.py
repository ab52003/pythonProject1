import unittest
import unit_1
import unit_2

calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(unit_1.RunnerTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(unit_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)