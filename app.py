import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# Set page configuration
st.set_page_config(page_title="Project CYBERNETS", layout="wide")

# Title and Introduction
st.title("Project CYBERNETS: AI-Driven Cybersecurity")
st.markdown("""
Welcome to **Project CYBERNETS**, an AI-powered cybersecurity framework that redefines digital defense. From intent detection to dynamic, adaptive protection, explore how this system stops threats before they strike. Interact with the layers of defense below to understand how CyberNets creates a self-learning, unbreakable security ecosystem.
""")

# Sidebar for Navigation
st.sidebar.header("Explore CyberNets")
section = st.sidebar.radio("Select a Section", [
    "Overview",
    "Intent Detection",
    "Deception-Based Defense",
    "Dynamic Firewalls",
    "Real-Time Threat Mapping",
    "Simulate Threat Detection"
])

# Overview Section
if section == "Overview":
    st.header("Overview of Project CYBERNETS")
    st.markdown("""
    CyberNets is a next-generation cybersecurity system that combines:
    - **Behavioral Analytics & Intent Detection**: Identifies threats by analyzing user behavior in real-time.
    - **Deception-Based Defenses**: Misleads attackers with honeypots and recursive traps.
    - **Dynamic Firewalls**: Deploys adaptive, morphing barriers tailored to evolving threats.
    - **Real-Time Threat Mapping**: Visualizes and tracks threats for instant response.

    Use the sidebar to dive into each component and see how CyberNets creates a seamless, autonomous defense system.
    """)
    st.image("https://via.placeholder.com/800x400.png?text=CyberNets+Overview", caption="CyberNets: A Self-Defending Ecosystem")

# Intent Detection Section
elif section == "Intent Detection":
    st.header("Intent Detection: Stopping Threats at the Source")
    st.markdown("""
    CyberNets uses AI-driven behavioral analytics to distinguish humans from bots by analyzing:
    - Keystroke patterns
    - Cursor movements
    - Behavioral deviations

    Try adjusting the sensitivity of the intent detection model below to see how it impacts detection accuracy.
    """)

    # Interactive Slider for Sensitivity
    sensitivity = st.slider("Intent Detection Sensitivity", 0.0, 1.0, 0.5, 0.01)
    st.write(f"Detection Sensitivity: {sensitivity:.2f}")
    
    # Simulate Detection Accuracy
    human_accuracy = 0.95 - (sensitivity * 0.1)  # Higher sensitivity may increase false positives
    bot_accuracy = 0.8 + (sensitivity * 0.15)    # Higher sensitivity improves bot detection
    st.write(f"Human Detection Accuracy: {human_accuracy:.2%}")
    st.write(f"Bot Detection Accuracy: {bot_accuracy:.2%}")

    # Bar Chart for Detection Accuracy
    data = pd.DataFrame({
        "Category": ["Human Detection", "Bot Detection"],
        "Accuracy": [human_accuracy, bot_accuracy]
    })
    fig = px.bar(data, x="Category", y="Accuracy", title="Detection Accuracy by Sensitivity",
                 color="Category", range_y=[0, 1])
    st.plotly_chart(fig)

# Deception-Based Defense Section
elif section == "Deception-Based Defense":
    st.header("Deception-Based Defense: Trapping Attackers")
    st.markdown("""
    CyberNets deploys honeypots, recursive trap paths, and false environments to mislead attackers. These traps waste attackers' resources and provide valuable forensic data.
    
    Simulate an attacker entering a honeypot below and see how long they are trapped.
    """)

    # Simulate Honeypot Trap
    if st.button("Deploy Honeypot"):
        trap_time = random.randint(5, 60)  # Random trap time in minutes
        st.success(f"Attacker trapped in honeypot for {trap_time} minutes!")
        st.markdown("The attacker is redirected through recursive trap paths, consuming their resources.")

    # Pie Chart for Trap Effectiveness
    trap_data = pd.DataFrame({
        "Trap Type": ["Honeypot", "Recursive Path", "False Environment"],
        "Effectiveness": [40, 35, 25]
    })
    fig = px.pie(trap_data, names="Trap Type", values="Effectiveness", title="Deception Trap Effectiveness")
    st.plotly_chart(fig)

