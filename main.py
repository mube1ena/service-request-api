
from fastapi import FastAPI, Depends
from fastapi import status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from fastapi import HTTPException


from database import engine, Base, get_db
import models

app = FastAPI(title="Service Request API")

Base.metadata.create_all(bind=engine)


# Request data validation
class TicketCreate(BaseModel):
    title: str
    priority: str
    status: str
# Create a ticket
class TicketUpdate(BaseModel):
    status: str

@app.post("/tickets", status_code=status.HTTP_201_CREATED)
def create_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db)
):
    new_ticket = models.Ticket(
        title=ticket.title,
        priority=ticket.priority,
        status=ticket.status
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket


@app.get("/")
def home():
    return {"message": "Service Request API is running"}

from typing import Optional

@app.get("/tickets")
def get_tickets(
    status: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Ticket)

    if status:
        query = query.filter(models.Ticket.status == status)

    return query.all()


@app.patch("/tickets/{ticket_id}")
def update_ticket(
    ticket_id: int,
    ticket: TicketUpdate,
    db: Session = Depends(get_db)
):
    existing_ticket = db.query(models.Ticket).filter(
        models.Ticket.id == ticket_id
    ).first()

    if existing_ticket is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    existing_ticket.status = ticket.status

    db.commit()
    db.refresh(existing_ticket)

    return existing_ticket
