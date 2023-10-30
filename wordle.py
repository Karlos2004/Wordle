from collections import defaultdict

class Wordle:
    """
    Wordle을 구현하였다.

    Attributes:
        answer: Wordle에서 사용될 정답 단어(string)
        userInput: Wordle에서 사용자가 입력한 단어(string)
        query: 사용자가 정답을 찾을 때까지 소모된 횟수(integer)
        __wordLength: 정답 단어 및 입력 단어의 길이(integer)
        wordList: 사전에 등재된 단어 모음집(set)
        history: 퍼즐을 푸는 동안 query를 기록(defaultdict: int -> int)

    Methods:
        __str__: 실제 Wordle 사이트에서 정답 공유할 때와 같은 문자열 반환
        verify: 단어가 Wordle의 조건을 만족하는지 확인
        setAnswer: 정답 단어를 입력하는 함수
        getAnswer: 정답 단어를 불러오는 함수
        compare: 입력 단어와 정답 단어를 비교하여 올바른 형태의 패턴을 출력하는 함수
        setInput: 입력 단어를 저장하는 함수
        getInput: 입력 단어를 불러오는 함수
    """
    def __init__(self):
        self.answer = ''
        self.userInput = ''
        self.query = 0
        self.__wordLength = 5
        self.wordList = set()
        self.history = defaultdict(int)
    
    def __str__(self):
        return None
    
    def verify(word):
        return True
    
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
        return None
    
    def setInput(self):
        pass

    def getInput(self):
        return self.userInput
    
    def repeat(self, forAll=True):
        return False