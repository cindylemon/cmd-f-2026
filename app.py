import streamlit as st
import cv2
import mediapipe as mp

# CSS
st.markdown("""
<style>
    .stApp {
        background-color: #040c29;
        color: white;
    }
    .stButton > button {
        background-color: #e63946;
        color: white;
        border-radius: 12px;
        padding: 20px;
        font-size: 18px;
        border: none;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #c1121f;
    }
</style>
""", unsafe_allow_html=True)

# session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# ---- HOME PAGE ----
if st.session_state.page == 'home':
    st.markdown("<h1 style='text-align: center;'>🏸 Coach Alan Wu</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #aaa;'>Select a shot to practice</p>", unsafe_allow_html=True)
    
    st.write("")  # spacer
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🏸 Overhead Clear", use_container_width=True):
            st.session_state.shot = 'overhead'
            st.session_state.page = 'coaching'
            st.rerun()
    with col2:
        if st.button("💥 Smash", use_container_width=True):
            st.session_state.shot = 'smash'
            st.session_state.page = 'coaching'
            st.rerun()
    with col3:
        if st.button("🪶 Net Shot", use_container_width=True):
            st.session_state.shot = 'net'
            st.session_state.page = 'coaching'
            st.rerun()

# ---- COACHING PAGE ----
elif st.session_state.page == 'coaching':
    shot = st.session_state.shot
    st.markdown(f"<h1 style='text-align: center;'>🏸 Practicing: {shot.title()}</h1>", unsafe_allow_html=True)
    
    if st.button("← Back to Home"):
        st.session_state.page = 'home'
        st.rerun()

    feedback = {
        "elbow_angle": 170,
        "shoulder_ok": True,
        "wrist_snapped": True,
        "overall": "bad"
    }

    def draw_feedback(frame, feedback):
        h, w = frame.shape[:2]
        
        overlay = frame.copy()
        cv2.rectangle(overlay, (10, 10), (400, 200), (0, 0, 0), -1)
        cv2.addWeighted(overlay, 0.4, frame, 0.6, 0, frame)
        
        elbow_color = (0, 255, 0) if feedback['elbow_angle'] > 160 else (0, 0, 255)
        cv2.putText(frame, f"Elbow: {feedback['elbow_angle']}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, elbow_color, 2)
        
        shoulder_color = (0, 255, 0) if feedback['shoulder_ok'] else (0, 0, 255)
        cv2.putText(frame, "Shoulder: Good!" if feedback['shoulder_ok'] else "Rotate more!", (20, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, shoulder_color, 2)

        overall_color = (0, 255, 0) if feedback['overall'] == 'good' else (0, 0, 255)
        cv2.putText(frame, "Great swing!" if feedback['overall'] == 'good' else "Keep practicing!", (20, h - 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, overall_color, 3)
        
        return frame

    frame_window = st.empty()
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = draw_feedback(frame, feedback)
        frame_window.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))