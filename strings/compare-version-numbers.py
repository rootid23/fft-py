#Use of map function
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        #0.1
        v1lst = version1.split('.')
        v2lst = version2.split('.')

        m,n = map(len, [v1lst, v2lst])
        tlen = min(m,n)
        last_idx = 0
        for i in range(tlen) :
            if(int(v1lst[i]) > int(v2lst[i])) : return 1
            if(int(v1lst[i]) < int(v2lst[i])) : return -1
            last_idx = i

        if(m == n) : return 0
        last_idx += 1
        if(m != n) :
            #convert to int
            nv1lst = map(int, v1lst[last_idx:])
            nv2lst = map(int,  v2lst[last_idx:])
            v1sum,v2sum = map(sum, [nv1lst, nv2lst])
            # for i in range(last_idx, len(v1lst)) :
            #     v1sum += int(v1lst[i])
            # for i in range(last_idx, len(v2lst)) :
            #     v2sum += int(v2lst[i])

            if(v1sum == v2sum) : return 0
            elif(v1sum > v2sum) : return 1
        return -1

#Compare two version numbers version1 and version2.
#If version1 > version2 return 1, if version1 < version2 return -1, otherwise
#return 0.
#You may assume that the version strings are non-empty and contain only digits
#and the . character.
#The . character does not represent a decimal point and is used to separate
#number sequences.
#For instance, 2.5 is not "two and a half" or "half way to version three", it
#is the fifth second-level revision of the second first-level revision.
#Here is an example of version numbers ordering:
#0.1 < 1.1 < 1.2 < 13.37

