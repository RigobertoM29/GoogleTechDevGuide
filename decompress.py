

def decompress(string):
    if '[' in string:
        start_brack_index = string.find('[')
        start_num_index = 0
        for x in range(start_brack_index, -1, -1):
            if string[x].isdigit():
                start_num_index = x

        val = string[start_num_index:start_brack_index]
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
        string = string.replace(string[start_num_index:end_brack_index + 1],
                    float(val) * string[start_brack_index + 1:end_brack_index])  # noqa
        return decompress(str(string))
    return string


if __name__ == '__main__':
    val = decompress('2[3[a]b]')
    print(val)
