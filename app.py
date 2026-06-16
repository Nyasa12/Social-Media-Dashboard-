import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AuraMetrics Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* ---------------- MAIN APP ---------------- */

.stApp{
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #111827 35%,
        #1e1b4b 100%
    );
    color:white;
}

/* ---------------- SIDEBAR ---------------- */

[data-testid="stSidebar"]{
    background:linear-gradient(
        180deg,
        #111827,
        #0f172a
    );
}

[data-testid="stSidebar"] *{
    color:white;
}

/* ---------------- TITLES ---------------- */

.main-title{
    font-size:48px;
    font-weight:700;
    color:white;
}

.subtitle{
    color:#94a3b8;
    font-size:18px;
}

/* ---------------- GLASS CARD ---------------- */

.glass-card{

    background:rgba(255,255,255,0.05);

    border:1px solid rgba(255,255,255,0.1);

    backdrop-filter: blur(18px);

    border-radius:28px;

    padding:25px;

    box-shadow:
        0 8px 32px rgba(0,0,0,0.4);

    transition:all .3s ease;
}

/* ---------------- HOVER EFFECT ---------------- */

.glass-card:hover{

    transform:translateY(-6px);

    box-shadow:
        0 15px 40px rgba(96,165,250,0.25);

    border:1px solid rgba(96,165,250,.4);
}


/* ---------------- METRIC CARDS ---------------- */

div[data-testid="metric-container"]{

    background:rgba(255,255,255,0.05);

    border:1px solid rgba(255,255,255,0.1);

    padding:20px;

    border-radius:22px;

    box-shadow:
        0 8px 30px rgba(0,0,0,0.3);

    transition:0.3s;
}

div[data-testid="metric-container"]:hover{

    transform:translateY(-5px);

    border:1px solid #60a5fa;

    box-shadow:
        0 10px 35px rgba(96,165,250,.3);
}


/* ---------------- BUTTONS ---------------- */

.stButton>button{

    width:100%;

    border:none;

    border-radius:15px;

    background:linear-gradient(
        90deg,
        #3b82f6,
        #8b5cf6
    );

    color:white;

    font-weight:600;

    height:50px;

    transition:.3s;
}

.stButton>button:hover{

    transform:scale(1.03);

    box-shadow:
        0 10px 25px rgba(59,130,246,.4);
}


/* ---------------- DATAFRAME ---------------- */

[data-testid="stDataFrame"]{

    border-radius:20px;

    overflow:hidden;
}


/* ---------------- PLOTLY CHARTS ---------------- */

.js-plotly-plot{

    border-radius:25px;

    background:rgba(255,255,255,0.03);

    padding:10px;
}


/* ---------------- SCROLL BAR ---------------- */

::-webkit-scrollbar{

    width:10px;
}

::-webkit-scrollbar-thumb{

    background:#3b82f6;

    border-radius:20px;
}


/* ---------------- ANIMATION ---------------- */

@keyframes fadeUp{

    from{
        opacity:0;
        transform:translateY(15px);
    }

    to{
        opacity:1;
        transform:translateY(0px);
    }
}

.glass-card{

    animation:fadeUp .7s ease;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown(
    """
    <div class='glass-card'>
        <div class='main-title'>
            📊 AuraMetrics Analytics
        </div>

        <div class='subtitle'>
            Enterprise Social Media Analytics Platform
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------- PLACEHOLDER SECTIONS ----------------
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class='glass-card'>
            <h3>📈 Instagram Ads Analytics</h3>
            <p>Campaign insights, ROAS, CTR and conversion tracking.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class='glass-card'>
            <h3>⭐ Creator Analytics</h3>
            <p>Influencer performance, engagement and revenue metrics.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

st.markdown(
    """
    <div class='glass-card'>
        <h3>🚀 Unified Dashboard</h3>
        <p>
        Central hub for monitoring Instagram Ads, Creator Analytics,
        Campaign Performance and AI Recommendations.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)








import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AuraMetrics Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0f172a,#111827);
    color:white;
}

/* Title */
.main-title{
    font-size:48px;
    font-weight:700;
    color:white;
}

.subtitle{
    color:#94a3b8;
    font-size:18px;
}

