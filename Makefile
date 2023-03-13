include env.template

build:
	docker compose build

up:
	docker compose --env-file env up -d

down:
	docker compose --env-file env down

restart:
	make down && make up

to_psql:
	docker exec -ti postgres psql postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}

to_mysql:
	docker exec -it mysql mysql --local-infile=1 -u "${MYSQL_USER}" -p "${MYSQL_PASSWORD}" ${MYSQL_DATABASE}

to_mysql_root:
	docker exec -it mysql mysql -u"root" -p"${MYSQL_ROOT_PASSWORD}" ${MYSQL_DATABASE}