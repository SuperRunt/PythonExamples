# I was thinking about figuring out how to extend the Set class, but
# considering I'm new to Python, and extending native classes isn't always
# the best idea anyway, I made up a new class.
# To be honest, I woudln't have bothered creating a class for this at
# all if it hadn't been for the fact that I wasn't able to get the tests
# to run without having a module to import...

class ArrayDiff( set ):

    def __init__(self, baseArray):
        self.baseArray = baseArray;

    # the next two coudl be class methods for this specific putpose,but I
    # figured they cousl come in handy on their own in the big scheme of things..
    def getArrayAdditions( self, target ):
        return set(target).difference(self.baseArray);

    def getArrayDeletions( self, target ):
        return set(self.baseArray).difference(target);

    def printArrayDiffs( self, target ):
        addToCurrent = self.getArrayAdditions(target);
        deleteFromCurrent = self.getArrayDeletions(target);

        print "additions: [" + ', '.join(str(x) for x in addToCurrent) + "]";
        print "deletions: [" + ', '.join(str(x) for x in deleteFromCurrent) + "]";



arrayToCompare = ArrayDiff([1, 3, 5, 6, 8, 9]);
arrayToCompare.printArrayDiffs([1, 2, 5, 7, 9]);
