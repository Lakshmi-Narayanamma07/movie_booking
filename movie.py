import streamlit as st
from datetime import datetime

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Lakshmi's Movie Ticket Booking",
    page_icon="🎬",
    layout="wide"
)

# ---------------------------------------------------------
# MOVIE DATA
# ---------------------------------------------------------
movies = {
    "🎬 Avengers: Endgame": {
        "language": "English",
        "genre": "Action / Sci-Fi",
        "rating": "8.4/10",
        "duration": "3h 2m",
        "showtimes": ["10:00 AM", "2:00 PM", "6:30 PM", "10:00 PM"]
    },

    "🕷️ Spider-Man: No Way Home": {
        "language": "English",
        "genre": "Action / Adventure",
        "rating": "8.2/10",
        "duration": "2h 28m",
        "showtimes": ["11:00 AM", "3:00 PM", "7:00 PM", "10:30 PM"]
    },

    "🚀 Kalki 2898 AD": {
        "language": "Telugu",
        "genre": "Sci-Fi / Action",
        "rating": "8.0/10",
        "duration": "3h",
        "showtimes": ["9:30 AM", "1:30 PM", "5:30 PM", "9:00 PM"]
    },

    "😂 Jathi Ratnalu": {
        "language": "Telugu",
        "genre": "Comedy",
        "rating": "8.0/10",
        "duration": "2h 25m",
        "showtimes": ["10:30 AM", "2:30 PM", "6:00 PM", "9:30 PM"]
    },

    "🔥 Pushpa: The Rise": {
        "language": "Telugu",
        "genre": "Action / Drama",
        "rating": "7.6/10",
        "duration": "2h 59m",
        "showtimes": ["10:00 AM", "1:45 PM", "5:30 PM", "9:15 PM"]
    },

    "🌊 RRR": {
        "language": "Telugu",
        "genre": "Action / Drama",
        "rating": "8.0/10",
        "duration": "3h 7m",
        "showtimes": ["9:00 AM", "1:00 PM", "5:00 PM", "9:00 PM"]
    },

    "🦸 Salaar": {
        "language": "Telugu",
        "genre": "Action",
        "rating": "7.0/10",
        "duration": "2h 55m",
        "showtimes": ["10:30 AM", "2:00 PM", "6:00 PM", "10:00 PM"]
    },

    "🌟 Baahubali 2": {
        "language": "Telugu",
        "genre": "Epic / Action",
        "rating": "8.2/10",
        "duration": "2h 47m",
        "showtimes": ["9:30 AM", "1:30 PM", "5:30 PM", "9:30 PM"]
    },

    "❤️ Sita Ramam": {
        "language": "Telugu",
        "genre": "Romance / Drama",
        "rating": "8.6/10",
        "duration": "2h 43m",
        "showtimes": ["11:30 AM", "3:00 PM", "6:30 PM", "9:45 PM"]
    },

    "🤣 F2: Fun and Frustration": {
        "language": "Telugu",
        "genre": "Comedy",
        "rating": "6.8/10",
        "duration": "2h 28m",
        "showtimes": ["10:00 AM", "2:00 PM", "6:00 PM", "9:30 PM"]
    },

    "🕶️ Vikram": {
        "language": "Tamil",
        "genre": "Action / Thriller",
        "rating": "8.3/10",
        "duration": "2h 54m",
        "showtimes": ["10:30 AM", "2:30 PM", "6:30 PM", "10:00 PM"]
    },

    "👑 KGF Chapter 2": {
        "language": "Kannada",
        "genre": "Action / Drama",
        "rating": "8.3/10",
        "duration": "2h 48m",
        "showtimes": ["9:30 AM", "1:30 PM", "5:30 PM", "9:30 PM"]
    }
}

# ---------------------------------------------------------
# THEATRE DATA
# ---------------------------------------------------------
theatres = {
    "🎭 PVR INOX": {
        "location": "City Center",
        "charge": 50
    },

    "🎥 Cinepolis": {
        "location": "Central Mall",
        "charge": 40
    },

    "🍿 AMB Cinemas": {
        "location": "Gachibowli",
        "charge": 80
    },

    "🎬 Asian Cinemas": {
        "location": "RTC X Roads",
        "charge": 30
    },

    "⭐ Prasads Multiplex": {
        "location": "Necklace Road",
        "charge": 60
    }
}

# ---------------------------------------------------------
# TICKET PRICES
# ---------------------------------------------------------
ticket_prices = {
    "Standard": 150,
    "Premium": 220,
    "VIP": 350
}

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.title("🎬 Lakshmi's Movie Ticket Booking")

st.write(
    "🍿 Book your favourite movie with just a few clicks!"
)

st.divider()

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
st.sidebar.header("🎟️ Booking Details")

