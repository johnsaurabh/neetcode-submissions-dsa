class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        split_path=path.split('/')

        for directory in split_path:
            if directory not in {'.','..',''}:
                stack.append(directory)
            elif directory=='..':
                if stack:
                    stack.pop()
        return '/'+ '/'.join(stack)
        