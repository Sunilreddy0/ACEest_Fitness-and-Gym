import unittest
from unittest.mock import MagicMock, patch
from ACEest_Fitness import FitnessTrackerApp

# Python

class TestFitnessTrackerAppInit(unittest.TestCase):
    @patch("ACEest_Fitness.tk.Label")
    @patch("ACEest_Fitness.tk.Entry")
    @patch("ACEest_Fitness.tk.Button")
    def test_init_widgets_and_title(self, mock_button, mock_entry, mock_label):
        mock_master = MagicMock()
        app = FitnessTrackerApp(mock_master)

        mock_master.title.assert_called_once_with("ACEestFitness and Gym")
        self.assertEqual(app.workouts, [])

        self.assertEqual(mock_label.call_count, 2)
        self.assertEqual(mock_entry.call_count, 2)
        self.assertEqual(mock_button.call_count, 2)

        self.assertTrue(mock_label.return_value.grid.called)
        self.assertTrue(mock_entry.return_value.grid.called)
        self.assertTrue(mock_button.return_value.grid.called)

if __name__ == "__main__":
    unittest.main()