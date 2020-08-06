print('Elections! Elections! Elections')

counties = ['Arapahoe','Denver','Jefferson']
print(counties)

counties_tuple = ("Arapahoe","Denver","Jefferson")

counties_dict = {}

counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

print(counties_dict)

print(len(counties_dict))

print(counties_dict.items())
print(counties_dict.values())

print(counties_dict['Arapahoe'])


voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

print(voting_data)



# How many votes did you get?
my_votes = int("200")

#  Total votes in the election
total_votes = int("997")

# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100

print("I received " + str(percentage_votes)+"% of the total votes.")


counties = ["Arapahoe","Denver","Jefferson"] 
if "Arapahoe" in counties: print("True")
else: print("False")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")




if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

for county in counties:
    print(county)


    numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)


for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])


for county in counties_dict:
    print(county)

for voters in counties_dict.values():
    print(voters)



for county in counties_dict:
    print(counties_dict.get(county))



for county, voters in counties_dict.items():
    print(county, voters)


for county, voters in counties_dict.items():
    print(county + " county has " +  str(voters) + " registered voters")



voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


for county_dict in voting_data:
    print(county_dict['county'])



my_votes = int("200")
total_votes = int("997")
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")



candidate_votes = int("3345")
total_votes = int("23123")
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)


# DEPENDENCIES - dates stamp
import datetime
now = datetime.datetime.now()
print("The time right now is ",now)


# or this way
import datetime as dt
now = dt.datetime.now()
print("The time right now is ",now)

