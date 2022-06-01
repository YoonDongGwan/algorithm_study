def process1(w):
    if not w:
        return []
    s = list(w)
    l_bracket = 0
    r_bracket = 0
    for i in range(len(s)):
        if s[i] == '(':
            l_bracket += 1
        elif s[i] == ')':
            r_bracket += 1

        if l_bracket == r_bracket:
            break
    u = s[:i + 1]
    v = s[i+1:]

    if check_complete(u):
        return u + process1(v)
    else:
        new_s = ['(']
        new_s += process1(v)
        new_s.append(')')
        new_s += process4(u)
        return new_s

def check_complete(s):
    l_count = 0
    for i in s:
        if i == '(':
            l_count += 1
        else:
            if l_count == 0:
                return False
            l_count -= 1
    return True

def process4(u):
    new_u = u[:len(u)-1]
    new_u = new_u[1:]

    for i in range(len(new_u)):
        if new_u[i] == '(':
            new_u[i] = ')'
        elif new_u[i] == ')':
            new_u[i] = '('
    return new_u

def solution(p):
    answer = ''.join(process1(p))
    return answer

p = "()(())()"
solution(p)
