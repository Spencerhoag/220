def encode(msg, key):
    nums = ""
    for letter in msg:
        key_chr = ord(letter) + int(key)
        nums = nums + str(chr(key_chr))
    return nums


def encode_better(msg, key):
    upper_msg = msg.upper()
    final_msg = upper_msg.strip(" ")
    key_upper = key.upper()
    answer = ""
    for i in range(len(final_msg)):
        msg_val = ord(final_msg[i])
        key_val = ord(key_upper[i % len(key_upper)])
        msg_val = msg_val - 65
        key_val = key_val - 65
        sum_ = msg_val + key_val
        sum_ = sum_ % 26
        final = sum_ + 65
        final = chr(final)
        answer = answer + final
    return answer
