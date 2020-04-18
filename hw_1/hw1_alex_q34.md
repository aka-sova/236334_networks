
____________

## Question #3 

First, we convert all the codes to the binary notation (assuming the it's the MSB-first code).

We obtain:

1. $R_1$ = 0x0 (g=5) = 0b0 = $X^5$
2. $R_2$ = 0x3B (g=6) = 0b1111011 = $X^6 + X^5 + X^4+ X^3 + X + 1$
3. $R_3$ = 0x13 (g=5) = 0b110011 = $X^5 + X^4 + X + 1$ 

### (a)

In the case when there are more than 1 error, we should use $R_2$ or $R_3$, which have more than 1 term in their polynomial. $R_1$, for example, will not detect the error in the fifth bit. (it will have no remainder)

### (b)

In the case where we have 1, 3, or 5 errors - the common thing between those is that those are all **odd** numbers.

Remembering the characteristic from the tutorial, if the $G(x)$ is divided by $(x+1)$ without any remainder, then **any odd** number of error bits will be discovered. We already know that $R_1$ will not divide $(x+1)$, so what is left to check are $R_2$ and $R_3$.

#### $R_2$:

```python
1111011
11
______
00
  11
  11
  __
  00
    011
     11
     __
     00
```

We can observe that for $R_2$ there is no remainder.




#### $R_3$:
```python
110011
11
______
00
  0011
    11
    __
    00
```

We can observe that for $R_3$ there is no remainder.

Both $R_2$ and $R_3$ will detect **any** amount of odd error bits, thus, we can choose the more optimal divisor - the one that its CRC code requires less bits. This will be $R_3$, which will require only 5 bits. But Emil chose $R_2$, whatever.


### (c)
Looking at the ASCII table for 'c', 's' chars, we get:

- c = 0x63
- s = 0x73

So the complete 'clean' message is 0x6373 = ‭0110 0011 0111 0011‬

Now, calculating the $T(x) = x^gM(x) - [(x^gM(x) \%  G(x)]$



### (d) 

We are required we check whether the errors of the type: 

$$E(x) = x^{k+7} + x^k = x^k (x^7 + 1)$$

will be detected. We have to check whether the $(x^7 + 1)$ will divide $R_2$ with no remainder. 

```python
10000001
1111011
______
01110111
 1111011
 _______
 0001100
 _______
    1100
```

We can see that there is a remainder. Which means that we do detect the error. 



### (e)

The message received is $T(x)$ = 0x1B0B = 0001 1011 0000 1011‬

We have to divide it by the Divisor $R_2$ and see if we get any remainder left. If we do, then **for sure** there is an error inside.

Performing the division:

```python 
1101100001011‬
1111011
_______
  1011100
  1111011
  _______
   1001111
   1111011
   _______
    1101000
    1111011
    _______
      1001111
      1111011
      _______
       110100
```
We can see that the remainder is not equal 0.

This means there is an error inside the message and we have to resend it. There is no way to detect which bit exactly was erroneous, we also don't know how many erroneous bits were received.




____________

## Question #4


### (a) 

We are given: the probability of 1 erroneous bit: $p = 5 \times 10^6$.

The probability of a successful bit: $(1-p)$

One frame contains 12500 bytes, which is $10^5$ bits.
The chance to receive the frame with no error, meaning all bits are received correctly, is:

<span style="font-size:16px;">

$$P_{success} = (1-p)^{10^5} \approx 0.607$$

</span>

Likewise, the chance to receive 1 bit with error is:

<span style="font-size:16px;">

$$P_{one\_bit\_error} = (10^5)\times(p\times(1-p)^{10^5-1}) \approx 0.303$$

</span>

where we multiplied the probability of some bit to be erroneous by a number of total bits.


### (b)

We are given a new measure, we denote it $S_{ch}$:

<span style="font-size:16px;">

$$S_{ch} = \frac{bits\ number\ in\ a\ frame}{frame\ average\ length} = \frac{N_{bits}}{F_v}$$

</span>

We consider each case separately:

#### (1) 

**Correction** code adds 100 bits, and requires no additional sendings to be performed, thus:

<span style="font-size:16px;">

$$S_{ch1} = \frac{10^5}{10^5 + 100} \approx 0.999$$

</span>



**Detection** code adds 10 bits, but that means we will have to send the erroneous frame again (which is successful by exercise condition). We define M - random variable symbolizing the amount of messages sent. Due to the geometric probability:

<span style="font-size:16px;">

$$E(M) = \frac{1}{P_{successful\ frame}} = \frac{1}{0.607} = 1.65$$

</span>

Thus, the average frame length and the throughtput:

<span style="font-size:16px;">

$$F_v = E(M) \times (10^5 + 10) = 1.65 \times (10^5 + 10) = 165016.5 [bits] $$

$$S_{ch2} = \frac{10^5}{165016.5} \approx 0.606  $$

</span>

Consequency, we obtain:

<span style="font-size:16px;">

$$S_{ch1} > S_{ch2}$$

</span>

Which means that throughput of the correction code is higher and on average more bits will be transmitted in the same amount of time.


#### (2)

Doing the same calculations as before, briefly:

**Correction**

<span style="font-size:16px;">

$$S_{ch1} = \frac{10^5}{10^5 + 29000} \approx 0.775$$

</span>


**Detection**

<span style="font-size:16px;">

$$F_v = E(M) \times (10^5 + 500) = 1.65 \times (10^5 + 500) = 165825 [bits] $$

$$S_{ch2} = \frac{10^5}{165825} \approx 0.603 $$

</span>

And we get:

<span style="font-size:16px;">

$$S_{ch1} > S_{ch2}$$

</span>

Which means that still, the **correction** code gives better throughput.














