from collections import defaultdict
import random

__wordLength = 5
wordSet = set()

class Wordle:
    global wordSet, __wordLength
    """
    Wordle을 구현하였다.

    Attributes:
        answer: Wordle에서 사용될 정답 단어(string)
        userInput: Wordle에서 사용자가 입력한 단어(string)
        query: 사용자가 정답을 찾을 때까지 입력한 횟수(integer)
        __wordLength: 정답 단어 및 입력 단어의 길이(integer)
        
    Methods:
        __str__: 실제 Wordle 사이트에서 정답 공유할 때와 같은 문자열 반환
        verify: 단어가 Wordle의 조건을 만족하는지 확인
        setAnswer: 정답 단어를 입력하는 함수
        getAnswer: 정답 단어를 불러오는 함수
        compare: 입력 단어와 정답 단어를 비교하여 올바른 형태의 패턴을 출력하는 함수
        setInput: 입력 단어를 저장하는 함수
        getInput: 입력 단어를 불러오는 함수
        isEnd: 게임이 종료되었을 때 True를 반환하는 함수
        getQuery: query를 반환
        convert_to_pattern: compare 함수에서 만든 문자열을 __str__에 저장할 패턴으로 변환하는 함수
    """
    def __init__(self):
        self.answer = ''
        self.userInput = ''
        self.query = 0
        self.end = False
    
    def __str__(self):
        return None
    
    def verify(word):
        """
            단어가 조건을 만족하는지 테스트한다.

            1) 길이가 __wordLength와 같은가?
            2) 알파벳으로만 구성되어 있는가?
            3) 사전에 등재되어 있는가?(wordSet에 포함되는가?)

            Args:
                word: 검증할 단어(string)
            
            Raises:
            
            Returns:
                verified: 검증 여부(boolean)
        """
        verified = True
        if verified: self.query += 1
        return verified
    
    def setAnswer(self, word):
        if not verify(word):
            return False
        self.answer = word
        return True
    
    def getAnswer(self):
        if self.answer: 
            return self.answer
        return None
    
    def compare(self):
        """
    입력 단어와 정답 단어를 비교하여 패턴을 출력한다.

    answer와 userInput에 대하여 알파벳을 차례대로 비교하여,
    정확한 위치에 해당 문자가 있으면 "2",
    위치는 잘못되었으나, 해당 문자가 포함되면 "1"
    알파벳이 없다면 "0"으로 된 __wordLength 길이의 문자열을 반환한다.
    단, 중복되는 문자들에 대해서는 앞에서부터 차례로 "1"을 부여하고,
    정답에 포함된 문자의 개수를 초과해서 출력할 수 없다.

    Args:

    Raises:
        assertionError: 두 문자열의 길이가 __wordLength가 아닌 경우

    Returns:
        pattern: "2","1","0"으로 구성된 __wordLength 길이의 문자열
    """
        pattern = ''
        return pattern
    
    def isEnd(self):
        return (self.userInput == self.answer)
    
    def setInput(self, input_word):
        self.userInput = input_word

    def getInput(self):
        return self.userInput
    
    def getQuery(self):
        return self.query
    
    def convert_to_pattern(self):
        return ""

class WordleGame():
    """
    다양한 환경에서 Wordle을 플레이할 수 있다.
    여러 번 반복하여 플레이한 통계를 알려준다.
    특정 전략에 따른 플레이 결과를 확인할 수 있다.

    Attributes:
        game: Wordle 클래스(class)
        history: query에 따른 answer들의 집합 (플레이 때마다 실행한 횟수들로 정답 단어들을 분류한 defaultdict)
    
    Methods:
        initialize: game을 초기화하는 함수


    """
    def __init__(self):
        self.game = Wordle()
        self.history = defaultdict(set)
    
    def initialize(self):
        self.game = Wordle()
    
    def set_answer_randomly(self):
        self.game.setAnswer(random.choice(wordSet))
    
    def set_answer_list(self, answer_word_set):
        for answers in answer_word_set:
            self.ga

    def play_live(self):
        self.initialize()
        self.set_answer_randomly()
        while not self.game.isEnd():
            input_live = input("Guess 5 letter word: ")
            if not self.game.verify(input_live): continue
            #write more codes!
            #compare those words
        #updates self.history
        return True

    def getHistory(self):
        return self.history
    
