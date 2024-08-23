import streamlit as st
import pandas as pd
import random
import numpy as np

df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)  # Same as st.write(df)

st.table(df)

st.dataframe(df.style.highlight_max(axis=0)) # To highlight the maximum value in each column

df = pd.DataFrame({
    "name": ["Roadmap", "Extras", "Issues"],
    "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
    "stars": [random.randint(0, 1000) for _ in range(3)],
    "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)]
})

st.dataframe(
    df,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True, use_container_width=True
)

st.metric(label="Temperature", value="30 °C", delta="1.2 °C")

col1, col2, col3 = st.columns(3)
col1.metric("溫度", "30 °C", "1.2°C")
col2.metric("風力", "9mpd", "-8%")
col3.metric("濕度", "60%", "0%")

data = {
    '姓名': '王小明',
    '年齡': 30,
    '地址': '台北市',
    '學歷': {
        '學士學位': '資訊科學',
        '碩士學位': '資訊管理',
    },
    '興趣': [
        '運動',
        '讀書',
        '旅遊',
    ],
}

st.json(data)