
#T - O(N), S - O(N)
class Solution:
    def numUniqueEmails(self, emails):
        email_set = set()
        for email in emails:
            local_name,domain_name = email.split("@")
            local_name ="".join(local_name.split('+')[0].split('.'))
            email = local_name +'@' + domain_name
            email_set.add(email)
        return len(email_set)

#T - O(N), S - O(N)
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        #local name@doamin name

        #split w/ +
        #remove dot
        #which one to remove
        #@ - wull be a special char?
        # Hashing w/ set
        aux_map = set()
        for email in emails :
            domain = email.split("@")[1]
            newLocalName = "".join(email.split("@")[0].split("+")[0].split("."))
            newEmail = ".".join( [newLocalName, domain] )
            #print(newEmail)
            if(newEmail not in aux_map) :

                aux_map.add(newEmail)
        return len(aux_map)

#Unique Email Addresses
#Every email consists of a local name and a domain name, separated by the @ sign.
#For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.
#Besides lowercase letters, these emails may contain '.'s or '+'s.
#If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)
#If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)
#It is possible to use both of these rules at the same time.
#Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails?
#
#Example 1:
#Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
#Output: 2
#Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
#
#Note:
#1 <= emails[i].length <= 100
#1 <= emails.length <= 100
#Each emails[i] contains exactly one '@' character.
