run_prod:
	docker-compose up

run_dev:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

db_backup:
	docker-compose exec postgres sh -c "pg_dump -U restraunt_menu restraunt_menu > /backup/backup.sql"

db_restore:
	docker-compose exec postgres sh -c "psql -U restraunt_menu restraunt_menu < /backup/backup.sql"

django_migrate:
	docker-compose exec django python3 manage.py migrate

django_collectstatic:
	docker-compose exec django python3 manage.py collectstatic

django_check_migrations:
	docker-compose exec django python3 manage.py makemigrations --dry-run

django_make_migrations:
	docker-compose exec django python3 manage.py makemigrations

django_shell:
	docker-compose exec django python3 manage.py shell_plus

tests:
	docker-compose exec django pytest

django_prepare: django_migrate django_collectstatic