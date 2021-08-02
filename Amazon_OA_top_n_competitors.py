def topNumCompetitors(numCompetitors, topNCompetitors, competitors, numReviews, reviews):
    counter = {comp:0 for comp in competitors}
    for review in reviews:
        words = [word.lower() for word in review.split()]
        for word in words:
            if word in counter:
                counter[word] += 1
    return sorted(counter, key=lambda x:(-counter[x], x))[:topNCompetitors]

numCompetitors=6
topNCompetitors = 2
competitors = ['newshop', 'shopnow', 'afashion', 'fashionbeats', 'mymarket', 'tcellular']
numReviews = 6
reviews = [
"newshop is providing good services in the city; everyone should use newshop",
"best services by newshop",
"fashionbeats has great services in the city",
"I am proud to have fashionbeats",
"mymarket has awesome services",
"Thanks Newshop for the quick delivery"]

print(topNumCompetitors(numCompetitors, topNCompetitors, competitors, numReviews, reviews))