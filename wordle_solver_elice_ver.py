class WordleSolver:
    def __init__(self):
        with open('dictionary.txt', 'r') as f:
            dic_file = f.readlines()
        
        self.dic = list(map(lambda x: x.strip(), dic_file))
        self.possible_set = set(self.dic)
        self.word = "trace"
    
    def start(self):
        return self.word
        
    def guess(self, prev):
        self.converge_possible_set(self.word, prev)
        self.word = self.frequency()
        return self.word
    
    def frequency(self):
        alphabet_counter = {v:[0 for _ in range(5)] for v in 'abcdefghijklmnopqurstuvwxyz'}
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
    
    def converge_possible_set(self, word, result):
        candidate = set()
        if not self.possible_set: return
        for possible_answer in self.possible_set:
            if WordleSolver.compare(word, possible_answer) == result:
                candidate.add(possible_answer)
        self.possible_set = candidate
    
    @staticmethod
    def compare(comp, crit):
        pattern = list('NNNNN')
        crit_dic = {}
        for j in range(5):
            if crit[j] in crit_dic: 
                crit_dic[crit[j]] += 1
            else:
                crit_dic[crit[j]] = 1
        for i in range(5):
            if comp[i] == crit[i]:
                pattern[i] = 'B'
                crit_dic[crit[i]] -= 1
            elif comp[i] not in crit:
                pattern[i] = 'G'
        for i in range(5):
            if pattern[i] == 'N' and crit_dic[comp[i]] > 0:
                pattern[i] = 'Y'
                crit_dic[comp[i]] -= 1
            elif pattern[i] == 'N':
                pattern[i] = 'G'
        return "".join(pattern)

#distinct letter ver.

class WordleSolver:
    def __init__(self):
        with open('dictionary.txt', 'r') as f:
            dic_file = f.readlines()
        
        self.dic = list(map(lambda x: x.strip(), dic_file))
        self.possible_set = set(self.dic)
        self.wordList = ["lucky", "doing"]
        self.word = 'stare'
    
    def start(self):
        return self.word
        
    def guess(self, prev):
        self.converge_possible_set(self.word, prev)
        if self.wordList:
            self.word = self.wordList.pop()
            return self.word
        self.word = self.frequency()
        return self.word
    
    def frequency(self):
        alphabet_counter = {v:[0 for _ in range(5)] for v in 'abcdefghijklmnopqurstuvwxyz'}
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
    
    def converge_possible_set(self, word, result):
        candidate = set()
        if not self.possible_set: return
        for possible_answer in self.possible_set:
            if WordleSolver.compare(word, possible_answer) == result:
                candidate.add(possible_answer)
        self.possible_set = candidate
    
    @staticmethod
    def compare(comp, crit):
        pattern = list('NNNNN')
        crit_dic = {}
        for j in range(5):
            if crit[j] in crit_dic: 
                crit_dic[crit[j]] += 1
            else:
                crit_dic[crit[j]] = 1
        for i in range(5):
            if comp[i] == crit[i]:
                pattern[i] = 'B'
                crit_dic[crit[i]] -= 1
            elif comp[i] not in crit:
                pattern[i] = 'G'
        for i in range(5):
            if pattern[i] == 'N' and crit_dic[comp[i]] > 0:
                pattern[i] = 'Y'
                crit_dic[comp[i]] -= 1
            elif pattern[i] == 'N':
                pattern[i] = 'G'
        return "".join(pattern)

#Four greens version.

class WordleSolver:
    def __init__(self):
        with open('dictionary.txt', 'r') as f:
            dic_file = f.readlines()
        self.dic = list(map(lambda x: x.strip(), dic_file))
        self.possible_set = tuple(self.dic)
        self.wordList = ["lucky", "doing"]
        self.word = 'stare'
        self.four_green = False
    
    def start(self):
        return self.word
        
    def guess(self, prev):
        self.converge_possible_set(self.word, prev)
        if prev.count('B') == 4 and len(self.possible_set) > 3: self.four_green = True
        if self.wordList:
            self.word = self.wordList.pop()
            return self.word
        if self.four_green: self._four_greens()
        self.word = self.frequency()
        return self.word
    
    def frequency(self):
        alphabet_counter = {v:[0 for _ in range(5)] for v in 'abcdefghijklmnopqurstuvwxyz'}
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
    
    def converge_possible_set(self, word, result):
        candidate = []
        if not self.possible_set: return
        for possible_answer in self.possible_set:
            if WordleSolver.compare(word, possible_answer) == result:
                candidate.append(possible_answer)
        self.possible_set = tuple(candidate)
    
    @staticmethod
    def compare(comp, crit):
        pattern = list('NNNNN')
        crit_dic = {}
        for j in range(5):
            if crit[j] in crit_dic: 
                crit_dic[crit[j]] += 1
            else:
                crit_dic[crit[j]] = 1
        for i in range(5):
            if comp[i] == crit[i]:
                pattern[i] = 'B'
                crit_dic[crit[i]] -= 1
            elif comp[i] not in crit:
                pattern[i] = 'G'
        for i in range(5):
            if pattern[i] == 'N' and crit_dic[comp[i]] > 0:
                pattern[i] = 'Y'
                crit_dic[comp[i]] -= 1
            elif pattern[i] == 'N':
                pattern[i] = 'G'
        return "".join(pattern)
    
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

        for word in self.dic:
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