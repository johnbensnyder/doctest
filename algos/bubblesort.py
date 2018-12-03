class Bubbblesort(object):
    """
    Some basic sorting using bubblesort.
    """
    def __init__(self, array=None):
        """
        Nothing needed to init
        """
        self.array=array

    @property
    def array(self):
        print("This is the current array")
        return self.__array

    @array.setter
    def array(self, x):
        self.__array=x

    def array_pass(self):
        """
        perform a single pass over the array
        :return: Counter of swaps
        """
        counter=0
        for i in range(1, len(self.__array)):
            if self.__array[i-1]>self.__array[i]:
                temp=self.__array[i]
                self.__array[i]=self.__array[i-1]
                self.__array[i-1]=temp
                counter+=1
        return counter

    def sort(self):
        """
        perform passes until counter==0
        :return: None
        """
        counter=self.array_pass()
        while counter:
            counter=self.array_pass()

