# Dockerfile para Weather App Django
FROM python:3.11-slim

# Información del mantenedor
LABEL maintainer="chalonov.coder@gmail.com"
LABEL description="Climante Weather App - Django containerizado"

# Configurar directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivo de requisitos
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY . .

# Crear directorio para archivos estáticos
RUN mkdir -p staticfiles

# Aplicar migraciones y recopilar archivos estáticos
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput

# Crear usuario no-root para seguridad
RUN adduser --disabled-password --gecos '' appuser
RUN chown -R appuser:appuser /app
USER appuser

# Exponer puerto 8000
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/ || exit 1

# Comando por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]