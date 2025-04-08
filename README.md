# Data QA Engineering with netCDF

This project focuses on quality assurance and data processing using netCDF files.

Resource: https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/

## Project Structure

```
data-QA-engineering-netCDF/
├── data/               # Directory for input and output data files
├── src/                # Python scripts for processing netCDF files
├── airflow/            # Airflow DAGs and configuration files
├── tests/              # Unit tests for the project
├── requirements.txt    # Python dependencies
├── docker-compose.yml  # Docker Compose configuration for Airflow
└── README.md           # Project overview and instructions
```

## Getting Started

### Prerequisites

- Python 3.11 or higher
- `pip` package manager
- Docker and Docker Compose installed

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/data-QA-engineering-netCDF.git
    cd data-QA-engineering-netCDF
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Place your netCDF files in the `data/` directory.
2. Run the main script:
    ```bash
    python src/main.py
    ```
3. Processed files and logs will be saved in the `data/` directory.

### Running Tests

Run the unit tests using `pytest` to ensure everything is working correctly:
```bash
pytest tests
```

### Running Airflow with Docker Compose

1. Start the Airflow services using Docker Compose:
    ```bash
    docker-compose up -d
    ```

2. Access the Airflow web interface at `http://localhost:8080`.

3. Add your DAGs to the `airflow/dags/` directory.

4. Monitor and manage your workflows through the Airflow UI.

5. To stop the services, run:
    ```bash
    docker-compose down
    ```

## Contributing

Feel free to submit issues or pull requests to improve the project.

## License

This project is licensed under the MIT License.