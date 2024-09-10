import streamlit as st

# Define the main page layout
def main_page():
    st.title("Welcome!")
    
    # Create a logo button
    if st.button("📞 Contact Us:"):
        phone_number_page()

# Define the phone number page
def phone_number_page():
    st.title("Contact Us")
    st.subheader("Phone Numbers")
    
    # Display phone numbers
    st.write("For inquiries, you can reach us at the following numbers:")
    st.write("- 📞 Customer Service: +91 9876543210")
    st.write("- 📞 Tech Support: +91 1234567890")
    st.write("- 📞 Billing: +91 1122334455")
    
    # Add a back button to return to the main page
    if st.button("🔙 Go Back"):
        main_page()

# Main entry point
if __name__ == "__main__":
    main_page()
