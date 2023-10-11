import random
import time


def murphys_law_complex_hacking_simulation(duration_in_seconds):
    # Define a list of 100 complex hacking attack scenarios with associated probabilities

    hacking_scenarios = [
        # Scenario 1: Advanced Persistent Threat (APT)
        {
            "name": "Advanced Persistent Threat (APT)",
            "probability": 0.05,
            "description": "A highly sophisticated, long-term intrusion by skilled hackers who stealthily compromise systems over time."
        },

        # Scenario 2: Zero-Day Exploit Chain
        {
            "name": "Zero-Day Exploit Chain",
            "probability": 0.1,
            "description": "A chain of zero-day vulnerabilities used to infiltrate and compromise secure systems."
        },

        # Scenario 3: Nation-State Sponsored Attack
        {
            "name": "Nation-State Sponsored Attack",
            "probability": 0.03,
            "description": "An attack orchestrated and funded by a nation-state with advanced cyber capabilities."
        },

        # Scenario 4: AI-Enhanced Social Engineering
        {
            "name": "AI-Enhanced Social Engineering",
            "probability": 0.07,
            "description": "Social engineering attacks enhanced with AI-driven impersonation and manipulation tactics."
        },

        # Scenario 5: Blockchain 51% Attack
        {
            "name": "Blockchain 51% Attack",
            "probability": 0.05,
            "description": "A scenario where an attacker controls over 51% of a blockchain network's computing power."
        },

        # Scenario 6: Quantum Cryptography Breakthrough
        {
            "name": "Quantum Cryptography Breakthrough",
            "probability": 0.02,
            "description": "A breakthrough in quantum computing that threatens existing cryptographic systems."
        },

        # Scenario 7: IoT Botnet Takeover
        {
            "name": "IoT Botnet Takeover",
            "probability": 0.08,
            "description": "A scenario in which a massive botnet takes control of vulnerable IoT devices."
        },

        # Scenario 8: Mainframe Ransomware
        {
            "name": "Mainframe Ransomware",
            "probability": 0.1,
            "description": "A ransomware attack targeting mainframe computer systems, causing widespread disruption."
        },

        # Scenario 9: Smart City Infrastructure Hijacking
        {
            "name": "Smart City Infrastructure Hijacking",
            "probability": 0.04,
            "description": "An attack on smart city infrastructure, leading to loss of control over critical services."
        },

        # Scenario 10: Deep Learning Malware
        {
            "name": "Deep Learning Malware",
            "probability": 0.06,
            "description": "Malware that employs deep learning techniques to evolve and adapt to defenses."
        },

        # Scenario 11: Satellite Communication Breach
        {
            "name": "Satellite Communication Breach",
            "probability": 0.05,
            "description": "A breach of satellite communication systems, potentially impacting global connectivity."
        },

        # Add more complex scenarios here
        # ...

    ]

    # Simulate Murphy's Law for the specified duration
    start_time = time.time()
    while time.time() - start_time < duration_in_seconds:
        hacking_event = random.choices(hacking_scenarios, [event["probability"] for event in hacking_scenarios])[0]
        if random.random() < hacking_event["probability"]:
            print("------------------------------------------------------------------")
            print(f"Murphy's Law: Complex Hacking Attack - {hacking_event['name']}")
            print("------------------------------------------------------------------")
            print(f"Description: {hacking_event['description']}\n")
            time.sleep(2)  # Pause for 2 seconds before the next event


if __name__ == "__main__":
    simulation_duration = 600  # Duration of the simulation in seconds (10 minutes)
    print(f"Murphy's Law Complex Hacking Simulation for {simulation_duration} seconds:")
    murphys_law_complex_hacking_simulation(simulation_duration)
