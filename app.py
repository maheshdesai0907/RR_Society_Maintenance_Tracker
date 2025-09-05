import streamlit as st
import pandas as pd
from datetime import datetime

# Step 1: Load data from Google Sheet
SHEET_ID = "1D2Se_QOfzKjLYLPC7VZ32WGTEhsjEiZcz1PPX08rmU8"
SHEET_NAME = "FY2025-2026"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

# Read sheet into DataFrame
df = pd.read_csv(URL)
df.head()

st.title("🏠 RR Dhansiri Society Maintenance Tracker (2025-2026)")

# Step 2: User Input
flat_number = st.text_input("Enter your Flat Number (Format E.g., D-908):", value = "D-")

if st.button("Submit"):
    if flat_number:
        result = df[df["Flat No."].astype(str) == flat_number]

        if not result.empty:
            # --- Extract main values ---
            one_time_payment_deadline = pd.to_datetime("10-Apr-2025")
            one_time_payment_date = pd.to_datetime(result.iloc[0]["Unnamed: 11"], errors="coerce")
            total_maintenance = result.iloc[0]["Unnamed: 6"]
            discounted_maintenance = result.iloc[0]["Unnamed: 7"]
            paid_maintenance = result.iloc[0]["Unnamed: 10"]
            previous_year_balance = result.iloc[0]["Unnamed: 5"]
            total_outstanding_balance = result.iloc[0]["Unnamed: 32"]

            first_inst_amt = result.iloc[0]["Unnamed: 46"]
            second_inst_amt = result.iloc[0]["Unnamed: 47"]
            third_inst_amt = result.iloc[0]["Unnamed: 48"]

            first_inst_paid_amt = result.iloc[0]["Unnamed: 12"]
            first_inst_paid_amt = "" if pd.isna(first_inst_paid_amt) else first_inst_paid_amt
            first_inst_late_interest = result.iloc[0]["Unnamed: 14"]
            first_inst_payment_date = pd.to_datetime(result.iloc[0]["Unnamed: 13"], errors="coerce")

            second_inst_paid_amt = result.iloc[0]["Unnamed: 16"]
            second_inst_paid_amt = "" if pd.isna(second_inst_paid_amt) else second_inst_paid_amt
            second_inst_late_interest = result.iloc[0]["Unnamed: 18"]
            second_inst_payment_date = pd.to_datetime(result.iloc[0]["Unnamed: 17"], errors="coerce")

            third_inst_paid_amt = result.iloc[0]["Unnamed: 20"]
            third_inst_paid_amt = "" if pd.isna(third_inst_paid_amt) else third_inst_paid_amt
            third_inst_late_interest = result.iloc[0]["Unnamed: 22"]
            third_inst_payment_date = pd.to_datetime(result.iloc[0]["Unnamed: 21"], errors="coerce")

            arrear1 = result.iloc[0]["Unnamed: 24"]
            arrear1 = "" if pd.isna(arrear1) else arrear1
            arrear1_date = pd.to_datetime(result.iloc[0]["Unnamed: 25"], errors="coerce")

            arrear2 = result.iloc[0]["Additional payment or \nArrears2 (₹)"]
            arrear2 = "" if pd.isna(arrear2) else arrear2
            arrear2_date = pd.to_datetime(result.iloc[0]["Paid On"], errors="coerce")

            arrear3 = result.iloc[0]["Additional payment or \nArrears3 (₹)"]
            arrear3 = "" if pd.isna(arrear3) else arrear3
            arrear3_date = pd.to_datetime(result.iloc[0]["Paid On.1"], errors="coerce")
            
            waiver = result.iloc[0]["Unnamed: 34"]
            waiver = "" if pd.isna(waiver) else waiver

            # --- Payment Method ---
            payment_method = result.iloc[0]["Payment Method"]

            if payment_method == "One Time Full Payment":
                st.success(f"✅ Flat {flat_number}")

                if one_time_payment_date <= one_time_payment_deadline:

                    st.write(f"**Total maintenance Amount (2025-2026):** ₹{total_maintenance}")
                    st.write(f"**Discounted maintenance Amount (If paid full before 10 Apr 2025):** ₹{discounted_maintenance}")
                    st.divider()
                    st.write(f"**Payment Status:** One time full payment completed for 2025-2026")
                    st.write(f"**Paid Amount:** ₹{paid_maintenance}")
                    if pd.notna(one_time_payment_date):
                        st.write(f"**Payment date:** {one_time_payment_date.strftime('%d-%b-%Y')}")
                    st.divider()
                    st.write(f"**Any previous years balance:** ₹{previous_year_balance}")
                    st.divider()
    
                    if str(arrear1).strip() != "" and pd.notna(arrear1_date):
                        st.write(f"**Previous balance / late interest (1):** ₹{arrear1} paid on {arrear1_date.strftime('%d-%b-%Y')}")
                    if str(arrear2).strip() != "" and pd.notna(arrear2_date):
                        st.write(f"**Previous balance / late interest (2):** ₹{arrear2} paid on {arrear2_date.strftime('%d-%b-%Y')}")
                    if str(arrear3).strip() != "" and pd.notna(arrear3_date):
                        st.write(f"**Previous balance / late interest (3):** ₹{arrear3} paid on {arrear3_date.strftime('%d-%b-%Y')}")
                    
                    st.divider()
                    if str(waiver).strip() != "":
                        st.write(f"**Any balance waived off (after appropriate approval):** ₹{waiver}")
    
                    st.divider()
                    st.write(f"**Total Outstanding Balance (including current year):** ₹{total_outstanding_balance}")
                    if total_outstanding_balance == "0.00":
                        st.success("**All Dues Clear**")

                else:
                    st.write(f"**Total maintenance Amount (2025-2026):** ₹{total_maintenance}")
                    st.write(f"**Discounted maintenance Amount (If paid full before 10 Apr 2025):** ₹{discounted_maintenance}")
                    st.divider()
                    st.write(f"**Payment Status:** Payment completed for 2025-2026")
                    st.write(f"Please Note: Discounted maintenance not applicable for you, because you have missed the deadline, you have to pay full maintenance amount, if not done already.")
                    st.write(f"**Paid Amount:** ₹{paid_maintenance}")
                    if pd.notna(one_time_payment_date):
                        st.write(f"**Payment date:** {one_time_payment_date.strftime('%d-%b-%Y')}")
                    st.divider()
                    st.write(f"**Any previous years balance:** ₹{previous_year_balance}")
                    st.divider()
    
                    if str(arrear1).strip() != "" and pd.notna(arrear1_date):
                        st.write(f"**Previous balance / late interest (1):** ₹{arrear1} paid on {arrear1_date.strftime('%d-%b-%Y')}")
                    if str(arrear2).strip() != "" and pd.notna(arrear2_date):
                        st.write(f"**Previous balance / late interest (2):** ₹{arrear2} paid on {arrear2_date.strftime('%d-%b-%Y')}")
                    if str(arrear3).strip() != "" and pd.notna(arrear3_date):
                        st.write(f"**Previous balance / late interest (3):** ₹{arrear3} paid on {arrear3_date.strftime('%d-%b-%Y')}")
    
                    st.divider()
                    if str(waiver).strip() != "":
                        st.write(f"**Any balance waived off (after appropriate approval):** ₹{waiver}")
                    st.divider()
                    st.write(f"**Total Outstanding Balance (including current year):** ₹{total_outstanding_balance}")
                    if total_outstanding_balance == "0.00":
                        st.success("**All Dues Clear**")

            elif payment_method == "Installment Payment":
                st.success(f"✅ Flat {flat_number}")
                st.divider()
                st.write(f"**Total maintenance Amount (2025-2026):** ₹{total_maintenance}")
                st.write(f"**Discounted maintenance Amount (If paid full before 10 Apr 2025):** ₹{discounted_maintenance}")
                st.divider()
                st.write("**Installment-wise payment amount and due dates:**")

                st.write(f"**First Installment Amount:** ₹{first_inst_amt} (pay before **April 10**)")
                st.write(f"**Second Installment Amount:** ₹{second_inst_amt} (pay before **August 10**)")
                st.write(f"**Third Installment Amount:** ₹{third_inst_amt} (pay before **December 10**)")
                st.divider()

                # First Installment
                if str(first_inst_paid_amt).strip() != "" and pd.notna(first_inst_payment_date):
                    st.write(f"**First Installment paid:** ₹{first_inst_paid_amt} on {first_inst_payment_date.strftime('%d-%b-%Y')}")
                else:
                    st.write("**First Installment not paid**")
                st.write(f"**Late charges (First Installment):** ₹{first_inst_late_interest}")
                st.divider()

                #st.markdown("<hr style='border:1px solid #4CAF50'>", unsafe_allow_html=True)

                # Second Installment
                if str(second_inst_paid_amt).strip() != "" and pd.notna(second_inst_payment_date):
                    st.write(f"**Second Installment paid:** ₹{second_inst_paid_amt} on {second_inst_payment_date.strftime('%d-%b-%Y')}")
                else:
                    st.write("**Second Installment not paid**")
                st.write(f"**Late charges (Second Installment):** ₹{second_inst_late_interest}")
                st.divider()

                #st.markdown("<hr style='border:1px solid #4CAF50'>", unsafe_allow_html=True)

                # Third Installment
                if str(third_inst_paid_amt).strip() != "" and pd.notna(third_inst_payment_date):
                    st.write(f"**Third Installment paid:** ₹{third_inst_paid_amt} on {third_inst_payment_date.strftime('%d-%b-%Y')}")
                else:
                    st.write("**Third Installment not paid**")
                st.write(f"**Late charges (Third Installment):** ₹{third_inst_late_interest}")

                st.divider()
                st.write(f"**Any previous years balance:** ₹{previous_year_balance}")
                st.divider()

                if str(arrear1).strip() != "" and pd.notna(arrear1_date):
                    st.write(f"**Previous balance / late interest (1):** ₹{arrear1} paid on {arrear1_date.strftime('%d-%b-%Y')}")
                if str(arrear2).strip() != "" and pd.notna(arrear2_date):
                    st.write(f"**Previous balance / late interest (2):** ₹{arrear2} paid on {arrear2_date.strftime('%d-%b-%Y')}")
                if str(arrear3).strip() != "" and pd.notna(arrear3_date):
                    st.write(f"**Previous balance / late interest (3):** ₹{arrear3} paid on {arrear3_date.strftime('%d-%b-%Y')}")
                st.divider()
                
                if str(waiver).strip() != "":
                    st.write(f"**Any balance waived off (after appropriate approval):** ₹{waiver}")
                st.divider()

                st.write(f"**Total Outstanding Balance (including current year):** ₹{total_outstanding_balance}")
                if total_outstanding_balance == "0.00":
                    st.success("**All Dues Clear**")

            else:
                st.write("**You have not paid maintenance amount yet for 2025-2026**")
                st.divider()

                st.write(f"**Total maintenance Amount (2025-2026):** ₹{total_maintenance}")
                st.write(f"**Discounted maintenance Amount (If paid full before 10 Apr 2025):** ₹{discounted_maintenance}")
                st.divider()

                st.write("**Installment-wise payment amount and due dates:**")
                st.write(f"**First Installment Amount:** ₹{first_inst_amt} (pay before **April 10**)")
                st.write(f"**Second Installment Amount:** ₹{second_inst_amt} (pay before **August 10**)")
                st.write(f"**Third Installment Amount:** ₹{third_inst_amt} (pay before **December 10**)")
                st.divider()

                # First Installment
                if str(first_inst_paid_amt).strip() != "" and pd.notna(first_inst_payment_date):
                    st.write(f"**First Installment paid:** ₹{first_inst_paid_amt} on {first_inst_payment_date.strftime('%d-%b-%Y')}")
                else:
                    st.write("**First Installment not paid**")
                st.write(f"**Late charges (First Installment):** ₹{first_inst_late_interest}")

                st.markdown("<hr style='border:1px solid #4CAF50'>", unsafe_allow_html=True)

                # Second Installment
                if str(second_inst_paid_amt).strip() != "" and pd.notna(second_inst_payment_date):
                    st.write(f"**Second Installment paid:** ₹{second_inst_paid_amt} on {second_inst_payment_date.strftime('%d-%b-%Y')}")
                else:
                    st.write("**Second Installment not paid**")
                st.write(f"**Late charges (Second Installment):** ₹{second_inst_late_interest}")

                st.markdown("<hr style='border:1px solid #4CAF50'>", unsafe_allow_html=True)

                # Third Installment
                if str(third_inst_paid_amt).strip() != "" and pd.notna(third_inst_payment_date):
                    st.write(f"**Third Installment paid:** ₹{third_inst_paid_amt} on {third_inst_payment_date.strftime('%d-%b-%Y')}")
                else:
                    st.write("**Third Installment not paid**")
                st.write(f"**Late charges (Third Installment):** ₹{third_inst_late_interest}")
                st.divider()
                
                st.write(f"**Any previous years balance:** ₹{previous_year_balance}")
                st.divider()

                if str(arrear1).strip() != "" and pd.notna(arrear1_date):
                    st.write(f"**Previous balance / late interest (1):** ₹{arrear1} paid on {arrear1_date.strftime('%d-%b-%Y')}")
                if str(arrear2).strip() != "" and pd.notna(arrear2_date):
                    st.write(f"**Previous balance / late interest (2):** ₹{arrear2} paid on {arrear2_date.strftime('%d-%b-%Y')}")
                if str(arrear3).strip() != "" and pd.notna(arrear3_date):
                    st.write(f"**Previous balance / late interest (3):** ₹{arrear3} paid on {arrear3_date.strftime('%d-%b-%Y')}")
                
                st.divider()
                if str(waiver).strip() != "":
                    st.write(f"**Any balance waived off (after appropriate approval):** ₹{waiver}")
                
                st.divider()
                
                st.write(f"**Total Outstanding Balance (including current year):** ₹{total_outstanding_balance}")

        else:
            st.error("❌ Please enter in the format D-XXXX (E.g: D-908, D-12011)")
