# ============================================================
# SUPPLY CHAIN & LOGISTICS ANALYTICS DASHBOARD
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Supply Chain & Logistics Analytics",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "supply_chain_cleaned.csv"
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    return df

df = load_data()

# ============================================================
# PAGE TITLE
# ============================================================

st.title("📦 Supply Chain & Logistics Analytics")

st.markdown(
    """
    **Interactive Data Science Dashboard**

    Analyze sales, profitability, product performance,
    logistics efficiency, and regional business performance
    using supply chain data.
    """
)

st.divider()


# ============================================================
# DATASET STATUS
# ============================================================

st.success(
    f"Dataset loaded successfully — {len(df):,} records"
)

# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("🔎 Dashboard Filters")

st.sidebar.caption(
    "Select filters to explore the supply chain data."
)


# ============================================================
# MARKET FILTER
# ============================================================

market_options = sorted(
    df["Market"].dropna().astype(str).unique().tolist()
)

market_filter = st.sidebar.selectbox(
    "Market",
    ["All Markets"] + market_options
)


# ============================================================
# ORDER REGION FILTER
# ============================================================

region_options = sorted(
    df["Order Region"].dropna().astype(str).unique().tolist()
)

region_filter = st.sidebar.selectbox(
    "Order Region",
    ["All Regions"] + region_options
)


# ============================================================
# CATEGORY FILTER
# ============================================================

category_options = sorted(
    df["Category Name"].dropna().astype(str).unique().tolist()
)

category_filter = st.sidebar.selectbox(
    "Category",
    ["All Categories"] + category_options
)


# ============================================================
# SHIPPING MODE FILTER
# ============================================================

shipping_options = sorted(
    df["Shipping Mode"].dropna().astype(str).unique().tolist()
)

shipping_filter = st.sidebar.selectbox(
    "Shipping Mode",
    ["All Shipping Modes"] + shipping_options
)


# ============================================================
# DELIVERY PERFORMANCE FILTER
# ============================================================

delivery_options = sorted(
    df["Delivery_Performance"].dropna().astype(str).unique().tolist()
)

