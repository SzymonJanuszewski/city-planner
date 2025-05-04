from models.attractions import Attraction, TicketInfo

# City database with attractions
def get_cities_data():
    return {
        "rome": {
            "vatican": {
                "Vatican Museums": Attraction(
                    name="Vatican Museums",
                    description="World's largest museum complex including the Sistine Chapel",
                    visit_time=180,
                    location=(41.906159, 12.453462),
                    category="vatican",
                    place_id="vatican_museums",
                    ticket_info=TicketInfo(
                        price=17.00,
                        currency="EUR",
                        needs_reservation=True,
                        booking_url="https://tickets.vatican.va",
                        notes="Book in advance to avoid long queues"
                    ),
                    opening_hours="Mon-Sat: 9:00-18:00 (last entry 16:00)"
                ),
                "St. Peter's Basilica": Attraction(
                    name="St. Peter's Basilica",
                    description="The center of the Catholic Church",
                    visit_time=120,
                    location=(41.902216, 12.453235),
                    category="vatican",
                    place_id="st_peters_basilica",
                    ticket_info=TicketInfo(
                        price=0.00,
                        currency="EUR",
                        needs_reservation=False,
                        notes="Free entry but expect queues"
                    ),
                    best_time="Early morning"
                ),
                "Castel Sant'Angelo": Attraction(
                    name="Castel Sant'Angelo",
                    description="Fortress and museum with great city views",
                    visit_time=90,
                    location=(41.903067, 12.466359),
                    category="vatican",
                    place_id="castel_sant_angelo",
                    ticket_info=TicketInfo(
                        price=15.00,
                        currency="EUR",
                        needs_reservation=False
                    )
                ),
                "Vatican Gardens": Attraction(
                    name="Vatican Gardens",
                    description="Beautiful gardens with stunning architecture",
                    visit_time=120,
                    location=(41.903898, 12.452136),
                    category="vatican",
                    place_id="vatican_gardens",
                    ticket_info=TicketInfo(
                        price=33.00,
                        currency="EUR",
                        needs_reservation=True,
                        booking_url="https://tickets.vatican.va"
                    )
                )
            },
            "ancient": {
                "Colosseum": Attraction(
                    name="Colosseum",
                    description="Ancient amphitheater and Rome's most famous landmark",
                    visit_time=120,
                    location=(41.890210, 12.492231),
                    category="ancient",
                    place_id="colosseum",
                    ticket_info=TicketInfo(
                        price=16.00,
                        currency="EUR",
                        needs_reservation=True,
                        booking_url="https://colosseum.it",
                        notes="Combined ticket with Roman Forum and Palatine Hill"
                    )
                ),
                "Roman Forum": Attraction(
                    name="Roman Forum",
                    description="Ancient city center ruins",
                    visit_time=150,
                    location=(41.892916, 12.485315),
                    category="ancient",
                    place_id="roman_forum",
                    ticket_info=TicketInfo(
                        price=0.00,  # Included with Colosseum ticket
                        currency="EUR",
                        needs_reservation=False
                    )
                ),
                "Palatine Hill": Attraction(
                    name="Palatine Hill",
                    description="Birthplace of ancient Rome",
                    visit_time=90,
                    location=(41.889283, 12.487148),
                    category="ancient",
                    place_id="palatine_hill",
                    ticket_info=TicketInfo(
                        price=0.00,  # Included with Colosseum ticket
                        currency="EUR",
                        needs_reservation=False
                    )
                ),
                "Circus Maximus": Attraction(
                    name="Circus Maximus",
                    description="Ancient Roman chariot racing stadium",
                    visit_time=45,
                    location=(41.886389, 12.485278),
                    category="ancient",
                    place_id="circus_maximus",
                    ticket_info=TicketInfo(
                        price=0.00,
                        currency="EUR",
                        needs_reservation=False
                    )
                ),
                "Baths of Caracalla": Attraction(
                    name="Baths of Caracalla",
                    description="Massive ancient Roman public baths",
                    visit_time=90,
                    location=(41.879167, 12.493889),
                    category="ancient",
                    place_id="baths_of_caracalla",
                    ticket_info=TicketInfo(
                        price=8.00,
                        currency="EUR",
                        needs_reservation=False
                    )
                )
            },
            "city_center": {
                "Trevi Fountain": Attraction(
                    name="Trevi Fountain",
                    description="Iconic Baroque fountain",
                    visit_time=30,
                    location=(41.900932, 12.483313),
                    category="city_center",
                    place_id="trevi_fountain",
                    ticket_info=TicketInfo(
                        price=0.00,
                        currency="EUR",
                        needs_reservation=False
                    ),
                    best_time="Early morning or late evening"
                ),
                "Pantheon": Attraction(
                    name="Pantheon",
                    description="Ancient temple with remarkable architecture",
                    visit_time=60,
                    location=(41.898614, 12.476886),
                    category="city_center",
                    place_id="pantheon",
                    ticket_info=TicketInfo(
                        price=5.00,
                        currency="EUR",
                        needs_reservation=False
                    )
                ),
                "Piazza Navona": Attraction(
                    name="Piazza Navona",
                    description="Beautiful square with fountains and cafes",
                    visit_time=45,
                    location=(41.899233, 12.473087),
                    category="city_center",
                    place_id="piazza_navona",
                    ticket_info=TicketInfo(
                        price=0.00,
                        currency="EUR",
                        needs_reservation=False
                    )
                ),
                "Spanish Steps": Attraction(
                    name="Spanish Steps",
                    description="Famous monumental staircase",
                    visit_time=30,
                    location=(41.905990, 12.482767),
                    category="city_center",
                    place_id="spanish_steps",
                    ticket_info=TicketInfo(
                        price=0.00,
                        currency="EUR",
                        needs_reservation=False
                    )
                ),
                "Galleria Borghese": Attraction(
                    name="Galleria Borghese",
                    description="Art museum in beautiful villa",
                    visit_time=120,
                    location=(41.914158, 12.492370),
                    category="city_center",
                    place_id="galleria_borghese",
                    ticket_info=TicketInfo(
                        price=13.00,
                        currency="EUR",
                        needs_reservation=True,
                        booking_url="https://galleriaborghese.it",
                        notes="Strict 2-hour visiting slots"
                    )
                ),
                "Campo de' Fiori": Attraction(
                    name="Campo de' Fiori",
                    description="Historic market square",
                    visit_time=45,
                    location=(41.895599, 12.472121),
                    category="city_center",
                    place_id="campo_de_fiori",
                    ticket_info=TicketInfo(
                        price=0.00,
                        currency="EUR",
                        needs_reservation=False
                    ),
                    best_time="Morning for market"
                )
            }
        }
        # Add more cities here
    }