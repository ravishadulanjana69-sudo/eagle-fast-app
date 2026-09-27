import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# --- CONFIGURATION ---
st.set_page_config(page_title="Eagle Fast Detailing", layout="wide", page_icon="🦅")

st.title("🦅 Eagle Fast Detailing & Auto Repair")
st.caption("Shop Management System: Appointments, Billing, and Inventory")
st.markdown("---")

# Establish connection and pull live data
conn = st.connection("gsheets", type=GSheetsConnection)
appt_data = conn.read(worksheet="Appointments", ttl=0)

# --- INITIALIZE TABS ---
tab_appt, tab_billing, tab_inventory = st.tabs([
    "📅 Appointments", 
    "💰 Billing & Financials", 
    "📦 Storage & Inventory"
])

# --- TAB 1: APPOINTMENTS ---
with tab_appt:
    st.header("Schedule & Vehicles")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        with st.form("new_appointment"):
            st.subheader("New Booking")
            customer_name = st.text_input("Customer Name")
            vehicle_plate = st.text_input("Vehicle Number Plate")
            service_type = st.selectbox("Service", ["Cut & Polish", "Interior Detailing", "Ceramic Coating", "Bodywork / Filler", "Wash"])
            date = st.date_input("Date")
            time = st.time_input("Time")
            submit_appt = st.form_submit_button("Save Appointment")
            
            if submit_appt:
                # Create a new record matching the Google Sheet columns
                new_record = pd.DataFrame([{
                    "Date": date.strftime("%Y-%m-%d"),
                    "Time": time.strftime("%I:%M %p"),
                    "Vehicle": vehicle_plate,
                    "Service": service_type,
                    "Status": "Pending",
                    "Customer Name": customer_name
                }])
                
                # Append to existing data and push back to Google Sheets
                updated_appts = pd.concat([appt_data, new_record], ignore_index=True)
                conn.update(worksheet="Appointments", data=updated_appts)
                
                st.success(f"Appointment saved for {vehicle_plate}!")
                st.rerun()

    with col2:
        st.subheader("Upcoming Appointments")
        st.dataframe(appt_data, use_container_width=True, hide_index=True)
