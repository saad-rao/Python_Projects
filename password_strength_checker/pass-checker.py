import streamlit as st
import re

st.set_page_config(page_title="Password Checker", page_icon="🔒")

st.title("🔐Password strength checker")
st.markdown("""
## Wellcome to the password strength checker!
- This app checks the strength of your password and provides feedback on how to improve it.
            """)

password = st.text_input("Enter your password:", type="password")

feedback = []

score = 0

if password:
    if(len(password)>=8):
        score += 1
    else:
        feedback.append(" ❌Password should be at least 8 characters long.")

if re.search("[a-z]", password) and re.search("[A-Z]",password):
    score += 1 
else:
    feedback.append(" ❌Password should contain both uppercase and lowercase letters.")

if re.search("[0-9]", password):
    score += 1
else:
    feedback.append("❌Password should contain at least one digit")

if re.search("[!@#$&*]", password):
    score += 1
else:
    feedback.append("❌Password should contain at least one special character(!@#$&*)")

if score==4:
    feedback.append("✅Your password is strong!")

elif score==3:
    feedback.append("⚠️Your password is medium.")

else:
    feedback.append("❌Your password is weak.")

    if feedback:
        st.markdown("### Feedback:")
        for item in feedback:
            st.markdown(item)


    else:
      st.markdown("### Feedback:")
      st.markdown("Please enter a password to check its strength.")