/* Glass Card */
.glass-card{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.1);
    backdrop-filter:blur(18px);
    border-radius:25px;
    padding:25px;
    box-shadow:0px 8px 32px rgba(0,0,0,0.3);
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#111827,#0f172a);
}

[data-testid="stSidebar"] *{
    color:white;
}

.sidebar-heading{
    color:#60a5fa;
    font-size:15px;
    font-weight:700;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.title("📊 AuraMetrics")

    st.markdown("---")

    st.markdown(
        "<div class='sidebar-heading'>MAIN MODULES</div>",
        unsafe_allow_html=True
    )

    selected_module = st.radio(
        "",
        [
            "🏠 Unified Dashboard",
            "📈 Instagram Ads",
            "⭐ Creator Analytics",
            "📊 Campaign Monitor",
            "🤖 AI Recommendations"
        ]
    )

    st.markdown("---")

    st.markdown(
        "<div class='sidebar-heading'>GLOBAL TOOLS</div>",
        unsafe_allow_html=True
    )

    st.button("📄 Export Reports")
    st.button("🔄 Multi Account Sync")
    st.button("⚙ Settings")

# ---------------- HEADER ----------------
st.markdown(
"""
<div class='glass-card'>
<div class='main-title'>
📊 AuraMetrics Analytics
</div>

<div class='subtitle'>
Enterprise Social Media Analytics Platform
</div>
</div>
""",
unsafe_allow_html=True
)

st.write("")

# ---------------- MODULE DISPLAY ----------------
st.subheader(selected_module)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='glass-card'>
        <h3>📈 Instagram Ads Analytics</h3>
        <p>Campaign insights, ROAS, CTR and conversion tracking.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='glass-card'>
        <h3>⭐ Creator Analytics</h3>
        <p>Influencer performance, engagement and revenue metrics.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

st.markdown("""
<div class='glass-card'>
<h3>🚀 Unified Dashboard</h3>

<p>
Central hub for monitoring Instagram Ads, Creator Analytics,
Campaign Performance and AI Recommendations.
</p>

</div>
""", unsafe_allow_html=True)





import plotly.express as px
import pandas as pd

# ---------------- KPI DATA ----------------
kpi_data = [
    ("💰 Total Ad Spend", "$42.5K", "+12%"),
    ("👁 Impressions", "8.9M", "+18%"),
    ("📡 Reach", "5.2M", "+9%"),
    ("💵 Revenue Generated", "$128K", "+24%"),
    ("🚀 ROAS", "3.8x", "+15%"),
    ("🎯 CTR", "4.7%", "+8%"),
    ("📈 Conversion Rate", "6.1%", "+11%"),
    ("📷 Followers Gained", "14.2K", "+20%"),
    ("❤️ Avg Engagement", "7.5%", "+14%")
]

# ---------------- KPI SECTION ----------------
st.write("")
st.subheader("📊 Key Performance Indicators")

cols = st.columns(3)

for i, (title, value, change) in enumerate(kpi_data):

    with cols[i % 3]:

        spark_df = pd.DataFrame({
            "x": [1,2,3,4,5,6,7],
            "y": [8,10,9,14,12,18,20]
        })

        fig = px.line(
            spark_df,
            x="x",
            y="y"
        )

        fig.update_layout(
            height=120,
            margin=dict(l=0,r=0,t=0,b=0),
            xaxis_visible=False,
            yaxis_visible=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )

        st.markdown(
            f"""
            <div class='glass-card'>
                <h4>{title}</h4>
                <h2>{value}</h2>
                <h4 style='color:#22c55e'>{change}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.plotly_chart(
          fig,
          use_container_width=True,
          key=f"sparkline_{i}"
       )







# ---------------- REVENUE VS AD SPEND SECTION ----------------

st.write("")
st.subheader("📈 Revenue & Investment Performance")

performance_df = pd.DataFrame({
    "Month": [
        "Jan","Feb","Mar","Apr",
        "May","Jun","Jul","Aug"
    ],
    "Ad Spend": [
        12000,15000,18000,22000,
        25000,27000,30000,34000
    ],
    "Revenue": [
        30000,38000,45000,55000,
        68000,76000,91000,108000
    ]
})

col1, col2 = st.columns(2)

# -------- Revenue vs Ad Spend Line Chart --------
with col1:

    fig_line = px.line(
        performance_df,
        x="Month",
        y=["Revenue", "Ad Spend"],
        markers=True,
        title="Revenue vs Ad Spend"
    )

    fig_line.update_traces(line_shape="spline")

    fig_line.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=450,
        legend_title="Metrics"
    )

    st.plotly_chart(
        fig_line,
        use_container_width=True
    )

# -------- Revenue Area Chart --------
with col2:

    fig_area = px.area(
        performance_df,
        x="Month",
        y="Revenue",
        title="Revenue Growth Trend"
    )

    fig_area.update_traces(line_shape="spline")

    fig_area.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=450
    )

    st.plotly_chart(
        fig_area,
        use_container_width=True
    )







# =====================================================
# INSTAGRAM ADS ANALYTICS
# =====================================================

st.write("")
st.subheader("📈 Instagram Ads Analytics")

# ---------------- METRICS ----------------

metric1, metric2, metric3, metric4 = st.columns(4)

metric1.metric(
    "CPC",
    "$0.42",
    "+5.2%"
)

metric2.metric(
    "CPM",
    "$6.85",
    "+3.1%"
)

metric3.metric(
    "CTR",
    "4.7%",
    "+0.9%"
)

metric4.metric(
    "ROAS",
    "3.8x",
    "+12.5%"
)

metric5, metric6, metric7, metric8 = st.columns(4)

metric5.metric(
    "Reach",
    "5.2M",
    "+8.5%"
)

metric6.metric(
    "Clicks",
    "132K",
    "+11%"
)

metric7.metric(
    "Conversions",
    "8.4K",
    "+9%"
)

metric8.metric(
    "Cost Per Conversion",
    "$5.06",
    "-4.2%"
)


# ---------------- DUMMY DATA ----------------

ads_df = pd.DataFrame({
    "Day": [
        "Mon","Tue","Wed","Thu",
        "Fri","Sat","Sun"
    ],

    "Spend": [
        3200,
        4100,
        3900,
        5200,
        6100,
        5800,
        7000
    ],

    "Conversions": [
        220,
        310,
        280,
        420,
        520,
        490,
        610
    ]
})


campaign_df = pd.DataFrame({
    "Campaign": [
        "Summer Sale",
        "Fashion Reel",
        "Beauty Launch",
        "Creator Promo",
        "Retargeting"
    ],

    "Revenue": [
        42000,
        36000,
        51000,
        29000,
        47000
    ]
})


audience_df = pd.DataFrame({
    "Audience": [
        "18-24",
        "25-34",
        "35-44",
        "45+"
    ],

    "Users": [
        35,
        42,
        17,
        6
    ]
})


# =====================================================
# CHARTS
# =====================================================

col1, col2 = st.columns(2)

# -------- Daily Spend Chart --------

with col1:

    fig_spend = px.line(
        ads_df,
        x="Day",
        y="Spend",
        markers=True,
        title="Daily Spend Trend"
    )

    fig_spend.update_traces(
        line_shape="spline"
    )

    fig_spend.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        height=450
    )

    st.plotly_chart(
        fig_spend,
        use_container_width=True
    )


# -------- Campaign Performance --------

with col2:

    fig_campaign = px.bar(
        campaign_df,
        x="Campaign",
        y="Revenue",
        title="Campaign Performance"
    )

    fig_campaign.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        height=450
    )

    st.plotly_chart(
        fig_campaign,
        use_container_width=True
    )


# =====================================================
# SECOND ROW
# =====================================================

col3, col4 = st.columns(2)

# -------- Conversion Funnel --------

with col3:

    funnel_df = pd.DataFrame({
        "Stage": [
            "Impressions",
            "Clicks",
            "Leads",
            "Conversions"
        ],

        "Value": [
            8900000,
            132000,
            28000,
            8400
        ]
    })

    fig_funnel = px.funnel(
        funnel_df,
        x="Value",
        y="Stage",
        title="Conversion Funnel"
    )

    fig_funnel.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        height=450
    )

    st.plotly_chart(
        fig_funnel,
        use_container_width=True
    )


# -------- Audience Distribution --------

with col4:

    fig_audience = px.pie(
        audience_df,
        names="Audience",
        values="Users",
        hole=0.6,
        title="Audience Distribution"
    )

    fig_audience.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        height=450
    )

    st.plotly_chart(
        fig_audience,
        use_container_width=True
    )





# =====================================================
# CREATOR ANALYTICS
# =====================================================

st.write("")
st.subheader("⭐ Creator Analytics")

# ---------------- DUMMY DATA ----------------

creator_df = pd.DataFrame({
    "Creator Name": [
        "Aarav Sharma",
        "Priya Mehta",
        "Rohan Verma",
        "Ananya Singh",
        "Karan Kapoor",
        "Neha Jain",
        "Rahul Gupta",
        "Simran Kaur",
        "Arjun Malhotra",
        "Ishita Roy"
    ],

    "Followers": [
        520000,430000,680000,750000,390000,
        580000,810000,460000,620000,540000
    ],

    "Engagement Rate": [
        7.8,6.9,8.5,9.1,6.5,
        7.4,8.9,7.0,8.2,7.6
    ],

    "Average Likes": [
        25000,18000,34000,39000,17000,
        28000,41000,21000,31000,26000
    ],

    "Average Comments": [
        1200,950,1600,1800,840,
        1350,2000,980,1450,1250
    ],

    "Revenue Generated": [
        52000,46000,71000,85000,39000,
        58000,94000,48000,76000,61000
    ],

    "Match Score": [
        91,84,95,97,80,
        88,98,83,94,89
    ]
})

# ---------------- TABLE ----------------

st.dataframe(
    creator_df,
    use_container_width=True
)

# =====================================================
# CHARTS
# =====================================================

col1, col2 = st.columns(2)

# -------- Revenue Chart --------

with col1:

    fig_creator_bar = px.bar(
        creator_df,
        x="Creator Name",
        y="Revenue Generated",
        title="Creator Revenue Comparison"
    )

    fig_creator_bar.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        height=450
    )

    st.plotly_chart(
        fig_creator_bar,
        use_container_width=True,
        key="creator_bar_chart"
    )

# -------- Engagement Chart --------

with col2:

    fig_engagement = px.line(
        creator_df,
        x="Creator Name",
        y="Engagement Rate",
        markers=True,
        title="Engagement Comparison"
    )

    fig_engagement.update_traces(
        line_shape="spline"
    )

    fig_engagement.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        height=450
    )

    st.plotly_chart(
        fig_engagement,
        use_container_width=True,
        key="engagement_chart"
    )

# =====================================================
# RADAR CHART
# =====================================================

radar_df = pd.DataFrame({
    "Metric": [
        "Followers",
        "Engagement",
        "Likes",
        "Comments",
        "Revenue"
    ],

    "Value": [
        81,
        92,
        86,
        75,
        95
    ]
})

fig_radar = px.line_polar(
    radar_df,
    r="Value",
    theta="Metric",
    line_close=True,
    title="Overall Creator Performance Radar"
)

fig_radar.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="white",
    height=550
)

st.plotly_chart(
    fig_radar,
    use_container_width=True,
    key="radar_chart"
)




# =====================================================
# CAMPAIGN MONITOR
# =====================================================

st.write("")
st.subheader("📊 Campaign Monitor")

# ---------------- KPI METRICS ----------------

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Active Campaigns",
    "12",
    "+2"
)

col2.metric(
    "Budget",
    "$150K",
    "+8%"
)

col3.metric(
    "Spend",
    "$92K",
    "+5%"
)

col4.metric(
    "Revenue",
    "$315K",
    "+16%"
)

col5.metric(
    "ROI",
    "242%",
    "+21%"
)

# ---------------- DUMMY DATA ----------------

campaign_monitor_df = pd.DataFrame({
    "Campaign": [
        "Summer Sale",
        "Creator Promo",
        "Beauty Launch",
        "Retargeting",
        "Festive Ads"
    ],

    "Revenue": [
        85000,
        62000,
        98000,
        54000,
        76000
    ],

    "ROI": [
        280,
        215,
        340,
        185,
        260
    ]
})


daily_df = pd.DataFrame({
    "Day": [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ],

    "Revenue": [
        32000,
        41000,
        39000,
        52000,
        61000,
        58000,
        70000
    ]
})

# =====================================================
# CHARTS
# =====================================================

col1, col2 = st.columns(2)

# -------- Campaign Performance --------

with col1:

    fig_campaign_perf = px.bar(
        campaign_monitor_df,
        x="Campaign",
        y="Revenue",
        title="Campaign Performance"
    )

    fig_campaign_perf.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        height=450
    )

    st.plotly_chart(
        fig_campaign_perf,
        use_container_width=True,
        key="campaign_performance_chart"
    )

# -------- ROI Comparison --------

with col2:

    fig_roi = px.bar(
        campaign_monitor_df,
        x="Campaign",
        y="ROI",
        title="ROI Comparison"
    )

    fig_roi.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        height=450
    )

    st.plotly_chart(
        fig_roi,
        use_container_width=True,
        key="roi_chart"
    )

# =====================================================
# DAILY TREND
# =====================================================

fig_daily = px.line(
    daily_df,
    x="Day",
    y="Revenue",
    markers=True,
    title="Daily Revenue Trend"
)

fig_daily.update_traces(
    line_shape="spline"
)

fig_daily.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="white",
    height=500
)

st.plotly_chart(
    fig_daily,
    use_container_width=True,
    key="daily_trend_chart"
)





# =====================================================
# AI RECOMMENDATION PANEL
# =====================================================

st.write("")
st.subheader("🤖 AI Recommendations")

# ---------------- FIRST ROW ----------------

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class='glass-card'>
        <h3>💰 Budget Optimization <span style='color:#22c55e'>(94)</span></h3>

        <p>
        Increase spend on top-performing campaigns.
        Shift 15% budget from low ROAS campaigns.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Apply Recommendation",
        key="budget_button"
    ):
        st.success("Budget optimization applied!")

with col2:

    st.markdown("""
    <div class='glass-card'>
        <h3>⭐ Best Creator Match <span style='color:#60a5fa'>(97)</span></h3>

        <p>
        Rahul Gupta has the highest engagement
        and strongest revenue potential.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "View Creator",
        key="creator_button"
    ):
        st.success("Creator profile loaded!")

# ---------------- SECOND ROW ----------------

col3, col4 = st.columns(2)

with col3:

    st.markdown("""
    <div class='glass-card'>
        <h3>📈 Campaign Suggestions <span style='color:#a855f7'>(91)</span></h3>

        <p>
        Video campaigns are outperforming image ads.
        Increase reel-based promotions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Optimize Campaign",
        key="campaign_button"
    ):
        st.success("Campaign updated!")

with col4:

    st.markdown("""
    <div class='glass-card'>
        <h3>🎯 Audience Suggestions <span style='color:#14b8a6'>(95)</span></h3>

        <p>
        Audience aged 25-34 shows highest
        conversion and engagement rates.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Target Audience",
        key="audience_button"
    ):
        st.success("Audience targeting improved!")








# =====================================================
# CREATOR PROFILE PAGE
# =====================================================

st.write("")
st.subheader("👤 Creator Profile")

# ---------------- PROFILE INFO ----------------

col1, col2 = st.columns([1,3])

with col1:

    st.image(
        "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=500",
        width=180
    )

with col2:

    st.markdown("## ⭐ Rahul Gupta")

    metric1, metric2 = st.columns(2)

    metric1.metric(
        "Followers",
        "810K",
        "+8%"
    )

    metric2.metric(
        "Engagement Rate",
        "8.9%",
        "+1.2%"
    )

    metric3, metric4 = st.columns(2)

    metric3.metric(
        "Average Views",
        "1.2M",
        "+11%"
    )

    metric4.metric(
        "Revenue Generated",
        "$94K",
        "+18%"
    )

# =====================================================
# AUDIENCE AGE DISTRIBUTION
# =====================================================

col1, col2 = st.columns(2)

with col1:

    age_df = pd.DataFrame({
        "Age Group": [
            "18-24",
            "25-34",
            "35-44",
            "45+"
        ],

        "Users": [
            28,
            46,
            18,
            8
        ]
    })

    fig_age = px.pie(
        age_df,
        names="Age Group",
        values="Users",
        hole=0.5,
        title="Audience Age Distribution"
    )

    fig_age.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=450
    )

    st.plotly_chart(
        fig_age,
        use_container_width=True,
        key="age_distribution"
    )


