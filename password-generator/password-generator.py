# import streamlit as st
# import random
# import string
# import pyperclip



# def password_generator(length,use_digits,use_special_chars):
#     character = string.ascii_letters

#     if use_digits:
#         character += string.digits

#     if use_special_chars:
#         character+=string.punctuation
#     return ''.join(random.choice(character) for _ in range(length))

    

# st.set_page_config(page_title="Password Generator", page_icon="🔑")
# st.title("🔐 Secure Password Generator")
# st.markdown("Generate strong passwords with an instant strength check.")

# length= st.slider("Length of the password", min_value=8, max_value=32, value=16)

# use_digits = st.checkbox("Include digits")

# use_special_chars = st.checkbox("Include special characters")


# def check_strength(password):
#         if len(password) < 8:
#             color = "red"
#             level = "Weak"
#         elif len(password) < 12:
#             color = "orange"
#             level = "Medium"
#         else:
#             color = "green"
#             level = "Strong"
#         return level, color


# generated_password = ""
# color = ""
# level = ""
       
        
# if st.button("Generate Password"):

#     generated_password = password_generator(length,use_digits,use_special_chars)

#     color, level = check_strength(generated_password)

#     st.success(f"Generated password : {generated_password}")

#     st.markdown(f"**Password Strength:{color}**", unsafe_allow_html=True)

#     st.markdown("### Strength Meter")
#     strength_percentage = (len(generated_password) / 32) * 100
#     st.progress(int(strength_percentage))
    

# if st.button("📋 Copy to Clipboard"):
#         pyperclip.copy(generated_password)
#         st.success("Password copied to clipboard!")

# st.write("Made with ❤️ by [Saad Naseem](https://github.com/saad-rao)")


import streamlit as st
import random
import string
import pyperclip

# Password generation function
def password_generator(length, use_digits, use_special_chars):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Password strength checker
def check_strength(password):
    length = len(password)
    if length < 8:
        return "Weak", "#ff4d4d"  # Red
    elif length < 12:
        return "Medium", "#ffa500"  # Orange
    elif length < 16:
        return "Good", "#ffff00"  # Yellow
    else:
        return "Strong", "#00cc00"  # Green

# Streamlit UI Configuration
st.set_page_config(page_title="Password Generator", page_icon="🔑", layout="centered")

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
   
    .password-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        border: 2px solid #ddd;
        font-size: 18px;
        word-wrap: break-word;
    }
    .footer {
        text-align: center;
        color: #888;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.title("🔐 Secure Password Generator")
st.markdown("Generate strong, secure passwords with ease and check their strength instantly!")

# Input Section
with st.container():
    st.subheader("Customize Your Password")
    col1, col2 = st.columns(2)
    with col1:
        length = st.slider("Password Length", min_value=8, max_value=32, value=16, step=1)
    with col2:
        use_digits = st.checkbox("Include Digits (0-9)", value=True)
        use_special_chars = st.checkbox("Include Special Characters (!@#$%)", value=True)

# Generate Button and Output
if "generated_password" not in st.session_state:
    st.session_state.generated_password = ""

if st.button("Generate Password"):
    st.session_state.generated_password = password_generator(length, use_digits, use_special_chars)

# Display Generated Password
if st.session_state.generated_password:
    st.markdown(f"<div class='password-box'>{st.session_state.generated_password}</div>", unsafe_allow_html=True)
    
    # Strength Meter
    level, color = check_strength(st.session_state.generated_password)
    strength_percentage = min((len(st.session_state.generated_password) - 8) / 24 * 100, 100)  # Scaled to 0-100
    
    st.subheader("Password Strength")
    st.markdown(f"<progress value='{int(strength_percentage)}' max='100' style='width: 100%; height: 20px; background-color: #ddd; border-radius: 5px;'><style>progress::-webkit-progress-value {{background-color: {color}; border-radius: 5px;}}</style></progress>", unsafe_allow_html=True)
    
    # Strength Level Text Below Bar
    st.markdown(f"<p style='color: {color}; text-align: center; font-weight: bold;'>{level}</p>", unsafe_allow_html=True)
    
    # Copy Button
    if st.button("📋 Copy to Clipboard"):
        pyperclip.copy(st.session_state.generated_password)
        st.success("Password copied to clipboard!", icon="✅")

# Footer
st.markdown("<div class='footer'>Made with ❤️ by <a href='https://github.com/saad-rao' target='_blank'>Saad Naseem</a></div>", unsafe_allow_html=True) 