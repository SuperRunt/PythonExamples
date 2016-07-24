from CsvConverter import CsvConverter;
from Post import Post;

CsvConverter.convertPostsDataToObjects('network_data.csv');
Post.printAllPostShares();