# =====================================================
# GENDER DISTRIBUTION
# =====================================================

with col2:

    gender_df = pd.DataFrame({
        "Gender": [
            "Male",
            "Female"
        ],

        "Users": [
            42,
            58
        ]
    })

    fig_gender = px.pie(
        gender_df,
        names="Gender",
        values="Users",
        hole=0.5,
        title="Gender Distribution"
    )

    fig_gender.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=450
    )

    st.plotly_chart(
        fig_gender,
        use_container_width=True,
        key="gender_distribution"
    )

# =====================================================
# TOP COUNTRIES
# =====================================================

col3, col4 = st.columns(2)

with col3:

    country_df = pd.DataFrame({
        "Country": [
            "India",
            "USA",
            "UK",
            "Canada",
            "Australia"
        ],

        "Audience": [
            62,
            15,
            9,
            8,
            6
        ]
    })

    fig_country = px.bar(
        country_df,
        x="Country",
        y="Audience",
        title="Top Countries"
    )

    fig_country.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=450
    )

    st.plotly_chart(
        fig_country,
        use_container_width=True,
        key="country_chart"
    )

# =====================================================
# DEVICE USAGE
# =====================================================

with col4:

    device_df = pd.DataFrame({
        "Device": [
            "Android",
            "iPhone",
            "Tablet",
            "Desktop"
        ],

        "Users": [
            52,
            31,
            7,
            10
        ]
    })

    fig_device = px.bar(
        device_df,
        x="Device",
        y="Users",
        title="Device Usage"
    )

    fig_device.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=450
    )

    st.plotly_chart(
        fig_device,
        use_container_width=True,
        key="device_chart"
    )






