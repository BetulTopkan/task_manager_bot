import unittest
import os

def run_tests():
    # tests klasöründeki tüm test dosyalarını bul
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests')

    # Test sonuçlarını çalıştır
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Test sonuçlarına göre çıkış kodu döndür
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    exit(run_tests()) 