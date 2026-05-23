# Hash Table

## Hash Table Description
The hash function produces an index that the add() and lookup() methods use to handle data collision via key placements in a dictionary.

### Core Functions

#### Init() method:
__init__ establishes a baseline empty dictionary the program will build off of.

#### Hash() method:
The hash() method sums the ord() values and returns the raw integer as the index

#### Add() method:
The add() method creates a new key:value if the data is absent from the dictionary, otherwise it updates the value to the existing key.

#### Remove() Method:
The remove() method tracks index and keys, then returns the result for later use, if needed.

#### Lookup() Method:
The lookup() method finds the key in the dictionary and returns the respective value.
