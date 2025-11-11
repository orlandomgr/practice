from typing import List
import heapq
import time

class MovieRentingSystem:

    def getMovieEntry(self, price: int, shop: int, movie: int):
        status = self.STATUS_AVAILABLE
        entry = [price, shop, movie, status]
        return entry

    def getMovieKey(self, price: int, shop: int, movie: int):
        key = str(price) + "_" + str(shop) + "_" + str(movie)
        return key

    def __init__(self, n: int, entries: List[List[int]]):
        self.rentalFinder = {}
        self.rents = []
        self.reportLimit = 5
        self.movieFinder = {}
        self.movies = {}

        self.FIELD_PRICE:int = 0
        self.FIELD_SHOP:int = 1
        self.FIELD_MOVIE:int = 2
        self.FIELD_STATUS:int = 3

        self.STATUS_AVAILABLE = "AVAILABLE"
        self.STATUS_RENTED = "RENTED"
        self.STATUS_DROP = "DROP"
        
        for entry in entries:
            shop = entry[0] # shop
            movie = entry[1] # movie
            price = entry[2] # price
            movieItem = self.getMovieEntry(price, shop, movie)
            movieKey = self.getMovieKey(price, shop, movie)

            self.movieFinder[str(shop) + "_" + str(movie)] = movieItem

            if movie not in self.movies:
                self.movies[movie] = [movieItem]
                heapq.heapify(self.movies[movie])
            else:
                heapq.heappush(self.movies[movie], movieItem)
        for movie in self.movies:
            self.movies[movie].sort()
        heapq.heapify(self.rents)

    def search(self, movie: int) -> List[int]:
        result = []
        if movie not in self.movies:
            return result
        counter = 0
        for entry in self.movies[movie]:
            if entry[self.FIELD_STATUS] != self.STATUS_AVAILABLE:
                continue
            result.append(entry[self.FIELD_SHOP])
            counter += 1
            if counter >= self.reportLimit:
                break
        return result

    def rent(self, shop: int, movie: int) -> None:
        entry = self.movieFinder[str(shop) + "_" + str(movie)]
        entry[self.FIELD_STATUS] = self.STATUS_RENTED
        price = entry[self.FIELD_PRICE]
        item = self.getMovieEntry(price, shop, movie)
        key = self.getMovieKey(price, shop, movie)
        self.rentalFinder[key] = item
        heapq.heappush(self.rents, item)

    def drop(self, shop: int, movie: int) -> None:
        entry = self.movieFinder[str(shop) + "_" + str(movie)]
        entry[self.FIELD_STATUS] = self.STATUS_AVAILABLE
        price = entry[self.FIELD_PRICE]
        key = self.getMovieKey(price, shop, movie)
        rentedMovie = self.rentalFinder[key]
        rentedMovie[self.FIELD_STATUS] = self.STATUS_DROP
        del self.rentalFinder[key]

    def cleanRents(self):
        rents = list(self.rents)
        idx = 0
        while rents:
            if idx >= len(rents):
                break
            if rents[idx][self.FIELD_STATUS] == self.STATUS_DROP:
                rents.pop(idx)
                continue
            idx += 1
        rents.sort()
        self.rents.clear()
        for rent in rents:
            heapq.heappush(self.rents, rent)

    def report(self) -> List[List[int]]:
        result = []
        self.cleanRents()
        counter = 0
        for i in range(len(self.rents)):
            entry = self.rents[i]
            if entry[self.FIELD_STATUS] != self.STATUS_AVAILABLE:
                continue
            # print("price:%s shop: %s movie: %s status: %s" %(entry[self.FIELD_PRICE],entry[self.FIELD_SHOP],entry[self.FIELD_MOVIE],entry[self.FIELD_STATUS]))
            result.append([int(entry[self.FIELD_SHOP]), int(entry[self.FIELD_MOVIE])])
            counter += 1
            if counter >= self.reportLimit:
                break

        return result


movieRentingSystem = MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]])

