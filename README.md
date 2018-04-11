# Game Guess the Number 

### in python


## Game description

The computer sorts a random number between 100-999 and you have to guess it in 10 guesses.

In each attempt, you get a random tip that should help you calculate the correct number.

The tips are:

for example on the random number: 256

|Num| Tip | Answer | for num 
|---|---|---|---|
| 1. |Sum of all digits in a three-digit number | 13 | [2+5+6]
| 2. |Multiply all digits in a three digit number | 60 | [2\*5\*6=]
| 3. |The even digits | X-X | [2=X | 5=- | 6=x]
| 4. |The big( who is bigger then 5) digits in the number | --X | [2=- | 5=- | 6=x]
| 5. |Is ascending ?  | True | [2<5<6 - Yes]
| 6. |The prime digits are | XX- | [2=X | 5=X | 6=-]

For each misguided guessing, you fall 10 points from the score in the previous step, you start the game with 100 points


have a nice time


Example of running


```
welcome to guess game! 
You have  10  changes to guess my random num of 3 digit.
In every try I give you a tip for helping the calculate the number.


	Tip:  The  even digits  :  -X-
 1) Enter num of 3-digits[or 'Enter' to finish]: 102

```
so after this tip, we can know that the 3 digit can be this options: 


[1 3 5 7 9]   [0 2 4 6 8]    [1 3 5 7 9]

```

	Tip:  The big(>5) digits:  ---
 2) Enter num of 3-digits[or 'Enter' to finish]: 101

```
and now we can filter more digit , keep save the digit under 5 

[1 3 5] [0 2 4] [1 3 5]

```

	Tip:  Sum of all digit  :  8
 3) Enter num of 3-digits[or 'Enter' to finish]: 125

```
and now we can calculate the optional answer that the sum of all thes digit is will be 8: 
for example: 

|d1|d2|d3|
|---|---|---|
|[1]|[2]|[5]|
|[1]|[4]|[3]|
|[3]|[0]|[5]|
|[3]|[4]|[1]|
|[5]|[0]|[3]|
|[5]|[2]|[1]|
  

```

	Tip:  The prime digits  :  XX-
 4) Enter num of 3-digits[or 'Enter' to finish]: 521


```
and after we know that the 2 first digit is a prime number, and the third isn't the option that stay for us is: 

[5] [2] [1]

and the Expected output has showen: 

```


	****************************************
	**** Yes correct! you win 70 points ****
	****************************************




### Do you want to play again? [Y|N] : 
```

Try it yourself...
