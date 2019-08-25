# conferences
american_teams = ["Cincinnati", "East Carolina", "South Florida", "Temple",
    "UCF", "Connecticut", "Houston", "Memphis", "Navy", "Southern Methodist",
    "Tulane", "Tulsa"]

acc_teams = ["Georgia Tech", "Boston College", "Clemson", "Florida State",
            "Louisville", "North Carolina State", "Syracuse", "Wake Forest",
            "Duke", "North Carolina", "Pittsburgh", "Virgina", "Virginia Tech",
            "Miami (FL)"]

big12_teams =   ["Baylor", "Iowa State", "Kansas", "Kansas State", "Oklahoma",
                "Oklahoma State", "Texas Christian", "Texas", "Texas Tech",
                "West Virginia"]

big_ten_teams = ["Illinois", "Iowa", "Minnesota", "Northwestern", "Purdue",
                "Wisconsin", "Indiana", "Maryland", "Michigan Sate", "Michigan",
                "Ohio State", "Penn State", "Rutgers"]

conference_usa_teams = ["Charlotte", "Florida Atlantic", "Florida International",
                        "Marshall", "Middle Tennessee", "Old Dominion",
                        "Western Kenturcky", "Louisiana Tech", "North Texas",
                        "Rice", "Southern Miss", "UAB", "UTEP", "UTSA"]

fbs_independent_teams = ["Army", "Brigham Young", "Liberty", "New Mexico State",
                        "Massachusetts"]

mac_teams = ["Akron", "Bowling Green", "Buffalo", "Kent State", "Miami (OH)",
            "Ohio", "Ball State", "Central Michigan", "Eastern Michigan",
            "Northern Illinois", "Toledo", "Western Michigan"]

mountain_west_teams =   ["Air Force", "Boise State", "Colorado State",
                        "New Mexico", "Utah State", "Wyoming", "Fresno",
                        "Hawaii", "Nevada", "San Diego State", "San Jose State",
                        "UNLV"]

pac12_teams =   ["California", "Oregon", "Oregon State", "Stanford",
                "Washington", "Washington State", "Arizona State", "Arizona",
                "Colorado", "UCLA", "USC", "Utah"]

sec_teams = ["Florida", "Georgia", "Kentucky", "Missouri", "South Carolina",
            "Tennessee", "Vanderbilt", "Alabama", "Arkansas", "Auburn",
            "Louisiana State", "Mississippi State", "Ole Miss", "Texas A&M"]

sun_belt_teams =    ["Appalachian State", "Coastal Carolina", "Georgia Southern",
                    "Georgia State", "Troy", "Arkansas State",
                    "Louisiana-Lafayette", "South Alabama", "Texas State",
                    "Louisana-Monroe"]

conference_map = {
                    "American" : american_teams,
                    "ACC" : acc_teams,
                    "Big 12" : big12_teams,
                    "Big Ten" : big_ten_teams,
                    "Conference USA" : conference_usa_teams,
                    "Independents" : fbs_independent_teams,
                    "MAC" : mac_teams,
                    "Mountain West" : mountain_west_teams,
                    "Pac 12" : pac12_teams,
                    "SEC" : sec_teams,
                    "Sun Belt" : sun_belt_teams
                  }

conferences = conference_map.keys()
