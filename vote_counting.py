votes = {}
while True:
    candidate = input("Enter candidate's name or -1 to quit: ")
    if candidate == '-1':
        break
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1
print(f"{'Candidate':<15}{'Vote'}")
for candidate, vote in votes.items():
    print(f"{candidate:<15}{vote}")
winner = ''
for candidate, vote in votes.items():
    if vote == max(votes.values()):
        winner = candidate

print(f"The winner of the presidential election is {winner} with the vote of ", max(votes.values()))
#
# over_all_best_student = {}
# while True:
#     subject = input("Enter the subject or -1 to quit: ")
#     best_student = input(f"Enter the name of the best student in {subject}: ")
#     if subject == '-1' and best_student == '-1':
#         break
#     if best_student in over_all_best_student:
#         over_all_best_student[best_student] += 1
#     else:
#         over_all_best_student[best_student] = 1
#
# print(f"{'best_student_name':<20}{'Subject':<13}")
# for best_student, subject in over_all_best_student.items():
#     print(f"{best_student:<15}{subject}")
# print(f"The overall best student is "
#       f"{max(over_all_best_student.keys())} with {max(over_all_best_student.values())} occurrences")


