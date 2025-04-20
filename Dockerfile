FROM apache/airflow:2.6.3-python3.11-slim

USER root
RUN apt-get update && apt-get install -y libhdf5-dev libnetcdf-dev && \
    pip install netCDF4

USER airflow