# Dynamic Firewalls Section
elif section == "Dynamic Firewalls":
    st.header("Dynamic Firewalls: Morphing Defenses")
    st.markdown("""
    Unlike static firewalls, CyberNets' firewalls evolve based on the organization's threat profile. Adjust the adaptation speed to see how it impacts firewall performance.
    """)

    # Slider for Firewall Adaptation Speed
    adaptation_speed = st.slider("Firewall Adaptation Speed (updates/hour)", 1, 10, 5)
    st.write(f"Firewall updates {adaptation_speed} times per hour.")

    # Simulate Firewall Performance
    performance = 0.7 + (adaptation_speed * 0.03)  # Faster adaptation improves performance
    st.write(f"Firewall Effectiveness: {performance:.2%}")

    # Line Chart for Firewall Performance Over Time
    time = np.arange(0, 24, 1)  # 24 hours
    effectiveness = [min(0.7 + (adaptation_speed * 0.03 * t / 24), 0.95) for t in time]
    firewall_data = pd.DataFrame({"Hour": time, "Effectiveness": effectiveness})
    fig = px.line(firewall_data, x="Hour", y="Effectiveness", title="Firewall Effectiveness Over Time",
                  range_y=[0, 1])
    st.plotly_chart(fig)

# Real-Time Threat Mapping Section
elif section == "Real-Time Threat Mapping":
    st.header("Real-Time Threat Mapping")
    st.markdown("""
    CyberNets visualizes threats in real-time, allowing organizations to track and respond instantly. Below is a simulated threat map showing attack origins.
    """)

    # Simulate Threat Data
    threats = pd.DataFrame({
        "Country": ["USA", "China", "Russia", "Brazil", "India"],
        "Attacks": [random.randint(10, 100) for _ in range(5)],
        "Latitude": [37.0902, 35.8617, 61.5240, -14.2350, 20.5937],
        "Longitude": [-95.7129, 104.1954, 105.3188, -51.9253, 78.9629]
    })

    # World Map of Threats
    fig = px.scatter_geo(threats, lat="Latitude", lon="Longitude", size="Attacks",
                         hover_name="Country", title="Global Threat Map",
                         projection="natural earth")
    st.plotly_chart(fig)

# Simulate Threat Detection Section
elif section == "Simulate Threat Detection":
    st.header("Simulate Threat Detection")
    st.markdown("""
    Test CyberNets' threat detection capabilities by simulating an attack. Choose the attack type and see how CyberNets responds.
    """)

    # Attack Type Selection
    attack_type = st.selectbox("Select Attack Type", ["Phishing", "Malware", "DDoS", "Brute Force"])
    
    if st.button("Simulate Attack"):
        # Simulate Response
        response_time = random.uniform(0.1, 2.0)  # Response time in seconds
        if attack_type == "Phishing":
            response = f"CyberNets detected phishing attempt via behavioral deviation. Session terminated in {response_time:.2f} seconds."
        elif attack_type == "Malware":
            response = f"CyberNets isolated malware in sandboxed environment. Threat neutralized in {response_time:.2f} seconds."
        elif attack_type == "DDoS":
            response = f"CyberNets redirected DDoS traffic to honeypot. Attack mitigated in {response_time:.2f} seconds."
        else:
            response = f"CyberNets blocked brute force attempt with dynamic firewall. Access denied in {response_time:.2f} seconds."
        st.success(response)

        # Plot Response Time
        response_data = pd.DataFrame({
            "Attack Type": [attack_type],
            "Response Time (s)": [response_time]
        })
        fig = px.bar(response_data, x="Attack Type", y="Response Time (s)",
                     title="Threat Detection Response Time")
        st.plotly_chart(fig)

# Footer
st.markdown("---")
st.markdown("""
**Project CYBERNETS** is redefining cybersecurity. Can it become the immune system of our digital world? Share your ideas to strengthen this framework at [x.ai](https://x.ai).
""")