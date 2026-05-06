# Prueba Técnica Backend 

## Descripción

API REST desarrollada con Django REST Framework para gestión de productos, órdenes y entregas.
Incluye auditoría de eventos en MongoDB y soporte multitenant mediante `tenant_id`.

---

Tecnologías

* Django
* Django REST Framework
* SQLite
* MongoDB
* Docker
* GitHub Actions

---

##  Instalación

```bash
git clone https://github.com/Jaisonstevencruz99/prueba-backend.git
cd prueba-backend
python -m venv venv
venv\Scripts\activate
pip install django djangorestframework pymongo
```

---

## Ejecución

```bash
python manage.py migrate
python manage.py runserver
```

---

## Docker

```bash
docker-compose up --build
```

---

## Endpoints

* GET /api/products
* POST /api/products
* GET /api/orders
* POST /api/orders
* GET /api/deliveries
* POST /api/deliveries

---

## Multitenancy

Cada entidad incluye `tenant_id` para separar datos por cliente.

---

## Auditoría

Eventos de órdenes almacenados en MongoDB (`audit_db.events`).

---

## CI/CD

Pipeline en GitHub Actions con:

* Instalación de dependencias
* Linting
* Validación Django
* Build Docker

---

## Autor

Ing. Jeison Cruz
