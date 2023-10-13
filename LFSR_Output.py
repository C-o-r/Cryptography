degree = 10
coefficients = [0,1,0,0,1,1,0,1,1,0]
initial_state = [1,0,1,0,1,0,0,1,1,0]
lfsr_output = []
for _ in range(20):
    lfsr_output.append(initial_state[-1])
    feedback_bit = sum(coeff * state for coeff, state in zip(coefficients, initial_state)) % 2
    initial_state = [feedback_bit] + initial_state[:-1]
print("First 20 bits of LFSR Output:", ''.join(map(str, lfsr_output)))