import sys, os

sys.path.append(os.getcwd())
from util.read import read, read_nums

entries = read(2021, 8)

def parse_entry(line):
    parts = line.split(" | ")
    signals = [set(signal) for signal in parts[0].split(" ")]
    output_values = [set(output_value) for output_value in parts[1].split(" ")]
    return [signals,output_values]

def decode_signals(signals):
    digits = [0] * 10
    for signal in signals:
        if len(signal) == 2:
            digits[1] = signal
        elif len(signal) == 3:
            digits[7] = signal
        elif len(signal) == 4:
            digits[4] = signal
        elif len(signal) == 7:
            digits[8] = signal
    fives = [signal for signal in signals if len(signal) == 5]
    for five in fives:
        if len(five - digits[1]) == 3:
            digits[3] = five
        elif len(five - digits[4]) == 3:
            digits[2] = five
        elif len(five - digits[4]) == 2:
            digits[5] = five
    sixes = [signal for signal in signals if len(signal) == 6]
    for six in sixes:
        if len(six - digits[3]) == 1:
            digits[9] = six
        elif len(six - digits[5]) == 1:
            digits[6] = six
        else:
            digits[0] = six
    return digits

def decode_entry(entry):
    parsed_entry = parse_entry(entry)
    digits = decode_signals(parsed_entry[0])
    output_values = parsed_entry[1]
    decoded_output = ""
    for output_value in output_values:
        for i in range(10):
            if output_value == digits[i]:
                decoded_output += str(i)
                break
    return int(decoded_output)

def output_values(entries):
    return sum([decode_entry(entry) for entry in entries])

print(output_values(entries))