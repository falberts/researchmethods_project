import re


def tweets_locations(file):
    """splits all lines in the input file into place and tweet, and counts the amount of times the search terms occur for 2 given regions."""

    searchterms = re.compile(r"corona|covid|vaccin|moderna|pfizer|astrazenica|janssen|maatregelen|persconferentie|persco")

    region1_keywords = re.compile(r"groningen|hoogezand|veendam|stadskanaal|winschoten|haren|delfzijl|hoogkerk|appingedam|leek|drenthe|assen|emmen|hoogeveen|meppel|roden|coevorden|klazienaveen|beilen|eelde-paterswolde|zuidlaren")
    region2_keywords = re.compile(r"brabant|eindhoven|tilburg|breda|'s-hertogenbosch|den bosch|helmond|roosendaal|oss|bergen op zoom|oosterhout|veldhoven")

    region1_total = 0
    region2_total = 0
    region1_found = 0
    region2_found = 0

    for line in file:
        line = line.rstrip().split()
        place = ' '.join(line[:3])
        tweet = ' '.join(line[3:])

        if region1_keywords.search(place.lower()) is not None:
            region1_total += 1
            if searchterms.search(tweet.lower()) is not None:
                region1_found += 1
                # print(tweet)
        elif region2_keywords.search(place.lower()) is not None:
            region2_total += 1
            if searchterms.search(tweet.lower()) is not None:
                region2_found += 1
                # print(tweet)

    return [region1_total, region1_found, region2_total, region2_found]


def main():
    with open('place_tweets_2021.txt', 'r', encoding='utf-8') as inp:
        file = inp.readlines()
    results = tweets_locations(file)

    print("________________________________________________________")
    print("{:^54}".format("REGION 1 (GRONINGEN/DRENTHE):"))
    print("Total: {0}".format(results[0]))
    print("Tweets containing search terms: {0}".format(results[1]))
    print("Tweets not containing search terms: {0}".format(results[0]-results[1]))
    print()
    print("Percentage: {0}%".format(round(((results[1]/results[0])*100), 2)))
    print("________________________________________________________")
    print("{:^54}".format("REGION 2 (BRABANT):"))
    print("Total: {0}".format(results[2]))
    print("Tweets containing search terms: {0}".format(results[3]))
    print("Tweets not containing search terms: {0}".format(results[2]-results[3]))
    print()
    print("Percentage: {0}%".format(round(((results[3]/results[2])*100), 2)))
    print("________________________________________________________")


if __name__=="__main__":
    main()
