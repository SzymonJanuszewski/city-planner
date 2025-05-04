# from dataclasses import dataclass
# from typing import List, Dict, Optional, Any
# from enum import Enum
# import json
# from datetime import datetime, timedelta
# from flask import Flask, request, jsonify
# from flask_cors import CORS

# class ActivityLevel(Enum):
#     EASY = "easy"
#     MEDIUM = "medium"
#     DEMANDING = "demanding"

# @dataclass
# class TicketInfo:
#     price: float
#     currency: str
#     needs_reservation: bool
#     booking_url: Optional[str] = None
#     notes: Optional[str] = None

# @dataclass
# class Attraction:
#     name: str
#     description: str
#     visit_time: int  # in minutes
#     location: tuple  # (latitude, longitude)
#     category: str
#     place_id: str = ""  # Added place_id for frontend
#     ticket_info: Optional[TicketInfo] = None
#     best_time: Optional[str] = None
#     opening_hours: Optional[str] = None

#     def to_dict(self):
#         return {
#             "name": self.name,
#             "description": self.description,
#             "visit_time": self.visit_time,
#             "location": self.location,
#             "category": self.category,
#             "place_id": self.place_id or self.name.lower().replace(' ', '_'),
#             "ticket_info": {
#                 "price": self.ticket_info.price,
#                 "currency": self.ticket_info.currency,
#                 "needs_reservation": self.ticket_info.needs_reservation,
#                 "booking_url": self.ticket_info.booking_url,
#                 "notes": self.ticket_info.notes
#             } if self.ticket_info else None,
#             "best_time": self.best_time,
#             "opening_hours": self.opening_hours
#         }

# @dataclass
# class RouteSegment:
#     start_point: str
#     end_point: str
#     walking_time: int  # in minutes
#     distance: float   # in kilometers

#     def to_dict(self):
#         return {
#             "start_point": self.start_point,
#             "end_point": self.end_point,
#             "walking_time": self.walking_time,
#             "distance": self.distance
#         }

# @dataclass
# class DayRoute:
#     day_number: int
#     attractions: List[Attraction]
#     route_segments: List[RouteSegment]
#     total_time: int
#     total_distance: float
#     total_cost: float
#     google_maps_link: str

#     def to_dict(self):
#         return {
#             "day_number": self.day_number,
#             "attractions": [attr.to_dict() for attr in self.attractions],
#             "walking_times": [segment.walking_time for segment in self.route_segments],
#             "total_time": self.total_time,
#             "total_distance": self.total_distance,
#             "total_cost": self.total_cost,
#             "google_maps_link": self.google_maps_link
#         }

