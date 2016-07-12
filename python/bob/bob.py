#
# Skeleton file for the Python "Bob" exercise.
#

def hey(what):
    sentence = what.strip()

    # Find empty or whitespace only strings
    if sentence == '':
        return 'Fine. Be that way!'

    # Find shouting, then verify that it contains letters
    if sentence == sentence.upper():
        alpha = False
        for char in sentence:
            if char.isalpha():
                alpha = True
                break
        if alpha:
            return 'Whoa, chill out!'

    # Find questions
    if sentence.endswith('?'):
        return 'Sure.'

    # Default return value
    return 'Whatever.'
