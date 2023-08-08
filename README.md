# Brazillian ecommerce Batch ETL
This is a simple ETL pipeline project using brazillian_ecommerce dataset

## Technologies used
- Docker
- Dagster
- Jupyter
- MinIO, MySQL, Postgres
- Git
## Set up Environment
Clone this repo and run `make up` or `docker compose up`

Then run this code to set the .env file
```bash
$cat env.template > .env
```

## Prepare dataset
Copy dataset into MySQL dataset
```bash
$docker cp /brazillian_ecommerce de_mysql:/tmp/dataset
```
then copy sql script to execute loading data
```bash
$docker cp mysql_schemas.sql de_mysql:/tmp/dataset
$docker cp load_data.sql de_mysql:/tmp/dataset
```
Then run command to execute sql and create blank table in MySQL, then load data into table
```bash
$docker exec -it de_mysql mysql --local_infile -u"${MYSQL_USER}" -p"${MYSQL_PASSWORD}" ${MYSQL_DATABASE} -e"source /tmp/dataset/mysql_schema.sql" #create table

$make to_mysql_root #access to MySQL container

SET GLOBAL LOCAL_INFILE=TRUE; #Set local_infile variable to load data from local

exit;

$docker exec -it de_mysql mysql --local_infile -u"${MYSQL_USER}" -p"${MYSQL_PASSWORD}" ${MYSQL_DATABASE} -e"source /tmp/dataset/load_data.sql"
```
Finally, create schemas for PostgreSQL
```bash
$make to_psql
CREATE SCHEMA IF NOT EXISTS analysis;
exit;
```
## How to use
```bash
$make restart
```
then check:
- port 9000 for MinIO
- port 3001 for DagsterUI


