candidates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Candidates : ", candidates)

#-------------------Normal Hiring---------------------------
interviewed_candidates = []
hired_candidates = []
max = -1
for candidate in candidates:
    interviewed_candidates.append(candidate)
    if candidate > max:
        hired_candidates.append(candidate)
        max = candidate

firing_cost = len(hired_candidates) - 1

print("\nNormal Way : ")
print("Interviewed candidates : ", interviewed_candidates)
print("Hired candidates : ", hired_candidates)
print("No of candidates hired", len(hired_candidates))
print("Firing Cost : ", firing_cost)

#----------------------Random Hiring--------------------------
import random
interviewed_candidates = []
hired_candidates = []
max = -1
for i in range(len(candidates)):
    selected_candidate = random.choice(candidates)
    interviewed_candidates.append(selected_candidate)
    if selected_candidate > max:
        max = selected_candidate
        hired_candidates.append(selected_candidate)
    candidates.remove(selected_candidate)
firing_cost = len(hired_candidates) - 1

print("\nCandidates hired in random order : ")
print("Interviewed candidates : ", interviewed_candidates)
print("Hired candidates : ", hired_candidates)
print("No of candidates hired", len(hired_candidates))
print("Firing Cost : ", firing_cost)
