import psycopg2

def data_query(query):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="choir",
        user="choir",
        password="spam889books"
    )

    cur = conn.cursor()
    
    try:
        cur.execute(query)
        result = cur.fetchall()
        return result
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()

def find_city_location(city_name):
    query = f"SELECT latitude, longitude FROM cities WHERE city_name = '{city_name}'"
    result = data_query(query)

    if result:
        latitude, longitude = result[0]
        print(f"{city_name} is located at Latitude: {latitude}, Longitude: {longitude}")
    else:
        print(f"{city_name} not in database.")

def city_largest_population():
    query = "SELECT city_name FROM cities ORDER BY population DESC LIMIT 1"
    result = data_query(query)

    if result:
        print(f"city with the largest population is: {result[0][0]}")

def city_smallest_population_minnesota():
    query = "SELECT city_name FROM cities WHERE state_name = 'Minnesota' ORDER BY population ASC LIMIT 1"
    result = data_query(query)

    if result:
        print(f"city in Minnesota with the smallest population is: {result[0][0]}")

def extreme_cities():
    queries = [
        "SELECT city_name FROM cities ORDER BY latitude DESC LIMIT 1",
        "SELECT city_name FROM cities ORDER BY longitude DESC LIMIT 1",
        "SELECT city_name FROM cities ORDER BY latitude ASC LIMIT 1",
        "SELECT city_name FROM cities ORDER BY longitude ASC LIMIT 1"
    ]

    directions = ["North", "East", "South", "West"]

    for i in range(len(queries)):
        result = data_query(queries[i])
        if result:
            print(f"The city furthest {directions[i]} is: {result[0][0]}")

def total_population_by_state(state_input):

    query_total_population = f"SELECT SUM(population) FROM cities WHERE state_name = '{state_input}'"
    result_total_population = data_query(query_total_population)

    if result_total_population[0][0]:
        print(f"The total population of cities in {state_input} is: {result_total_population[0][0]}")
    else:
        print(f"No cities found for the specified state.")

def main():
    find_city_location("Northfield")

    city_largest_population()

    city_smallest_population_minnesota()

    extreme_cities()

    user_input_state = input("Enter a State in full name: ")
    total_population_by_state(user_input_state)

main()
