# Huffman coding

*Encoding and analysis of Huffman prefix codes*


## Run
```shell
$ python3 huffman_coding.py
```


## Usage
1. set the frequencies in [line 114](https://github.com/FIUP/algotests/blob/master/utils/huffman_coding.py#L114)
2. run
3. see best huffman coding output in terminal

... or if you want to check your solution ...

1. set the frequencies in [line 114](https://github.com/FIUP/algotests/blob/master/utils/huffman_coding.py#L114)
2. set your huffman coding in [line 132](https://github.com/FIUP/algotests/blob/master/utils/huffman_coding.py#L114) as a dict, that is {"a": "001", "b": "0000", "c": ... }
3. call ```calc_avg_word(freq, code)``` and check if average word length is the same as using the best algorithm
