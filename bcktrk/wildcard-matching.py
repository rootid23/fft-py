#For example if the pattern is 'ab*cd*e?*gh':
#    Turn that into ['ab', 'cd', 'e.', 'gh'] (turn ? into . and split on *).
#    Check that the start of the string matches 'ab' (and chop it off the string).
#    Check that the end of the string matches 'gh' (and chop it off the string).
#    Check that 'cd' and 'e.' are matched somewhere in the string in that order. Just be greedy, always use the first occurrence.
#
def isMatch(self, s, p):
    parts = p.replace('?', '.').split('*')
    if len(parts) == 1:
      return bool(re.match(parts[0] + '$', s))
    if not re.match(parts[0], s):
      return False
    s = s[len(parts.pop(0)):]
    if not re.search(parts[-1] + '$', s):
      return False

    s = s[:len(s) - len(parts.pop())]

    for part in parts:
      m = re.search(part, s)
    if not m:
      return False
    s = s[m.end():]
      return True

#The difference is that: the * in this problem can match any sequence independently, while the * in Regex Matching would only match duplicates, if any, of the character prior to it.

#The demo test case isMatch("aa", "*") for this problem and isMatch("aa", "a*") for Regex Matching problem could be the best effort to distinguish them for now. isMatch("aab", "c*a*b") → false for this problem was a bit confusing to me in the beginning. I think adding a test case such as isMatch("adcab", "*a*b") → true might be helpful.


class Solution(object):
    def isMatch(self, s, p):
        m, n = map(len, [s,p])

        if(m == 0 or n == 0) :
            return s == p or p == '*'

        i = j = 0
        si = sj = -1
        while True:
            if i == m and j == n :
                return True
            #handle *
            elif j != n and p[j] == '*' :
                while j < n and p[j] == '*' :
                    j += 1
                if j == n :
                    return True
                sj = j
                si = i
            #Handle ? and *
            elif i == m or j == n or p[j] not in ['*', '?'] and s[i] != p[j] :
                if sj == -1 or i == m:
                    return False
                si += 1
                i = si
                j = sj
            else :
                i += 1
                j += 1






public class Solution {
    public boolean isMatch(String s, String p) {
        return helper(s.toCharArray(), p.toCharArray(), 0, 0, 0, -1);
    }

    private boolean helper(char[] s, char[] p, int i, int j, int lastS, int lastP) {
        if(i == s.length && j == p.length) return true;
        if(j < p.length) {
            if(i == s.length)
                return p[j] == '*' ? helper(s, p, i, j + 1, lastS, lastP) : false;
            if(p[j] == '?' || s[i] == p[j])
                return helper(s, p, i + 1, j + 1, lastS, lastP);
            if(p[j] == '*')
                return helper(s, p, i, j + 1, i, j);
        }
        if(lastP != -1) return helper(s, p, lastS + 1, lastP, lastS + 1, lastP);
        return false;
    }
}


bool isMatch(const char *s, const char *p) {
        char cs = *s;
        char cp = *p;
        if(cp == '\0') {
            return cs == cp;
        } else if (cp == '?') {
            if (cs == '\0') return false;
            return isMatch(s + 1,p + 1);
        } else if (cp == '*') {
            const char *st = s;
            for(; *st != '\0'; ++st) {
                if (isMatch(st, p+1)) return true;
            }
            return isMatch(st,p+1);
        } else if (cp != cs)
            return false;
        return isMatch(s + 1,p + 1);
    }



## back
def isMatch(self, s, p):
    m = len(s)
    n = len(p)

    if n == 0 and m == 0:
        return True
    if n == 0 and m != 0:
        return False
    if p.count('*') == len(p):
        return True
    if len(p) - p.count('*') > m:
        return False

    x = y = 0
    lastx = 0
    lasty = -1
    while x < m:
        if y < n and (s[x] == p[y] or p[y] == '?'):
            x += 1
            y += 1
        elif y < n and p[y] == '*':
            lastx = x
            lasty = y
            y += 1
        elif lasty >= 0:
            lastx += 1
            x = lastx
            y = lasty
        else:
            return False

    return p[y:].count('*') == len(p[y:])

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == "" or s == "":
            return p == s or p == '*'
        i, j = 0, 0
        si, sj = -1, -1
        while True:
            if i == len(s) and j == len(p):
                return True
            elif j != len(p) and p[j] == '*':
                while j < len(p) and p[j] == '*':
                    j += 1
                if j == len(p):
                    return True
                sj = j
                si = i
            elif i == len(s) or j == len(p) or p[j] not in ['*', '?'] and s[i] != p[j]:
                if sj == -1 or i == len(s):
                    return False
                si += 1
                i = si
                j = sj
            else:
                i += 1
                j += 1

