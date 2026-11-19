import sys
from html.parser import HTMLParser

class TagChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void_tags = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.void_tags:
            self.stack.append((tag.lower(), self.getpos()))

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in self.void_tags:
            return
        if not self.stack:
            print(f"Extra closing tag </{tag}> at line {self.getpos()[0]}")
            return
        last_tag, pos = self.stack[-1]
        if last_tag == tag:
            self.stack.pop()
        else:
            # find if tag in stack
            found = False
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    found = True
                    # pop everything above it
                    while len(self.stack) > i:
                        unclosed, u_pos = self.stack.pop()
                        if unclosed != tag:
                            print(f"Unclosed <{unclosed}> from line {u_pos[0]}")
                    break
            if not found:
                print(f"Mismatched closing tag </{tag}> at line {self.getpos()[0]}, expected </{last_tag}> from line {pos[0]}")

if __name__ == '__main__':
    with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    checker = TagChecker()
    checker.feed(content)
    print("Unclosed tags remaining:", len(checker.stack))
    for t, pos in checker.stack[-10:]:
        print(f"Unclosed <{t}> from line {pos[0]}")
