class Post( object ):

    # storage for Post objects
    allPosts = [];

    def __init__( self, postID, repostID, shares ):
        # in case post is brand new and don't have an id yet
        if postID is None:
            postID = len(self.allPosts) + 1;

        self.postID = postID;
        self.shares = shares;
        self.repostID = repostID;
        # add post to storage
        self.storePost();

    def updateShares( self, shares ):
        # add (on creation of re-posts) or remove (on deletion of re-posts) shares
        self.shares += shares;

    def storePost(self):
        self.allPosts.append(self);

    def updateOriginalPosts( self, repostID, addedShares ):
        if repostID > -1:
            # since this was a re-post, find which post it shares by looking up
            # the post with postID same as this repostID
            sharedPost = next((p for p in self.allPosts if p.postID == repostID), None);
            if sharedPost != None:
                # add to the post's shares number
                sharedPost.updateShares(addedShares);
                # update the post this one was shared from
                self.updateOriginalPosts(sharedPost.repostID, addedShares);

    @classmethod
    def createNewAndUpdateExisting( self, postID, repostID, shares ):
        self = self(postID, repostID, shares);
        # update number of shares on shared post(s)
        self.updateOriginalPosts(self.repostID, self.shares);

    @classmethod
    def getAllPosts( self ):
        return self.allPosts;

    @classmethod
    def printAllPostShares( self ):
        for p in self.allPosts:
            print p.postID, p.shares;
