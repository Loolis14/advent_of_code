from collections import deque
from functools import lru_cache


def second_part(file: str) -> int:
    """Top Down avec memoization"""
    devices_connections = {}
    with open(file) as f:
        for line in f:
            device, connection = line.split(":")
            connection = connection.split()
            devices_connections[device] = connection
    stack = [("svr", ["svr"])]
    path_possible = 0
    while stack:
        current_device, path = stack.pop()
        if current_device == "out":
            if "dac" in path and "fft" in path:
                path_possible += 1
            continue
        if current_device in devices_connections.keys():
            for connection in devices_connections[current_device]:
                if connection in path:
                    continue
                new_path = path + [connection]
                stack.append((connection, new_path))
    return path_possible


def recursive_memoization(file) -> int:
    devices_connections = {}
    with open(file) as f:
        for line in f:
            device, connection = line.split(":")
            connection = connection.split()
            devices_connections[device] = connection

    @lru_cache(maxsize=None)
    def count_paths(current_device: str, has_dac: bool, has_fft: bool) -> int:
        has_dac = has_dac or (current_device == "dac")
        has_fft = has_fft or (current_device == "fft")

        if current_device == "out":
            return 1 if (has_dac and has_fft) else 0

        if current_device not in devices_connections:
            return 0

        total_paths = 0
        for neighbor in devices_connections[current_device]:
            total_paths += count_paths(neighbor, has_dac, has_fft)

        return total_paths

    return count_paths("svr", False, False)


def first_part(file) -> int:
    devices_connections = {}
    with open(file) as f:
        for line in f:
            device, connection = line.split(":")
            connection = connection.split()
            devices_connections[device] = connection
    stack = deque(["you"])
    path_possible = 0
    while stack:
        current_device = stack.popleft()
        if current_device == "out":
            path_possible += 1
            continue
        if current_device in devices_connections.keys():
            for connection in devices_connections[current_device]:
                stack.append(connection)
    return path_possible


# print('First part result:', first_part('test2.txt'))
# print('Second part result:', second_part('test1.txt'))
print('Second part result:', recursive_memoization('test2.txt'))
