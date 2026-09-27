import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="Eagle Fast Detailing", layout="wide", page_icon="🦅")

st.title("🦅 Eagle Fast Detailing & Auto Repair")
st.caption("Shop Management System: Appointments, Billing, and Inventory")
st.markdown("---")

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
            service_type = st.selectbox("Service",
                                        ["Cut & Polish", "Interior Detailing", "Ceramic Coating", "Bodywork / Filler",
                                         "Wash"])
            date = st.date_input("Date")
            time = st.time_input("Time")
            submit_appt = st.form_submit_button("Save Appointment")

            if submit_appt:
                # Logic to save to database goes here
                st.success(f"Appointment saved for {vehicle_plate} on {date}.")

    with col2:
        st.subheader("Upcoming Appointments")
        # Placeholder data - this will be replaced by your database pull
        mock_data = pd.DataFrame({
            "Date": ["2026-09-28", "2026-09-28"],
            "Time": ["09:00 AM", "01:30 PM"],
            "Vehicle": ["CBB-1234", "WP CAB-9988"],
            "Service": ["Cut & Polish", "Interior Detailing"],
            "Status": ["Pending", "In Progress"]
        })
        st.dataframe(mock_data, use_container_width=True, hide_index=True)

# --- TAB 2: BILLING & FINANCIALS ---
with tab_billing:
    st.header("Financial Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Today's Revenue", "Rs. 0")
    col2.metric("Pending Invoices", "Rs. 0")
    col3.metric("Monthly Expenses", "Rs. 0")

    st.markdown("### Record Transaction")
    with st.form("finance_form"):
        trans_type = st.radio("Type", ["Income (Bill)", "Expense (Supplies/Parts)"], horizontal=True)
        amount = st.number_input("Amount (Rs.)", min_value=0)
        desc = st.text_input("Description / Invoice Number")
        submit_finance = st.form_submit_button("Record Transaction")

        if submit_finance:
            st.success("Transaction recorded successfully.")

# --- TAB 3: STORAGE & INVENTORY ---
with tab_inventory:
    st.header("Inventory Management")

    col1, col2 = st.columns([1, 2])
    with col1:
        with st.form("inventory_form"):
            st.subheader("Add/Update Stock")
            item_name = st.text_input("Item Name (e.g., Rubbing Compound, Clear Coat)")
            qty = st.number_input("Quantity", min_value=0)
            unit = st.selectbox("Unit", ["Liters", "Bottles", "Pads", "Pieces"])
            submit_inv = st.form_submit_button("Update Stock")

            if submit_inv:
                st.success(f"Updated {item_name} stock.")

    with col2:
        st.subheader("Current Stock Levels")
        # Placeholder data
        inv_data = pd.DataFrame({
            "Item": ["3M Rubbing Compound", "Polishing Pads", "Microfiber Cloths", "Body Filler"],
            "Quantity": [5, 12, 30, 8],
            "Unit": ["Bottles", "Pieces", "Pieces", "Tins"],
            "Status": ["Good", "Low", "Good", "Good"]
        })
        st.dataframe(inv_data, use_container_width=True, hide_index=True)