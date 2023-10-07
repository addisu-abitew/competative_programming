class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dictionary = {}
        for path in paths:
            des = path.split()
            for txt in des[1:]:
                parts = txt.split('(')
                fileName = parts[0]
                content = parts[1][:-1]
                path = des[0]+'/'+fileName
                if content in dictionary:
                    dictionary[content].append(path)
                else:
                    dictionary[content] = [des[0]+'/'+fileName]
        # print(dictionary)
        ans = []
        for word in dictionary:
            if len(dictionary[word])>1:
                ans.append(dictionary[word])
        return ans