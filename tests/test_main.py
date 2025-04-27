import sys
import os

# Add the src directory to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import load_and_process_data

def test_no_duplicates(capsys):  # Use capsys to capture print output
    """Test if duplicate rows are removed and capture print output."""
    # Call the function to load and process the data
    load_and_process_data("data/dataset.csv", "data/test_processed_dataset.csv")
    
    # Capture the output of the print statements
    captured = capsys.readouterr()
    
    # Check if the output contains the expected text
    assert "Original dataset shape:" in captured.out
    assert "Dataset shape after removing duplicates:" in captured.out
    assert "Processed dataset saved to" in captured.out
