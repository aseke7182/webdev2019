import textwrap

def wrap(string, max_width):
    a = textwrap.fill(string,max_width)
    return a

if __name__ == '__main__':