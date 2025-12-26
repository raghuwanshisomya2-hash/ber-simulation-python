# Bit Error Rate (BER) Simulation
# ECE Digital Communication Concept

import random

def generate_bits(n):
    """Generate random binary data"""
    return [random.choice([0, 1]) for _ in range(n)]

def add_noise(bits, error_probability):
    """Simulate noise by flipping bits"""
    received_bits = []
    for bit in bits:
        if random.random() < error_probability:
            received_bits.append(1 - bit)  # flip bit
        else:
            received_bits.append(bit)
    return received_bits

def calculate_ber(transmitted, received):
    """Calculate Bit Error Rate"""
    errors = sum(t != r for t, r in zip(transmitted, received))
    return errors / len(transmitted)

def main():
    num_bits = int(input("Enter number of bits to transmit: "))
    error_probability = float(input("Enter noise probability (0 to 1): "))

    transmitted_bits = generate_bits(num_bits)
    received_bits = add_noise(transmitted_bits, error_probability)

    ber = calculate_ber(transmitted_bits, received_bits)

    print("\n--- Simulation Result ---")
    print("Transmitted bits:", transmitted_bits)
    print("Received bits   :", received_bits)
    print("Bit Error Rate  :", ber)

if __name__ == "__main__":
    main()
