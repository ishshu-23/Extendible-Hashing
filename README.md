# Extendible-Hashing
This repository contains the Python implementation of Extendible Hashing, a data structure used for hash table management. The code demonstrates how directory and bucket expansion is performed when collisions occur during key insertion.

## Getting Started

To run the code, ensure you have Python installed on your system. Simply execute the `main.py` script to see the Extendible Hashing in action.

## Implementation Details

The code consists of the following main components:

- `Directory`: Represents the directory used for storing pointers to buckets.
- `Bucket`: Represents the buckets that hold keys in the hash table.
- `Hash`: Implements the hash function used to convert keys into binary format.
- `LsbToIndex`: Contains the conversion function to map binary strings to index values.
- `KeyInsertion`: Handles the insertion of keys into the hash table, performing bucket and directory expansion as needed.
- `Main`: The main class that orchestrates the execution and reads keys from a file for insertion.

## Usage

You can use this code as a reference to understand the basics of Extendible Hashing and how to handle hash table collisions through bucket and directory expansion.

Feel free to modify and extend the code to suit your specific requirements.

## Contributing

Pull requests are welcome. For major changes or enhancements, please open an issue first to discuss the proposed changes.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

