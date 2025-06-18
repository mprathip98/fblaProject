#importing library
import streamlit as sl

page_bg_img = f"""
<style>
.st-emotion-cache-bm2z3a {{
    background-image: url("https://wallpapercat.com/w/full/a/3/1/1239112-2048x1370-desktop-hd-green-forest-background-photo.jpg");
    background-size: cover;
}}

.st-emotion-cache-h4xjwg {{
    background-color: rgba(0, 0, 0, 0);
}}

.st-emotion-cache-16h9saz{{
    background-color: rgba(0, 0, 0, 0.6);
}}
</style>
"""
sl.markdown(page_bg_img, unsafe_allow_html=True)

#tab title and page title
#sl.set_page_config(page_title="Instructions")

with ((sl.container(border=True))):
    sl.title("About")
    sl.markdown("It has a total of three pages:")
    sl.markdown("- Home - All of the main content lies here")
    sl.markdown("- About - Quick facts about the project")
    sl.markdown("- Instructions - Simple instructions to use the app.")
    sl.markdown("This project also has a responsive design, adapting to any screen size")

    sl.title("Documentation")
    sl.markdown("This project uses Streamlit to cast the website and deploy it through the Streamlit Community Cloud.")
    sl.markdown("- Design Documentation: https://docs.streamlit.io/")
    sl.markdown("- Streamlit Community Cloud Deployment Documentation: https://docs.streamlit.io/deploy/streamlit-community-cloud")
    sl.write(" ")


