import csv
import random
from time import sleep
from concurrent.futures import ProcessPoolExecutor, as_completed

# set the number of Voters and the range of Voters IDs
NM = 10
VIR = range(1000, 2000)


# function to enroll Voters
def enroll_V(name):
    V_ID = random.choice(VIR)
    return {"id": V_ID, "name": name}


# here is a function to simulate the voting booth
def VB(booth_name, V):
    V_ID = V["id"]
    V_name = V["name"]
    print(f"\n\nWelcome to the {booth_name} voting booth, {V_name}")
    sleep(2)
    print(f"{V_name} has  walked into the {booth_name} voting booth")
    sleep(3)
    print(f"{V_name} is currently voting........")
    sleep(1)
    print(f"{V_name} has voted \n")
    sleep(2)
    return [V_name, booth_name]


# here is a function to simulate the voting process
def simulate_voting(Vs):
    results = []
    with ProcessPoolExecutor() as executor:
        futures = []
        for V in Vs:
            booth_name = random.choice(["Booth A", "Booth B", "Booth C"])
            futures.append(executor.submit(VB, booth_name, V))
        for future in as_completed(futures):
            results.append(future.result())
    return results


if __name__ == "__main__":
    # enrolling the Voters
    Vs = []
    for i in range(NM):
        name = input(f"V #{i+1}, please enter your full name: ")
        Vs.append(enroll_V(name))

    # simulation of the voting process
    results = simulate_voting(Vs)

    # write voting data to a CSV file
    with open("votes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(results)

    # printing results
    print("\nVoting Complete!\nThank you for voting.")
