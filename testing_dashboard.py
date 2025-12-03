import pytest
from dash.testing.application_runners import import_app

# Use the dash testing fixture
@pytest.fixture
def dash_app_runner(dash_duo):
    # Import your app
    app = import_app("dash_app_creation")  # replace with your app filename without .py
    dash_duo.start_server(app)
    return dash_duo

# Test 1: Header is present
def test_header_present(dash_app_runner):
    dash_duo = dash_app_runner
    header = dash_duo.find_element("#header")
    assert header is not None
    assert "Pink Morsel Sales Visualizer" in header.text

# Test 2: Graph is present
def test_graph_present(dash_app_runner):
    dash_duo = dash_app_runner
    graph = dash_duo.find_element("#sales_chart")
    assert graph is not None

# Test 3: Region picker is present
def test_region_picker_present(dash_app_runner):
    dash_duo = dash_app_runner
    radio = dash_duo.find_element("#region_selector")
    assert radio is not None