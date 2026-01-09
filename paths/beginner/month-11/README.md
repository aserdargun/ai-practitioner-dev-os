# Month 11: Interactive Dashboards

**Theme**: Build interactive data applications with Streamlit.

## Why It Matters

Dashboards make data accessible to non-technical stakeholders. They turn analyses into tools people actually use. Streamlit lets you create professional dashboards quickly—a high-value skill for any data role.

## Prerequisites

- Month 4 completed (visualization)
- Month 10 completed (Python web basics)
- Pandas and plotting proficiency

## Learning Goals

### Streamlit Fundamentals (Week 1-2)
- [ ] Streamlit installation and setup
- [ ] Basic elements (text, data, charts)
- [ ] User inputs (buttons, sliders, dropdowns)
- [ ] Layouts and columns
- [ ] Caching for performance
- [ ] Session state

### Interactive Features (Week 3)
- [ ] File uploaders
- [ ] Dynamic filtering
- [ ] Plotly integration
- [ ] Multi-page apps
- [ ] Connecting to data sources

### Deployment (Week 4)
- [ ] Streamlit Cloud deployment
- [ ] Environment configuration
- [ ] Sharing and embedding
- [ ] Performance optimization

## Main Project: Analytics Dashboard

Build a comprehensive analytics dashboard.

### Choose Your Focus
Pick a domain you've worked with:
- Sales analytics (Month 2 data)
- ML model explorer (Month 5-6 models)
- Time series forecaster (Month 7 model)
- Text analysis tool (Month 8 model)

### Deliverables
1. Interactive dashboard with:
   - Data overview page
   - Filtering and selection
   - Multiple visualizations
   - Summary statistics

2. Optional ML integration:
   - Model predictions in dashboard
   - What-if analysis

3. Deployment:
   - Live on Streamlit Cloud
   - Shareable link

### Definition of Done
- [ ] Dashboard runs locally
- [ ] At least 3 interactive elements
- [ ] Multiple chart types
- [ ] Data filtering works
- [ ] Deployed to Streamlit Cloud
- [ ] Can share with others

## Stretch Goals

- [ ] Add authentication
- [ ] Connect to database
- [ ] Real-time data updates
- [ ] Export to PDF/Excel
- [ ] Mobile-responsive design

## Weekly Breakdown

### Week 1: Streamlit Basics
- Installation and "Hello World"
- Basic elements
- First simple dashboard
- Learn layout options

### Week 2: Interactivity
- User inputs
- Dynamic updates
- Caching
- Build core dashboard

### Week 3: Advanced Features
- File upload
- Multi-page setup
- Plotly integration
- Polish UX

### Week 4: Deploy & Ship
- Streamlit Cloud setup
- Environment config
- Testing deployed app
- Share and demo

## Claude Prompts

### Planning
```
/plan-week
Month 11 Week 1 - Focus on Streamlit basics
I want to build a sales analytics dashboard
```

### Building
```
Ask the Builder to help me create a Streamlit
dashboard with sidebar filters for date range
and category, showing sales visualizations.
```

### Design Help
```
Ask the Researcher to suggest best practices
for dashboard layout and user experience.
What makes a dashboard useful vs confusing?
```

### Review
```
Ask the Reviewer to review my Streamlit app.
Is the code organized well? Any UX improvements?
```

## How to Publish

### Demo
1. Show the deployed dashboard
2. Walk through key features
3. Demonstrate interactivity
4. Show filtering in action
5. Explain the use case

### Write-up Topics
- Why dashboards matter
- Streamlit vs other tools
- UX decisions made
- Deployment experience

### Portfolio Entry
- Live deployed app
- GitHub with clean code
- Screenshots for non-live viewing

## Resources

### Streamlit
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Streamlit Cheat Sheet](https://cheat-sheet.streamlit.app/)

### Deployment
- [Streamlit Cloud](https://streamlit.io/cloud)
- [Deployment Guide](https://docs.streamlit.io/streamlit-community-cloud/get-started)

### Alternatives (Reference)
- [Dash by Plotly](https://dash.plotly.com/)
- [Panel](https://panel.holoviz.org/)

## Tips

1. **Start minimal** — Add features incrementally
2. **Use caching** — `@st.cache_data` for data loading
3. **Think mobile** — Many users view on phones
4. **Test interactions** — Every control should do something useful
5. **Get feedback early** — Show to non-technical users