# class CityTripPlanner:
#     def __init__(self):
#         # Example database for Rome - in real application, this would be loaded from external database
#         self.cities = {
#             "rome": {
#                 "vatican": {
#                     "Vatican Museums": Attraction(
#                         name="Vatican Museums",
#                         description="World's largest museum complex including the Sistine Chapel",
#                         visit_time=180,
#                         location=(41.906159, 12.453462),
#                         category="vatican",
#                         place_id="vatican_museums",
#                         ticket_info=TicketInfo(
#                             price=17.00,
#                             currency="EUR",
#                             needs_reservation=True,
#                             booking_url="https://tickets.vatican.va",
#                             notes="Book in advance to avoid long queues"
#                         ),
#                         opening_hours="Mon-Sat: 9:00-18:00 (last entry 16:00)"
#                     ),
#                     "St. Peter's Basilica": Attraction(
#                         name="St. Peter's Basilica",
#                         description="The center of the Catholic Church",
#                         visit_time=120,
#                         location=(41.902216, 12.453235),
#                         category="vatican",
#                         place_id="st_peters_basilica",
#                         ticket_info=TicketInfo(
#                             price=0.00,
#                             currency="EUR",
#                             needs_reservation=False,
#                             notes="Free entry but expect queues"
#                         ),
#                         best_time="Early morning"
#                     ),
#                     "Castel Sant'Angelo": Attraction(
#                         name="Castel Sant'Angelo",
#                         description="Fortress and museum with great city views",
#                         visit_time=90,
#                         location=(41.903067, 12.466359),
#                         category="vatican",
#                         place_id="castel_sant_angelo",
#                         ticket_info=TicketInfo(
#                             price=15.00,
#                             currency="EUR",
#                             needs_reservation=False
#                         )
#                     ),
#                     "Vatican Gardens": Attraction(
#                         name="Vatican Gardens",
#                         description="Beautiful gardens with stunning architecture",
#                         visit_time=120,
#                         location=(41.903898, 12.452136),
#                         category="vatican",
#                         place_id="vatican_gardens",
#                         ticket_info=TicketInfo(
#                             price=33.00,
#                             currency="EUR",
#                             needs_reservation=True,
#                             booking_url="https://tickets.vatican.va"
#                         )
#                     )
#                 },
#                 "ancient": {
#                     "Colosseum": Attraction(
#                         name="Colosseum",
#                         description="Ancient amphitheater and Rome's most famous landmark",
#                         visit_time=120,
#                         location=(41.890210, 12.492231),
#                         category="ancient",
#                         place_id="colosseum",
#                         ticket_info=TicketInfo(
#                             price=16.00,
#                             currency="EUR",
#                             needs_reservation=True,
#                             booking_url="https://colosseum.it",
#                             notes="Combined ticket with Roman Forum and Palatine Hill"
#                         )
#                     ),
#                     "Roman Forum": Attraction(
#                         name="Roman Forum",
#                         description="Ancient city center ruins",
#                         visit_time=150,
#                         location=(41.892916, 12.485315),
#                         category="ancient",
#                         place_id="roman_forum",
#                         ticket_info=TicketInfo(
#                             price=0.00,  # Included with Colosseum ticket
#                             currency="EUR",
#                             needs_reservation=False
#                         )
#                     ),
#                     "Palatine Hill": Attraction(
#                         name="Palatine Hill",
#                         description="Birthplace of ancient Rome",
#                         visit_time=90,
#                         location=(41.889283, 12.487148),
#                         category="ancient",
#                         place_id="palatine_hill",
#                         ticket_info=TicketInfo(
#                             price=0.00,  # Included with Colosseum ticket
#                             currency="EUR",
#                             needs_reservation=False
#                         )
#                     ),
#                     "Circus Maximus": Attraction(
#                         name="Circus Maximus",
#                         description="Ancient Roman chariot racing stadium",
#                         visit_time=45,
#                         location=(41.886389, 12.485278),
#                         category="ancient",
#                         place_id="circus_maximus",
#                         ticket_info=TicketInfo(
#                             price=0.00,
#                             currency="EUR",
#                             needs_reservation=False
#                         )
#                     ),
#                     "Baths of Caracalla": Attraction(
#                         name="Baths of Caracalla",
#                         description="Massive ancient Roman public baths",
#                         visit_time=90,
#                         location=(41.879167, 12.493889),
#                         category="ancient",
#                         place_id="baths_of_caracalla",
#                         ticket_info=TicketInfo(
#                             price=8.00,
#                             currency="EUR",
#                             needs_reservation=False
#                         )
#                     )
#                 },
#                 "city_center": {
#                     "Trevi Fountain": Attraction(
#                         name="Trevi Fountain",
#                         description="Iconic Baroque fountain",
#                         visit_time=30,
#                         location=(41.900932, 12.483313),
#                         category="city_center",
#                         place_id="trevi_fountain",
#                         ticket_info=TicketInfo(
#                             price=0.00,
#                             currency="EUR",
#                             needs_reservation=False
#                         ),
#                         best_time="Early morning or late evening"
#                     ),
#                     "Pantheon": Attraction(
#                         name="Pantheon",
#                         description="Ancient temple with remarkable architecture",
#                         visit_time=60,
#                         location=(41.898614, 12.476886),
#                         category="city_center",
#                         place_id="pantheon",
#                         ticket_info=TicketInfo(
#                             price=5.00,
#                             currency="EUR",
#                             needs_reservation=False
#                         )
#                     ),
#                     "Piazza Navona": Attraction(
#                         name="Piazza Navona",
#                         description="Beautiful square with fountains and cafes",
#                         visit_time=45,
#                         location=(41.899233, 12.473087),
#                         category="city_center",
#                         place_id="piazza_navona",
#                         ticket_info=TicketInfo(
#                             price=0.00,
#                             currency="EUR",
#                             needs_reservation=False
#                         )
#                     ),
#                     "Spanish Steps": Attraction(
#                         name="Spanish Steps",
#                         description="Famous monumental staircase",
#                         visit_time=30,
#                         location=(41.905990, 12.482767),
#                         category="city_center",
#                         place_id="spanish_steps",
#                         ticket_info=TicketInfo(
#                             price=0.00,
#                             currency="EUR",
#                             needs_reservation=False
#                         )
#                     ),
#                     "Galleria Borghese": Attraction(
#                         name="Galleria Borghese",
#                         description="Art museum in beautiful villa",
#                         visit_time=120,
#                         location=(41.914158, 12.492370),
#                         category="city_center",
#                         place_id="galleria_borghese",
#                         ticket_info=TicketInfo(
#                             price=13.00,
#                             currency="EUR",
#                             needs_reservation=True,
#                             booking_url="https://galleriaborghese.it",
#                             notes="Strict 2-hour visiting slots"
#                         )
#                     ),
#                     "Campo de' Fiori": Attraction(
#                         name="Campo de' Fiori",
#                         description="Historic market square",
#                         visit_time=45,
#                         location=(41.895599, 12.472121),
#                         category="city_center",
#                         place_id="campo_de_fiori",
#                         ticket_info=TicketInfo(
#                             price=0.00,
#                             currency="EUR",
#                             needs_reservation=False
#                         ),
#                         best_time="Morning for market"
#                     )
#                 }
#             }
#             # Add more cities here
#         }

