speedrun_scores = [32.5, 46.1, 28.2, 50.9, 33.4]
totalscore = 0
counter = 0

def calculate_average(total, amount):
    average = (total/amount)
    return average


for score in speedrun_scores:
    totalscore += score
    counter += 1

average_score = calculate_average(totalscore, counter)

print (average_score)