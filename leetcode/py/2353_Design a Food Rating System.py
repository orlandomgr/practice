from typing import List
import heapq
import itertools

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodToCuisines = {}
        self.cuisinesMap = {}
        self.foodFinder = {}
        self.counter = itertools.count()
        for i in range(len(foods)):
            food = foods[i]
            cuisine = cuisines[i]
            if food not in self.foodToCuisines:
                self.foodToCuisines[foods[i]] = cuisines[i]
            if cuisine not in self.cuisinesMap:
                self.cuisinesMap[cuisines[i]] = []
            entry = [-ratings[i], foods[i], next(self.counter)]
            self.foodFinder[food] = entry
            heapq.heappush(self.cuisinesMap[cuisines[i]], entry)

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foodToCuisines[food]
        if cuisine is None:
            raise Exception("Food or cuisine not found")

        entry = self.foodFinder.pop(food)
        entry[-1] = "removed"
        entry[-2] = "removed"
        # entry[-3] = 1000
        entry = None
        newEntry = [-newRating, food, next(self.counter)]
        self.foodFinder[food] = newEntry
        heapq.heappush(self.cuisinesMap[cuisine], newEntry)

    def highestRated(self, cuisine: str) -> str:
        if cuisine not in self.cuisinesMap:
            raise Exception("Food or cuisine not found")

        idx = 0
        name = self.cuisinesMap[cuisine][idx][1]
        while name == "removed":
            heapq.heappop(self.cuisinesMap[cuisine])
            name = self.cuisinesMap[cuisine][idx][1]
        print(self.cuisinesMap[cuisine])
        print(self.cuisinesMap[cuisine][idx][1])
        return self.cuisinesMap[cuisine][idx][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)


# foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
# cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
# ratings = [9, 12, 8, 15, 14, 7]
# # , ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]


# obj = FoodRatings(foods, cuisines, ratings)
# obj.highestRated("korean")  # kimchi
# obj.highestRated("japanese")  # ramen
# obj.changeRating("sushi", 16)
# obj.highestRated("japanese") # sushi
# obj.changeRating("ramen", 16)
# obj.highestRated("japanese") # ramen



# ["FoodRatings","changeRating","highestRated","changeRating","changeRating","changeRating","highestRated","highestRated"]
foods = ["emgqdbo","jmvfxjohq","qnvseohnoe","yhptazyko","ocqmvmwjq"]
cuisines = ["snaxol","snaxol","snaxol","fajbervsj","fajbervsj"]
ratings = [2,6,18,6,5]

obj = FoodRatings(foods, cuisines, ratings)
obj.changeRating("qnvseohnoe", 11)
obj.highestRated("fajbervsj")  # yhptazyko
obj.changeRating("emgqdbo", 3)
obj.changeRating("jmvfxjohq", 9)
obj.changeRating("emgqdbo", 14)
obj.highestRated("fajbervsj")  # yhptazyko
obj.highestRated("snaxol")  # emgqdbo

