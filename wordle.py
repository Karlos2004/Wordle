from collections import defaultdict
import random
from set_word_list import wordSet
import copy
import statistics
import time
import openpyxl

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
    elif word not in wordSet: verified = False
    return verified

def compare(comp, crit):
    """
    입력 단어와 정답 단어를 비교하여 패턴을 출력한다.

    answer와 userInput에 대하여 알파벳을 차례대로 비교하여,
    정확한 위치에 해당 문자가 있으면 "B",
    위치는 잘못되었으나, 해당 문자가 포함되면 "Y"
    알파벳이 없다면 "G"으로 된 _wordLength 길이의 문자열을 반환한다.
    단, 중복되는 문자들에 대해서는 앞에서부터 차례로 "Y"을 부여하고,
    정답에 포함된 문자의 개수를 초과해서 출력할 수 없다.

    Args:

    Raises:
        assertionError: 두 문자열의 길이가 __wordLength가 아닌 경우

    Returns:
        pattern: "B","Y","G"로 구성된 문자열
    """
    pattern = list('NNNNN')
    crit_dic = defaultdict(int)
    for j in range(_wordLength):
        crit_dic[crit[j]] += 1
    for i in range(_wordLength):
        if comp[i] == crit[i]:
            pattern[i] = 'B'
            crit_dic[crit[i]] -= 1
        elif comp[i] not in crit:
            pattern[i] = 'G'
    for i in range(_wordLength):
        if pattern[i] == 'N' and crit_dic[comp[i]] > 0:
            pattern[i] = 'Y'
            crit_dic[comp[i]] -= 1
        elif pattern[i] == 'N':
            pattern[i] = 'G'
    return "".join(pattern)


def convert_pattern(int_pattern):
    """
    3진수 문자열을 패턴으로 변환하는 함수
        Args:
            int_pattern: 3진수로 표현된 _wordLength 길이의 문자열(string)
        
        Raises:

        Returns:
            str_pattern: "B", "G", "Y"로 구성된 _wordLength 길이의 문자열(string)
    """
    digit_dictionary = {"0":"G", "1":"Y", "2":"B"}
    str_pattern = ""
    for digit in int_pattern:
        str_pattern += digit_dictionary[digit]
    return str_pattern

def revert_pattern(str_pattern):
    """
    패턴을 10진수로 변환하는 함수
        Args:
            str_pattern: "B", "G", "Y"로 구성된 _wordLength 길이의 문자열(string)
        
        Raises:

        Returns:
            int_pattern: 3진수로 대응시킨 10진수(integer)
    """
    char_dictionary = {"G":"0", "Y":"1", "B":"2"}
    int_pattern = ""
    for char in str_pattern:
        int_pattern += char_dictionary[char]
    return ternary_to_decimal(int_pattern)

def decimal_to_ternary(dec_num):
    """
    10진수를 3진수로 변환하는 함수
        Args:
            dec_num: 10진수(integer)
        
        Raises:

        Returns:
            ter_num.zfill(5): 3진수(string)
    """
    ter_num = ""
    while dec_num > 0:
        ter_num = str(dec_num % 3) + ter_num
        dec_num //= 3
    return ter_num.zfill(5)

def ternary_to_decimal(ter_num):
    """
    3진수를 10진수로 변환하는 함수
        Args:
            ter_num: 3진수(string)
        
        Raises:

        Returns:
            dec_num: 10진수(integer)
    """
    dec_num = int(ter_num, 3)
    return dec_num

