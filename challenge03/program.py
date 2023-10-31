# Chanwoo Ray Bae
# Programming Challenges

import re

# takes tags from the input of line series 
def extract_tags(html):
    reg_pattern = re.compile(r'</?[a-zA-Z]+>')

    return reg_pattern.findall(html)


def check_balance(tags):
    stack = []

    for tag in tags:
        if not tag.startswith('</'):
            stack.append(tag[1:])

        else: # checking if stack top matches or is empty
            if not stack or stack[-1] != tag[2:]:
                return 'Unbalanced'

            stack.pop()

    # empty stack returns Balanced as it should
    return 'Balanced' if not stack else 'Unbalanced'


def main():
    while 1:
        try:
            html = input()
        except EOFError:
            break

        tags = extract_tags(html)

        print(check_balance(tags))


if __name__ == "__main__":
    main()
