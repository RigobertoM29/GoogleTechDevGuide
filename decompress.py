def decompress(string: str):
    """
    The Challenge
    In this exercise, you're going to decompress a compressed string.

    Your input is a compressed string of the format number[string] and the decompressed output form should be the string written number times. For example:

    The input

    3[abc]4[ab]c

    Would be output as

    abcabcabcababababc

    Other rules
    Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa

    One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab

    Characters allowed as input include digits, small English letters and brackets [ ].

    Digits are only to represent amount of repetitions.

    Letters are just letters.

    Brackets are only part of syntax of writing repeated substring.

    Input is always valid, so no need to check its validity.
    :param string: compressed string that needs to be decompressed
    :return: decompressed string
    """
    if '['not in string:
        return string
    else:
        start_brack_index = string.find('[')
        start_num_index = 0
        for x in range(start_brack_index, -1, -1):
            if string[x].isdigit():
                start_num_index = x

        val = int(string[start_num_index:start_brack_index])
        start_brack_count = 0
        end_brack_index = 0
        for x in range(start_brack_index, len(string) - 1):
            if string[x] is '[':
                start_brack_count = start_brack_count + 1
            elif string[x] is ']':
                start_brack_count = start_brack_count - 1
            if start_brack_count == 0:
                end_brack_index = x
                break
        string = string.replace(string[start_num_index:end_brack_index + 1], val * string[start_brack_index + 1:end_brack_index])
        return decompress(string)

if __name__ == '__main__':
    val = decompress('1[abc3[c]]2[de]f')
    print(val)
