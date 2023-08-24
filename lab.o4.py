class FlightTable:
    def __init__(self):
        self.data = [
            ("Mumbai", "India", "Sri Lanka", "DAY"),
            ("Delhi", "England", "Australia", "DAY-NIGHT"),
            ("Chennai", "India", "South Africa", "DAY"),
            ("Indore", "England", "Sri Lanka", "DAY-NIGHT"),
            ("Mohali", "Australia", "South Africa", "DAY-NIGHT"),
            ("Delhi", "India", "Australia", "DAY")
        ]

    def list_matches_of_team(self, team_name):
        matches = []
        for match in self.data:
            if team_name in (match[1], match[2]):
                matches.append(match)
        return matches

    def list_matches_on_location(self, location):
        matches = []
        for match in self.data:
            if match[0] == location:
                matches.append(match)
        return matches

    def list_matches_based_on_timing(self, timing):
        matches = []
        for match in self.data:
            if match[3] == timing:
                matches.append(match)
        return matches

def main():
    flight_table = FlightTable()

    while True:
        print("Choose search parameter:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            team_name = input("Enter the team name: ")
            matches = flight_table.list_matches_of_team(team_name)
            print("Matches of", team_name)
            for match in matches:
                print(match)

        elif choice == 2:
            location = input("Enter the location: ")
            matches = flight_table.list_matches_on_location(location)
            print("Matches in", location)
            for match in matches:
                print(match)

        elif choice == 3:
            timing = input("Enter the timing: ")
            matches = flight_table.list_matches_based_on_timing(timing)
            print("Matches with timing", timing)
            for match in matches:
                print(match)

        elif choice == 4:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()






