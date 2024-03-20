# Wordle Guess Finder and Helper

Just a little Python script I wrote. I use it to put other people's guess patterns in based on the answer of the wordle and find what their guesses could have been. 

Because the logic was really similar, I also started using it to help give me words that could be the answer based on my current guess. 

I am using Python 3.11.4 currently.

## Commands
`py .\guessfinder.py` 
Enter the wordle answer: SPELT
Enter your guesses separated by commas: GYBYB,GBGGG

Your Guesses:
For guess :large_green_square::large_yellow_square::black_large_square::large_yellow_square::black_large_square:: SLOTH
For guess :large_green_square::black_large_square::large_green_square::large_green_square::large_green_square:: SMELT

It prints it out in a format that I could post it into slack as a comment and show people what I think their guesses are.

`py .\guessfinder.py --extensive`
This was made to use the "allowedList.txt" so that it shows more words that aren't commonly used but could still be used because Wordle accepts them as valid words. (They won't ever be the anwer though)

`py .\guessfinder.py` 
You can also hit enter on the first question and then it will ask you more questions so that it can recommend words for you to put in to solve Wordle for the day. 

Enter the wordle answer: 
Enter your guesses separated by commas: BBGBB
Enter your guess for the pattern: STICK
Enter any characters that are already eliminated:

So I entered the color pattern on the 2nd line and then the word that I used on the 3rd line. If I had already guessed a word I could put the "Black" letters on the 4th line so that it wouldn't recommend words with those letters.