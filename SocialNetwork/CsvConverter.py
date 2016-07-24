import csv;
from Post import Post;

class CsvConverter():

    @staticmethod
    def convertPostsDataToObjects( fileName ):
        # read csv file
        with open(fileName, 'rb') as f:
            reader = csv.reader(f);
            postList = list(reader);

        # get rid of file headers
        postList.pop(0);
        # create a post object for each entry in list
        for post in postList:
            Post.createNewAndUpdateExisting(int(float(post[0])), int(float(post[1])), int(float(post[2])));
