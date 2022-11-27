from sqlalchemy.orm import Session

import models


def get_incident(db: Session, incident_id: int):
    return db.query(models.Incidents).filter(models.Incidents.incident_id == incident_id).first()


def get_incidents(db: Session, limit, **kwargs):
    unfiltered_kwargs = locals()
    kwargs = {}
    for each in unfiltered_kwargs['kwargs']:
        if unfiltered_kwargs['kwargs'][each] is not None:
            kwargs[each] = unfiltered_kwargs['kwargs'][each]
    return db.query(models.Incidents).filter_by(**kwargs).limit(limit).all()


def create_incident(db: Session, **kwargs):
    unfiltered_kwargs = locals()
    kwargs = {}
    for each in unfiltered_kwargs['kwargs']:
        if unfiltered_kwargs['kwargs'][each] is not None:
            kwargs[each] = unfiltered_kwargs['kwargs'][each]
    incident = models.Incidents(incident_id='12341234', **kwargs)
    db.add(incident)
    db.commit()
    db.refresh(incident)
    return incident


def update_incident(db: Session, incident_id, **kwargs):
    unfiltered_kwargs = locals()
    kwargs = {}
    for each in unfiltered_kwargs['kwargs']:
        if unfiltered_kwargs['kwargs'][each] is not None:
            kwargs[each] = unfiltered_kwargs['kwargs'][each]
    incident_data = get_incident(db, incident_id)
    print(kwargs)
    for key, value in kwargs.items():
        setattr(incident_data, key, value)
    db.add(incident_data)
    db.commit()
    db.refresh(incident_data)
    return incident_data


def delete_incident(db: Session, incident_id):
    incident_data = get_incident(db, incident_id)
    db.delete(incident_data)
    db.commit()
    return {"ok": True}
