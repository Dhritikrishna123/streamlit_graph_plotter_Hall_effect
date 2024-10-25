import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# App title and creator
st.title("Voltage vs Current (V-I) Plotter")
st.write("Created by Dhritikrishna Tripathi")

# Instructions
st.markdown("### Enter Voltage and Current values:")
st.write("Enter the values as comma-separated numbers (e.g., 0.5, 1.0, 1.5)")

# User input for voltages and currents
voltages = st.text_input("Voltage values (in V):", "0.5, 1.0, 1.5, 2.0, 2.5, 3.0")
low_intensity = st.text_input("Current values for Low Intensity (in mA):", "0.44, 0.47, 0.51, 0.54, 0.57, 0.60")
medium_intensity = st.text_input("Current values for Medium Intensity (in mA):", "3.32, 5.20, 5.68, 6.08, 6.57, 7.01")
high_intensity = st.text_input("Current values for High Intensity (in mA):", "5.07, 8.72, 9.76, 10.68, 11.60, 12.55")

# Convert input strings to lists of floats
try:
    voltages = [float(v) for v in voltages.split(",")]
    low_intensity = [float(v) for v in low_intensity.split(",")]
    medium_intensity = [float(v) for v in medium_intensity.split(",")]
    high_intensity = [float(v) for v in high_intensity.split(",")]

    # Ensure that all input lists have the same length
    if len(voltages) == len(low_intensity) == len(medium_intensity) == len(high_intensity):
        # Plot the data
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(voltages, low_intensity, marker='o', linestyle='-', color='blue', label='Low Intensity')
        ax.plot(voltages, medium_intensity, marker='o', linestyle='-', color='green', label='Medium Intensity')
        ax.plot(voltages, high_intensity, marker='o', linestyle='-', color='red', label='High Intensity')

        # Add titles and labels
        ax.set_title('Voltage vs Current (V-I)', fontsize=16)
        ax.set_xlabel('Voltage (V)', fontsize=14)
        ax.set_ylabel('Current (mA)', fontsize=14)
        ax.grid(True)

        # Add a legend
        ax.legend()

        # Display the plot in the Streamlit app
        st.pyplot(fig)

        # Provide a download button for the plot
        from io import BytesIO
        buffer = BytesIO()
        fig.savefig(buffer, format='pdf')
        buffer.seek(0)

        st.download_button(
            label="Download Plot as PDF",
            data=buffer,
            file_name="voltage_current_plot.pdf",
            mime="application/pdf"
        )
    else:
        st.error("All input lists must have the same length.")
except ValueError:
    st.error("Please enter valid comma-separated numbers.")
