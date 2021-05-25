import random
import numpy as np

P_forgive = .25
P_forgive_in_exploit_phase = .25
START_FANCY = 20

pointsArray = np.array([[1,5],[0,3]])

def strategy(history, memory):
    """
    Statistician, but it keeps retaliating after the initial phase
    """
    if history.shape[1] == 0:
        return 1, None
    elif history.shape[1] < START_FANCY:
        return history[1, -1] or (1 if random.random() <= P_forgive else 0), None
    else:
        # This is where the fancy stuff kicks in
        ourHistory = history[0, 0:-1]
        theirResponses = history[1, 1:]
        betraySample = theirResponses[ourHistory == 0]
        allySample = theirResponses[ourHistory == 1]

        P0 = np.average(betraySample) if len(betraySample) else 0
        P1 = np.average(allySample) if len(allySample) else 1

        statistician_result = np.dot(pointsArray[1], (1 - P1, P1)) >= np.dot(pointsArray[0], (1 - P0, P0))

        tft_result = history[1, -1] or (1 if random.random() <= P_forgive_in_exploit_phase else 0)
        
        return tft_result and statistician_result, None