delivery_filter = st.sidebar.selectbox(
    "Delivery Performance",
    ["All Delivery Status"] + delivery_options
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


if market_filter != "All Markets":
    filtered_df = filtered_df[
        filtered_df["Market"].astype(str) == market_filter
    ]


if region_filter != "All Regions":
    filtered_df = filtered_df[
        filtered_df["Order Region"].astype(str) == region_filter
    ]


if category_filter != "All Categories":
    filtered_df = filtered_df[
        filtered_df["Category Name"].astype(str) == category_filter
    ]


if shipping_filter != "All Shipping Modes":
    filtered_df = filtered_df[
        filtered_df["Shipping Mode"].astype(str) == shipping_filter
    ]


if delivery_filter != "All Delivery Status":
    filtered_df = filtered_df[
        filtered_df["Delivery_Performance"].astype(str)
        == delivery_filter
    ]


# ============================================================
# FILTER STATUS
# ============================================================

st.sidebar.divider()

st.sidebar.metric(
    "Filtered Records",
    f"{len(filtered_df):,}"
)

# ============================================================
# KPI CALCULATIONS
# ============================================================

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()

total_orders = len(filtered_df)

total_units = filtered_df["Order Item Quantity"].sum()

profit_margin = (
    (total_profit / total_sales) * 100
    if total_sales != 0
    else 0
)

average_order_value = (
    total_sales / total_orders
    if total_orders != 0
    else 0
)


# ============================================================
# KPI CARDS
# ============================================================

st.subheader("📊 Executive Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Sales",
        value=f"${total_sales:,.0f}"
    )

with col2:
    st.metric(
        label="Total Profit",
        value=f"${total_profit:,.0f}"
    )

with col3:
    st.metric(
        label="Total Records / Orders",
        value=f"{total_orders:,}"
    )

with col4:
    st.metric(
        label="Profit Margin",
        value=f"{profit_margin:.2f}%"
    )


# ============================================================
# SECOND KPI ROW
# ============================================================

col5, col6, col7, col8 = st.columns(4)

with col5:
    st.metric(
        label="Units Sold",
        value=f"{total_units:,.0f}"
    )

with col6:
    st.metric(
        label="Average Order Value",
        value=f"${average_order_value:,.2f}"
    )

with col7:
    average_delivery_delay = filtered_df[
        "Delivery_Delay_Days"
    ].mean()

    st.metric(
        label="Avg Delivery Delay",
        value=f"{average_delivery_delay:.2f} days"
    )

with col8:
    delayed_percentage = (
        filtered_df["Delivery_Performance"]
        .eq("Delayed")
        .mean()
        * 100
        if len(filtered_df) > 0
        else 0
    )

    st.metric(
        label="Delayed Orders",
        value=f"{delayed_percentage:.2f}%"
    )

# st.divider()

# ============================================================
# BUSINESS INSIGHTS & RECOMMENDATIONS
# ============================================================

st.markdown("---")

st.subheader("💡 Business Insights & Recommendations")

st.caption(
    "Key observations generated from the filtered supply chain data."
)

# Calculate current filtered metrics
if not filtered_df.empty:

    insight_col1, insight_col2 = st.columns(2)

    with insight_col1:
        st.markdown("### 📈 Sales & Profitability")

        filtered_sales = filtered_df["Sales"].sum()
        filtered_profit = filtered_df["Profit"].sum()

        if filtered_sales > 0:
            filtered_margin = (
                filtered_profit / filtered_sales
            ) * 100
        else:
            filtered_margin = 0

        st.write(
            f"• Total filtered sales are **${filtered_sales:,.2f}**."
        )

        st.write(
            f"• Total filtered profit is **${filtered_profit:,.2f}**."
        )

        st.write(
            f"• The filtered profit margin is "
            f"**{filtered_margin:.2f}%**."
        )

    with insight_col2:
        st.markdown("### 🚚 Logistics Performance")

        if "Delivery Status" in filtered_df.columns:

            delivery_counts = (
                filtered_df["Delivery Status"]
                .value_counts()
            )

            if not delivery_counts.empty:
                top_delivery_status = delivery_counts.idxmax()
                top_delivery_count = delivery_counts.max()

                st.write(
                    f"• The most common delivery status is "
                    f"**{top_delivery_status}**."
                )

                st.write(
                    f"• It represents approximately "
                    f"**{top_delivery_count:,} records**."
                )

        if "Days for shipping (real)" in filtered_df.columns:

            avg_shipping_days = filtered_df[
                "Days for shipping (real)"
            ].mean()

            st.write(
                f"• Average actual shipping time is "
                f"**{avg_shipping_days:.2f} days**."
            )

    st.markdown("### 🎯 Recommended Actions")

    recommendations = []

    if filtered_margin < 10:
        recommendations.append(
            "Review low-margin products, pricing, and operating costs."
        )
    else:
        recommendations.append(
            "Maintain current pricing and profitability strategies."
        )

    if "Delivery Status" in filtered_df.columns:
        delayed_count = (
            filtered_df["Delivery Status"]
            .astype(str)
            .str.lower()
            .str.contains("late|delay")
            .sum()
        )

        delayed_percentage = (
            delayed_count / len(filtered_df)
        ) * 100

        if delayed_percentage > 20:
            recommendations.append(
                "Investigate delayed deliveries and improve logistics planning."
            )
        else:
            recommendations.append(
                "Continue monitoring delivery performance and logistics efficiency."
            )

    recommendations.append(
        "Use the available filters to identify high-performing markets, "
        "regions, categories, and shipping modes."
    )

    for recommendation in recommendations:
        st.markdown(f"• {recommendation}")

else:
    st.info(
        "No filtered records are available to generate business insights."
    )

# ============================================================
# SALES & REVENUE ANALYSIS
# ============================================================

st.divider()

st.subheader("📈 Sales & Revenue Analysis")

# ------------------------------------------------------------
# Sales and Profit by Category
# ------------------------------------------------------------

category_sales = (
    filtered_df
    .groupby("Category Name", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Sales", ascending=False)
)

fig_category = px.bar(
    category_sales,
    x="Category Name",
    y="Sales",
    title="Sales by Category",
    labels={
        "Category Name": "Category",
        "Sales": "Total Sales"
    }
)

fig_category.update_layout(
    xaxis_tickangle=-45
)

st.plotly_chart(
    fig_category,
    use_container_width=True
)


# ============================================================
# PROFITABILITY ANALYSIS
# ============================================================

st.subheader("💰 Profitability Analysis")

# ------------------------------------------------------------
# Profit by Category
# ------------------------------------------------------------

category_profit = (
    filtered_df
    .groupby("Category Name", as_index=False)
    .agg(
        Profit=("Profit", "sum")
    )
    .sort_values("Profit", ascending=False)
    .head(15)
)

fig_profit = px.bar(
    category_profit,
    x="Category Name",
    y="Profit",
    title="Top 15 Categories by Profit",
    labels={
        "Category Name": "Category",
        "Profit": "Total Profit"
    }
)

fig_profit.update_layout(
    xaxis_tickangle=-35,
    height=500,
    margin=dict(
        l=20,
        r=20,
        t=70,
        b=120
    )
)

st.plotly_chart(
    fig_profit,
    use_container_width=True
)

# ============================================================
# SALES VS PROFIT ANALYSIS
# ============================================================

st.subheader("📊 Sales vs Profit Analysis")

# ------------------------------------------------------------
# Sales vs Profit by Category
# ------------------------------------------------------------

sales_profit = (
    filtered_df
    .groupby("Category Name", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

fig_sales_profit = px.scatter(
    sales_profit,
    x="Sales",
    y="Profit",
    hover_name="Category Name",
    hover_data={
        "Sales": ":,.0f",
        "Profit": ":,.0f"
    },
    title="Sales vs Profit by Category"
)

fig_sales_profit.update_layout(
    xaxis_title="Total Sales",
    yaxis_title="Total Profit",
    height=500
)

st.plotly_chart(
    fig_sales_profit,
    use_container_width=True
)

# ============================================================
# LOGISTICS & DELIVERY PERFORMANCE
# ============================================================

st.subheader("🚚 Logistics & Delivery Performance")

# ------------------------------------------------------------
# Delivery Performance Distribution
# ------------------------------------------------------------

delivery_performance = (
    filtered_df["Delivery Status"]
    .value_counts()
    .reset_index()
)

delivery_performance.columns = [
    "Delivery Status",
    "Orders"
]

fig_delivery = px.bar(
    delivery_performance,
    x="Delivery Status",
    y="Orders",
    title="Delivery Performance",
    labels={
        "Delivery Status": "Delivery Status",
        "Orders": "Number of Orders"
    },
    text="Orders"
)

fig_delivery.update_traces(
    texttemplate="%{text:,}",
    textposition="outside"
)

fig_delivery.update_layout(
    height=500
)

st.plotly_chart(
    fig_delivery,
    use_container_width=True
)

# ============================================================
# SHIPPING MODE ANALYSIS
# ============================================================

st.subheader("🚢 Shipping Mode Analysis")

# ------------------------------------------------------------
# Sales and Profit by Shipping Mode
# ------------------------------------------------------------

shipping_analysis = (
    filtered_df
    .groupby("Shipping Mode", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Shipping Mode", "count")
    )
    .sort_values("Sales", ascending=False)
)

fig_shipping = px.bar(
    shipping_analysis,
    x="Shipping Mode",
    y=["Sales", "Profit"],
    barmode="group",
    title="Sales and Profit by Shipping Mode",
    labels={
        "Shipping Mode": "Shipping Mode",
        "value": "Amount",
        "variable": "Metric"
    }
)

fig_shipping.update_layout(
    height=500
)

st.plotly_chart(
    fig_shipping,
    use_container_width=True
)

# ============================================================
# PRODUCT & CATEGORY PERFORMANCE
# ============================================================

st.subheader("📦 Product & Category Performance")

# ------------------------------------------------------------
# Top 10 Products by Sales
# ------------------------------------------------------------

top_products = (
    filtered_df
    .groupby("Product Name", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Sales", ascending=False)
    .head(10)
)

fig_products = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Sales",
    labels={
        "Sales": "Total Sales",
        "Product Name": "Product"
    },
    text="Sales"
)

fig_products.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

fig_products.update_layout(
    height=550,
    yaxis={
        "categoryorder": "total ascending"
    }
)

st.plotly_chart(
    fig_products,
    use_container_width=True
)

# ============================================================
# REGIONAL & GEOGRAPHIC PERFORMANCE
# ============================================================

st.subheader("🌍 Regional & Geographic Performance")

# ------------------------------------------------------------
# Sales and Profit by Region
# ------------------------------------------------------------

regional_analysis = (
    filtered_df
    .groupby("Order Region", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order Region", "count")
    )
    .sort_values("Sales", ascending=False)
)

fig_region = px.bar(
    regional_analysis,
    x="Order Region",
    y="Sales",
    title="Sales by Region",
    labels={
        "Order Region": "Region",
        "Sales": "Total Sales"
    },
    text="Sales"
)

fig_region.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

fig_region.update_layout(
    xaxis_tickangle=-35,
    height=500,
    margin=dict(
        l=20,
        r=20,
        t=70,
        b=120
    )
)

st.plotly_chart(
    fig_region,
    use_container_width=True
)

# ============================================================
# REGIONAL PROFITABILITY ANALYSIS
# ============================================================

st.subheader("💰 Regional Profitability")

# ------------------------------------------------------------
# Profit by Region
# ------------------------------------------------------------

regional_profit = (
    filtered_df
    .groupby("Order Region", as_index=False)
    .agg(
        Profit=("Profit", "sum"),
        Sales=("Sales", "sum")
    )
    .sort_values("Profit", ascending=False)
)

fig_region_profit = px.bar(
    regional_profit,
    x="Order Region",
    y="Profit",
    title="Profit by Region",
    labels={
        "Order Region": "Region",
        "Profit": "Total Profit"
    },
    text="Profit"
)

fig_region_profit.update_traces(
    texttemplate="%{text:,.0f}",
    textposition="outside"
)

fig_region_profit.update_layout(
    xaxis_tickangle=-35,
    height=500,
    margin=dict(
        l=20,
        r=20,
        t=70,
        b=120
    )
)

st.plotly_chart(
    fig_region_profit,
    use_container_width=True
)

# ============================================================
# CATEGORY PROFIT MARGIN ANALYSIS
# ============================================================

st.subheader("📊 Category Profit Margin")

# ------------------------------------------------------------
# Calculate Profit Margin by Category
# ------------------------------------------------------------

category_margin = (
    filtered_df
    .groupby("Category Name", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

category_margin["Profit Margin %"] = (
    category_margin["Profit"]
    / category_margin["Sales"]
    * 100
)

category_margin = (
    category_margin
    .replace([np.inf, -np.inf], np.nan)
    .dropna(subset=["Profit Margin %"])
    .sort_values("Profit Margin %", ascending=False)
    .head(15)
)

# ------------------------------------------------------------
# Create Chart
# ------------------------------------------------------------

fig_margin = px.bar(
    category_margin,
    x="Category Name",
    y="Profit Margin %",
    title="Top 15 Categories by Profit Margin",
    labels={
        "Category Name": "Category",
        "Profit Margin %": "Profit Margin (%)"
    },
    text="Profit Margin %"
)

fig_margin.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside"
)

fig_margin.update_layout(
    xaxis_tickangle=-35,
    height=500,
    margin=dict(
        l=20,
        r=20,
        t=70,
        b=120
    )
)

st.plotly_chart(
    fig_margin,
    use_container_width=True
)

# ============================================================
# MARKET PERFORMANCE ANALYSIS
# ============================================================

st.subheader("🌐 Market Performance")

# ------------------------------------------------------------
# Sales and Profit by Market
# ------------------------------------------------------------

market_performance = (
    filtered_df
    .groupby("Market", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

# ------------------------------------------------------------
# Create grouped bar chart
# ------------------------------------------------------------

market_chart = market_performance.melt(
    id_vars="Market",
    value_vars=["Sales", "Profit"],
    var_name="Metric",
    value_name="Value"
)

fig_market = px.bar(
    market_chart,
    x="Market",
    y="Value",
    color="Metric",
    barmode="group",
    title="Sales vs Profit by Market",
    labels={
        "Market": "Market",
        "Value": "Amount",
        "Metric": "Metric"
    }
)

fig_market.update_layout(
    height=500,
    margin=dict(
        l=20,
        r=20,
        t=70,
        b=80
    )
)

st.plotly_chart(
    fig_market,
    use_container_width=True
)

# ============================================================
# TOP PRODUCTS BY PROFIT
# ============================================================

st.subheader("🏆 Top Products by Profit")

# ------------------------------------------------------------
# Calculate product-level profit
# ------------------------------------------------------------

top_products_profit = (
    filtered_df
    .groupby("Product Name", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Profit", ascending=False)
    .head(10)
)

# ------------------------------------------------------------
# Create horizontal bar chart
# ------------------------------------------------------------

fig_top_profit = px.bar(
    top_products_profit.sort_values("Profit"),
    x="Profit",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Profit",
    labels={
        "Profit": "Total Profit",
        "Product Name": "Product"
    },
    text="Profit"
)

fig_top_profit.update_traces(
    texttemplate="$%{text:,.0f}",
    textposition="outside"
)

fig_top_profit.update_layout(
    height=550,
    margin=dict(
        l=20,
        r=80,
        t=70,
        b=50
    )
)

st.plotly_chart(
    fig_top_profit,
    use_container_width=True
)

# ============================================================
# LOSS-MAKING PRODUCTS ANALYSIS
# ============================================================

st.subheader("⚠️ Loss-Making Products")

# ------------------------------------------------------------
# Calculate product-level sales and profit
# ------------------------------------------------------------

loss_products = (
    filtered_df
    .groupby("Product Name", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

# Keep only products with negative profit
loss_products = (
    loss_products[loss_products["Profit"] < 0]
    .sort_values("Profit", ascending=True)
    .head(10)
)

# ------------------------------------------------------------
# Display result
# ------------------------------------------------------------

if loss_products.empty:

    st.success("No loss-making products found for the selected filters.")

else:

    fig_loss = px.bar(
        loss_products.sort_values("Profit", ascending=True),
        x="Profit",
        y="Product Name",
        orientation="h",
        title="Top 10 Loss-Making Products",
        labels={
            "Profit": "Total Loss",
            "Product Name": "Product"
        },
        text="Profit"
    )

    fig_loss.update_traces(
        texttemplate="$%{text:,.0f}",
        textposition="outside"
    )

    fig_loss.update_layout(
        height=550,
        margin=dict(
            l=20,
            r=80,
            t=70,
            b=50
        )
    )

    st.plotly_chart(
        fig_loss,
        use_container_width=True
    )
    
# ============================================================
# ORDER VOLUME BY REGION
# ============================================================

st.subheader("📦 Order Volume by Region")

# ------------------------------------------------------------
# Calculate order volume by region
# ------------------------------------------------------------

region_orders = (
    filtered_df
    .groupby("Order Region", as_index=False)
    .size()
    .rename(columns={"size": "Orders"})
    .sort_values("Orders", ascending=False)
)

# ------------------------------------------------------------
# Create chart
# ------------------------------------------------------------

fig_region_orders = px.bar(
    region_orders,
    x="Order Region",
    y="Orders",
    title="Order Volume by Region",
    labels={
        "Order Region": "Region",
        "Orders": "Number of Orders"
    },
    text="Orders"
)

fig_region_orders.update_traces(
    texttemplate="%{text:,}",
    textposition="outside"
)

fig_region_orders.update_layout(
    xaxis_tickangle=-35,
    height=500,
    margin=dict(
        l=20,
        r=20,
        t=70,
        b=120
    )
)

st.plotly_chart(
    fig_region_orders,
    use_container_width=True
)

# ============================================================
# DELIVERY DELAY ANALYSIS
# ============================================================

st.subheader("⏱️ Delivery Delay Analysis")

# ------------------------------------------------------------
# Average Delivery Delay by Shipping Mode
# ------------------------------------------------------------

delay_analysis = (
    filtered_df
    .groupby("Shipping Mode", as_index=False)
    .agg(
        Average_Delay_Days=("Delivery_Delay_Days", "mean")
    )
    .sort_values("Average_Delay_Days", ascending=False)
)

# ------------------------------------------------------------
# Create chart
# ------------------------------------------------------------

fig_delay = px.bar(
    delay_analysis,
    x="Shipping Mode",
    y="Average_Delay_Days",
    title="Average Delivery Delay by Shipping Mode",
    labels={
        "Shipping Mode": "Shipping Mode",
        "Average_Delay_Days": "Average Delay (Days)"
    },
    text="Average_Delay_Days"
)

fig_delay.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

fig_delay.update_layout(
    height=500,
    margin=dict(
        l=20,
        r=20,
        t=70,
        b=80
    )
)

st.plotly_chart(
    fig_delay,
    use_container_width=True
)

# ============================================================
# DELIVERY PERFORMANCE BY REGION
# ============================================================

st.subheader("🚚 Delivery Performance by Region")

# ------------------------------------------------------------
# Count delivery status by region
# ------------------------------------------------------------

delivery_region = (
    filtered_df
    .groupby(
        ["Order Region", "Delivery Status"],
        as_index=False
    )
    .size()
    .rename(columns={"size": "Orders"})
)

# ------------------------------------------------------------
# Create chart
# ------------------------------------------------------------

fig_delivery_region = px.bar(
    delivery_region,
    x="Order Region",
    y="Orders",
    color="Delivery Status",
    barmode="group",
    title="Delivery Performance by Region",
    labels={
        "Order Region": "Region",
        "Orders": "Number of Orders",
        "Delivery Status": "Delivery Status"
    }
)

fig_delivery_region.update_layout(
    height=550,
    xaxis_tickangle=-35,
    margin=dict(
        l=20,
        r=20,
        t=70,
        b=120
    )
)

st.plotly_chart(
    fig_delivery_region,
    use_container_width=True
)

# ============================================================
# SALES & PROFIT BY SHIPPING MODE
# ============================================================

st.subheader("🚢 Sales & Profit by Shipping Mode")

# ------------------------------------------------------------
# Calculate sales and profit
# ------------------------------------------------------------

shipping_performance = (
    filtered_df
    .groupby("Shipping Mode", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

# ------------------------------------------------------------
# Convert to long format
# ------------------------------------------------------------

shipping_chart = shipping_performance.melt(
    id_vars="Shipping Mode",
    value_vars=["Sales", "Profit"],
    var_name="Metric",
    value_name="Value"
)

# ------------------------------------------------------------
# Create chart
# ------------------------------------------------------------

fig_shipping = px.bar(
    shipping_chart,
    x="Shipping Mode",
    y="Value",
    color="Metric",
    barmode="group",
    title="Sales & Profit by Shipping Mode",
    labels={
        "Shipping Mode": "Shipping Mode",
        "Value": "Amount",
        "Metric": "Metric"
    }
)

fig_shipping.update_layout(
    height=500,
    margin=dict(
        l=20,
        r=20,
        t=70,
        b=80
    )
)

st.plotly_chart(
    fig_shipping,
    use_container_width=True
)

# ============================================================
# REGIONAL SALES VS PROFIT ANALYSIS
# ============================================================

st.subheader("🌍 Regional Sales vs Profit")

# ------------------------------------------------------------
# Calculate sales and profit by region
# ------------------------------------------------------------

regional_performance = (
    filtered_df
    .groupby("Order Region", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

# ------------------------------------------------------------
# Create scatter plot
# ------------------------------------------------------------

fig_regional = px.scatter(
    regional_performance,
    x="Sales",
    y="Profit",
    size="Sales",
    hover_name="Order Region",
    hover_data={
        "Sales": ":,.0f",
        "Profit": ":,.0f"
    },
    title="Sales vs Profit by Region",
    labels={
        "Sales": "Total Sales",
        "Profit": "Total Profit",
        "Order Region": "Region"
    }
)

fig_regional.update_layout(
    height=550,
    margin=dict(
        l=20,
        r=20,
        t=70,
        b=50
    )
)

st.plotly_chart(
    fig_regional,
    use_container_width=True
)

# ============================================================
# PROFIT MARGIN BY SHIPPING MODE
# ============================================================

st.subheader("💰 Profit Margin by Shipping Mode")

# ------------------------------------------------------------
# Calculate sales and profit
# ------------------------------------------------------------

shipping_margin = (
    filtered_df
    .groupby("Shipping Mode", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

# ------------------------------------------------------------
# Calculate profit margin
# ------------------------------------------------------------

shipping_margin["Profit Margin %"] = (
    shipping_margin["Profit"]
    / shipping_margin["Sales"]
    * 100
)

# Remove invalid values
shipping_margin = shipping_margin.replace(
    [np.inf, -np.inf],
    np.nan
).dropna(
    subset=["Profit Margin %"]
)

# ------------------------------------------------------------
# Create chart
# ------------------------------------------------------------

fig_shipping_margin = px.bar(
    shipping_margin.sort_values(
        "Profit Margin %",
        ascending=False
    ),
    x="Shipping Mode",
    y="Profit Margin %",
    title="Profit Margin by Shipping Mode",
    labels={
        "Shipping Mode": "Shipping Mode",
        "Profit Margin %": "Profit Margin (%)"
    },
    text="Profit Margin %"
)

fig_shipping_margin.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

fig_shipping_margin.update_layout(
    height=500,
    margin=dict(
        l=20,
        r=20,
        t=70,
        b=80
    )
)

st.plotly_chart(
    fig_shipping_margin,
    use_container_width=True
)

# ============================================================
# CATEGORY SALES VS PROFIT ANALYSIS
# ============================================================

st.subheader("📊 Category Sales vs Profit")

# ------------------------------------------------------------
# Calculate sales and profit by category
# ------------------------------------------------------------

category_performance = (
    filtered_df
    .groupby("Category Name", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

# ------------------------------------------------------------
# Create scatter plot
# ------------------------------------------------------------

fig_category_scatter = px.scatter(
    category_performance,
    x="Sales",
    y="Profit",
    size="Sales",
    hover_name="Category Name",
    hover_data={
        "Sales": ":,.0f",
        "Profit": ":,.0f"
    },
    title="Sales vs Profit by Category",
    labels={
        "Sales": "Total Sales",
        "Profit": "Total Profit",
        "Category Name": "Category"
    }
)

fig_category_scatter.update_layout(
    height=550,
    margin=dict(
        l=20,
        r=20,
        t=70,
        b=50
    )
)

st.plotly_chart(
    fig_category_scatter,
    use_container_width=True
)

# ============================================================
# TOP CATEGORIES BY PROFIT MARGIN
# ============================================================

st.subheader("🏅 Top Categories by Profit Margin")

# ------------------------------------------------------------
# Calculate category sales and profit
# ------------------------------------------------------------

top_category_margin = (
    filtered_df
    .groupby("Category Name", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

# ------------------------------------------------------------
# Calculate profit margin
# ------------------------------------------------------------

top_category_margin["Profit Margin %"] = (
    top_category_margin["Profit"]
    / top_category_margin["Sales"]
    * 100
)

# Remove invalid values
top_category_margin = (
    top_category_margin
    .replace([np.inf, -np.inf], np.nan)
    .dropna(subset=["Profit Margin %"])
    .sort_values("Profit Margin %", ascending=False)
    .head(10)
)

# ------------------------------------------------------------
# Create horizontal bar chart
# ------------------------------------------------------------

fig_category_margin = px.bar(
    top_category_margin.sort_values(
        "Profit Margin %",
        ascending=True
    ),
    x="Profit Margin %",
    y="Category Name",
    orientation="h",
    title="Top 10 Categories by Profit Margin",
    labels={
        "Profit Margin %": "Profit Margin (%)",
        "Category Name": "Category"
    },
    text="Profit Margin %"
)

fig_category_margin.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

fig_category_margin.update_layout(
    height=550,
    margin=dict(
        l=20,
        r=80,
        t=70,
        b=50
    )
)

st.plotly_chart(
    fig_category_margin,
    use_container_width=True
)

# ============================================================
# FILTERED DATA EXPLORER
# ============================================================

st.subheader("📋 Filtered Data Explorer")

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=500
)

# ============================================================
# DOWNLOAD FILTERED DATA
# ============================================================

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Filtered Data (CSV)",
    data=csv,
    file_name="filtered_supply_chain_data.csv",
    mime="text/csv"
)

# ============================================================
# FILTERED DATA EXPLORER
# ============================================================

st.markdown("---")

st.subheader("📋 Filtered Data Explorer")

st.caption(
    "Explore the records based on the filters selected in the sidebar."
)

if filtered_df.empty:
    st.warning("No records match the selected filters.")
else:
    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=450
    )

    # Download filtered data
    csv_data = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Filtered Data (CSV)",
        data=csv_data,
        file_name="filtered_supply_chain_data.csv",
        mime="text/csv",
        use_container_width=False,
        key="filtered_data_download"
    )

# ============================================================
# DASHBOARD FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align: center; padding: 10px;">

    <h4>Supply Chain & Logistics Analytics</h4>

    <p>
    Interactive Data Science Dashboard for Sales, Profitability,
    Logistics, Product, and Regional Performance Analysis.
    </p>

    <p style="font-size: 13px;">
    Built with Python • Pandas • Plotly • Streamlit
    </p>

    </div>
    """,
    unsafe_allow_html=True
)