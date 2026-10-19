"""Tests for the greeting example."""

import unittest

from main import greet


class GreetTests(unittest.TestCase):
    """Checks greeting output."""

    def test_greet_with_name(self):
        """Includes the supplied name in the greeting."""
        self.assertEqual(greet("Giovanni"), "Hello, Giovanni!")

    def test_greet_defaults_to_world(self):
        """Uses the default name when none is supplied."""
        self.assertEqual(greet(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
