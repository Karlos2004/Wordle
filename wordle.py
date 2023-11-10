from collections import defaultdict
import random
from set_word_list import wordSet

__wordLength = 5

class Wordle:
    global wordSet, __wordLength
    """
    Wordle의 기본적인 기능을 담은 클래스다.

    Attributes:
        _answer: Wordle에서 사용될 정답 단어(string)
        _userInput: Wordle에서 사용자가 입력한 단어(string)
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
    def __init__(self, answer_word=''):
        self.setAnswer(answer_word)
        self._userInput = ''
        self.query = 0
        self.end = False
    
    def __str__(self):
        """
            Wordle의 플레이 내역을 문자열의 형태로 반환하는 함수다.
            Wordle 공식 홈페이지를 참조하여 만들고자 한다.

            Args:
            Raises:
                assertionError: 플레이가 종료된 후 불러올 수 있다.
            
            Returns:
                summary: 플레이 내역을 담은 문자열(string)
        """
        return None
    
    @staticmethod
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
        if len(word) != __wordLength: verified = False
        if verified: self.query += 1
        return verified
    
    @property
    def answer(self):
        return self._answer
        
    @answer.setter
    def answer(self, answer_word):
        if not verify(answer_word):
            return False
        self._answer = answer_word
        return True
        
    
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
        return (self._userInput == self._answer)
    
    @property
    def userInput(self):
        return self._userInput
    
    @userInput.setter
    def userInput(self, input_word):
        self._userInput = input_word

    def getQuery(self):
        return self.query
    
    @staticmethod
    def convert_to_pattern(int_pattern):
        digit_dictionary = {"0":"G", "1":"Y", "2":"B"}
        str_pattern = ""
        for digit in int_pattern:
            str_pattern += digit_dictionary[digit]
        return str_pattern
    
    @staticmethod
    def decimal_to_ternary(dec_num):
        ter_num = ""
        while dec_num > 0:
            ter_num = str(dec_num % 3) + ter_num
            dec_num //= 3
        return ter_num.zfill(5)
    
    @staticmethod
    def ternary_to_decimal(ter_num):
        dec_num = int(ter_num, 3)
        return dec_num

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
        set_answer_randomly: answer를 임의로 정하는 함수
        set_answer_list: answer_word가 주어졌을 때, answer로 설정하는 함수
        play_live_randomly: 임의의 정답에 대해서 실시간 플레이할 수 있는 함수
        play_live_with_list: 단어 리스트 순서대로 입력할 때 플레이 결과를 보여주는 함수
        getHistory: history를 반환하는 함수
    """
    def __init__(self):
        self.game = Wordle()
        self.history = defaultdict(set)
    
    def initialize(self):
        self.game = Wordle()
    
    def set_answer_randomly(self):
        self.game.setAnswer(random.choice(wordSet))
    
    def set_answer_list(self, answer_word):
        self.game.setAnswer(answer_word)

    def play_live_randomly(self):
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
