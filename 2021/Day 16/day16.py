input_file = 'input'

with open(input_file, 'r') as f:
    data = ''.join(['{:04b}'.format(int(e, 16)) for e in list(f.read()[:-1])])


def _read_literal_group(msg):
    return msg[0] == '1', msg[1:5], msg[5:]   # Return: More groups? (True/False), Binary value, rest of the msg


def read_literal(msg):
    values = []
    more_data = True
    while more_data:
        more_data, value, msg = _read_literal_group(msg)
        values.append(value)
    return int(''.join(values), 2), msg


def read_subpackets(msg):
    length, msg = msg[0], msg[1:]
    if length == '0':
        length, msg = msg[:15], msg[15:]
        subpackets, msg = msg[:int(length, 2)], msg[int(length, 2):]
        values = []
        while len(subpackets) > 0:
            *packet, subpackets = read_packet(subpackets)
            values.append(packet)
        return values, msg
    elif length == '1':
        length, msg = int(msg[:11], 2), msg[11:]
        values = []
        while length > 0:
            *packet, msg = read_packet(msg)
            values.append(packet)
            length -= 1
        return values, msg


def read_packet(msg):
    version, type_id, msg = int(msg[:3], 2), int(msg[3:6], 2), msg[6:]
    if type_id == 4:
        return version, type_id, *read_literal(msg)
    else:
        return version, type_id, *read_subpackets(msg)


*data, _ = read_packet(data)

def sum_version(packets):
    version, type_id, content = packets
    if type_id == 4:
        return version
    else:
        return version + sum([sum_version(packet) for packet in content])


print('[DAY 16]: Part 1')
print('Sum of all version numbers: {}'.format(sum_version(data)))

