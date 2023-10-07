class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dictionary = {}
        for cpdomain in cpdomains:
            num, domain = cpdomain.split()
            num = int(num)
            splited = domain.split('.')
            for i in range(len(splited)-1, -1, -1):
                connected = '.'.join(splited[i:])
                if connected in dictionary:
                    dictionary[connected] += num
                else:
                    dictionary[connected] = num
        # print(dictionary)
        ans  = []
        for site in dictionary:
            ans.append(str(dictionary[site]) + ' ' + site)
        return ans