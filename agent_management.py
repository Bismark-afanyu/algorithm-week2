import math
import datetime
# The AgentManagement class is used for managing agents.
#agent_assignment
class AgentManagement:
    def get_closest_agent(request_location, agents):
        """
        The function `get_closest_agent` takes a request location and a list of agents, and returns the
        agent that is closest to the request location.
        A list of dictionaries, where each dictionary represents an agent and contains
        information about the agent, including their location. Each dictionary has a key 'location' which
        maps to a tuple representing the agent's location
        :return: the closest agent from the list of agents based on their distance from the request
        location.
        """
        closest_agent = None
        closest_distance = math.inf

        for agent in agents:
            agent_location = agent['location']
            distance = AgentManagement.calculate_distance(request_location, agent_location)

            if distance < closest_distance:
                closest_agent = agent
                closest_distance = distance

        return closest_agent

    def calculate_distance(location1, location2):
        """
        The function calculates the distance between two locations using the Pythagorean theorem.
        
        :param location1: A dictionary representing the coordinates of the first location. It should have
        keys 'x' and 'y' representing the x and y coordinates respectively
        """
        x_distance = location1['x'] - location2['x']
        y_distance = location1['y'] - location2['y']
        distance = math.sqrt(x_distance**2 + y_distance**2)

        return distance

    def assign_agent(request, agents):
        """
        The function assigns an agent to a request based on the request volume, either by automatically
        assigning the closest available agent or by sending a list of available agents and their
        distances to the requester.
         The function  returns either the closest available agent if the request
        volume is less than 160, or a list of available agents and their distances if the request volume
        is 160 or greater.
        """
        request_volume = request['volume']

        if request_volume < 160:
            # Automatically assign the closest available agent
            closest_agent = AgentManagement.get_closest_agent(request['location'], agents)
            return closest_agent

        else:
            # Send a list of available agents and their distances to the requester
            available_agents = []

            for agent in agents:
                if agent['available']:
                    agent_distance = AgentManagement.calculate_distance(request['location'], agent['location'])
                    available_agents.append({
                        'agent': agent,
                        'distance': agent_distance
                    })

            # Sort the list of available agents by distance
            available_agents.sort(key=lambda agent: agent['distance'])

            return available_agents

   #Agent Performance
    
    
    def calculate_punctuality_score(expected_arrival_time, actual_arrival_time):
        """
        The function calculates the punctuality score based on the expected and actual arrival times.
        
    the function returns the punctuality score, which is a float value representing the overall punctuality of
        the actual arrival times compared to the expected arrival times.
        """
        punctuality_weight = 0.2
        score = 0.0

        for expected, actual in zip(expected_arrival_time, actual_arrival_time):
            expected_datetime = datetime.datetime.combine(datetime.date.today(), expected)
            actual_datetime = datetime.datetime.combine(datetime.date.today(), actual)
            time_difference = actual_datetime - expected_datetime

            if time_difference <= datetime.timedelta(minutes=5):
                score += 1.0
            elif time_difference <= datetime.timedelta(minutes=30):
                score += 0.5

        punctuality_score = score / len(expected_arrival_time) * punctuality_weight
        return punctuality_score




    def calculate_agent_performance(agent_data):
        """
        The function calculates the performance score of an agent based on various factors such as
        ratings, hours worked, requests completed, shifts done, and punctuality.
        The function `calculate_agent_performance` returns a dictionary containing the
        following keys and values:
        """
        rating_weight = 0.3
        hours_weight = 0.2
        requests_weight = 0.2
        shifts_weight = 0.1
        punctuality_weight = 0.2

        # Calculate the average rating
        average_rating = sum(agent_data['ratings_received']) / len(agent_data['ratings_received'])
        rating_score = average_rating * rating_weight

        hours_score = agent_data['hours_worked'] * hours_weight
        requests_score = agent_data['requests_completed'] * requests_weight
        shifts_score = agent_data['shifts_done'] * shifts_weight

        punctuality_score = AgentManagement.calculate_punctuality_score(
            agent_data['expected_arrival_time'],
            agent_data['actual_arrival_time']
        ) * punctuality_weight

        total_score = rating_score + hours_score + requests_score + shifts_score + punctuality_score

        return {
            'rating_score': rating_score,
            'hours_score': hours_score,
            'requests_score': requests_score,
            'shifts_score': shifts_score,
            'punctuality_score': punctuality_score,
            'total_score': total_score
        }

        
        #Closest Landfill
        
    def haversine_distance(lat1, lon1, lat2, lon2):
            """
            The function calculates the haversine distance between two sets of latitude and longitude
            coordinates.
            :return: the haversine distance between two sets of latitude and longitude coordinates.
            """
            radius = 6371  # Earth's radius in kilometers

            # Convert coordinates to radians
            lat1_radians = math.radians(lat1)
            lon1_radians = math.radians(lon1)
            lat2_radians = math.radians(lat2)
            lon2_radians = math.radians(lon2)

            # Calculate the change in latitude and longitude
            delta_lat = lat2_radians - lat1_radians
            delta_lon = lon2_radians - lon1_radians

            a = math.sin(delta_lat/2) ** 2 + math.cos(lat1_radians) * math.sin(delta_lat/2) ** 2 * math.cos(lon1_radians) * math.cos(lon2_radians)
            c = 2 * math.asin(math.sqrt(a))

            return radius * c


    def find_closest_landfill(request_location, landfills):
            """
            The function `find_closest_landfill` takes a request location and a list of landfills, and
            returns the closest landfill to the request location.
            Each landfill dictionary have a 'location' key, which contains the
            latitude and longitude coordinates of the landfill
            :return: the closest landfill to the given request location.
            """
            closest_landfill = None
            closest_distance = math.inf

            for landfill in landfills:
                landfill_location = landfill['location']
                distance = AgentManagement.haversine_distance(
                    request_location['latitude'],
                    request_location['longitude'],
                    landfill_location['latitude'],
                    landfill_location['longitude']
                )

                if distance < closest_distance:
                    closest_landfill = landfill
                    closest_distance = distance

            return closest_landfill



