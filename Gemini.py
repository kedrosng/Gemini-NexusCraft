import streamlit as st
import pandas as pd

# Data provided
data = {
    'Capability': ['MMLU', 'CoT@32*', 'Big-Bench Hard', 'DROP', 'HellaSwag', 'GSM8K', 'maj1@32', 'MATH', 'HumanEval', 'Natural2Code'],
    'Benchmark': ['Representation of questions in 57 subjects', 'Reasoning', 'Reading comprehension (F1 Score)', 'Commonsense reasoning for everyday tasks', 'Basic arithmetic manipulations', 'Basic arithmetic manipulations', 'Python code generation', 'Challenging math problems', 'Python code generation', 'Python code generation'],
    'Higher is better': [90.0, 86.4, 83.6, 82.4, 87.8, 94.4, 92.0, 53.2, 74.4, 74.9],
    'Description': ['CoT@32*', '5-shot** (reported)', '3-shot', 'Variable shots', '10-shot*', 'maj1@32', '5-shot CoT (reported)', '4-shot', '0-shot (IT)*', '0-shot']
}
# Create a DataFrame from the data
df = pd.DataFrame(data)

# Page Title
st.title("Google Gemini")

# Introduction to Google Gemini
st.header("Introduction")
st.write("""
Google Gemini is a multimodal large language model (LLM) capable of understanding different types of information, including text, audio, images, and video. It consists of Gemini Ultra, Gemini Pro, and Gemini Nano. Announced on December 6, 2023, Google positions Gemini as a strong competitor to OpenAI's GPT-4, claiming it to be their most capable and general-purpose AI model.

Gemini Pro Availability
""")
st.write("""
Google has made Gemini Pro, a language model designed for developers, available worldwide. Developers can access Google AI Studio, a free tool enabling them to explore Gemini's capabilities and integrate it into their applications.
""")

# Additional Language Support
st.write("""
Additional Language Support
""")
st.write("""
Gemini now supports six additional languages: Hindi, Japanese, Korean, Portuguese, Chinese, and Spanish. Google plans to expand language support to more languages in early 2024.
""")

# Gemini Model Capabilities Table
st.header("Gemini Model Capabilities")
st.table(df)

# Learn More section
st.header("Learn More")
# Add a clickable link
st.markdown("""
For a deeper understanding and additional insights, check out the accompanying [blog post](https://deepmind.google/technologies/gemini/#introduction) dedicated to Google's Gemini Model. Let's embark on this exciting journey together! 🌟🔍.
""", unsafe_allow_html=True)
