import streamlit as st
from streamlit_option_menu import option_menu
import datetime

# Page configuration
st.set_page_config(
    page_title="University Events",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject custom CSS for the chat widget
st.markdown(
    """
    <style>
    #wotchat-container {
        z-index: 1000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Inject the chat widget
st.components.v1.html(
    """
    <script src="https://app.wotnot.io/chat-widget/nhVP8wJYUZam165958636448p4JHOLR5.js" defer></script>
    <div id="wotchat-container"></div>
    """,
    height=0
)

# Sample data
EVENTS = [
    {
        "title": "Annual Science Fair 2023",
        "date": "2023-11-15",
        "time": "10:00 AM - 4:00 PM",
        "location": "Science Building",
        "description": "Explore innovative projects from our science and engineering students.",
        "category": "Academic"
    },
    {
        "title": "Coding Competition",
        "date": "2023-11-20",
        "time": "9:00 AM - 5:00 PM",
        "location": "Computer Lab 3",
        "description": "Annual inter-departmental coding competition. Prizes for top coders!",
        "category": "Competition"
    },
    {
        "title": "Cultural Fest",
        "date": "2023-12-01",
        "time": "11:00 AM - 8:00 PM",
        "location": "University Grounds",
        "description": "Experience diverse cultures through music, dance, and food from around the world.",
        "category": "Cultural"
    }
]

# Sidebar navigation
with st.sidebar:
    st.image("https://via.placeholder.com/150x50?text=University+Logo", width=150)
    st.title("University Events")
    
    menu = option_menu(
        menu_title=None,
        options=["Home", "Upcoming Events", "Submit Event", "About", "Feedback"],
        icons=["house", "calendar-event", "plus-circle", "info-circle", "chat-dots"],
        default_index=0
    )
    
    # Add Google Form link in the sidebar
    st.markdown("---")
    st.markdown("### Quick Links")
    st.markdown("""
    - [Event Feedback Form](https://forms.gle/ofCWgEPcZqa22A5R6)
    - [Resources Folder](https://drive.google.com/drive/folders/1zGPfWwCSZj5o-8HspPq2VBlwMOvjkvHo)
    """, unsafe_allow_html=True)

# Page content
if menu == "Home":
    st.header("Welcome to University Events Portal")
    st.markdown("""
    Discover and participate in various events happening across our university campus. 
    Stay updated with academic, cultural, and social events organized by different departments and student groups.
    """)
    
    st.image("https://via.placeholder.com/1200x400?text=University+Events", use_column_width=True)
    
    st.markdown("### Featured Events")
    for event in EVENTS[:2]:
        with st.expander(f"{event['title']} - {event['date']}"):
            st.write(f"**Time:** {event['time']}")
            st.write(f"**Location:** {event['location']}")
            st.write(event['description'])

elif menu == "Upcoming Events":
    st.header("Upcoming Events")
    
    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        category_filter = st.selectbox(
            "Filter by category",
            ["All"] + list(set(event["category"] for event in EVENTS))
        )
    with col2:
        search_query = st.text_input("Search events")
    
    # Apply filters
    filtered_events = EVENTS
    if category_filter != "All":
        filtered_events = [e for e in filtered_events if e["category"] == category_filter]
    if search_query:
        search_query = search_query.lower()
        filtered_events = [
            e for e in filtered_events
            if (search_query in e["title"].lower() or 
                 search_query in e["description"].lower())
        ]
    
    # Display events
    if not filtered_events:
        st.warning("No events found matching your criteria.")
    else:
        for event in filtered_events:
            with st.container():
                st.subheader(event["title"])
                st.caption(f"{event['date']} • {event['time']} • {event['location']}")
                st.write(event["description"])
                st.markdown(f"**Category:** {event['category']}")
                st.button("Learn More", key=f"btn_{event['title']}")
                st.divider()

elif menu == "Submit Event":
    st.header("Submit a New Event")
    
    with st.form("event_form"):
        title = st.text_input("Event Title*")
        description = st.text_area("Event Description*")
        
        col1, col2 = st.columns(2)
        with col1:
            date = st.date_input("Event Date*", min_value=datetime.date.today())
        with col2:
            time = st.time_input("Event Time*")
        
        location = st.text_input("Event Location*")
        category = st.selectbox("Category*", ["Academic", "Cultural", "Sports", "Workshop", "Other"])
        contact_email = st.text_input("Contact Email*")
        
        submitted = st.form_submit_button("Submit Event")
        if submitted:
            if not all([title, description, date, time, location, category, contact_email]):
                st.error("Please fill in all required fields.")
            else:
                # In a real app, you would save this to a database
                st.success("Thank you for submitting your event! It will be reviewed by our team.")

elif menu == "Feedback":
    st.header("Event Feedback")
    st.markdown("""
    We value your feedback! Please take a moment to share your thoughts about our events.
    
    [Submit Feedback Form](https://forms.gle/ofCWgEPcZqa22A5R6)
    
    Your input helps us improve future events and better serve our university community.
    """)
    
elif menu == "About":
    st.header("About University Events")
    st.markdown("""
    The University Events Portal is your one-stop destination for all events happening across our campus.
    
    ### Features:
    - Browse upcoming events
    - Filter events by category
    - Submit your own events
    - Get event details and updates
    
    ### Contact Us
    For any questions or support, please contact:
    - Email: events@university.edu
    - Phone: (123) 456-7890
    - Office: Administration Building, Room 101
    """)
    
    st.image("https://via.placeholder.com/800x300?text=University+Campus", use_column_width=True)

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: gray;">
    <p>© 2023 University Name. All rights reserved.</p>
    <p>
        <a href="#" style="color: gray; margin: 0 10px;">Privacy Policy</a> | 
        <a href="#" style="color: gray; margin: 0 10px;">Terms of Service</a> | 
        <a href="#" style="color: gray; margin: 0 10px;">Contact Us</a>
    </p>
</div>
""", unsafe_allow_html=True)
