import os
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Directory to save graphs
save_dir = os.path.join(os.getcwd(), 'saved_graphs')
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

st.title('Hall Voltage Graph Plotter')
st.write("Enter comma-separated values for I_x, V_h for I_x, B_z, and V_h for B_z.")

# Input fields
ix_input = st.text_input('Enter I_x values (in A, comma-separated)', '0.1, 0.2, 0.3')
vh_input1 = st.text_input('Enter V_h values for I_x (in mV, comma-separated)', '1.0, 2.0, 3.0')
bz_input = st.text_input('Enter B_z values (in Wb/cm², comma-separated)', '0.1, 0.2, 0.3')
vh_input2 = st.text_input('Enter V_h values for B_z (in mV, comma-separated)', '1.0, 2.0, 3.0')

# Process inputs when the button is clicked
if st.button('Plot and Save Graphs'):
    try:
        # Convert inputs to numpy arrays
        ix_values = np.array([float(x) for x in ix_input.split(',')])
        vh_values1 = np.array([float(x) for x in vh_input1.split(',')])
        bz_values = np.array([float(x) for x in bz_input.split(',')])
        vh_values2 = np.array([float(x) for x in vh_input2.split(',')])

        # Validate input lengths
        if len(ix_values) != len(vh_values1) or len(bz_values) != len(vh_values2):
            st.error("Input arrays must have the same length.")
        else:
            # Create plots
            fig, axs = plt.subplots(2, 1, figsize=(8, 10))

            # V_h vs I_x
            axs[0].plot(ix_values, vh_values1, marker='o', linestyle='-', color='blue')
            axs[0].set_title(r'Hall Voltage ($V_h$) vs Current ($I_x$)')
            axs[0].set_xlabel(r'Current ($I_x$) in A')
            axs[0].set_ylabel(r'Hall Voltage ($V_h$) in mV')
            axs[0].grid(True)

            # V_h vs B_z
            axs[1].plot(bz_values, vh_values2, marker='o', linestyle='-', color='green')
            axs[1].set_title(r'Hall Voltage ($V_h$) vs Magnetic Field ($B_z$)')
            axs[1].set_xlabel(r'Magnetic Field ($B_z$) in Wb/cm²')
            axs[1].set_ylabel(r'Hall Voltage ($V_h$) in mV')
            axs[1].grid(True)

            # Save the figure as a PDF
            pdf_file_path = os.path.join(save_dir, 'Hall_Voltage_Graphs.pdf')
            fig.tight_layout()
            plt.savefig(pdf_file_path)
            st.pyplot(fig)

            st.success(f"Graphs saved to {pdf_file_path}")
            st.write(f"[Download the PDF](./saved_graphs/Hall_Voltage_Graphs.pdf)")
    except ValueError as e:
        st.error(f"Please enter valid numbers: {e}")

st.write("Created by Dhritikrishna Tripathi")
