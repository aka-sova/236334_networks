import math



def print_var(var_name : str):
    print(f"\t{var_name} = {eval(var_name)}")

dist = 2 * 10**6
R = 5 * 10**6

msg_len = 512*8
ack_len = 16*8

speed = 2*(10**8)


print("\nA:")
# SNW

T_i = msg_len/R
T_ack = ack_len/R
T_p = dist / speed

print_var("T_i")
print_var("T_ack")
print_var("T_p")

RTT = T_p*2
T_out = RTT + T_ack

print_var("T_out")

print("\nB:")
# calculating throughput

T_t = T_i + T_out
print_var("T_t")
M1_avg = lambda p : 1/(1-p)


T_i_over_T_t = T_i / T_t
print_var("T_i_over_T_t")

beta_exact = RTT / T_i

throughput_SNW = lambda p : T_i_over_T_t / M1_avg(p)
throughput_SNW_2 = lambda p : (1-p) / (1 + beta_exact)


print("\nC:")

# GBN

beta_round = math.ceil(beta_exact)

print_var("beta_exact")
print_var("beta_round")

n = beta_round + 1
T_window = n * T_i
print_var("T_window")


print("\nD:")

p = 0.3

S_SWN = throughput_SNW(p)
S_SWN_2 = throughput_SNW(p)

print_var("S_SWN")
print_var("S_SWN_2")

E_k = lambda p : p / (1-p)

T_v = T_i + E_k(p) * (T_window)

print_var("T_v")

S_GBN = T_i / T_v

throughput_GBN_2 = lambda p : 1 / (1 + (p/(1-p)*(beta_round + 1)))
S_GBN_2 = throughput_GBN_2(p)

print_var("S_GBN")
print_var("S_GBN_2")