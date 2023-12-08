class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        output = {}
        for dirs in paths:
            path, *files = dirs.split()
            for file in files:
                name, content_ = file.split('(')
                content = content_[:-1]
                path_file = path+'/'+name
                output[content] = output.get(content, []) + [path_file]
        return [val for val in output.values() if len(val) > 1]