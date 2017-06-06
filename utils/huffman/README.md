# Huffman coding

*Encoding and analysis of Huffman prefix codes*


## Run
```shell
$ python3 huffman_coding.py
```


## Usage
1. set the frequencies in [line 114](https://github.com/FIUP/algotests/blob/master/utils/huffman/huffman_coding.py#L114)
2. run
3. see best huffman coding output in terminal

... or if you want to check your solution ...

1. set the frequencies in [line 114](https://github.com/FIUP/algotests/blob/master/utils/huffman/huffman_coding.py#L114)
2. set your huffman coding in [line 122](https://github.com/FIUP/algotests/blob/master/utils/huffman/huffman_coding.py#L122) as a dict, that is {"a": "001", "b": "0000", "c": ... }
3. call ```calc_avg_word(freq, code)``` and check if average word length is the same as using the best algorithm


## Sample output
```shell
→ python3 utils/huffman/huffman_coding.py 
e  12.70 100
t   9.06 000
a   8.17 1110
o   7.51 1101
i   6.97 1011
n   6.75 1010
s   6.33 0111
h   6.09 0110
r   5.99 0101
d   4.25 11111
l   4.03 11110
c   2.78 01001
u   2.76 01000
m   2.41 00111
w   2.37 00110
f   2.23 00100
g   2.02 110011
y   1.97 110010
p   1.93 110001
b   1.49 110000
v   1.04 001010
k   0.75 0010111
j   0.15 001011011
x   0.15 001011010
q   0.10 001011001
z   0.07 001011000
Average word length is 4.205461924468702
```
