import sys

def parse_state(line):
    pegs = line.strip().split(',')
    state = [[] for _ in range(3)]
    for i, peg in enumerate(pegs):
        if peg.strip():
            state[i] = list(map(int, peg.strip().split()))
    return state

def encode_state(state, total_disks):
    """Generate a unique string representation of current state"""
    pos = [None] * (total_disks + 1)
    for peg_idx, peg in enumerate(state):
        for disk in peg:
            pos[disk] = 'ABC'[peg_idx]
    return ''.join(pos[1:])

def hanoi_simulation(n, from_peg, aux_peg, to_peg, current, path, states):
    """Standard recursive Tower of Hanoi simulation with state recording"""
    if n == 0:
        return
    hanoi_simulation(n - 1, from_peg, to_peg, aux_peg, current, path, states)
    disk = current[from_peg].pop()
    current[to_peg].append(disk)
    states.append(encode_state(current, len(path)))
    hanoi_simulation(n - 1, aux_peg, from_peg, to_peg, current, path, states)

def find_solution(state):
    total_disks = sum(len(peg) for peg in state)
    final_encoded = encode_state(state, total_disks)
    pegs = ['A', 'B', 'C']

    for peg in pegs:
        current = {'A': [], 'B': [], 'C': []}
        current[peg] = list(range(total_disks, 0, -1))
        current_copy = {
            'A': current['A'][:],
            'B': current['B'][:],
            'C': current['C'][:]
        }

        states = [encode_state(current_copy, total_disks)]
        hanoi_simulation(total_disks, peg, pegs[(pegs.index(peg)+1)%3], pegs[(pegs.index(peg)+2)%3], current_copy, list(range(1, total_disks+1)), states)

        if final_encoded in states:
            return peg, states.index(final_encoded)
    return "impossible", None

# Main execution
if __name__ == "__main__":
    import sys
    input_lines = sys.stdin.read().splitlines()
    num_cases = int(input_lines[0])
    for i in range(1, num_cases + 1):
        state = parse_state(input_lines[i])
        result = find_solution(state)
        if result[0] == "impossible":
            print("impossible")
        else:
            print(result[0], result[1])
