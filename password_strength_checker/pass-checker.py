import streamlit as st
import re

# Set page config
st.set_page_config(page_title="Password Checker", page_icon="🔒")

# Title and description
st.title("🔐Password Strength Checker")
st.markdown("""
## Welcome to the Password Strength Checker!
- Enter your password to check its strength and get suggestions to improve it.
""")

# Password input
password = st.text_input("Enter your password:", type="password")

# Function to check password strength
def check_password_strength(password):
    feedback = []
    suggestions = []
    score = 0

    # Common passwords list (small for demo)
    common_passwords = ["password", "123456", "qwerty", "abc123", "letmein"]

    if not password:
        return feedback, score, suggestions

    # Check for common passwords
    if password.lower() in common_passwords:
        feedback.append("❌ Password is too common and easily guessable.")
        suggestions.append("🔧 Choose a unique password that isn't commonly used.")
        return feedback, score, suggestions

    # Check length
    if len(password) < 10:
        feedback.append("❌ Password should be at least 10 characters long.")
        suggestions.append("🔧 Add more characters to increase length.")
    elif len(password) > 100:
        feedback.append("❌ Password is too long (max 100 characters).")
        suggestions.append("🔧 Shorten the password for practicality.")
    else:
        score += min(len(password) // 4, 3)  # 1-3 points based on length

    # Check for uppercase and lowercase
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 2
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters.")
        suggestions.append("🔧 Include at least one uppercase and one lowercase letter.")

    # Check for digits
    if re.search("[0-9]", password):
        score += 2
    else:
        feedback.append("❌ Password should contain at least one digit.")
        suggestions.append("🔧 Add a number to your password.")

    # Check for special characters
    if re.search("[!@#$%^&*()_+-=]", password):
        score += 2
    else:
        feedback.append("❌ Password should contain at least one special character (!@#$%^&*).")
        suggestions.append("🔧 Include a special character like !, @, or #.")

    # Check for spaces
    if " " in password:
        feedback.append("❌ Password should not contain spaces.")
        suggestions.append("🔧 Remove any spaces from the password.")

    # Check for repetitive characters (e.g., "aaa" or "111")
    if re.search(r"(.)\1{2}", password):
        feedback.append("❌ Password contains repetitive characters (e.g., 'aaa').")
        suggestions.append("🔧 Avoid repeating the same character multiple times.")

    # Check for sequential characters (e.g., "abc", "123")
    sequential_patterns = ["abc", "123", "xyz"]
    for pattern in sequential_patterns:
        if pattern in password.lower():
            feedback.append("❌ Password contains sequential characters (e.g., 'abc', '123').")
            suggestions.append("🔧 Avoid predictable sequences like 'abc' or '123'.")
            break

    # Determine strength based on score
    if score >= 8:
        strength = "✅ Your password is **Strong**!"
    elif score >= 5:
        strength = "⚠️ Your password is **Medium**."
    else:
        strength = "❌ Your password is **Weak**."

    return feedback, score, suggestions, strength

# Check password and display results
if password:
    feedback, score, suggestions, strength = check_password_strength(password)

    # Display strength progress bar
    strength_percentage = min(score * 10, 100)  # Scale score to 0-100%
    st.progress(strength_percentage)
    st.markdown(f"**Strength Score**: {score}/10")

    # Display feedback
    st.markdown("### Feedback:")
    st.markdown(strength)  # Show strength first

    # Show detailed feedback (errors) if any
    if feedback:
        for item in feedback:
            st.markdown(item)

    # Display suggestions if password is not strong
    if score < 8 and suggestions:
        st.markdown("#### Suggestions to Improve:")
        for suggestion in suggestions:
            st.markdown(suggestion)
else:
    st.info("Please enter a password to check its strength.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 15px;">
    <p>Made With ❤ By Saad Naseem </p>
    <p>
        <a href="https://github.com/saad-rao" target="_blank" style="text-decoration: none; color:black; margin-right: 15px;">
            <i class="fab fa-github" style="font-size: 24px; vertical-align: middle; margin-right: 5px;"></i> GitHub
        </a>
        <a href="https://www.linkedin.com/in/saad-naseem-99651a2b4/" target="_blank" style="text-decoration: none; color: #0077B5;">
          <i class="fab fa-linkedin" style="font-size: 24px; vertical-align: middle; margin-right: 5px; color: #0077B5;"></i> LinkedIn
        </a>
    </p>
   
</div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" integrity="sha512-Kc323vGBEqzTmouAECnVceyQqyqdsSiqLQISBL29aUW4U/M7pSPA/gEUZQqv1cwx4OnYxTxve5UMg5GT6L4JJg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
<style>
a:hover {
    text-decoration: underline;
    opacity: 0.8;
}
</style>
""", unsafe_allow_html=True)




