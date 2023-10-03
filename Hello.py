import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Jobs In Fusion! 👋")

    st.write(st.secrets.db_username)

    conn = st.experimental_connection("postgresql", type="sql")
    df = conn.query("SELECT * FROM jobs;", ttl="10m")
    for row in df.itertuples():
        st.write(f"{row.company}")


if __name__ == "__main__":
    run()
