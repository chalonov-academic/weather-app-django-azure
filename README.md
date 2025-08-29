# Guía de Desarrollo - Django en AWS (EC2)

![Django CI](https://github.com/chalonov/weather-app-django-ec2/workflows/Django%20CI/badge.svg)

## ☀️ Climante - Weather App Django

Esta aplicación web de clima tiene dos funcionalidades principales:

### 🌍 Temperatura en Cualquier Lugar
Selecciona una ciudad aleatoria del mundo desde una base de datos de ciudades globales
Muestra la temperatura actual de esa ubicación usando la API de Open-Meteo

### 📍 Temperatura Aquí
Detecta tu ubicación actual basada en la IP, muestra la temperatura de donde te encuentras en tiempo real

## 🔧 Cómo Funciona:

Usa geocodificación para obtener coordenadas (latitud/longitud)
Consulta la API gratuita de Open-Meteo para datos meteorológicos actuales
Presenta los resultados en una interfaz web limpia con ciudad, país y temperatura

**Ideal para:** Curiosear sobre el clima mundial o verificar rápidamente la temperatura local sin apps adicionales.

## 🤖 Automatización con GitHub Actions

### ✅ ¿Qué se automatiza?
- **Tests automáticos:** Se ejecutan cada vez que haces push
- **Validación de código:** Verifica sintaxis Python
- **Checks de Django:** Valida configuración del proyecto
- **Verificación de migraciones:** Asegura que no falten migraciones

### 🔄 ¿Cuándo se ejecuta?
- Cada push a la rama `main`
- Cada Pull Request
- Manualmente desde GitHub

### 📊 Estado actual:
El badge de arriba te muestra si los tests están pasando ✅ o fallando ❌

### 🧪 Ejecutar tests localmente:
```bash
# Activar entorno virtual
source .venv/bin/activate

# Ejecutar todos los tests
python manage.py test

# Ejecutar tests específicos
python manage.py test tests.test_basic
```

## 📋 Requisitos Previos

- Instancia EC2 creada y corriendo
- Security Group configurado con puertos 22 (SSH) y 8000 (desarrollo)
- Acceso SSH a la instancia

## 🚀 Paso 1: Conectarse a la Instancia EC2

### Opción A: EC2 Instance Connect (Recomendado)
1. Ve a **AWS Console** → **EC2** → **Instances**
2. Selecciona tu instancia
3. Clic en **"Connect"**
4. Selecciona **"EC2 Instance Connect"**
5. Clic en **"Connect"**

## 🔧 Paso 2: Preparar el Entorno

### Actualizar sistema e instalar dependencias:
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install python3-pip python3-venv
```

## 📥 Paso 3: Clonar el Repositorio

```bash
git clone https://github.com/chalonov/weather-app-django-ec2.git
cd weather-app-django-ec2
```

## 🐍 Paso 4: Configurar Entorno Virtual

```bash
# Crear entorno virtual
python3 -m venv .venv

# Activar entorno virtual
source .venv/bin/activate
```

## 📦 Paso 5: Instalar Dependencias

```bash
pip install -r requirements.txt
```

## 🗄️ Paso 6: Configurar Base de Datos

```bash
# Crear archivos de migración
python manage.py makemigrations
# Aplicar migraciones
python manage.py migrate
```

## 🧪 Paso 7: Ejecutar Tests (Opcional)

```bash
python manage.py test
```

## 🚀 Paso 8: Ejecutar el Servidor de Desarrollo

```bash
python manage.py runserver 0.0.0.0:8000
```

## 🌐 Paso 9: Acceder a la Aplicación

Ir al navegador: `http://tu-ip-publica-ec2:8000`

## 🛑 Paso 10: Detener el Servidor

Presiona **Ctrl + C** en la terminal

## 🛡️ Configuración del Security Group

Asegúrate de que tu Security Group tenga estas reglas:

| Tipo | Puerto | Origen | Descripción |
|------|--------|--------|-------------|
| SSH | 22 | Tu IP o 0.0.0.0/0 | Acceso SSH |
| TCP Personalizado | 8000 | 0.0.0.0/0 | Servidor desarrollo |

## 🔧 Para Desarrolladores

### 🧪 Agregar nuevos tests:
1. Crea archivos en la carpeta `tests/`
2. Los tests se ejecutarán automáticamente en GitHub Actions
3. Mantén el badge verde ✅

### 📝 Estructura de tests:
```
tests/
├── __init__.py
├── test_basic.py      # Tests básicos
├── test_models.py     # Tests de modelos (opcional)
└── test_views.py      # Tests de vistas (opcional)
```

### 🚨 Si los tests fallan:
1. Revisa el badge en GitHub
2. Ve a "Actions" en tu repositorio
3. Revisa los logs de error
4. Corrige el problema y haz push

## ⚠️ Notas Importantes

- **Solo para desarrollo**: No usar en producción
- **Sin persistencia**: Si cierras la terminal, la app se detiene
- **IP dinámica**: Si detienes/inicias la instancia, cambia la IP
- **Sin SSL**: Solo HTTP, no HTTPS
- **Tests automáticos**: GitHub Actions valida tu código automáticamente