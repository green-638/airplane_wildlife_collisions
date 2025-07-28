# Airplane Wildlife Collisions

This project analyzes data from the FAA's Wildlife Strike Database. The goal of this project is to determine what conditions make collisions more likely, when collisions occur, and how collisions can be reduced. The projects' conclusions are in project.ipynb.

## Scope
The following columns from the dataset are used: INCIDENT_YEAR, INCIDENT_MONTH, AIRPORT, SPECIES, SKY, TIME_OF_DAY, and PHASE_OF_FLIGHT.
The dataset was cleaned by assigning dtype values for columns with mixed types and by removing rows with the value 'UNKNOWN.' This is perfomed by the load_data.py module.

## Running the project
The jupyter notebook, project.ipynb, has already been run and is ready to view. To run it again, the annual_collisions.py, avg_monthly_collisions.py, and load_data.py modules and the dataset are required. The dataset must include years 1990-2015, which is included by default. Instructions for accessing the dataset are below.

## Dataset access
To access the dataset, go to the address at the end of the citation and click the 'Download Excel' button under the 'Download the FAA Wildlife Strike Database' section.

## References
Federal Aviation Administration (2025). FAA Wildlife Strike Database [DATASET]. https://wildlife.faa.gov/search
