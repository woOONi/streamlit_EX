import streamlit as st
view = [100, 150, 30]
st.write('# 지금 streamlit 하는중')
st.write('## raw 데이터')
view
st.write('## barchart')
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview