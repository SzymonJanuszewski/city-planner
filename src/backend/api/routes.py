from flask import Blueprint, request, jsonify
from services.planner import CityTripPlanner

# Create Blueprint
api_bp = Blueprint('api', __name__)
planner = CityTripPlanner()

@api_bp.route('/plan', methods=['POST'])
def plan_trip():
    try:
        data = request.json
        
        # Extract parameters from request
        city = data.get('city', '').strip()
        days = int(data.get('days', 3))
        activity_level = data.get('activity_level', 'medium')
        max_walking_time = int(data.get('max_walking_time', 30))
        early_start = bool(data.get('early_start', False))
        
        # Input validation
        if not city:
            return jsonify({"error": "City name is required"}), 400
        
        if days < 1 or days > 7:
            return jsonify({"error": "Number of days must be between 1 and 7"}), 400
            
        # Generate itinerary
        itinerary = planner.generate_itinerary(
            city=city, 
            days=days, 
            activity_level=activity_level,
            max_walking_time=max_walking_time,
            early_start=early_start
        )
        
        if not itinerary:
            return jsonify({"error": f"Could not generate itinerary for {city}"}), 404
            
        # Create response
        response = planner.create_trip_response(itinerary, city)
        return jsonify(response)
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@api_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "available_cities": list(planner.cities.keys())})