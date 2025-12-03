#!/bin/bash

# --- Activate virtual environment ---
# Adjust the path to your venv if different
VENV_PATH="./.venv"

if [ -f "$VENV_PATH/Scripts/activate" ]; then
    source "$VENV_PATH/Scripts/activate"
else
    echo "Virtual environment not found at $VENV_PATH"
    exit 1
fi

# --- Run tests ---
pytest testing_dashboard.py --no-header --no-summary -q
TEST_EXIT_CODE=$?

# --- Deactivate virtual environment ---
deactivate

# --- Return proper exit code ---
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "All tests passed ✅"
    exit 0
else
    echo "Some tests failed ❌"
    exit 1
fi