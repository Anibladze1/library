#!/bin/bash
set -e

# Check PostgreSQL readiness
echo "Checking PostgreSQL readiness..."
python /app/scripts/check_service.py --service-name postgres --ip "${DATABASE_HOST-postgres}" --port "${DATABASE_PORT-5432}"

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Start Django development server
echo "Starting Django development server..."
python manage.py runserver 0.0.0.0:8000

exec "$@"
