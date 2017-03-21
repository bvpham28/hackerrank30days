def computeDifference(self):
    # Set Max to 0
    maximum = 0

    #Track one element in the array
    for i in range(len(self.__elements)):
        #Track the other element in the array
        for j in range(len(self.__elements)):
        #Find the absolute value
            absolute = abs(self.__elements[i] - self.__elements[j])
            # Find the max value
            if absolute > maximum:
                maximum = absolute

    self.maximumDifference = maximum