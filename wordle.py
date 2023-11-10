from collections import defaultdict
import random
from set_word_list import wordSet
import copy
import statistics
import cProfile

_wordLength = 5

def verify(word):
    """
        단어가 조건을 만족하는지 테스트한다.

        1) 길이가 __wordLength와 같은가?
        2) 알파벳으로만 구성되어 있는가? (3번으로부터 확인 가능)
        3) 사전에 등재되어 있는가?(wordSet에 포함되는가?)

        Args:
            word: 검증할 단어(string)
        
        Raises:
        
        Returns:
            verified: 검증 여부(boolean)
    """
    verified = True
    if len(word) != _wordLength: verified = False
    elif word.lower() not in wordSet: verified = False
    return verified

def compare(comp, crit):
    """
    입력 단어와 정답 단어를 비교하여 패턴을 출력한다.

    answer와 userInput에 대하여 알파벳을 차례대로 비교하여,
    정확한 위치에 해당 문자가 있으면 "2",
    위치는 잘못되었으나, 해당 문자가 포함되면 "1"
    알파벳이 없다면 "0"으로 된 _wordLength 길이의 문자열을 반환한다.
    단, 중복되는 문자들에 대해서는 앞에서부터 차례로 "1"을 부여하고,
    정답에 포함된 문자의 개수를 초과해서 출력할 수 없다.

    Args:

    Raises:
        assertionError: 두 문자열의 길이가 __wordLength가 아닌 경우

    Returns:
        pattern: "2","1","0"으로 구성된 _wordLength 길이의 문자열
    """
    pattern = list('44444')
    crit_dic = defaultdict(int)
    for j in range(_wordLength):
        crit_dic[crit[j]] += 1
    #Find out Perfectly Matched character between two words
    for i in range(_wordLength):
        if comp[i] == crit[i]:
            pattern[i] = '2'
            crit_dic[crit[i]] -= 1
        elif comp[i] not in crit:
            pattern[i] = '0'
    for i in range(_wordLength):
        if pattern[i] == '4' and crit_dic[comp[i]]:
            pattern[i] = '1'
            crit_dic[comp[i]] -= 1
        elif pattern[i] == '4':
            pattern[i] = '0'
    return "".join(pattern)

def convert_to_pattern(int_pattern):
    digit_dictionary = {"0":"G", "1":"Y", "2":"B"}
    str_pattern = ""
    for digit in int_pattern:
        str_pattern += digit_dictionary[digit]
    return str_pattern
    
def decimal_to_ternary(dec_num):
    ter_num = ""
    while dec_num > 0:
        ter_num = str(dec_num % 3) + ter_num
        dec_num //= 3
    return ter_num.zfill(5)

def ternary_to_decimal(ter_num):
    dec_num = int(ter_num, 3)
    return dec_num

class Wordle:
    global wordSet, _wordLength
    """
    Wordle의 기본적인 기능을 담은 클래스다.

    Attributes:
        _answer: Wordle에서 사용될 정답 단어(string)
        _userInput: Wordle에서 사용자가 입력한 단어(string)
        query: 사용자가 정답을 찾을 때까지 입력한 횟수(integer)
        _wordLength: 정답 단어 및 입력 단어의 길이(integer)
        
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
        self.answer = answer_word
        self._userInput = ''
        self.query = 0
    
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
        summary = f"I guessed this {_wordLength}-letter word in {self.query} tries.\n\n"
        return summary

    @property
    def answer(self):
        return self._answer
        
    @answer.setter
    def answer(self, answer_word):
        self._answer = answer_word
    
    def isEnd(self):
        return (self.userInput == self.answer)
    
    @property
    def userInput(self):
        return self._userInput
    
    @userInput.setter
    def userInput(self, input_word):
        self._userInput = input_word
        self.query += 1

    def getQuery(self):
        return self.query

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
        self.possible_set = set()
        self.history = defaultdict(set)
    
    def initialize(self):
        self.game = Wordle()
        self.possible_set = copy.deepcopy(wordSet)
    
    def play_interactive(self):
        self.initialize()
        self.set_answer_randomly()
        while not self.game.isEnd():
            input_live = input("Guess 5 letter word: ")
            if not self.game.verify(input_live): continue
            #write more codes!
            #compare those words
        #updates self.history
        return True
    
    def play_single_word(self, answer_word, command):
        assert verify(answer_word)
        self.initialize()
        self.game.answer = answer_word
        while not self.game.isEnd():
            guess = self.evaluate_mode(command)
            if not verify(guess): return len(wordSet)
            self.userInput = guess
            guessed_result = compare(self.game.userInput, self.game.answer)
            self.converge_possible_set(guess, guessed_result)
        return self.game.getQuery()
    
    def play_with_dictionary(self, command="partition_minMax"):
        evaluation_index = [0,0] #(average, worst)
        for word in wordSet:
            query = self.play_single_word(word, command)
            evaluation_index[0] += query
            evaluation_index[1] = max(query, evaluation_index)
        evaluation_index[0] /= len(wordSet)
        return evaluation_index
    
    def play_K_repeated(self, K, command="partition_minMax"):
        X = [0, 0, 0]
        for times in range(K):
            index = self.play_with_dictionary(command)
            X[0] += index[0]; X[1] += index[1]
            X[2] = max(X[2], index[1])
        X[0] /= K; X[1] /= K
        return X
    
    def evaluate_mode(self, command=None):
        if command == "partition_minMax":
            return self._minMax()
        if command == "partition_average":
            return self._average()
        if command == "partition_variance":
            return self._variance()
        return None
    
    def _partition(self, comp_word):
        possibility = [0 for _ in range(243)] #(=3^5 for distinct pattern)
        for possible_word in self.possible_set:
            int_pattern = ternary_to_decimal(compare(possible_word, comp_word)) #'compare' function required 
            possibility[int_pattern] += 1
        return sorted(possibility)

    def _average(self):
        best_value = float('inf'); guess_word = ''
        for comp_word in wordSet:
            possibility = self._partition(comp_word)
            value = statistics.mean([x[i]*(i+1) for i in range(243)])
            if best_value > value: best_value = value; guess_word = comp_word
        return guess_word
    
    def _minMax(self):
        best_value = float('inf'); guess_word = ''
        for comp_word in wordSet:
            possibility = self._partition(comp_word)
            value = possibility[0]
            if best_value > value: best_value = value; guess_word = comp_word
        return guess_word
    
    def _variance(self):
        best_value = float('inf'); guess_word = ''
        for comp_word in wordSet:
            possibility = self._partition(comp_word)
            value = statistics.variance(possibility)
            if best_value > value: best_value = value; guess_word = comp_word
        return guess_word
    
    def converge_possible_set(self, word, result):
        candidate = set()
        for possible_word in self.possible_set:
            if compare(possible_word, word) == result: #edit here
                candidate.add(possible_word)
        self.possible_set = candidate

    def getHistory(self):
        return self.history

def profile_code():
    test = WordleGame()
    test.initialize()
    test.game.answer = "actor"
    print(test._minMax())

cProfile.run("profile_code()")