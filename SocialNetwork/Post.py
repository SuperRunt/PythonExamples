# IRL this woudl be a db table...
allPosts = [];

class Post( object ):

    def __init__( self, postID, repostID, shares ):
        # in case post is brand new and don't have an id yet
        if postID is None:
            postID = len(allPosts) + 1;

        self.postID = postID;
        self.shares = shares;
        self.repostID = repostID;
        # add post to 'database'
        self.storePost();

    def updateShares( self, shares ):
        # add (on creation of re-posts) or remove (on deletion of re-posts) shares
        self.shares += shares;

    def storePost(self):
        allPosts.append(self);

    def updateOriginalPosts( self, repostID, addedShares ):
        if repostID > -1:
            # since this was a re-post, find which post it shares by looking up
            # the post with postID same as this repostID
            sharedPost = next((p for p in allPosts if p.postID == repostID), None);
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

    @staticmethod
    def getAllPosts():
        return allPosts;

    @staticmethod
    def printAllPostShares():
        for p in allPosts:
            print p.postID, p.shares;