# Example usage
# Agent_assignment
print("\n\n")

request = {
        'location': {
            'x': 10,
            'y': 20
        },
        'volume': 100
    }
agents = [
        {
            'id': 1,
            'location': {
                'x': 5,
                'y': 10
            },
            'available': True
        },
        {
            'id': 2,
            'location': {
                'x': 15,
                'y': 25
            },
            'available': True
        },
        {
            'id': 3,
            'location': {
                'x': 20,
                'y': 30
            },
            'available': False
        }
    ]
   
assigned_agent = AgentManagement.assign_agent(request, agents)

if assigned_agent is not None:
        print(f"Assigned agent: {assigned_agent}")
else:
        print("No available agents")

print("\n\n")

#Agent Performance

agent_data = {
        'ratings_received': [4.5, 5.0, 4.0],
        'hours_worked': 20.0,
        'requests_completed': 10,
        'shifts_done': 5,
        'expected_arrival_time': [
            datetime.time(10, 00, 00),
            datetime.time(14, 00, 00),
            datetime.time(16, 00, 00)
        ],
        'actual_arrival_time': [
            datetime.time(10, 0o5, 00),
            datetime.time(14, 10, 00),
            datetime.time(16, 0o3, 00)
        ]
    }

agent_performance = AgentManagement.calculate_agent_performance(agent_data)

print("Agent Performance:")
print(f"Rating Score: {agent_performance['rating_score']:.3f}")
print("Hours Score:", agent_performance['hours_score'])
print("Requests Score:", agent_performance['requests_score'])
print("Shifts Score:", agent_performance['shifts_score'])
print(f"Punctuality Score:, {agent_performance['punctuality_score']:.3f}")
print(f"Total Score:, {agent_performance['total_score']:.3f}")
print("\n\n")

    
#closest Landfill
request_location = {
        'latitude': 37.7833,  # Latitude of request location
        'longitude': -122.4167  # Longitude of request location
    }

landfills = [
        {
            'id': 1,
            'location': {
                'latitude': 37.7749,  # Latitude of landfill 1
                'longitude': -122.4194  # Longitude of landfill 1
            }
        },
        {
            'id': 2,
            'location': {
                'latitude': 37.7945,  # Latitude of landfill 2
                'longitude': -122.4000  # Longitude of landfill 2
            }
        }
    ]

closest_landfill = AgentManagement.find_closest_landfill(request_location, landfills)

print("Closest landfill:", closest_landfill)