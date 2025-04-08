# Load necessary libraries
library(ncdf4)

# Define a function to test a variable in a NetCDF file
test_variable <- function(file_path, variable_name) {
    # Open the NetCDF file
    nc <- nc_open(file_path)
    
    # Check if the variable exists
    if (!(variable_name %in% names(nc$var))) {
        stop(paste("Variable", variable_name, "not found in the NetCDF file."))
    }
    
    # Retrieve the variable data
    variable_data <- ncvar_get(nc, variable_name)
    
    # Perform a simple test (e.g., check if the variable contains NA values)
    if (any(is.na(variable_data))) {
        stop(paste("Variable", variable_name, "contains NA values."))
    }
    
    # Close the NetCDF file
    nc_close(nc)
    
    # Return success message
    return(paste("Variable", variable_name, "passed all tests."))
}

# Example usage
# Replace 'example.nc' and 'temperature' with your file and variable
file_path <- "precipitation.nc"
variable_name <- "precipitation"

tryCatch({
    result <- test_variable(file_path, variable_name)
    cat(result, "\n")
}, error = function(e) {
    cat("Error:", e$message, "\n")
})