from collections import Counter


def is_valid(start_packet: str, len_message: int) -> bool:
    return len(Counter(start_packet)) == len_message


def find_marker(file: str, len_message: int) -> int:
    with open(file) as f:
        signal = f.read()
    start_index = 0
    end_index = len_message
    while end_index < len(signal):
        start_of_packet = [signal[i] for i in range(start_index, end_index)]
        if is_valid(start_of_packet, len_message):
            return end_index
        start_index, end_index = start_index + 1, end_index + 1


# print('First part:', find_marker('test2.txt', 4))
print('Second part:', find_marker('test2.txt', 14))