#     def get_attractions_per_day(self, activity_level: ActivityLevel) -> int:
#         """Determine number of attractions based on activity level"""
#         return {
#             ActivityLevel.EASY: 4,
#             ActivityLevel.MEDIUM: 5,
#             ActivityLevel.DEMANDING: 7
#         }[activity_level]

#     def generate_google_maps_link(self, attractions: List[Attraction]) -> str:
#         """Generate Google Maps link for the route"""
#         base_url = "https://www.google.com/maps/dir/"
#         waypoints = "/".join([f"{attr.location[0]},{attr.location[1]}" for attr in attractions])
#         return base_url + waypoints

#     def create_day_route(self, city: str, category: str, max_attractions: int, day_number: int, max_walking_time: int = 30) -> DayRoute:
#         """Create a route for a specific category of attractions"""
#         attractions = list(self.cities[city][category].values())[:max_attractions]
#         route_segments = []
#         total_cost = sum(attr.ticket_info.price for attr in attractions if attr.ticket_info)
        
#         for i in range(len(attractions) - 1):
#             start = attractions[i].location
#             end = attractions[i + 1].location
#             distance = ((start[0] - end[0])**2 + (start[1] - end[1])**2)**0.5 * 111
#             walking_time = int(distance * 20)  # assuming 20 minutes per km
            
#             # Adjust routing based on max_walking_time
#             if walking_time > max_walking_time:
#                 # In a real app, you might suggest alternative transportation
#                 walking_time = max_walking_time
            
#             route_segments.append(RouteSegment(
#                 start_point=attractions[i].name,
#                 end_point=attractions[i + 1].name,
#                 walking_time=walking_time,
#                 distance=distance
#             ))

#         total_time = sum(attr.visit_time for attr in attractions) + \
#                     sum(segment.walking_time for segment in route_segments)
#         total_distance = sum(segment.distance for segment in route_segments)

#         return DayRoute(
#             day_number=day_number,
#             attractions=attractions,
#             route_segments=route_segments,
#             total_time=total_time,
#             total_distance=total_distance,
#             total_cost=total_cost,
#             google_maps_link=self.generate_google_maps_link(attractions)
#         )

#     def generate_itinerary(self, city: str, days: int, activity_level: str, max_walking_time: int = 30, early_start: bool = False) -> List[DayRoute]:
#         """Generate multi-day itinerary based on parameters"""
#         city = city.lower()
#         if city not in self.cities:
#             raise ValueError(f"City {city} not found in database")
        
#         # Convert string activity level to enum
#         activity_level_enum = ActivityLevel(activity_level)
#         max_attractions = self.get_attractions_per_day(activity_level_enum)
        
#         # For Rome specific planning
#         if city == "rome":
#             itinerary = []
#             categories = ["vatican", "ancient", "city_center"]
            
#             # Adjust order based on early_start preference
#             if early_start:
#                 # Vatican first (opens early)
#                 pass
#             else:
#                 # Maybe different order
#                 pass
                
#             for i in range(min(days, len(categories))):
#                 itinerary.append(
#                     self.create_day_route(city, categories[i], max_attractions, i+1, max_walking_time)
#                 )
            
#             return itinerary
#         return []
        
#     def create_trip_response(self, itinerary: List[DayRoute], city: str) -> Dict:
#         """Format the itinerary as a JSON-friendly response"""
#         return {
#             "city": city.capitalize(),
#             "days": [day.to_dict() for day in itinerary]
#         }


# # Create Flask app
# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes
# planner = CityTripPlanner()

# @app.route('/plan', methods=['POST'])
# def plan_trip():
#     try:
#         data = request.json
        
#         # Extract parameters from request
#         city = data.get('city', '').strip()
#         days = int(data.get('days', 3))
#         activity_level = data.get('activity_level', 'medium')
#         max_walking_time = int(data.get('max_walking_time', 30))
#         early_start = bool(data.get('early_start', False))
        
#         # Input validation
#         if not city:
#             return jsonify({"error": "City name is required"}), 400
        
#         if days < 1 or days > 7:
#             return jsonify({"error": "Number of days must be between 1 and 7"}), 400
            
#         # Generate itinerary
#         itinerary = planner.generate_itinerary(
#             city=city, 
#             days=days, 
#             activity_level=activity_level,
#             max_walking_time=max_walking_time,
#             early_start=early_start
#         )
        
#         if not itinerary:
#             return jsonify({"error": f"Could not generate itinerary for {city}"}), 404
            
#         # Create response
#         response = planner.create_trip_response(itinerary, city)
#         return jsonify(response)
        
#     except ValueError as e:
#         return jsonify({"error": str(e)}), 400
#     except Exception as e:
#         return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500
# # 
# # Add a health check endpoint
# @app.route('/health', methods=['GET'])
# def health_check():
#     return jsonify({"status": "ok", "available_cities": list(planner.cities.keys())})

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=8000)