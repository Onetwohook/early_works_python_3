import random

# assigns 8ball answers to numbers 1 - 9
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply isno'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

# gets random no 1-9, prints return from function above
# these last three lines can be written as one line of code
# but as i didnt think of it myself, leaving as it is
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
