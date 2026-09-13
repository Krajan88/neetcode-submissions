"""
*You can optimize this code by changing getNewsFeed()

Right now, you are putting all of the user's posts and all the posts of the users he follows into the tempMaxHeap.
Instead, you can put just his most recent post and the most recent post of every of the users he follows, and as you
pop the most recent one from the tempMaxHeap, push the user's you just popped 2nd most recent post etc.

1) put every user's most recent post in the temp heap
2)pop the most recent one, and, depending on which user that was, push their 2nd most recent one
3)continue until you either did 10 posts or heap is empty
"""

class Twitter:

    def __init__(self):
        self.posts = defaultdict(list) #hashmap where key - userID and value - maxHeap made up of tuples (recency, tweetID)
        self.followerList = defaultdict(list)
        self.recency = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        #Every posts' recency is tracked globally. The user's posts are kept in a max heap sorted by said recency
        self.recency -= 1
        heapq.heappush(self.posts[userId], (self.recency, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        #the userId user's news feed will be stored in a temporary max heap -- it will consist of 
        #a) the user's posts, b) posts of the users that they follow
        tempMaxHeap = []
        res = []
        
        #user's own posts must be included in their feed
        for element in self.posts[userId]:
            heapq.heappush(tempMaxHeap, element)
        
        #the followers' posts must be included in the feed
        for follower in self.followerList[userId]:
            for post in self.posts[follower]:
                heapq.heappush(tempMaxHeap, post)

        #we are only interested in the 10 most recent posts across user and his followers in the feed
        for i in range(10):
            if tempMaxHeap:
                recency, tweet = heapq.heappop(tempMaxHeap)
                res.append(tweet)
            else:
                break
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        #Check whether a user(followerId) follows anoter user(followeeId) to avoid double counting
        if followeeId not in self.followerList[followerId]:
            self.followerList[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #Check whether a user(followerId) follows anoter user(followeeId).
        #If they don't, they cannot unfollow that another user
        if followeeId in self.followerList[followerId]:
            self.followerList[followerId].remove(followeeId)

       