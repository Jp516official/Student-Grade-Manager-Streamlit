import streamlit as st #type:ignore

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Grade Calculator",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ==================================================
# SESSION STATE
# ==================================================

if "grade" not in st.session_state:
    st.session_state.grade = None

if "mark" not in st.session_state:
    st.session_state.mark = None

if "message" not in st.session_state:
    st.session_state.message = None


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>

    /* Main application background */
    .stApp {
        background: linear-gradient(
            135deg,
            #f8fafc 0%,
            #eef2ff 100%
        );
    }

    /* Main content width */
    .block-container {
        max-width: 750px;
        padding-top: 2.5rem;
        padding-bottom: 2rem;
    }

    /* Header */
    .app-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #111827;
        margin-bottom: 5px;
    }

    .app-subtitle {
        text-align: center;
        font-size: 17px;
        color: #6b7280;
        margin-bottom: 30px;
    }

    /* Section titles */
    .section-title {
        font-size: 22px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 15px;
    }

    /* Result title */
    .result-title {
        text-align: center;
        font-size: 20px;
        font-weight: 700;
        color: #6b7280;
        margin-bottom: 5px;
    }

    /* Large grade */
    .grade-display {
        text-align: center;
        font-size: 90px;
        font-weight: 900;
        line-height: 1;
        margin: 10px 0;
    }

    /* Mark display */
    .mark-display {
        text-align: center;
        font-size: 20px;
        color: #374151;
        margin-bottom: 10px;
    }

    /* Message */
    .message-display {
        text-align: center;
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 10px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #9ca3af;
        font-size: 14px;
        margin-top: 30px;
    }

    /* Button */
    div.stButton > button {
        width: 100%;
        height: 48px;
        border-radius: 12px;
        border: none;
        background-color: #4f46e5;
        color: white;
        font-size: 16px;
        font-weight: 700;
    }

    div.stButton > button:hover {
        background-color: #4338ca;
        color: white;
    }

    /* Number input */
    div[data-testid="stNumberInput"] input {
        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# HEADER
# ==================================================

st.markdown(
    '<div class="app-title">🎓 Grade Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="app-subtitle">'
    'Enter your mark and instantly find your letter grade'
    '</div>',
    unsafe_allow_html=True
)


# ==================================================
# INPUT SECTION
# ==================================================

with st.container(border=True):

    st.markdown(
        '<div class="section-title">📊 Enter Your Mark</div>',
        unsafe_allow_html=True
    )

    mark = st.number_input(
        "Mark",
        min_value=0,
        max_value=100,
        value=0,
        step=1,
        help="Enter a mark between 0 and 100."
    )

    # Progress bar
    st.progress(
        mark / 100,
        text=f"{mark}%"
    )

    calculate = st.button(
        "Calculate Grade",
        use_container_width=True
    )


# ==================================================
# CALCULATE GRADE
# ==================================================

if calculate:

    if mark >= 90:
        st.session_state.grade = "A"
        st.session_state.message = "Excellent performance! 🎉"

    elif mark >= 80:
        st.session_state.grade = "B"
        st.session_state.message = "Great job! Keep it up! 👏"

    elif mark >= 70:
        st.session_state.grade = "C"
        st.session_state.message = "Good effort! Keep improving! 💪"

    elif mark >= 60:
        st.session_state.grade = "D"
        st.session_state.message = "You passed. Keep working hard! 📚"

    else:
        st.session_state.grade = "E"
        st.session_state.message = (
            "Don't give up. Keep learning and try again! 🌟"
        )

    st.session_state.mark = mark


# ==================================================
# DISPLAY RESULT
# ==================================================

if st.session_state.grade is not None:

    grade = st.session_state.grade
    saved_mark = st.session_state.mark
    message = st.session_state.message

    # Grade-specific colors
    if grade == "A":
        grade_color = "#16a34a"
        result_type = "success"

    elif grade == "B":
        grade_color = "#2563eb"
        result_type = "info"

    elif grade == "C":
        grade_color = "#ca8a04"
        result_type = "warning"

    elif grade == "D":
        grade_color = "#ea580c"
        result_type = "warning"

    else:
        grade_color = "#dc2626"
        result_type = "error"

    st.write("")

    # Result container
    with st.container(border=True):

        st.markdown(
            '<div class="result-title">🏆 Your Result</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="mark-display">'
            f'Mark: <strong>{saved_mark}/100</strong>'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="grade-display" '
            f'style="color: {grade_color};">'
            f'{grade}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="message-display" '
            f'style="color: {grade_color};">'
            f'{message}'
            f'</div>',
            unsafe_allow_html=True
        )

        # Additional Streamlit message
        if result_type == "success":
            st.success("You achieved an excellent grade!")

        elif result_type == "info":
            st.info("You achieved a very good grade!")

        elif result_type == "warning":
            st.warning("There is room for improvement. Keep working!")

        else:
            st.error("Keep learning and try again!")


# ==================================================
# GRADING SCALE
# ==================================================

st.write("")

with st.container(border=True):

    st.markdown(
        '<div class="section-title">📋 Grading Scale</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.success("**A**  →  90 – 100")
        st.success("**B**  →  80 – 89")
        st.info("**C**  →  70 – 79")

    with col2:
        st.warning("**D**  →  60 – 69")
        st.error("**E**  →  Below 60")


# ==================================================
# FOOTER
# ==================================================

st.markdown(
    '<div class="footer">'
    'Built with ❤️ using Python & Streamlit'
    '</div>',
    unsafe_allow_html=True
)