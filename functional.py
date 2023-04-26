# lambda calculus
(lambda x, y: x and y)(True, False)



(lambda x, y: x * y)(3, 4)



metersToFeet = lambda x: x * 3.28084
metersToFeet(5)



expr = lambda a, b: (lambda x: x + b)((lambda x: x ** 2)(a))
expr(2, 3)



# passing and returning functions
square = lambda x: x ** 2
twice = lambda f: lambda x: f(f(x))
quad = twice(square)
quad(3)



# closure
def multiplier_of(n):
    def multiplier(number):
        return number * n    
    return multiplier
multiplywith5 = multiplier_of(5)
multiplywith5(9)




import random
def generate(n):
    random_list = [random.randint(1, n) for i in range(n)]
    def choose():
        return random.choice(random_list)
    return choose
rng = generate(10)
print(rng())



# map
def encrpyt(char):
    if char.isalpha():
        return chr(ord(char) + 3)
    return char
string = "Hello World!"
encrypted_string = "".join(list(map(encrpyt, string)))
print(encrypted_string)



# reduce
from functools import reduce
from math import sqrt
def standard_deviation(scores):
    mean = sum(scores) / len(scores)
    variance = reduce(lambda x, y: x + (y - mean) ** 2, scores, 0)
    return sqrt(variance / len(scores))
scores1 = [45, 38, 76, 23, 69]
scores2 = [55, 42, 81, 35, 58]
sd1 = standard_deviation(scores1)
sd2 = standard_deviation(scores2)
if sd1 < sd2:
    print("Player 1 is more consistent")
elif sd1 > sd2:
    print("Player 2 is more consistent")
else:
    print("Both players are equally consistent")




# filter
marks = [
    [60, 70, 80, 90, 75],
    [45, 50, 55, 60, 40],
    [80, 85, 90, 95, 85],
    [35, 45, 55, 65, 40],
    [50, 60, 70, 26, 55]
]
def did_fail(subjects):
    for subject in subjects:
        if subject < 40:
            return True
    return False
failed_students = list(filter(did_fail, marks))
print(failed_students)



# map, reduce, filter
from functools import reduce
tweets = [
    "Bun.js is a lightweight and fast JavaScript library for building user interfaces. It's perfect for modern web apps that need to be performant #bunjs #javascript",  
    "Zod is a TypeScript-first schema validation tool. It provides a simple and intuitive way to validate and sanitize data #zod #typescript",  
    "TypeScript is the future of web development. Its strong typing system and advanced features make it a great choice for building complex applications #typescript #webdev",  
    "Lighthouse is an amazing tool for auditing and improving the performance, accessibility, and best practices of your web app. Highly recommend using it! #lighthouse #webperf",  
    "Netlify is a game-changer for web development. Its continuous deployment and integration features make deploying and managing web apps a breeze #netlify #webdev",  
    "ESLint is a powerful tool for enforcing code style and catching errors in your JavaScript code. It helps ensure consistency and maintainability in your codebase #eslint #javascript",  
    "Webpack is the go-to tool for bundling and optimizing JavaScript code. Its modular architecture and plugin system make it incredibly flexible and customizable #webpack #javascript",  
    "Gatsby is a great tool for building fast, SEO-friendly, and dynamic web apps. Its plugin system and rich ecosystem make it easy to add new features and integrations #gatsby #webdev",  
    "Figma is a fantastic tool for designing and prototyping web interfaces. Its collaborative features and intuitive interface make it a great choice for teams #figma #webdesign",  
    "Tailwind CSS is an incredibly useful utility-first CSS framework. It allows you to quickly build beautiful and responsive web interfaces without writing custom CSS #tailwindcss #webdesign"
]
trending_topics = ["web", "tool"]
def contains_topic(tweet, topic):
    return topic in tweet.lower()
def count_tweets_with_topic(total, tweet):
    if tweet:
        return total + 1
    else:
        return total
filtered_tweets = list(filter(lambda tweet: contains_topic(tweet, trending_topics[0]) or contains_topic(tweet, trending_topics[1]), tweets))
counts = []
for topic in trending_topics:
    topic_tweets = list(map(lambda tweet: contains_topic(tweet, topic), filtered_tweets))
    topic_count = reduce(count_tweets_with_topic, topic_tweets, 0)
    counts.append(topic_count)
print(f"Number of tweets containing '{trending_topics[0]}': {counts[0]}")
print(f"Number of tweets containing '{trending_topics[1]}': {counts[1]}")



from functools import reduce
def get_top_scorers(scores):
    subject_scores = list(map(list, zip(*scores)))
    top_scorers = reduce(lambda acc, x: acc + [x.index(max(x))], subject_scores, [])
    
    return top_scorers
scores = [
    [90, 85, 95, 80],
    [80, 95, 70, 90],
    [100, 80, 90, 85],
]
top_scorers = get_top_scorers(scores)
print(top_scorers)




# compute average and highest score
scores = [[99, 102, 23], [34, 56, 78], [98, 78, 56], [45, 67, 89], [67, 89, 90]]
avg_highest_scores = list(map(lambda score: (round(sum(score) / len(score), 2), max(score)), scores))
for avg, highest in avg_highest_scores:
    print(f"Average: {avg}, Highest: {highest}")
    
    
    
from functools import reduce
grains = list(map(lambda x: 2 ** x, range(64)))
total_grains = reduce(lambda x, y: x + y, grains)
print(total_grains)