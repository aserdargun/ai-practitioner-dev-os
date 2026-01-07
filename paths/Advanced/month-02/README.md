# Month 02: Data Engineering

**Tier**: 1 (Foundations)
**Duration**: 4 weeks
**Status**: ⏳ Upcoming

---

## Objectives

By the end of this month, you will:

1. Build robust data pipelines
2. Implement data validation with Pydantic
3. Handle data quality issues
4. Create reproducible data workflows

---

## Weekly Breakdown

### Week 1: Data Loading & Exploration

**Focus**: Load and understand data

**Tasks**:
- [ ] Load data from various formats (CSV, JSON, Parquet)
- [ ] Perform exploratory data analysis (EDA)
- [ ] Document data quality issues
- [ ] Use the EDA skill playbook

**Deliverables**:
- EDA notebook with findings
- Data quality report

### Week 2: Data Validation

**Focus**: Ensure data quality

**Tasks**:
- [ ] Create Pydantic models for data schemas
- [ ] Implement validation rules
- [ ] Handle validation errors gracefully
- [ ] Write tests for validation logic

**Deliverables**:
- Pydantic data models
- Validation pipeline
- Validation tests

### Week 3: Data Transformation

**Focus**: Build transformation pipelines

**Tasks**:
- [ ] Create transformation functions
- [ ] Handle missing data strategies
- [ ] Implement feature engineering basics
- [ ] Create reusable pipeline components

**Deliverables**:
- Transformation pipeline
- Feature engineering functions
- Pipeline tests

### Week 4: Data Pipeline Project

**Focus**: End-to-end pipeline

**Tasks**:
- [ ] Build complete data pipeline
- [ ] Add logging and monitoring
- [ ] Document the pipeline
- [ ] Create CLI interface

**Deliverables**:
- Complete data pipeline
- Documentation
- CLI tool

---

## Resources

### Documentation
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [Pydantic Docs](https://docs.pydantic.dev/)

### Skills
- [EDA to Insight](../../../.claude/skills/eda.md)

### Templates
- [Data Pipeline Template](../../../templates/template-data-pipeline/)

---

## Project: Data Processing Pipeline

Build a pipeline that:
1. Loads data from multiple sources
2. Validates against schema
3. Transforms and cleans
4. Outputs in multiple formats

**Bonus challenges**:
- Add data versioning
- Implement incremental processing
- Add data lineage tracking

---

## Success Criteria

- [ ] Can load data from 3+ formats
- [ ] Validation catches all invalid data
- [ ] Transformations are tested
- [ ] Pipeline runs end-to-end

---

## Navigation

- [Previous: Month 01](../month-01/README.md)
- [Back to Dashboard](../README.md)
- [Next: Month 03](../month-03/README.md)
