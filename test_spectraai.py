# test_spectraai.py
"""
Tests for SpectraAI module.
"""

import unittest
from spectraai import SpectraAI

class TestSpectraAI(unittest.TestCase):
    """Test cases for SpectraAI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SpectraAI()
        self.assertIsInstance(instance, SpectraAI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SpectraAI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
