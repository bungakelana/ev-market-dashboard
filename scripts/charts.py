
plt.figure(figsize=(12,7))

sns.lineplot(
    data=filtered_sales,
    x='year',
    y='annual_sales_units',
    hue='brand',
    marker='o',
    palette='Set1'
)

plt.title("Sales Trends (Top 5 Brands)")
plt.xlabel("Year")
plt.ylabel("Annual Sales Units")

plt.tight_layout()
plt.show()


#MARKET
fig_market = px.pie(
        market,
        names="brand",
        values="sales_units",
        title="EV Market Share by Brand (2026)"
    )
    fig_market.update_layout(
        title_x=0.5,
        template="plotly_white"
    )