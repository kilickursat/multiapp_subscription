import streamlit as st
from st_paywall import add_auth
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

# Add authentication
add_auth(required=True)

# Buy Me a Coffee link
bmac_link = "https://www.buymeacoffee.com/kursatkilic"  # Replace with your actual link

# Check if user is subscribed
if not st.session_state.user_subscribed:
    st.write("Please subscribe to access the apps.")
    st.markdown(f"[Buy me a coffee]({bmac_link}) to support these apps!")
    st.stop()

# If user is subscribed, show the app selector
st.title("Multi-App Dashboard")

# Function to load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animations for each app
lottie_borehole = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_9gRLAnPr83.json")
lottie_comprehensive = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_49rdyysj.json")
lottie_dataanalysis = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_qp1q7mct.json")
lottie_digization = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_vPnn3K.json")

# Create a sidebar for app selection
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Borehole Visualization", "Comprehensive App", "Data Analysis", "Digization"],
        icons=["graph-up", "clipboard-data", "bar-chart-line", "tablet"],
        menu_icon="cast",
        default_index=0,
    )

# Define functions for each app
def borehole_visualization():
    st.header("Borehole Visualization")
    st_lottie(lottie_borehole, height=300, key="borehole")
    st.write("This app provides borehole visualization tools.")
    st.markdown("[Go to Borehole Visualization App](https://boreholevisu-kilickursat.streamlit.app/)")
    # Add more details or embedded functionality here

def comprehensive_app():
    st.header("Comprehensive App")
    st_lottie(lottie_comprehensive, height=300, key="comprehensive")
    st.write("This is a comprehensive app with various features.")
    st.markdown("[Go to Comprehensive App](https://comprehensiveapp-kursatkilic.streamlit.app/)")
    # Add more details or embedded functionality here

def data_analysis():
    st.header("Data Analysis")
    st_lottie(lottie_dataanalysis, height=300, key="dataanalysis")
    st.write("Perform data analysis with this app.")
    st.markdown("[Go to Data Analysis App](https://dataanalysis-createdbykursat.streamlit.app/)")
    # Add more details or embedded functionality here

def digization():
    st.header("Digization")
    st_lottie(lottie_digization, height=300, key="digization")
    st.write("Digitize your data with this app.")
    st.markdown("[Go to Digization App](https://digization-kki.streamlit.app/)")
    # Add more details or embedded functionality here

# Main app logic
if selected == "Borehole Visualization":
    borehole_visualization()
elif selected == "Comprehensive App":
    comprehensive_app()
elif selected == "Data Analysis":
    data_analysis()
elif selected == "Digization":
    digization()

# Footer
st.sidebar.markdown("---")
st.sidebar.write(f"Logged in as: {st.session_state.email}")
st.sidebar.write("Subscription status: Active" if st.session_state.user_subscribed else "Subscription status: Inactive")