class Wordle:
    global wordSet, _wordLength
    """
    Wordle의 기본적인 기능을 담은 클래스다.

    Attributes:
        _answer: Wordle에서 사용될 정답 단어(string)
        _userInput: Wordle에서 사용자가 입력한 단어(string), 새로 지정될 때마다 query가 증가
        query: 사용자가 정답을 찾을 때까지 입력한 횟수(integer)
        
    Methods:
        __str__: 실제 Wordle 사이트에서 정답 공유할 때와 같은 문자열 반환
        isEnd: 게임이 종료되었을 때 True를 반환하는 함수
        getQuery: query를 반환
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

class WordleGame:
    """
    다양한 환경에서 Wordle을 플레이할 수 있다.
    여러 번 반복하여 플레이한 통계를 알려준다.
    특정 전략에 따른 플레이 결과를 확인할 수 있다.

    Attributes:
        game: Wordle 클래스(class)
        possible_set: single_game을 실행할 때, 정답단어로 가능한 후보군 단어 모음(frozenset)
        history: query에 따른 answer들의 집합 (플레이 때마다 실행한 횟수들로 정답 단어들을 분류한 defaultdict)
    
    Methods:
        initialize: game을 초기화하는 함수
        play_interactive: 실시간으로 wordle을 플레이할 수 있는 함수
        play_single_word: answer word와 mode를 지정하여 wordle을 플레이하는 함수
        play_with_dictionary: mode를 지정하여 사전의 모든 단어에 대해 wordle을 플레이하는 함수
        play_K_repeated: 사전의 모든 단어에 대해 K번 플레이하는 함수
        evaluate_mode: guess를 생성할 방법을 반환하는 함수
        _partition: 주어진 단어에 의해 가능한 패턴의 확률을 반환해주는 함수
        _average: 파티션한 확률의 평균값(기댓값)으로 단어를 추천하는 함수
        _minMax: 파티션한 최대 확률의 최솟값으로 단어를 추천하는 함수
        _variance: 파티션한 확률의 분산이 작은 단어를 추천해주는 함수
        _frequency: 각 자리별 알파벳의 등장횟수를 scoring하여 단어를 추천하는 함수
        _combination: 각 자리별 가능한 알파벳을 랜덤하게 골라서 단어를 추천하는 함수
        converge_possible_set: 정답 단어로 가능한 단어의 모임을 업데이트하는 함수

        getHistory: history를 반환하는 함수
    """
    def __init__(self):
        self.game = None
        self.possible_set = tuple()
        self.history = defaultdict(list)
        self.positions = [set('abcdefghijklmnopqrstuvwxyz') for _ in range(_wordLength)]
        self.green_by_pos = [[] for _ in range(_wordLength)]
        self.grey_by_pos = [[] for _ in range(_wordLength)]
        self.allowed_times = [set('abcdefghijklmnopqrstuvwxyz') for _ in range(4)]
        self.four_green = False

    def initialize(self):
        self.game = Wordle()
        self.possible_set = copy.deepcopy(wordSet)
        self.positions = [set('abcdefghijklmnopqrstuvwxyz') for _ in range(_wordLength)]
        self.green_by_pos = [[] for _ in range(_wordLength)]
        self.grey_by_pos = [[] for _ in range(_wordLength)]
        self.allowed_times = [set('abcdefghijklmnopqrstuvwxyz') for _ in range(4)]
    
    def play_interactive(self, answer_word):
        assert verify(answer_word)
        self.initialize()
        self.game.answer = answer_word
        while not self.game.isEnd():
            guess = input("guess here: ")
            while not verify(guess):
                guess = input("guess here: ")
            self.history[answer_word].append(guess)
            self.game.userInput = guess
            guessed_result = compare(self.game.userInput, self.game.answer)
            print(guessed_result)
            self.converge_possible_set(guess, guessed_result)
            if len(self.possible_set) < 20:
                print(self.possible_set)
        return self.game.getQuery()
    
    def play_single_word(self, answer_word, command, first_guess='', second_guess='', third_guess=''):
        assert verify(answer_word)
        self.initialize()
        self.game.answer = answer_word
        while not self.game.isEnd():
            if first_guess: 
                guess = first_guess
                first_guess = ''
            elif second_guess:
                guess = second_guess
                second_guess = ''
            elif third_guess:
                guess = third_guess
                third_guess = ''
            else:
                guess = self.evaluate_mode(command)
            self.history[answer_word].append(guess)
            if not verify(guess): return len(wordSet)
            self.game.userInput = guess
            guessed_result = compare(self.game.userInput, self.game.answer)
            if guessed_result.count('B') == 4 and len(self.possible_set) > 3: self.four_green = True
            self.converge_possible_set(guess, guessed_result, command)
        return self.game.getQuery()
    
    def play_with_dictionary(self, command="letter_frequency", first_guess='', second_guess='', third_guess=''):
        evaluation_index = [0,0] #(average, worst)
        trial = 1
        time_stamp = []; query_stamp = []
        for word in wordSet:
            start_time = time.time()
            query = self.play_single_word(word, command, first_guess, second_guess, third_guess)
            end_time = time.time()
            exec_time = end_time - start_time
            evaluation_index[0] += query
            evaluation_index[1] = max(query, evaluation_index[1])
            print(f"{trial:05}th execution succeed! // time: {round(exec_time, 3):05.3f}s // queries: {query} times")
            time_stamp.append(exec_time); query_stamp.append(query)
            trial += 1
        evaluation_index[0] /= len(wordSet)
        print(f'average execution time: {round(sum(time_stamp) / len(time_stamp), 6)} s, worst execution time: {round(max(time_stamp), 6)} s')
        print(f'average queries used: {round(sum(query_stamp) / len(query_stamp), 6)} times, worst queries used: {max(query_stamp)} times')
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
        if self.four_green: return self._four_greens()
        if command == "partition_minMax":
            return self._minMax()
        if command == "partition_average":
            return self._average()
        if command == "partition_variance":
            return self._variance()
        if command == "letter_frequency":
            return self._frequency()
        if command == "position_managing":
            return self._position_manage()
        if command == "combination":
            return self._combination()
        return None
    
    def _partition(self, comp_word):
        possibility = [0 for _ in range(243)] #(=3^5 for distinct pattern)
        for possible_word in self.possible_set:
            int_pattern = revert_pattern(compare(possible_word, comp_word)) 
            possibility[int_pattern] += 1
        return sorted(possibility)

    def _average(self):
        best_value = float('inf'); guess_word = ''
        for comp_word in self.possible_set:
            possibility = self._partition(comp_word)
            value = statistics.mean([possibility[i]*(i+1) for i in range(243)])
            if best_value > value: best_value = value; guess_word = comp_word
        return guess_word
    
    def _minMax(self):
        best_value = float('inf'); guess_word = ''
        for comp_word in self.possible_set:
            possibility = self._partition(comp_word)
            value = possibility[0]
            if best_value > value: best_value = value; guess_word = comp_word
        return guess_word
    
    def _variance(self):
        best_value = float('inf'); guess_word = ''
        for comp_word in self.possible_set:
            possibility = self._partition(comp_word)
            value = statistics.variance(possibility)
            if best_value > value: best_value = value; guess_word = comp_word
        return guess_word
    
    def _frequency(self):
        alphabet_counter = {v:[0 for _ in range(_wordLength)] for v in 'abcdefghijklmnopqurstuvwxyz'}
        for word in self.possible_set:
            for i, c in enumerate(word):
                alphabet_counter[c][i] += 1
        maxScore = float('-inf'); maxWord = ''
        for word in self.possible_set:
            curr_score = {}
            for i, c in enumerate(word):
                if c not in curr_score:
                    curr_score[c] = alphabet_counter[c][i] 
                else:
                    curr_score[c] = max(curr_score[c], alphabet_counter[c][i])
            if maxScore < sum(curr_score.values()):
                maxScore = sum(curr_score.values())
                maxWord = word
        return maxWord
    
    def _four_greens(self):
        self.four_green = False
        prev = ''; idx = 0
        for word in self.possible_set:
            if not prev: 
                prev = word
            elif prev:
                for i in range(5):
                    if prev[i] != word[i]:
                        idx = i
                        break
                break
        
        priority_letters = set()
        for word in self.possible_set:
            priority_letters.add(word[idx])

        max_score = 0
        max_word = ''

        for word in wordSet:
            curr_score = 0
            used_letter = set()
            for letter in word:
                if letter in used_letter: continue
                used_letter.add(letter)
                if letter in priority_letters:
                    curr_score += 1
            if max_score < curr_score:
                max_score = curr_score
                max_word = word
        return max_word
    
    @staticmethod
    def __filter_combination(wordList, green_by_pos, grey_by_pos, allowed_times):
        candidate = set()
        for word in wordList:
            check = True
            wordCounter = defaultdict(int)
            for letter in word:
                wordCounter[letter] += 1
            for letter in wordCounter:
                if letter not in allowed_times[wordCounter[letter]]:
                    check = False
            for i in range(_wordLength):
                if green_by_pos[i] and word[i] not in green_by_pos[i]:
                    check = False
                    break
                elif word[i] in grey_by_pos[i]:
                    check = False
                    break
            if check: 
                candidate.add(word)
        return candidate

    def __converge_combination(self, word, result):
        self.__update_green_by_pos(word, result)
        self.__update_grey_by_pos(word, result)
        self.__update_allowed_times(word, result)

        self.possible_set = WordleGame.__filter_combination(self.possible_set, self.green_by_pos, self.grey_by_pos, self.allowed_times)

    def _combination(self):

        if self.green_by_pos != [[] for _ in range(_wordLength)]:
            reuse_green_word = self.reuse_green()
            if reuse_green_word: return reuse_green_word

        return random.choice(list(self.possible_set)) if self.possible_set else ''

    def __update_green_by_pos(self, word, result):
        for i in range(_wordLength):
            if result[i] == "B":
                self.green_by_pos[i] = [word[i]]

    def __update_grey_by_pos(self, word, result):
        for i in range(_wordLength):
            if result[i] == "Y" and word[i] not in self.grey_by_pos[i]:
                self.grey_by_pos[i].append(word[i])
            elif result[i] == "G":
                if word[i] not in self.grey_by_pos[i]:
                    self.grey_by_pos[i].append(word[i])

    def __update_allowed_times(self, word, result):
        letter_result = defaultdict(list)
        for i, letter in enumerate(word):
            letter_result[letter].append(result[i])

        for letter, stats in letter_result.items():
            if 'G' in stats:
                allowed_count = len(stats) - stats.count('G')
                for i in range(allowed_count+1, 4):
                    self.allowed_times[i].discard(letter)
            elif 'Y' in stats or 'B' in stats:
                required_count = stats.count('Y') + stats.count('B')
                for i in range(required_count):
                    self.allowed_times[i].discard(letter)
        return
    
    def reuse_green(self):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        def get_maximized_word(words, priority_letters):
            max_score = 4
            max_word = ''

            for word in words:
                curr_score = 0
                for letter in word:
                    if letter in priority_letters:
                        curr_score += 1
                if max_score < curr_score:
                    max_score = curr_score
                    max_word = word
            return max_word
        
        def count_vowels(letters):
            cnt = 0
            for letter in letters:
                if letter in vowels:
                    cnt += 1
            return cnt
        
        greens_n_yellows = set(letter for letters in self.green_by_pos + self.grey_by_pos for letter in letters)
        priority_letters = self.allowed_times[1] - greens_n_yellows
        letters_for_allowed_times = priority_letters.union(vowels) if count_vowels(priority_letters) == 0 else priority_letters
        
        temp_allowed_times = [set('abcdefghijklmnopqrstuvwxyz')] + [letters_for_allowed_times for _ in range(3)]
        temp_green_by_pos = [[] for _ in range(_wordLength)]
        temp_grey_by_pos = self.green_by_pos

        temp_words = WordleGame.__filter_combination(wordSet, temp_green_by_pos, temp_grey_by_pos, temp_allowed_times)

        if temp_words:
            return get_maximized_word(temp_words, priority_letters)

        return ""

    #not working
    def _position_manage(self):
        guess = ['' for _ in range(_wordLength)]
        while ''.join(guess) not in wordSet:
            for i in range(_wordLength):
                guess[i] = random.choice(tuple(self.positions[i]))
        return ''.join(guess)
    
    #not working
    def __converge_position(self, word, result):
        for i in range(_wordLength):
            if result[i] == "B":
                self.positions[i] = set(word[i])
            elif result[i] == "Y":
                self.positions[i].discard(word[i])
            else:
                for j in range(_wordLength):
                    self.positions[j].discard(word[i])

    def converge_possible_set(self, word, result, command=""):
        if command == "position_managing":
            return self.__converge_position(word, result)
        if command == "combination":
            return self.__converge_combination(word, result)
        candidate = []
        if not self.possible_set: return
        for possible_answer in self.possible_set:
            if compare(word, possible_answer) == result:
                candidate.append(possible_answer)
        self.possible_set = tuple(candidate)

    def getHistory(self):
        return self.history
    
    def save_history_into_Excel(self):
        modes = 'ordered_four_greens'
        file_path = './history.xlsx'
        write_wb = openpyxl.load_workbook(file_path)
        write_ws = write_wb.create_sheet(title=modes)
        write_ws.append(['answer', 'query','guessed_list'])
        for answer_word in self.history:
            datas = [answer_word, len(self.history[answer_word])] + self.history[answer_word]
            write_ws.append(datas)
        write_wb.save(file_path)

"""
def profile_code():
    test = WordleGame()
    test.initialize()
    test.play_with_dictionary()

cProfile.run("profile_code()")
"""

test = WordleGame()
test.initialize()
test.play_with_dictionary(command="letter_frequency", first_guess="stare", second_guess="doing", third_guess="lucky")
test.save_history_into_Excel()
