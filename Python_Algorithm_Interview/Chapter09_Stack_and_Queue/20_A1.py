# 풀이 1 - 스택 일치 여부 판별

def isValid(s: str) -> bool:
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # 스택 이용 예외 처리 및 일치 여부 판별
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or stack.pop() != table[char]:
            return False

    return len(stack) == 0
