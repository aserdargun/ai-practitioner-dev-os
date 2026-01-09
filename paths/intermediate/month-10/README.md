# Month 10: Observability

**Focus**: Set up comprehensive monitoring, logging, and alerting for ML systems.

---

## Why It Matters

You can't improve what you can't measure. Observability is critical for understanding system behavior, debugging production issues, and ensuring reliability. This month teaches you to build systems you can actually maintain.

**Job Relevance**: Essential for production ML roles; differentiates reliable engineers.

---

## Prerequisites

- Month 01-09 complete
- Cloud deployment experience
- API development experience

---

## Learning Goals

**Tier 2 Technologies**:
- Prometheus (metrics)
- Grafana (visualization)
- Structured logging
- Alerting systems
- CloudWatch/Datadog (optional)

**Skills**:
- Metrics design
- Dashboard creation
- Alert configuration
- Incident response basics

---

## Main Project: Monitored ML System

Add comprehensive observability to an existing ML service.

### Deliverables

1. **Metrics Instrumentation** for key signals
2. **Grafana Dashboard** visualizing system health
3. **Structured Logging** with request correlation
4. **Alert Rules** for critical conditions
5. **Runbook** for common alerts

### Definition of Done

- [ ] Four golden signals instrumented (latency, traffic, errors, saturation)
- [ ] ML-specific metrics added (prediction latency, model version)
- [ ] Prometheus scraping metrics
- [ ] Grafana dashboard with 4+ panels
- [ ] Structured JSON logging implemented
- [ ] Request IDs correlate logs
- [ ] At least 3 alert rules configured
- [ ] Alerts tested and working
- [ ] Runbook for each alert
- [ ] Documentation complete

---

## Stretch Goals

- [ ] Distributed tracing with OpenTelemetry
- [ ] Model performance monitoring (drift detection)
- [ ] SLO/SLI definition
- [ ] On-call rotation documentation

---

## Weekly Cadence

### Week 1: Metrics & Instrumentation
- Add prometheus_client
- Instrument key endpoints
- Set up Prometheus
- Verify metrics collection

### Week 2: Visualization
- Set up Grafana
- Create main dashboard
- Add ML-specific panels
- Test with traffic

### Week 3: Logging & Alerting
- Implement structured logging
- Configure log aggregation
- Set up alert rules
- Test alerts

### Week 4: Document & Ship
- Write runbooks
- Finalize documentation
- Demo and write-up
- Retrospective

---

## Claude Prompts

### Planning
```
/plan-week

Starting Month 10 on observability. I have my cloud ML service from Month 9.
Help me plan the monitoring and alerting setup.
```

### Skill Application
```
Apply the Observability Starter skill to my project.
I want to make sure I'm covering the basics.
```

### Building
```
/ship-mvp

I have:
- Prometheus metrics
- Basic Grafana dashboard
- JSON logging
What alerts should I set up first?
```

### Review
```
/harden

Review my observability setup for:
- Coverage gaps
- Alert fatigue risks
- Dashboard usefulness
- Logging quality
```

---

## How to Publish

### Demo
- Show dashboard under load
- Demonstrate alert firing
- Walk through log correlation

### Write-up
- "Making ML Observable: A Practical Guide"
- Include dashboard screenshots
- Share alert configurations

---

## Resources

### Skill Playbooks
- [Observability Starter](../../../.claude/skills/observability-starter.md)

### Documentation
- [Prometheus Documentation](https://prometheus.io/docs/)
- [Grafana Documentation](https://grafana.com/docs/)
- [OpenTelemetry](https://opentelemetry.io/docs/)

---

## Next Month Preview

**Month 11**: Advanced LLM — Build agentic systems with LangGraph.