customer_name = st.sidebar.text_input(
    "👤 Customer Name",
    placeholder="Enter your name"
)

selected_movie = st.sidebar.selectbox(
    "🎬 Select Movie",
    list(movies.keys())
)

selected_theatre = st.sidebar.selectbox(
    "🏢 Select Theatre",
    list(theatres.keys())
)

movie_info = movies[selected_movie]
theatre_info = theatres[selected_theatre]

selected_showtime = st.sidebar.selectbox(
    "🕒 Select Showtime",
    movie_info["showtimes"]
)

selected_category = st.sidebar.selectbox(
    "💺 Ticket Category",
    list(ticket_prices.keys())
)

number_of_tickets = st.sidebar.number_input(
    "🎟️ Number of Tickets",
    min_value=1,
    max_value=10,
    value=2,
    step=1
)

# ---------------------------------------------------------
# MOVIE INFORMATION
# ---------------------------------------------------------
st.header(selected_movie)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🌐 Language",
        movie_info["language"]
    )

with col2:
    st.metric(
        "🎭 Genre",
        movie_info["genre"]
    )

with col3:
    st.metric(
        "⭐ Rating",
        movie_info["rating"]
    )

with col4:
    st.metric(
        "⏱️ Duration",
        movie_info["duration"]
    )

st.divider()

# ---------------------------------------------------------
# THEATRE INFORMATION
# ---------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏢 Theatre")

    st.info(
        f"🎭 {selected_theatre}\n\n"
        f"📍 Location: {theatre_info['location']}"
    )

with col2:
    st.subheader("🎟️ Ticket Information")

    st.info(
        f"💺 Category: {selected_category}\n\n"
        f"🎫 Tickets: {number_of_tickets}\n\n"
        f"💰 Base Price: ₹{ticket_prices[selected_category]}"
    )

# ---------------------------------------------------------
# PRICE CALCULATION
# ---------------------------------------------------------
base_price = ticket_prices[selected_category]

theatre_charge = theatre_info["charge"]

price_per_ticket = base_price + theatre_charge

subtotal = price_per_ticket * number_of_tickets

discount = 0

if number_of_tickets >= 5:
    discount = subtotal * 0.10

final_total = subtotal - discount

# ---------------------------------------------------------
# PRICE SUMMARY
# ---------------------------------------------------------
st.header("💰 Price Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🎟️ Base Ticket",
        f"₹{base_price:.2f}"
    )

with col2:
    st.metric(
        "🏢 Theatre Charge",
        f"₹{theatre_charge:.2f}"
    )

with col3:
    st.metric(
        "🎫 Tickets",
        number_of_tickets
    )

with col4:
    st.metric(
        "💰 Total",
        f"₹{final_total:.2f}"
    )

if number_of_tickets >= 5:
    st.success(
        "🎉 10% Group Booking Discount Applied!"
    )

st.divider()

# ---------------------------------------------------------
# TOTAL BOOKING AMOUNT
# ---------------------------------------------------------
st.header("🎬 Total Booking Amount")

st.success(
    f"💰 ₹{final_total:.2f}"
)

st.write(
    f"🎟️ {number_of_tickets} × {selected_category} Ticket"
)

st.divider()

# ---------------------------------------------------------
# CONFIRM BOOKING
# ---------------------------------------------------------
if st.button(
    "🎟️ CONFIRM BOOKING",
    use_container_width=True,
    type="primary"
):

    if customer_name.strip() == "":
        st.warning(
            "⚠️ Please enter your name before confirming the booking."
        )

    else:

        booking_time = datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        )

        st.balloons()

        # -------------------------------------------------
        # BOOKING CONFIRMATION
        # -------------------------------------------------
        st.success(
            "🎉 BOOKING CONFIRMED!"
        )

        st.header("🎬 Movie Ticket")

        st.subheader(selected_movie)

        st.write("### 👤 Customer")
        st.write(customer_name)

        st.write("### 🏢 Theatre")
        st.write(selected_theatre)

        st.write("### 📍 Location")
        st.write(theatre_info["location"])

        st.write("### 🕒 Showtime")
        st.write(selected_showtime)

        st.write("### 💺 Ticket Category")
        st.write(selected_category)

        st.write("### 🎟️ Number of Tickets")
        st.write(number_of_tickets)

        st.write("### 💰 Price Per Ticket")
        st.write(f"₹{price_per_ticket:.2f}")

        st.divider()

        st.subheader("💰 TOTAL AMOUNT")

        st.success(
            f"₹{final_total:.2f}"
        )

        st.write(
            f"🕐 Booking Time: {booking_time}"
        )

        st.divider()

        st.info(
            "🍿 Enjoy your movie!\n\n"
            "❤️ Thank you for booking with us!"
        )