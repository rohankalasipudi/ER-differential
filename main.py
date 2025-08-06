# main.py
# This is a Streamlit application for a progressive, ER-focused diagnostic tool.

import streamlit as st
from er_symptoms import ER_PRESENTATIONS
from er_treatments import ER_TREATMENTS

def initialize_session_state():
    """Initializes session state variables if they don't exist."""
    if "step" not in st.session_state:
        st.session_state.step = "start"
    if "chief_complaint" not in st.session_state:
        st.session_state.chief_complaint = None
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "diagnosis" not in st.session_state:
        st.session_state.diagnosis = None

def reset_app():
    """Resets the application to the initial state."""
    st.session_state.step = "start"
    st.session_state.chief_complaint = None
    st.session_state.answers = {}
    st.session_state.diagnosis = None

def get_next_question(presentation, answers):
    """
    Determines the next question to ask based on the current answers.
    Returns the question key and a list of options.
    """
    for question_key in ER_PRESENTATIONS[presentation]["questions"]:
        if question_key not in answers:
            return question_key, ER_PRESENTATIONS[presentation]["questions"][question_key]
    return None, None

def match_diagnosis(presentation, answers):
    """
    Matches the user's answers to a possible diagnosis based on the ER_PRESENTATIONS data.
    """
    diagnoses = ER_PRESENTATIONS[presentation]["diagnoses"]
    for diagnosis in diagnoses:
        match_criteria = diagnosis["match"]
        is_match = True
        for key, value in match_criteria.items():
            user_answer = answers.get(key)
            if isinstance(value, list):
                if user_answer not in value:
                    is_match = False
                    break
            else:
                if user_answer != value:
                    is_match = False
                    break
        if is_match:
            return diagnosis
    return None

def main():
    initialize_session_state()

    st.set_page_config(
        page_title="ER Diagnostic Tree",
        page_icon="🏥",
        layout="centered",
    )

    st.title("🏥 ER Diagnostic Tree")
    st.markdown("A progressive tool to practice differential diagnosis for common ER presentations.")
    
    if st.session_state.step == "start":
        st.subheader("Select a Chief Complaint")
        complaints = list(ER_PRESENTATIONS.keys())
        
        col1, col2 = st.columns(2)
        
        with col1:
            for i in range(len(complaints) // 2 + len(complaints) % 2):
                if st.button(complaints[i], use_container_width=True, key=f"btn_{i}"):
                    st.session_state.chief_complaint = complaints[i]
                    st.session_state.step = "questions"
                    st.experimental_rerun()
        
        with col2:
            for i in range(len(complaints) // 2, len(complaints)):
                if st.button(complaints[i], use_container_width=True, key=f"btn_{i}"):
                    st.session_state.chief_complaint = complaints[i]
                    st.session_state.step = "questions"
                    st.experimental_rerun()


    elif st.session_state.step == "questions":
        presentation = st.session_state.chief_complaint
        st.subheader(f"Chief Complaint: {presentation}")
        
        question_key, options = get_next_question(presentation, st.session_state.answers)
        
        if question_key:
            st.markdown(f"**Question:** What is the {question_key} of the pain?")
            
            # Create buttons for each option
            cols = st.columns(len(options))
            for i, option in enumerate(options):
                with cols[i]:
                    if st.button(option, key=f"{question_key}_{option}"):
                        st.session_state.answers[question_key] = option
                        st.experimental_rerun()
        else:
            # All questions have been answered, now find the diagnosis
            st.session_state.diagnosis = match_diagnosis(presentation, st.session_state.answers)
            st.session_state.step = "results"
            st.experimental_rerun()

    elif st.session_state.step == "results":
        st.subheader("Your Analysis")
        st.markdown(f"**Chief Complaint:** {st.session_state.chief_complaint}")
        st.markdown("**Your Findings:**")
        for key, value in st.session_state.answers.items():
            st.markdown(f"- {key.capitalize()}: {value}")
        
        st.markdown("---")
        
        diagnosis = st.session_state.diagnosis
        if diagnosis:
            st.success(f"**Most Probable Diagnosis:** {diagnosis['name']}")
            st.info(f"**Differentiating Factors:** {diagnosis['differentiating_factors']}")
            
            # Display treatment plan from the treatments file
            if diagnosis['name'] in ER_TREATMENTS:
                treatment_data = ER_TREATMENTS[diagnosis['name']]
                st.markdown("#### **Initial Management (ER)**")
                st.markdown("**First-Line Therapy:**")
                for item in treatment_data['first_line']:
                    st.markdown(f"- {item}")
                st.markdown("**Supportive Care:**")
                for item in treatment_data['supportive_care']:
                    st.markdown(f"- {item}")
            else:
                st.warning("Treatment protocol not found for this diagnosis.")
        else:
            st.warning("Could not match a specific diagnosis with these findings.")
        
        st.markdown("---")
        st.button("Start Over", on_click=reset_app)

if __name__ == "__main__":
    main()
