def mutate_string(string, position, character):
    s = list(string)
    s[position] = character
    ans = "".join(s)
    return ans

if __name__ == '__main__':