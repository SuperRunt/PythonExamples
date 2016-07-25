import unittest;
from CsvConverter import CsvConverter;
from Post import Post;

postList = [
    ['postId', ' repostId', ' followers'],
    ['1', ' -1', ' 120'],
    ['2', ' 1', ' 60'],
    ['3', ' 1', ' 30'],
    ['4', ' 2', ' 90'],
    ['5', ' 3', ' 40'],
    ['6', ' 4', ' 10'],
    ['7', ' -1', ' 240'],
    ['8', ' 7', ' 190'],
    ['9', ' 7', ' 50']
];

class TestCsvConverter(unittest.TestCase):

    #  test that the data read from file matches expected output
    def test_csvReadData( self ):
        convertedList = CsvConverter.readPostDataFromFile('network_data.csv');
        self.assertEqual(len(convertedList), 10);
        self.assertEqual(sorted(convertedList), sorted(postList));

    # test that conversion of data creates objects with shares that
    # match expected numbers
    def test_csvConversionAndShares( self ):
        CsvConverter.convertPostsDataToObjects('network_data.csv');
        allPosts = Post.getAllPosts();
        self.assertEqual(allPosts[0].shares, 350);
        self.assertEqual(allPosts[6].shares, 480);

if __name__ == '__main__':
    unittest.main()