# =====================================================
# CSV UPLOAD SUPPORT
# =====================================================

st.write("")
st.subheader("📂 Upload Campaign Data")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("CSV uploaded successfully!")

    st.write("Preview Data")
    st.dataframe(
        df.head(),
        use_container_width=True
    )

    # -------------------------------------------------
    # CALCULATED METRICS
    # -------------------------------------------------

    if all(col in df.columns for col in [
        "Spend",
        "Revenue",
        "Impressions",
        "Clicks",
        "Conversions"
    ]):

        total_spend = df["Spend"].sum()
        total_revenue = df["Revenue"].sum()
        total_impressions = df["Impressions"].sum()
        total_clicks = df["Clicks"].sum()
        total_conversions = df["Conversions"].sum()

        # ROAS
        roas = total_revenue / total_spend

        # CTR
        ctr = (total_clicks / total_impressions) * 100

        # CPC
        cpc = total_spend / total_clicks

        # CPM
        cpm = (total_spend / total_impressions) * 1000

        # Cost Per Conversion
        cost_per_conversion = total_spend / total_conversions

        st.write("")
        st.subheader("📊 Dynamic Metrics")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "ROAS",
            f"{roas:.2f}x"
        )

        col2.metric(
            "CTR",
            f"{ctr:.2f}%"
        )

        col3.metric(
            "CPC",
            f"${cpc:.2f}"
        )

        col4, col5 = st.columns(2)

        col4.metric(
            "CPM",
            f"${cpm:.2f}"
        )

        col5.metric(
            "Cost Per Conversion",
            f"${cost_per_conversion:.2f}"
        )

        # -------------------------------------------------
        # DYNAMIC CHART
        # -------------------------------------------------

        if "Date" in df.columns:

            chart = px.line(
                df,
                x="Date",
                y=["Revenue", "Spend"],
                title="Revenue vs Spend"
            )

            chart.update_traces(
                line_shape="spline"
            )

            chart.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font_color="white",
                height=500
            )

            st.plotly_chart(
                chart,
                use_container_width=True,
                key="dynamic_chart"
            )

    else:

        st.warning(
            """
            CSV should contain these columns:

            Spend
            Revenue
            Impressions
            Clicks
            Conversions
            """
        )







