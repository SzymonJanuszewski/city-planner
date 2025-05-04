from typing import List, Dict
from models.attractions import ActivityLevel, Attraction, RouteSegment, DayRoute
from data.cities import get_cities_data

class CityTripPlanner:
    def __init__(self):
        # Load city data from the module
        self.cities = get_cities_data()

    def get_attractions_per_day(self, activity_level: ActivityLevel) -> int:
        """Determine number of attractions based on activity level"""
        return {
            ActivityLevel.EASY: 4,
            ActivityLevel.MEDIUM: 5,
            ActivityLevel.DEMANDING: 7
        }[activity_level]

    def generate_google_maps_link(self, attractions: List[Attraction]) -> str:
        """Generate Google Maps link for the route"""
        base_url = "https://www.google.com/maps/dir/"
        waypoints = "/".join([f"{attr.location[0]},{attr.location[1]}" for attr in attractions])
        return base_url + waypoints

    def create_day_route(self, city: str, category: str, max_attractions: int, day_number: int, max_walking_time: int = 30) -> DayRoute:
        """Create a route for a specific category of attractions"""
        attractions = list(self.cities[city][category].values())[:max_attractions]
        route_segments = []
        total_cost = sum(attr.ticket_info.price for attr in attractions if attr.ticket_info)
        
        for i in range(len(attractions) - 1):
            start = attractions[i].location
            end = attractions[i + 1].location
            distance = ((start[0] - end[0])**2 + (start[1] - end[1])**2)**0.5 * 111
            walking_time = int(distance * 20)  # assuming 20 minutes per km
            
            # Adjust routing based on max_walking_time
            if walking_time > max_walking_time:
                # In a real app, you might suggest alternative transportation
                walking_time = max_walking_time
            
            route_segments.append(RouteSegment(
                start_point=attractions[i].name,
                end_point=attractions[i + 1].name,
                walking_time=walking_time,
                distance=distance
            ))

        total_time = sum(attr.visit_time for attr in attractions) + \
                    sum(segment.walking_time for segment in route_segments)
        total_distance = sum(segment.distance for segment in route_segments)

        return DayRoute(
            day_number=day_number,
            attractions=attractions,
            route_segments=route_segments,
            total_time=total_time,
            total_distance=total_distance,
            total_cost=total_cost,
            google_maps_link=self.generate_google_maps_link(attractions)
        )

    def generate_itinerary(self, city: str, days: int, activity_level: str, max_walking_time: int = 30, early_start: bool = False) -> List[DayRoute]:
        """Generate multi-day itinerary based on parameters"""
        city = city.lower()
        if city not in self.cities:
            raise ValueError(f"City {city} not found in database")
        
        # Convert string activity level to enum
        activity_level_enum = ActivityLevel(activity_level)
        max_attractions = self.get_attractions_per_day(activity_level_enum)
        
        # For Rome specific planning
        if city == "rome":
            itinerary = []
            categories = ["vatican", "ancient", "city_center"]
            
            # Adjust order based on early_start preference
            if early_start:
                # Vatican first (opens early)
                pass
            else:
                # Maybe different order
                pass
                
            for i in range(min(days, len(categories))):
                itinerary.append(
                    self.create_day_route(city, categories[i], max_attractions, i+1, max_walking_time)
                )
            
            return itinerary
        return []
        
    def create_trip_response(self, itinerary: List[DayRoute], city: str) -> Dict:
        """Format the itinerary as a JSON-friendly response"""
        return {
            "city": city.capitalize(),
            "days": [day.to_dict() for day in itinerary]
        }