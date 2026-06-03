import streamlit as st
import requests  

st.title("Vehicle Damage Detection (Client Dashboard)")

uploaded_file = st.file_uploader("Upload the file", type=["jpg", "png"])

FASTAPI_URL = "http://127.0.0.1:8000"

if uploaded_file:
    # 1. Display the image locally immediately for the user
    st.image(uploaded_file, caption="Uploaded File", use_container_width=True)
    
    # 2. Package the raw memory bytes into a standard HTML form format
    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
    
    with st.spinner("Streaming image to AI Server..."):
        try:
            # 3. Send the image over the network wire to FastAPI
            response = requests.post(FASTAPI_URL, files=files)
            
            if response.status_code == 200:
                result = response.json()
                
                if "prediction" in result:
                    st.info(f"Predicted Class: {result['prediction']}")
                else:
                    st.error(f"Server Error: {result.get('error')}")
            else:
                st.error(f"Failed to connect to AI server. Status code: {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            st.error("Could not reach the backend server. Is uvicorn running?")

