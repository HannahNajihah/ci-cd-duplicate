import sys
import os
import pytest
import pandas as pd  # Add this import

# Add the src directory to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import load_and_process_data

def test_no_duplicates(capsys):
    """Test if duplicate rows are removed."""
    
    # Run the function
    load_and_process_data("data/dataset.csv", "data/test_processed_dataset.csv")
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Check that the print statements include the expected lines
    assert "Original dataset shape" in captured.out
    assert "Dataset shape after removing duplicates" in captured.out
    
    # Load the processed dataset and check for duplicates
    df = pd.read_csv("data/test_processed_dataset.csv")
    assert df.duplicated().sum() == 0, "Duplicate rows were not fully removed"
