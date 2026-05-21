import os
import streamlit as st

current_dir = os.path.dirname(__file__)

def show():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.
7), rgba(0, 0, 0, 0.8)),
                    url("picture/1_back_car.jpeg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    [data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.7)
        !important;
        backdrop-filter: blur(12px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    h1, h2, h3 {
        color: #ffffff !important;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
    }
    p, span, label {
        color: #e0e0e0 !important;
    }
    .stPlotlyChart {
        background-color: rgba(0, 0, 0, 0.3);
        border-radius: 12px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.8)),
                        url("picture/1_back_car.jpeg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        [data-testid="stSidebar"] {
            background-color: rgba(0, 0, 0, 0.7) !important;
            backdrop-filter: blur(12px);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }
        h1, h2, h3 {
            color: #ffffff !important;
            text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
        }
        p, span, label {
            color: #e0e0e0 !important;
        }
        .stPlotlyChart {
            background-color: rgba(0, 0, 0, 0.3);
            border-radius: 12px;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


    col1, col2 = st.columns([1.08, 2], gap="medium")

    with col1:
        root_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

        image_candidates = [
            os.path.join(root_dir, "picture", "1_back_car.jpeg"),
            os.path.join(root_dir, "picture", "2_back_car.jpeg"),
            os.path.join(root_dir, "picture", "3_back_car.jpg"),
            os.path.join(root_dir, "gambar", "DRK_6468.jpg"),
        ]

        img_path = next((path for path in image_candidates if os.path.exists(path)), None)

        if img_path:
            st.image(img_path, caption="Mochammad Reyhan Mauluddi")
        else:
            st.error(
                "No profile image found; expected one of: picture/1_back_car.jpeg, picture/2_back_car.jpeg, picture/3_back_car.jpg, gambar/DRK_6468.jpg"
            )

    with col2:
        st.title("About Me")
        st.subheader("Data Analytics Specialist")
        st.write(
            """
            In today’s data-heavy world, everyone has information, but very few have clear answers.
            As a Data Analytics Specialist with over years of experience,
            my career has been defined by a single mission: transforming complex, high-volume datasets
            into the strategic blueprints that drive business solution. I specialize in the intersection of
            mathematical precision and commercial intuition.
            """
        )

    st.divider()

    st.subheader("Hobbies and Interests")
    st.write(
        """
         * **Sport**: Beyond the data, you’ll find me out for a run or a ride.
         * **Investment**: I actively explore investment opportunities in both physical assets and digital banking platforms.
         * **Data Analytics and AI**: Passionate about architecting end-to-end data solutions and diving deep into the world of
         Generative AI to build smarter, data-driven systems.
         """
    )

    st.subheader("Life Mission")
    st.info(
        """
    To build impactful data solutions using the latest technology and analytics while growing my career globally.
    """
    )

    st.divider()

    st.subheader("Contact Me")
    st.write(
        """
        If you're interested in discussing data projects or potential collaborations,
         please feel free to reach out via:
         """
    )

    contact_col1, contact_col2 = st.columns(2)
    with contact_col1:
        st.write("📧 **Email:** reyhanmauluddiin@gmail.com")
    with contact_col2:
        st.write("🔗 **LinkedIn:** [linkedin.com/in/reyhanmauluddi](https://www.linkedin.com)")
