class Twitter:

    def __init__(self):
        self.posts = defaultdict(list) #hashmap where key - userID and value - maxHeap made up of tuples (recency, tweetID)
        self.followerList = defaultdict(list)
        self.recency = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.recency -= 1
        heapq.heappush(self.posts[userId], (self.recency, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        tempMaxHeap = []
        res = []
        
        #user's own posts must be included in their feed
        for element in self.posts[userId]:
            heapq.heappush(tempMaxHeap, element)
        
       # print(tempMaxHeap)
       # print(self.followerList)



       # print(self.followerList)
        for follower in self.followerList[userId]:
            for post in self.posts[follower]:
                heapq.heappush(tempMaxHeap, post)

       # print(tempMaxHeap)

   
        for i in range(10):
           # print(tempMaxHeap)
            if tempMaxHeap:
                recency, tweet = heapq.heappop(tempMaxHeap)
                res.append(tweet)
            else:
                break
    
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followerList[followerId]:
            self.followerList[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #er unfollows ee
        #print(self.followerList)

        if followeeId in self.followerList[followerId]:
            self.followerList[followerId].remove(followeeId)

       
        
