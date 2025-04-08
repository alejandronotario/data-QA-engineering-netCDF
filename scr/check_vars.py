import netCDF4 as nc
import os

# Get the absolute path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the file
fn = os.path.join(script_dir, '../data/precipitation.nc')
ds = nc.Dataset(fn)

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
        print(f"Variable '{variable_name}' not found in the dataset.")
        return False

    variable_data = dataset.variables[variable_name][:]
    if not ((variable_data >= min_value) & (variable_data <= max_value)).all():
        print(f"Variable '{variable_name}' has values outside the range {min_value} to {max_value}.")
        return False

    print(f"Variable '{variable_name}' passed the range check ({min_value} to {max_value}).")
    return True

# Example QA checks for precipitation.nc
check_variable_in_range(ds, 'precipitation', 0, 500)  # Replace with actual variable name and range
check_variable_in_range(ds, 'latitude', -90, 90)  # Replace with actual variable name and range
check_variable_in_range(ds, 'longitude', -180, 180)  # Replace with actual variable name and range