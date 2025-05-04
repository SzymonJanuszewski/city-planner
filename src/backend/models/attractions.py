from dataclasses import dataclass
from typing import List, Dict, Optional, Any
from enum import Enum

class ActivityLevel(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    DEMANDING = "demanding"

@dataclass
class TicketInfo:
    price: float
    currency: str
    needs_reservation: bool
    booking_url: Optional[str] = None
    notes: Optional[str] = None

@dataclass
class Attraction:
    name: str
    description: str
    visit_time: int  # in minutes
    location: tuple  # (latitude, longitude)
    category: str
    place_id: str = ""  # Added place_id for frontend
    ticket_info: Optional[TicketInfo] = None
    best_time: Optional[str] = None
    opening_hours: Optional[str] = None

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "visit_time": self.visit_time,
            "location": self.location,
            "category": self.category,
            "place_id": self.place_id or self.name.lower().replace(' ', '_'),
            "ticket_info": {
                "price": self.ticket_info.price,
                "currency": self.ticket_info.currency,
                "needs_reservation": self.ticket_info.needs_reservation,
                "booking_url": self.ticket_info.booking_url,
                "notes": self.ticket_info.notes
            } if self.ticket_info else None,
            "best_time": self.best_time,
            "opening_hours": self.opening_hours
        }

@dataclass
class RouteSegment:
    start_point: str
    end_point: str
    walking_time: int  # in minutes
    distance: float   # in kilometers

    def to_dict(self):
        return {
            "start_point": self.start_point,
            "end_point": self.end_point,
            "walking_time": self.walking_time,
            "distance": self.distance
        }

@dataclass
class DayRoute:
    day_number: int
    attractions: List[Attraction]
    route_segments: List[RouteSegment]
    total_time: int
    total_distance: float
    total_cost: float
    google_maps_link: str

    def to_dict(self):
        return {
            "day_number": self.day_number,
            "attractions": [attr.to_dict() for attr in self.attractions],
            "walking_times": [segment.walking_time for segment in self.route_segments],
            "total_time": self.total_time,
            "total_distance": self.total_distance,
            "total_cost": self.total_cost,
            "google_maps_link": self.google_maps_link
        }