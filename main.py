from fastapi import FastAPI
import database
import models
from routers import access_groups, classifiers, customer_employees, customers, dashboards, extractors, fields,\
    incident_types, incidents, indicator_types, indicators, reports, runbooks, scripts, tenants, users, verdicts

db_instance = database.Database()
db_instance.create_engine()
db_engine = db_instance.db_engine

# TODO: Implement Alembic for database intialization.
models.Base.metadata.create_all(bind=db_engine)

app = FastAPI()

app.include_router(access_groups.router)
app.include_router(classifiers.router)
app.include_router(customer_employees.router)
app.include_router(customers.router)
app.include_router(dashboards.router)
app.include_router(extractors.router)
app.include_router(fields.router)
app.include_router(incident_types.router)
app.include_router(incidents.router)
app.include_router(indicator_types.router)
app.include_router(indicators.router)
app.include_router(reports.router)
app.include_router(runbooks.router)
app.include_router(scripts.router)
app.include_router(tenants.router)
app.include_router(users.router)
app.include_router(verdicts.router)



