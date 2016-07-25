import unittest;
from Post import Post;

class TestPost(unittest.TestCase):

    def test_updateShares( self ):
        # create post with 30 shares
        post = Post(None, -1, 30);
        # add 20 shares
        post.updateShares(20);
        self.assertEqual(post.shares, 50);
        #subtract 30 shares
        post.updateShares(-30);
        self.assertEqual(post.shares, 20);

    def test_storePost( self ):
        # create post
        post = Post(None, -1, 30);
        post.storePost();
        allPosts = Post.getAllPosts();
        self.assertEqual(allPosts[-1], post);

if __name__ == '__main__':
    unittest.main()
