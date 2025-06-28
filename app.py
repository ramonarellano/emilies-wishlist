import streamlit as st
import pandas as pd
from datetime import datetime
import uuid
import json
import os

# Set page config
st.set_page_config(
    page_title="💖 Emilies Ønskeliste",
    page_icon="🎁",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Data persistence functions
DATA_FILE = 'wishlist_data.json'

def load_data():
    """Load wishlist data from JSON file"""
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        st.error(f"Feil ved lasting av data: {e}")
    return []

def save_data(data):
    """Save wishlist data to JSON file"""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        st.error(f"Feil ved lagring av data: {e}")
        return False

# Initialize session state
if 'wishlist_items' not in st.session_state:
    st.session_state.wishlist_items = load_data()
    
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
    
if 'user_type' not in st.session_state:
    st.session_state.user_type = None

# Load passwords from Streamlit secrets
try:
    USERS = {
        'emilie': {'password': st.secrets["EMILIE_PASSWORD"], 'type': 'emilie'},
        'family': {'password': st.secrets["FAMILY_PASSWORD"], 'type': 'family'}
    }
except KeyError as e:
    st.error(f"Missing secret: {e}. Please configure secrets in Streamlit Cloud.")
    st.stop()

# Custom CSS for pink, cozy theme
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #e91e63 0%, #f48fb1 50%, #f8bbd9 100%);
    }
    .main-header {
        text-align: center;
        color: #ffffff;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .welcome-text {
        text-align: center;
        color: #ffffff;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    .stButton > button {
        background: linear-gradient(45deg, #ad1457, #e91e63);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
    .wishlist-table {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 1rem;
        margin: 1rem 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    .stDataFrame {
        background: white;
        border-radius: 10px;
    }
    .header-row {
        background: rgba(0, 0, 0, 0.1) !important;
        padding: 0.8rem !important;
        border-radius: 10px !important;
        margin-bottom: 0.5rem !important;
        font-weight: bold !important;
    }
    .header-row .stMarkdown {
        background: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

# Data structure for wishlist items
class WishlistItem:
    def __init__(self, name, description, url):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.url = url
        self.is_bought = False
        self.bought_by = None
        self.date_added = datetime.now().strftime("%Y-%m-%d")
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'url': self.url,
            'is_bought': self.is_bought,
            'bought_by': self.bought_by,
            'date_added': self.date_added
        }

# Authentication based on password
def login():
    st.markdown('<h1 class="main-header">💖 Emilies Ønskeliste 🎁</h1>', unsafe_allow_html=True)
    st.markdown('<p class="welcome-text">Et magisk sted for ønsker og drømmer ✨</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### 🔐 Logg inn")
        
        with st.form(key='login_form'):
            password = st.text_input("🔑 Passord", type="password")
            login_submitted = st.form_submit_button("Logg inn")
            
            if login_submitted:
                for user, info in USERS.items():
                    if info['password'] == password:
                        st.session_state.authenticated = True
                        st.session_state.user_type = info['type']
                        st.success(f"Velkommen! 🎉")
                        st.rerun()
                        return
                st.error("Feil passord 😞")
        
        st.markdown("---")
        st.markdown("**Info:**")
        st.markdown("• Spør Ramon om passord hvis du ikke har det")
        st.markdown("• Emilie og familie har ulike passord")

def logout():
    if st.sidebar.button("Logg ut"):
        st.session_state.authenticated = False
        st.session_state.user_type = None
        st.rerun()

# Main app logic
if not st.session_state.authenticated:
    login()
else:
    # Show logout button
    logout()
    
    # Display header for authenticated users
    st.markdown('<h1 class="main-header">💖 Emilies Ønskeliste 🎁</h1>', unsafe_allow_html=True)
    
    if st.session_state.user_type == 'emilie':
        st.markdown('<p class="welcome-text">Hei Emilie! Her kan du legge til dine ønsker 💕</p>', unsafe_allow_html=True)
        
        # Add new wishlist item form
        with st.form(key='add_item_form'):
            st.subheader("✨ Legg til et nytt ønske")
            col1, col2 = st.columns(2)
            
            with col1:
                name = st.text_input("🎁 Navn på ønsket*", placeholder="F.eks: Nintendo Switch")
                url = st.text_input("🔗 Lenke (valgfri)", placeholder="https://...")
            
            with col2:
                description = st.text_area("📝 Beskrivelse", placeholder="Fortell litt om ønsket ditt...")
            
            submit = st.form_submit_button("Legg til ønsket 🎀")
            
            if submit and name.strip():
                new_item = WishlistItem(name.strip(), description.strip(), url.strip())
                st.session_state.wishlist_items.append(new_item.to_dict())
                if save_data(st.session_state.wishlist_items):
                    st.success(f"🎉 '{name}' ble lagt til på ønskelisten!")
                else:
                    st.error("Feil ved lagring av ønsket")
                st.rerun()
            elif submit and not name.strip():
                st.error("Du må skrive navnet på ønsket ditt! 😊")

        # Display current wishlist items
        st.subheader(f"💖 Dine ønsker ({len(st.session_state.wishlist_items)})")

        if not st.session_state.wishlist_items:
            st.info("Ingen ønsker lagt til enda. Legg til ditt første ønske ovenfor! 🌟")
        else:
            st.markdown('<div class="wishlist-table">', unsafe_allow_html=True)
            
            # Add column headers with darker background
            st.markdown('<div style="background: rgba(0, 0, 0, 0.1); padding: 0.8rem; border-radius: 10px; margin-bottom: 0.5rem;">', unsafe_allow_html=True)
            header_cols = st.columns([3, 2, 1.5, 1, 0.8])
            with header_cols[0]:
                st.markdown("**🎁 Ønske**")
            with header_cols[1]:
                st.markdown("**📝 Beskrivelse**")
            with header_cols[2]:
                st.markdown("**🔗 Lenke**")
            with header_cols[3]:
                st.markdown("**📅 Dato**")
            with header_cols[4]:
                st.markdown("**🗑️**")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Create table with buttons for each row
            for i, item in enumerate(st.session_state.wishlist_items):
                cols = st.columns([3, 2, 1.5, 1, 0.8])
                
                with cols[0]:
                    st.write(f"🎁 **{item['name']}**")
                
                with cols[1]:
                    st.write(item['description'] if item['description'] else "-")
                
                with cols[2]:
                    if item['url']:
                        # Truncate URL if longer than 30 characters
                        display_url = item['url'] if len(item['url']) <= 30 else item['url'][:27] + "..."
                        st.markdown(f"[{display_url}]({item['url']})", unsafe_allow_html=True)
                    else:
                        st.write("-")
                
                with cols[3]:
                    st.write(item['date_added'])
                
                with cols[4]:
                    if st.button("🗑️", key=f"remove_{item['id']}", help=f"Fjern '{item['name']}"):
                        st.session_state.wishlist_items = [
                            it for it in st.session_state.wishlist_items 
                            if it['id'] != item['id']
                        ]
                        if save_data(st.session_state.wishlist_items):
                            st.success(f"'{item['name']}' ble fjernet fra ønskelisten!")
                        else:
                            st.error("Feil ved lagring")
                        st.rerun()
                
                # Add a subtle divider between rows
                if i < len(st.session_state.wishlist_items) - 1:
                    st.markdown("<hr style='margin: 0.5rem 0; border: 1px solid rgba(0,0,0,0.1);'>", unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
    elif st.session_state.user_type == 'family':
        st.markdown('<p class="welcome-text">Velkommen familie! Her kan du se Emilies ønskeliste 👨‍👩‍👧‍👦</p>', unsafe_allow_html=True)
        
        # Display wishlist for family members
        st.subheader(f"🎁 Emilies ønskeliste ({len(st.session_state.wishlist_items)} ønsker)")
        
        if not st.session_state.wishlist_items:
            st.info("Emilie har ikke lagt til noen ønsker enda 😊")
        else:
            # Show statistics
            bought_items = [item for item in st.session_state.wishlist_items if item['is_bought']]
            not_bought_items = [item for item in st.session_state.wishlist_items if not item['is_bought']]
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("📦 Totalt ønsker", len(st.session_state.wishlist_items))
            with col2:
                st.metric("✅ Kjøpt", len(bought_items))
            with col3:
                st.metric("🛒 Ikke kjøpt", len(not_bought_items))
            
            st.markdown("---")
            
            # Display items in table format
            st.markdown('<div class="wishlist-table">', unsafe_allow_html=True)
            
            # Add column headers with darker background
            st.markdown('<div style="background: rgba(0, 0, 0, 0.1); padding: 0.8rem; border-radius: 10px; margin-bottom: 0.5rem;">', unsafe_allow_html=True)
            header_cols = st.columns([2.5, 1.5, 1.5, 1, 1, 1.5])
            with header_cols[0]:
                st.markdown("**🎁 Ønske**")
            with header_cols[1]:
                st.markdown("**📝 Beskrivelse**")
            with header_cols[2]:
                st.markdown("**🔗 Lenke**")
            with header_cols[3]:
                st.markdown("**📅 Dato**")
            with header_cols[4]:
                st.markdown("**✅ Status**")
            with header_cols[5]:
                st.markdown("**👤 Kjøpt av**")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Display each item
            for i, item in enumerate(st.session_state.wishlist_items):
                cols = st.columns([2.5, 1.5, 1.5, 1, 1, 1.5])
                
                with cols[0]:
                    if item['is_bought']:
                        st.write(f"~~🎁 {item['name']}~~")  # Strikethrough for bought items
                    else:
                        st.write(f"🎁 **{item['name']}**")
                
                with cols[1]:
                    st.write(item['description'] if item['description'] else "-")
                
                with cols[2]:
                    if item['url']:
                        display_url = item['url'] if len(item['url']) <= 30 else item['url'][:27] + "..."
                        st.markdown(f"[{display_url}]({item['url']})", unsafe_allow_html=True)
                    else:
                        st.write("-")
                
                with cols[3]:
                    st.write(item['date_added'])
                
                with cols[4]:
                    if item['is_bought']:
                        purchase_date = item.get('purchase_date', item['date_added'])
                        st.write(f"✅ Kjøpt {purchase_date}")
                    else:
                        # Button to mark as bought
                        if st.button("✅ Merk som kjøpt", key=f"buy_{item['id']}", help=f"Marker '{item['name']}' som kjøpt"):
                            # Show form to enter buyer name
                            st.session_state[f"buying_{item['id']}"] = True
                            st.rerun()
                
                with cols[5]:
                    if item['is_bought']:
                        st.write(f"👤 {item['bought_by']}")
                    elif f"buying_{item['id']}" in st.session_state and st.session_state[f"buying_{item['id']}"]:
                        # Show input for buyer name
                        buyer_name = st.text_input("Ditt navn:", key=f"buyer_name_{item['id']}", placeholder="Skriv navnet ditt")
                        col_confirm, col_cancel = st.columns(2)
                        
                        with col_confirm:
                            if st.button("✅ Ok", key=f"confirm_{item['id']}"):
                                if buyer_name.strip():
                                    # Mark as bought
                                    for wishlist_item in st.session_state.wishlist_items:
                                        if wishlist_item['id'] == item['id']:
                                            wishlist_item['is_bought'] = True
                                            wishlist_item['bought_by'] = buyer_name.strip()
                                            wishlist_item['purchase_date'] = datetime.now().strftime("%Y-%m-%d")
                                            break
                                    
                                    # Save data and clean up session state
                                    if save_data(st.session_state.wishlist_items):
                                        del st.session_state[f"buying_{item['id']}"]
                                        st.success(f"🎉 '{item['name']}' markert som kjøpt av {buyer_name}!")
                                    else:
                                        st.error("Feil ved lagring")
                                    st.rerun()
                                else:
                                    st.error("Skriv navnet ditt først!")
                        
                        with col_cancel:
                            if st.button("❌ Avbryt", key=f"cancel_{item['id']}"):
                                del st.session_state[f"buying_{item['id']}"]
                                st.rerun()
                    else:
                        st.write("-")
                
                # Add divider between rows
                if i < len(st.session_state.wishlist_items) - 1:
                    st.markdown("<hr style='margin: 0.5rem 0; border: 1px solid rgba(0,0,0,0.1);'>", unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
