def encode(string_in):
    result = ''
    index = 0
    while index < len(string_in):
        char = string_in[index]
        count = 1
        while (count + index) < len(string_in) and char == string_in[index + count]:
            count += 1

        if count > 1:
            result += str(count) + char
        else:
            result += char
        index += count
    return result

def decode(string_in):
    result = ''
    index = 0
    while index < len(string_in):
        char = string_in[index]
        if not char.isdigit():
            result += char
            index += 1
            continue

        count = 1
        while (count + index) < len(string_in) and string_in[index + count].isdigit():
            count += 1

        num = int(string_in[index:index + count])
        alpha = string_in[index + count]
        result += alpha * num
        index += (count + 1)

    return result
