class HashTable:
    ''' 
    This class creates a dictionary from scratch
    '''
    def __init__(self,numberOfBuckets):

        self.numberOfBuckets=numberOfBuckets
        self.dictionary=[[] for bucket in range (0,self.numberOfBuckets)]
    
    def addRecord(self,key,value):
        '''
        This method adds a record to the dictinary
        Args:
            key: key of the value to store
            value: value of the key to store
        '''
        bucketNumber=self._hashFunction(key)  #Get bucket number using hash function
        arrayBucket=self.dictionary[bucketNumber]  #find the array bucket that contains the key 
        for idx, (k,v) in enumerate(arrayBucket):  #Loop to validate the existance of a key. If it is found overwrites the value
            if k==key:   #Conditional to verify the existance of a key
                arrayBucket[idx]=(key,value)  #Change the value of the key
                return
        arrayBucket.append((key,value))  #Append the value in the case that it does not exist
        return

    def getRecord(self,key):
        '''
        Get the record passing as specifiic key in time O(1)
        '''
        bucketNumber=self._hashFunction(key)  #Get the bucket number that corresponds to a key
        bucket=self.dictionary[bucketNumber]   #Get the array bucket with the element that we look for
        for k,v in bucket:  #Iterate through the elements of the bucket
            if k==key:
                print(f'Found value {v}')
                break
        print(f'Key not found')

    def printRecords(self):
        '''
        Method to print the elements of the dictionary O(n)
        '''
        for bucket in self.dictionary: # Iterate through each bucket
            for element in bucket:   #Iterate through each element in a bucket
                print(element)   #print the element

    def _hashFunction(self,key):
        '''
        Function to generate the bucket number to be stored
        '''
        keyStr=str(key)  #Transform to a string
        bucketNumber=0
        for character in keyStr: #Iterate through each string
            bucketNumber=(bucketNumber*50+ord(character))%self.numberOfBuckets  #Has function
        return bucketNumber
    

if __name__=="__main__":
    hashTable=HashTable(5)
    hashTable.addRecord('name','ricardo')
    hashTable.addRecord('name','alejandro')
    hashTable.addRecord('lastName','manzano')
    hashTable.addRecord('address','Armenia')
    hashTable.addRecord('city','Quito')
    
    hashTable.printRecords()
    hashTable.getRecord('city')
