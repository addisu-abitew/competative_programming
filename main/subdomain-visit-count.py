class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        output = {}
        for cpdom in cpdomains:
            str_num, domain = cpdom.split()
            dom_parts = domain.split('.')
            for i in range(len(dom_parts)):
                url = '.'.join(dom_parts[i:])
                output[url] = output.get(url, 0) + int(str_num)
        
        return [str(num)+' '+url for url, num in output.items()]