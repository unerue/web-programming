from fastapi import APIRouter, HTTPException, status
from src.models.events import Event


event_router = APIRouter(prefix="/events", tags=["Events"])
events: list[Event] = []


@event_router.get("/", response_model=list[Event])
async def retrieve_all_events() -> list[Event]:
    return events


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int) -> Event:
    if event := next((event for event in events if event.id == id), None):
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


@event_router.post("/", response_model=dict[str, str], status_code=status.HTTP_201_CREATED)
async def create_event(event: Event) -> dict[str, str]:
    events.append(event)
    return {
        "message": "Event created successfully"
    }


@event_router.delete("/{id}", response_model=dict[str, str])
async def delete_event(id: int) -> dict[str, str]:
    if event := next((event for event in events if event.id == id), None):
        events.remove(event)
        return {
            "message": "Event deleted successfully"
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


@event_router.delete("/", response_model=dict[str, str])
async def delete_all_events() -> dict[str, str]:
    events.clear()
    return {
        "message": "Events deleted successfully"
    }