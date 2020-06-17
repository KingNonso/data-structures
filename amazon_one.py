from collections import Counter
import re

def popularNFeatures(numFeatures, topFeatures, possibleFeatures,
                     numFeatureRequests, featureRequests):
    cnt = Counter()
    for word in possibleFeatures:
        cnt[word] += 1
    work = re.findall(r'\w+', featureRequests)
    Counter(work).most_common(topFeatures)

    # WRITE YOUR CODE HERE
    pass