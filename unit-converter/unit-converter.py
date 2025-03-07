
import streamlit as st 

def convert_unit(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer": 1 / 1000,
        "kilometer_meter": 1000,
        "gram_kilogram": 1 / 1000,
        "kilogram_gram": 1000,
        "millimeter_centimeter": 1 / 10,
        "centimeter_millimeter": 10,
        "celsius_fahrenheit": lambda c: (c * 9 / 5) + 32,
        "fahrenheit_celsius": lambda f: (f - 32) * 5 / 9,
        "liter_gallon": 1 / 3.785,
        "gallon_liter": 3.785,
        "pound_kilogram": 1 / 2.20462,
        "kilogram_pound": 2.20462,
        "ounce_gram": 1 / 28.3495,
        "gram_ounce": 28.3495,
        "length_meter": 1,
        "meter_length": 1,
        "length_kilometer": 1 / 1000,
        "kilometer_length": 1000,
        "length_centimeter": 100,
        "centimeter_length": 1 / 100,
        "millimeter_micrometer": 1 / 1000,
        "micrometer_millimeter": 1000,
        "centimeter_micrometer": 1 / 100,
        "micrometer_centimeter": 100,
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return conversion(value) if callable(conversion) else value * conversion
    else:
        return "Conversion not supported"

# Streamlit UI
st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("🌎 Unit Converter")
st.markdown("### Convert between various units with ease!")

# Input section
value = st.number_input("Enter the value to convert", min_value=1.0, step=1.0)
unit_from = st.selectbox("Select the unit to convert from", 
    ["meter", "kilometer", "gram", "kilogram", "celsius", "fahrenheit",
     "liter", "gallon", "centimeter", "millimeter", "micrometer"])

unit_to = st.selectbox("Select the unit to convert to", 
    ["meter", "kilometer", "gram", "kilogram", "celsius", "fahrenheit",
     "liter", "gallon", "pound", "ounce", "centimeter", "millimeter", "micrometer"])

# Convert button
if st.button("Convert"):
    result = convert_unit(value, unit_from, unit_to)
    if isinstance(result, str):
        st.error(result)  # Show error message if conversion is not supported
    else:
        st.success(f"{value} {unit_from} is equal to {result:.2f} {unit_to}")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by saad")