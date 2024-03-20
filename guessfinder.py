import argparse

# This function is used to help me determine if a word already has one of the letters it needs
# In wordle if you guess with a duplicate letter it won't hilight the second letter yellow, it will be black
# This function helps account for that
def count_duplicates(word):
    """Count the occurrences of each letter in a word."""
    counts = {}
    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts

def filter_words(possible_words, guess, answer, isAnswer, notAllowedCharacters=None):
    possible = []
    answer_counts = count_duplicates(answer)
    for word in possible_words:
        word_counts = count_duplicates(word)
        valid = True

        if notAllowedCharacters and any(char in word for char in notAllowedCharacters):
            continue  # Skip the word if it contains any of the not allowed characters
        if isAnswer:
            for i in range(len(word)):
                if guess[i] == 'B':
                    if word[i] in answer: # if the letter of this word is in the answer 
                        valid = False 
                        break
                elif guess[i] == 'Y':
                    if word[i] == answer[i] or (word[i] not in answer or word_counts.get(word[i], 0) != answer_counts.get(word[i], 0)): # if the letter is in the right spot or not in the word 
                        valid = False # then its not a valid guess
                        break
                elif guess[i] == 'G':
                    if word[i] != answer[i]: # if the letter isn't in the right spot 
                        valid = False # then its not a valid guess
                        break
        else: # This is my logic copied so that I could use it to help me find the answer rather than find the guesses. 
            for i in range(len(word)):
                if guess[i] == 'B':
                    if answer[i] in word: # if the letter of this word is in the potential answer 
                        valid = False 
                        break
                elif guess[i] == 'Y':
                    if answer[i] == word[i] or (answer[i] not in word or word_counts.get(answer[i], 0) != answer_counts.get(answer[i], 0)): # if the letter is in the right spot or not in the word 
                        valid = False # then its not a valid answer
                        break
                elif guess[i] == 'G':
                    if answer[i] != word[i]: # if the letter isn't in the right spot 
                        valid = False # then its not a valid answer
                        break
        if valid:
            possible.append(word)
    return possible

def convert_to_slack(guess):
    slack_guess = ''
    for letter in guess:
        if letter == 'B':
            slack_guess += ':black_large_square:'
        elif letter == 'G':
            slack_guess += ':large_green_square:'
        elif letter == 'Y':
            slack_guess += ':large_yellow_square:'
    return slack_guess

def main():
    parser = argparse.ArgumentParser(description='Wordle Solver')
    parser.add_argument('--extensive', action='store_true', help='Perform an extensive search')
    args = parser.parse_args()

    extensive_search = args.extensive

    answer = input("Enter the wordle answer: ").upper()
    your_attempts = input("Enter your guesses separated by commas: ").split(',')
    
    # Read possible words from file
    with open("answerList.txt", "r") as file:
        possible_words = file.read().upper().splitlines()

    if extensive_search:
        # Read possible words from an extensive list file
        with open("allowedList.txt", "r") as file:
            additional_possible_words = file.read().upper().splitlines()
        
        # Combine the words from both files
        possible_words.extend(additional_possible_words)
    
    if not answer:
        myGuessWord = input("Enter your guess for the pattern: ").upper()
        notAllowedCharacters = input("Enter any characters that are already eliminated: ").upper()
        notAllowedCharacterList = [char for char in notAllowedCharacters]
        for guess in your_attempts:
            possible_answers = filter_words(possible_words, guess, myGuessWord, False, notAllowedCharacterList)
            print("\nYour Possible Answers:")
            print(f"For guess {myGuessWord} with patterns {', '.join(your_attempts)}: {', '.join(possible_answers)}")

    else: 
        print("\nYour Guesses:")
        for guess in your_attempts:
            possible = filter_words(possible_words, guess, answer, True)
            slack_guess = convert_to_slack(guess)
            print(f"For guess {slack_guess}: {', '.join(possible)}")

if __name__ == "__main__":
    main()