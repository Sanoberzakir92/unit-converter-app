import streamlit as st

def convert_units(category, value, from_unit, to_unit):
    conversions = {
        "Length": {"Meter": 1, "Kilometer": 0.001, "Mile": 0.000621371},
        "Weight": {"Gram": 1, "Kilogram": 0.001, "Pound": 0.00220462},
        "Temperature": {
            "Celsius": lambda c: (c * 9 / 5) + 32 if to_unit == "Fahrenheit" else c + 273.15,
            "Fahrenheit": lambda f: (f - 32) * 5 / 9 if to_unit == "Celsius" else (f - 32) * 5 / 9 + 273.15,
            "Kelvin": lambda k: k - 273.15 if to_unit == "Celsius" else (k - 273.15) * 9 / 5 + 32,
        }
    }
    
    if category == "Temperature":
        return conversions[category][from_unit](value)
    else:
        return value / conversions[category][from_unit] * conversions[category][to_unit]

# Streamlit UI
st.title("⏳Unit Converter App")

category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

units = {
    "Length": ["Meter", "Kilometer", "Mile"],
    "Weight": ["Gram", "Kilogram", "Pound"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

from_unit = st.selectbox("From Unit", units[category])
to_unit = st.selectbox("To Unit", units[category])
value = st.number_input("Enter Value", value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert_units(category, value, from_unit, to_unit)
    st.success(f"Converted Value: {result:.2f} {to_unit}")
