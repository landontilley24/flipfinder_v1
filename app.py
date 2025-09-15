import streamlit as st
from analyzer import analyze_item
from ebay_client import search_ebay

st.title("FlipFinder AI v1")

query = st.text_input("Enter product to analyze:")

if query:
    st.write(f"Searching eBay for: {query}...")
    results = search_ebay(query)
    analysis = analyze_item(results)
    st.write("### Analysis")
    st.write(analysis)
