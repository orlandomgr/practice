from myUtils.Utils import printResult
from collections import defaultdict, OrderedDict
from typing import List


class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(List)
        self.maxSize = 10
        self.ts = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.ts, tweetId))
        self.ts += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        if userId in self.tweets:
            news.extend(self.tweets[userId])
        if userId in self.follows:
            for user in self.follows[userId]:
                if user in self.tweets:
                    news.extend(self.tweets[user])

        news.sort(reverse=True)
        news = news[: self.maxSize]
        tmp = []
        for ts, tweet in news:
            tmp.append(tweet)
        return tmp

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


twitter = Twitter()
twitter.postTweet(1, 5)
printResult(twitter.getNewsFeed(1), [5])
twitter.follow(1, 2)
twitter.postTweet(2, 6)
printResult(twitter.getNewsFeed(1), [6, 5])
twitter.unfollow(1, 2)
printResult(twitter.getNewsFeed(1), [5])

twitter = Twitter()
twitter.postTweet(1,5)
twitter.postTweet(1,3)
printResult(twitter.getNewsFeed(1), [3, 5])

twitter = Twitter()
twitter.postTweet(1,5)
twitter.follow(1,2)
twitter.follow(2,1)
printResult(twitter.getNewsFeed(2), [5])
twitter.postTweet(2,6)
printResult(twitter.getNewsFeed(1), [6, 5])
printResult(twitter.getNewsFeed(2), [6, 5])
twitter.unfollow(2,1)
printResult(twitter.getNewsFeed(1), [6, 5])
printResult(twitter.getNewsFeed(2), [6])
twitter.unfollow(1,2)
printResult(twitter.getNewsFeed(1), [5])
printResult(twitter.getNewsFeed(2), [6])
