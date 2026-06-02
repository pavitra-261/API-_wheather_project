import requests

while True:
    city = input("\nEnter city name (or 'exit' to quit): ")

    if city.lower() == "exit":
        break

    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)
        data = response.json()

        current = data["current_condition"][0]

        temp = int(current["temp_C"])
        humidity = current["humidity"]
        weather = current["weatherDesc"][0]["value"]

        print("\n------ Weather Report ------")
        print("City:", city)
        print("Temperature:", temp, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", weather)

        # Filter
        if temp > 30:
            print("Filter Result: Hot Weather")
        elif temp > 20:
            print("Filter Result: Moderate Weather")
        else:
            print("Filter Result: Cold Weather")

    except Exception:
        print("Invalid city or network error")