# =====================================================
# ADVANCED FILTERS
# =====================================================

st.write("")
st.subheader("🔍 Advanced Filters")

filter_col1, filter_col2 = st.columns(2)

with filter_col1:

    date_range = st.date_input(
        "📅 Select Date Range"
    )

    creator_filter = st.multiselect(
        "⭐ Select Creator",
        [
            "Rahul Gupta",
            "Aarav Sharma",
            "Priya Mehta",
            "Ananya Singh",
            "Rohan Verma"
        ]
    )

with filter_col2:

    campaign_filter = st.multiselect(
        "📢 Select Campaign",
        [
            "Summer Sale",
            "Beauty Launch",
            "Creator Promo",
            "Retargeting",
            "Festive Ads"
        ]
    )

    platform_filter = st.multiselect(
        "🌐 Select Platform",
        [
            "Instagram",
            "Facebook",
            "YouTube",
            "TikTok"
        ]
    )

# ---------------- FILTER SUMMARY ----------------

st.write("")
st.markdown("### 📋 Current Filters")

summary_col1, summary_col2 = st.columns(2)

with summary_col1:

    st.info(
        f"""
        Selected Creators:
        {creator_filter if creator_filter else "All"}
        """
    )

with summary_col2:

    st.info(
        f"""
        Selected Campaigns:
        {campaign_filter if campaign_filter else "All"}
        """
    )

