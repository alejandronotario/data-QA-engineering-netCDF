import pytest
from netCDF4 import Dataset
import numpy as np

def check_variable_in_range(dataset, variable_name, min_value, max_value):
    """
    Check if all values of a variable in the dataset are within a specified range.

    :param dataset: netCDF4.Dataset object
    :param variable_name: Name of the variable to check
    :param min_value: Minimum acceptable value
    :param max_value: Maximum acceptable value
    :return: True if all values are within range, False otherwise
    """
    if variable_name not in dataset.variables:
        return False

    variable_data = dataset.variables[variable_name][:]
    return ((variable_data >= min_value) & (variable_data <= max_value)).all()

@pytest.fixture
def mock_dataset(tmp_path):
    """Fixture to create a mock netCDF dataset for testing."""
    file_path = tmp_path / "mock_data.nc"
    with Dataset(file_path, "w", format="NETCDF4") as ds:
        # Create dimensions
        ds.createDimension("time", None)
        ds.createDimension("lat", 10)
        ds.createDimension("lon", 10)

        # Create variables
        precipitation = ds.createVariable("precipitation", "f4", ("time", "lat", "lon"))
        latitude = ds.createVariable("latitude", "f4", ("lat",))
        longitude = ds.createVariable("longitude", "f4", ("lon",))

        # Assign data
        precipitation[:] = np.random.uniform(0, 500, (1, 10, 10))
        latitude[:] = np.linspace(-90, 90, 10)
        longitude[:] = np.linspace(-180, 180, 10)

    return Dataset(file_path, "r")

def test_precipitation_in_range(mock_dataset):
    assert check_variable_in_range(mock_dataset, "precipitation", 0, 500)

def test_latitude_in_range(mock_dataset):
    assert check_variable_in_range(mock_dataset, "latitude", -90, 90)

def test_longitude_in_range(mock_dataset):
    assert check_variable_in_range(mock_dataset, "longitude", -180, 180)

def test_variable_not_found(mock_dataset):
    assert not check_variable_in_range(mock_dataset, "nonexistent_variable", 0, 100)

