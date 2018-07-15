#A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and
#uppercase letters only.
#We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
#The rules of Goat Latin are as follows:
#    If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
#    For example, the word 'apple' becomes 'applema'.
#    If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to
#the end, then add "ma".
#    For example, the word "goat" becomes "oatgma".
#    Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
#    For example, the first word gets "a" added to the end, the second word gets "aa" added to the
#end and so on.
#Return the final sentence representing the conversion from S to Goat Latin.
#Example 1:
#Input: "I speak Goat Latin"
#Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
#Example 2:
#Input: "The quick brown fox jumped over the lazy dog"
#Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa
#azylmaaaaaaaaa ogdmaaaaaaaaaa"
#Notes:
#    S contains only uppercase, lowercase and spaces. Exactly one space between each word.
#    1 <= S.length <= 150.

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """

        vowels = set(['a','A','e', 'E', 'i', 'I', 'o','O', 'u', 'U'])

        sl = S.split(' ')

        for idx in range(len(sl)) :
            if(sl[idx][0] not in vowels) :
                sl[idx] = sl[idx][1:] + sl[idx][0]
            sl[idx] += 'ma'
            sufx = ''
            for _ in range(idx+1) :
                sufx += 'a'
            sl[idx] += sufx

        return " ".join(sl)

#
class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split()
        vowels = 'AEIOUaeiou'
        def transform(stuff):
            idx, word = stuff
            if word[0] in vowels:
                word += 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            word += 'a'*(idx+1)
            return word
        return " ".join(list(map(transform, enumerate(words))))


#
class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split()
        vowels = 'AEIOUaeiou'
        def transform(stuff):
            idx, word = stuff
            if word[0] in vowels:
                word += 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            word += 'a'*(idx+1)
            return word

