import streamlit as st
import re
from database.db_manager import register_user, verify_user, reset_password

def is_valid_email(email: str) -> bool:
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email.strip()) is not None

def render_auth_page():
    """Render Login, Registration, and Forgot Password tabs with modern cards."""
    st.markdown("""
        <div style="text-align: center; margin-top: 20px; margin-bottom: 25px;">
            <div style="font-size: 3rem;">🌸</div>
            <h1 style="font-size: 2.2rem; font-weight: 800; margin: 0; background: linear-gradient(135deg, #4f46e5, #9333ea); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                Iris Flower Classification System
            </h1>
            <p style="color: #64748b; font-size: 1rem; margin-top: 6px;">Secure Member Access & Botanical Machine Learning Portal</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2.2, 1])
    
    with col2:
        tab_login, tab_register, tab_forgot = st.tabs(["🔐 Sign In", "📝 Create Account", "🔑 Forgot Password"])
        
        # ----------------- LOGIN TAB -----------------
        with tab_login:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.subheader("Welcome Back")
            st.caption("Sign in with your email and password to access the AI dashboard.")
            
            with st.form("login_form", clear_on_submit=False):
                login_email = st.text_input("Email Address", placeholder="name@domain.com")
                login_password = st.text_input("Password", type="password", placeholder="Enter your password")
                remember_me = st.checkbox("Remember Me", value=True)
                
                submitted = st.form_submit_button("Sign In to Dashboard", use_container_width=True, type="primary")
                
                if submitted:
                    if not login_email or not login_password:
                        st.error("Please fill in both email and password.")
                    elif not is_valid_email(login_email):
                        st.warning("Please enter a valid email address.")
                    else:
                        success, user_data, msg = verify_user(login_email, login_password)
                        if success:
                            st.session_state['user'] = user_data
                            st.session_state['logged_in'] = True
                            st.session_state['current_page'] = "Dashboard"
                            st.success(f"Welcome back, {user_data['fullname']}!")
                            st.rerun()
                        else:
                            st.error(msg)
                            
            st.markdown("""
                <div style="margin-top: 15px; font-size: 0.85rem; color: #64748b; text-align: center;">
                    <b>Default Demo Credentials:</b><br/>
                    Email: <code>admin@iris.ai</code> | Password: <code>Admin@123</code>
                </div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # ----------------- REGISTER TAB -----------------
        with tab_register:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.subheader("Create Your Account")
            st.caption("Register for immediate access to dataset analytics and ML models.")
            
            with st.form("register_form", clear_on_submit=True):
                reg_name = st.text_input("Full Name", placeholder="e.g. Dr. Jane Botanist")
                reg_email = st.text_input("Email Address", placeholder="e.g. jane@organization.org")
                reg_password = st.text_input("Password", type="password", placeholder="At least 6 characters")
                reg_confirm = st.text_input("Confirm Password", type="password", placeholder="Re-enter password")
                
                reg_submit = st.form_submit_button("Register Account", use_container_width=True, type="primary")
                
                if reg_submit:
                    if not reg_name or not reg_email or not reg_password:
                        st.error("Please fill in all mandatory fields.")
                    elif not is_valid_email(reg_email):
                        st.warning("Please provide a valid email format.")
                    elif len(reg_password) < 6:
                        st.warning("Password must contain at least 6 characters.")
                    elif reg_password != reg_confirm:
                        st.error("Passwords do not match.")
                    else:
                        success, msg = register_user(reg_name, reg_email, reg_password)
                        if success:
                            st.success(msg)
                            st.info("You can now sign in using the 'Sign In' tab.")
                        else:
                            st.error(msg)
            st.markdown('</div>', unsafe_allow_html=True)

        # ----------------- FORGOT PASSWORD TAB -----------------
        with tab_forgot:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.subheader("Password Recovery")
            st.caption("Reset your credentials to regain access to your account.")
            
            with st.form("forgot_password_form", clear_on_submit=True):
                forgot_email = st.text_input("Registered Email", placeholder="your_email@example.com")
                new_pw = st.text_input("New Password", type="password", placeholder="Enter new password (min 6 chars)")
                confirm_new_pw = st.text_input("Confirm New Password", type="password", placeholder="Re-enter new password")
                
                reset_submit = st.form_submit_button("Reset Password", use_container_width=True)
                
                if reset_submit:
                    if not forgot_email or not new_pw:
                        st.error("Please complete all fields.")
                    elif new_pw != confirm_new_pw:
                        st.error("New passwords do not match.")
                    elif len(new_pw) < 6:
                        st.warning("Password must have at least 6 characters.")
                    else:
                        success, msg = reset_password(forgot_email, new_pw)
                        if success:
                            st.success(msg)
                        else:
                            st.error(msg)
            st.markdown('</div>', unsafe_allow_html=True)

def render_user_profile_sidebar():
    """Display logged in user in the sidebar with signout button."""
    user = st.session_state.get('user', {})
    st.sidebar.markdown(f"""
        <div style="background: rgba(99, 102, 241, 0.08); border: 1px solid rgba(99, 102, 241, 0.2); border-radius: 12px; padding: 12px 16px; margin-bottom: 15px;">
            <div style="font-size: 0.8rem; text-transform: uppercase; color: #6366f1; font-weight: 700; letter-spacing: 0.05em;">Authenticated User</div>
            <div style="font-weight: 700; font-size: 1.05rem; margin-top: 2px;">{user.get('fullname', 'User')}</div>
            <div style="font-size: 0.8rem; color: #64748b;">{user.get('email', '')}</div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.sidebar.button("🚪 Sign Out", use_container_width=True):
        st.session_state['user'] = None
        st.session_state['logged_in'] = False
        st.session_state['current_page'] = "Landing"
        st.rerun()
