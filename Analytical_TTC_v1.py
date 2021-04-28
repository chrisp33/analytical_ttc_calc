import streamlit as st


"""
Author: Christopher Pulliam 
# Toxicological Threshold Calculator 

### Fill in the blanks and the Analytical TTC will be returned
"""

"""
## GPS Threshold
"""
ttc = st.number_input('Input GPS threshold in mg/g', format = '%.3f')

'''## Analytical Concentration in mg/mL'''

anal_conc = st.number_input("Input Analytical Concentration", 0.0,)

"""
## Select Extraction Ratio or Extraction Percent
"""
ext_val_type = st.radio('Select', ['Extraction Ratio', 'Extraction Percent'])

if ext_val_type == 'Extraction Ratio':
	
	ext_ratio = st.number_input(f'Input {ext_val_type}', format = '%.3f', key = 1)

	st.markdown(f'## Analytical TTC based on {anal_conc} mg/mL:')
	try:
		val = ttc*ext_ratio/1000/anal_conc*100
	except ZeroDivisionError: #addresses initial conc = 0.00
		val = 0
	st.title('{:.3f} mg/mL'.format(val))


else: 
	ext_percent = st.number_input(f'Input {ext_val_type}', None, format = '%.3f', key = 2)

	
	try:
		ext_ratio = 100/ext_percent
	except ZeroDivisionError: #Eliminates the need for a real default value. 
		ext_ratio = 0
		
	st.markdown(f'## Analytical TTC based on {anal_conc} mg/mL:')

	try:
		val = ttc*ext_ratio/1000/anal_conc*100
	except ZeroDivisionError: #addresses initial conc = 0.00
		val = 0
	st.title('{:.3f} mg/mL'.format(val))



# if ext_val_type ==

"""version 1.1"""