movieRentingSystem.search(10)  # return [1, 0, 2], Movies of ID 1 are unrented at shops 1, 0, and 2. Shop 1 is cheapest shop 0 and 2 are the same price, so order by shop number.
movieRentingSystem.rent(0, 1) # Rent movie 1 from shop 0. Unrented movies at shop 0 are now [2,3].
movieRentingSystem.rent(1, 2) # Rent movie 2 from shop 1. Unrented movies at shop 1 are now [1].
movieRentingSystem.report()   # return [[0, 1], [1, 2]]. Movie 1 from shop 0 is cheapest, followed by movie 2 from shop 1.
movieRentingSystem.drop(1, 2) # Drop off movie 2 at shop 1. Unrented movies at shop 1 are now [1,2].
movieRentingSystem.search(2)  # return [0, 1]. Movies of ID 2 are unrented at shops 0 and 1. Shop 0 is cheapest, followed by shop 1.

action = ["MovieRentingSystem","rent","search","search","report","rent","rent","report","report","search","search","rent","rent","search","drop","drop","drop","drop","rent","report","report","rent","drop","search","report","drop","report","drop","rent","report","search","search","rent","rent","report","report","drop","report","report","drop","report","drop","rent","drop","search","rent","search","drop","rent","drop","report","rent","drop","rent","rent","drop","report","report","report","report","rent","drop","report","drop","rent","search","drop","report","rent","search","search","report","rent","report","report","rent","report","report","search","rent","rent","search"]
value = [[69,[[16,4156,1511],[20,8501,8417],[34,7901,7776],[54,6691,9511],[44,8931,8434],[42,9640,5251],[22,4534,9161],[32,6506,6831],[13,8501,731],[4,7610,8474],[33,820,2341],[17,6490,1161],[29,7120,2703],[8,8723,7613],[38,9544,1804],[30,8723,1047],[1,5015,7763],[60,1625,2383],[29,3336,3542],[39,7535,6066],[1,9074,9400],[39,1625,7944],[26,9160,6874],[55,2465,888],[35,8530,6025]]],[32,6506],[8501],[6275],[],[30,8723],[8,8723],[],[],[6699],[115],[20,8501],[16,4156],[9447],[30,8723],[8,8723],[32,6506],[16,4156],[42,9640],[],[],[17,6490],[20,8501],[8175],[],[17,6490],[],[42,9640],[54,6691],[],[1625],[3291],[60,1625],[39,1625],[],[],[60,1625],[],[],[39,1625],[],[54,6691],[8,8723],[8,8723],[2260],[29,7120],[746],[29,7120],[38,9544],[38,9544],[],[1,9074],[1,9074],[54,6691],[39,1625],[54,6691],[],[],[],[],[26,9160],[26,9160],[],[39,1625],[42,9640],[9640],[42,9640],[],[29,7120],[5630],[1842],[],[16,4156],[],[],[1,9074],[],[],[7992],[4,7610],[29,3336],[1333]]
expected = [None,None,[13,20],[],[[32,6506]],None,None,[[30,8723],[32,6506],[8,8723]],[[30,8723],[32,6506],[8,8723]],[],[],None,None,[],None,None,None,None,None,[[42,9640],[20,8501]],[[42,9640],[20,8501]],None,None,[],[[17,6490],[42,9640]],None,[[42,9640]],None,None,[[54,6691]],[60,39],[],None,None,[[60,1625],[39,1625],[54,6691]],[[60,1625],[39,1625],[54,6691]],None,[[39,1625],[54,6691]],[[39,1625],[54,6691]],None,[[54,6691]],None,None,None,[],None,[],None,None,None,[],None,None,None,None,None,[[39,1625]],[[39,1625]],[[39,1625]],[[39,1625]],None,None,[[39,1625]],None,None,[],None,[],None,[],[],[[29,7120]],None,[[16,4156],[29,7120]],[[16,4156],[29,7120]],None,[[16,4156],[29,7120],[1,9074]],[[16,4156],[29,7120],[1,9074]],[],None,None,[]]

movieRentingSystem = None
for i in range(len(action)):
    val = value[i]
    result = None
    if action[i] == "MovieRentingSystem":
        movieRentingSystem = MovieRentingSystem(val[0], val[1])
    elif action[i] == "rent":
        result = movieRentingSystem.rent(val[0], val[1])
    elif action[i] == "drop":
        result = movieRentingSystem.drop(val[0], val[1])
    elif action[i] == "search":
        result = movieRentingSystem.search(val[0])
    elif action[i] == "report":
        result = movieRentingSystem.report()

    if result != expected[i]:
        print("fail")
        print(action[i])
        print(value[i])
        print(expected[i])
        print(result)
        raise Exception("failed")

