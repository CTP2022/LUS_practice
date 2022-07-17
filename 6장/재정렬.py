class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        for log in logs:
            log = log.split()
            if log[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key=lambda x: (x[1:], x[0]))
        for i in range(len(digits)):
            digits[i] = " ".join(digits[i])
        for i in range(len(letters)):
            letters[i] = " ".join(letters[i])
        return letters + digits