"""20 Questions Game!!!"""
import sys


class Answer:
    def __init__(self, name, qualities):
        assert type(name) is str
        assert type(qualities) is list
        self.name = name
        self.qualities = qualities

    def __str__(self):
        return self.name

    def correct(self):
        return 'Is {0} correct? '.format(self.name)

class Question:
    def __init__(self, term, phrase):
        assert type(term) is str
        assert type(phrase) is str
        self.term = term
        self.phrase = phrase

    def __str__(self):
        return '{0} {1}?'.format(self.phrase, self.term)

def create_matrix(answer_list, question_list):
    matrix = []
    for question in question_list:
        row = []
        for answer in answer_list:
            if question.term in answer.qualities:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def best_question(answer_list, question_list):
    matrix = create_matrix(answer_list, question_list)
    best, index = len(answer_list)+1, 0
    for row in matrix:
        total = abs(sum(row) - len(row)/2)
        if total == 0:
            return question_list[index]
        if total < best:
            best = total
            bestvar = index
        index += 1
    return question_list[bestvar]

traits = []
def start_game():
	answer_list = load_answers()
	question_list = load_questions()
	for answer in answer_list:
	    answer.option = True
	play(answer_list, question_list)

def play(answer_list, question_list):
    if len(answer_list) == 1:
        userchoice = input(answer_list[0].correct())
        if userchoice == 'yes' or userchoice == 'y' or userchoice =='yee':
            print('yay!')
        else:
            add_answer()
        return
    current_question = best_question(answer_list, question_list)
    answered = False
    new_list = []
    while not answered:
        response = input(str(current_question))
        if response == 'endgame':
            return
        elif response == 'yes' or response == 'y' or response == 'yee':
            answered = True
            traits.append(current_question.term)
            for answer in answer_list:
                for quality in answer.qualities:
                    if current_question.term == quality:
                        new_list.append(answer)
        elif response == 'no' or response == 'n' or response == 'nah':
            answered = True
            for answer in answer_list:
                include = True
                for quality in answer.qualities:
                    if quality == current_question.term:
                        include = False
                if include:
                    new_list.append(answer)
        else:
            print('Please answer with yes or no >W<')
    play(new_list, question_list)
    #add new answer to database using current_question and response variables


def load_answers():
    answer_text = open("animals.txt", "r+")
    answer_list = []
    for line in answer_text:
        words = line.split()
        answer_list.append(Answer(words[0], words[1:]))
    answer_text.close()
    return answer_list

def load_questions():
    question_text = open("questions.txt", "r+")
    question_list = []
    for line in question_text:
        words = line.rsplit(' ', 1)
        question_list.append(Question(words[1][:-2], words[0]))
    question_text.close()
    return question_list

def add_answer():
	answers = open("animals.txt","a")
	newEntry = input('What were you thinking of?(please write as one word)')
	str1 = ""
	for trait in traits:
		str1 = str1 + trait + " "
	answers.write(" \n{} {}".format(newEntry, str1))
	print(str(newEntry), 'has been added to the database')
	answers.close()

def main(args):
    input("Welcome to 20 Questions!\nThink of an animal and press enter when ready.")
    print("Answer the questions with yes or no and respond endgame if you wish to exit the game.")
    start_game()

if __name__ == "__main__":
    main(sys.argv)

#this is pretty broken rn i'm working on itz
