import numpy as np

life_score = np.array([
    [6, 6, 5, 7, 4],  # Mood score for 5 days
    [6, 6, 5, 8, 7],  # Sleep score for 5 days
    [5, 4, 3, 5, 5], #Number of glass of water for 5 days
    [2, 4, 5, 5, 5,], #Number of yawns
    [2, 1, 1, 1, 1] ]  #Number of times I went outside            
)


mood_ave = np.average(life_score[0])
print(mood_ave)

sleep_ave = np.average(life_score[1])
print(sleep_ave)