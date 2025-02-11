import unittest
import os

def run_tests():
  
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests')

  
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
   
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    exit(run_tests()) 