# ---------------- PLATFORM SUMMARY ----------------

st.info(
    f"""
    Selected Platforms:
    {platform_filter if platform_filter else "All"}
    """
)










# =====================================================
# EXPORT OPTIONS
# =====================================================

import io

st.write("")
st.subheader("📤 Export Reports")

export_col1, export_col2, export_col3 = st.columns(3)

# -----------------------------------------------------
# SAMPLE DATA FOR EXPORT
# -----------------------------------------------------

export_df = pd.DataFrame({
    "Campaign": [
        "Summer Sale",
        "Beauty Launch",
        "Creator Promo",
        "Retargeting"
    ],

    "Spend": [
        25000,
        32000,
        18000,
        21000
    ],

    "Revenue": [
        78000,
        96000,
        51000,
        65000
    ],

    "ROI": [
        212,
        240,
        183,
        209
    ]
})

# -----------------------------------------------------
# EXPORT CSV
# -----------------------------------------------------

csv = export_df.to_csv(index=False)

with export_col1:

    st.download_button(
        label="📄 Export CSV",
        data=csv,
        file_name="campaign_report.csv",
        mime="text/csv"
    )

# -----------------------------------------------------
# EXPORT EXCEL
# -----------------------------------------------------

excel_buffer = io.BytesIO()

with pd.ExcelWriter(
    excel_buffer,
    engine="openpyxl"
) as writer:

    export_df.to_excel(
        writer,
        index=False,
        sheet_name="Campaign Report"
    )

excel_data = excel_buffer.getvalue()

with export_col2:

    st.download_button(
        label="📊 Export Excel",
        data=excel_data,
        file_name="campaign_report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# -----------------------------------------------------
# DOWNLOAD CHART IMAGE
# -----------------------------------------------------

with export_col3:

    st.button(
        "📥 Download Charts",
        key="download_chart_btn"
    )

    st.info(
        "Chart download feature will be connected in later stages."
    )






# =====================================================
# LOGIN SESSION STATE
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =====================================================
# LOGIN PAGE
# =====================================================

if not st.session_state.logged_in:

    st.title("🔐 AuraMetrics Login")

    st.write("Welcome to AuraMetrics Analytics Platform")

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    login_btn = st.button(
        "Login"
    )

    if login_btn:

        # Dummy credentials
        if email == "admin@gmail.com" and password == "admin123":

            st.session_state.logged_in = True
            st.rerun()

        else:

            st.error(
                "Invalid email or password"
            )

    st.stop()


if st.button(
    "🚪 Logout",
    key="logout_btn"
):

    st.session_state.logged_in = False
    st.rerun()




