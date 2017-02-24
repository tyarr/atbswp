spam= ['apples', 'bananas', 'tofu', 'cats']
def list_thing(words):
    if len(words) == 1:
        return words[0]
    if len(words) == 2:
        return words[1]
    if len(words) == 3:
        return words[2]
    #if len(words) == 4:
    #   return words[3]
    return '{}, and {}'.format(', '.join(words[:-1]), words[-1])
