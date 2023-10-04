import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Jobs In Fusion! 👋")

    conn = st.experimental_connection("jobs_db", type="sql")
    print(conn)
    df = conn.query("SELECT * FROM fusion_job;", ttl="10m")
    for row in df.itertuples():
        st.write(f"{row}")


if __name__ == "__main__":
    run()
