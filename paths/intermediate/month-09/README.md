# Month 09: Cloud Deployment

**Focus**: Deploy ML systems to cloud platforms (AWS, Azure, or GCP).

---

## Why It Matters

Most production ML runs in the cloud. Understanding cloud services, managed ML platforms, and deployment patterns is essential for ML engineers. This month bridges local development with production infrastructure.

**Job Relevance**: Required for most ML engineering roles; cloud skills are highly valued.

---

## Prerequisites

- Month 01-08 complete
- Docker proficiency
- Basic networking concepts
- API development experience

---

## Learning Goals

**Tier 2 Technologies**:
- AWS, Azure, or GCP (choose one)
- S3/Blob Storage
- Lambda/Azure Functions (serverless)
- SageMaker/Azure ML/Vertex AI (ML platforms)
- API Gateway
- Container services

**Skills**:
- Cloud architecture basics
- Managed ML services
- Serverless deployment
- Cost management

---

## Main Project: Cloud ML Service

Deploy an ML model to a cloud platform with proper architecture.

### Deliverables

1. **Cloud Architecture** diagram
2. **Deployed Model** on managed service or containers
3. **API Endpoint** with authentication
4. **Infrastructure as Code** (optional but recommended)
5. **Cost Analysis** document

### Definition of Done

- [ ] Cloud account set up with proper IAM
- [ ] Model uploaded to cloud storage
- [ ] Deployment method chosen and implemented
- [ ] API endpoint accessible
- [ ] Basic authentication in place
- [ ] Health monitoring configured
- [ ] Cost monitoring enabled
- [ ] Latency and throughput tested
- [ ] Documentation complete
- [ ] Can update model without downtime

---

## Stretch Goals

- [ ] Infrastructure as Code (Terraform/CloudFormation)
- [ ] Auto-scaling configured
- [ ] Multi-region deployment
- [ ] Blue-green deployment

---

## Weekly Cadence

### Week 1: Cloud Setup
- Create cloud account
- Understand IAM and security
- Set up storage
- Upload model artifacts

### Week 2: Deployment
- Choose deployment approach
- Deploy model
- Configure endpoint
- Add authentication

### Week 3: Production Readiness
- Add monitoring
- Test performance
- Configure scaling
- Cost optimization

### Week 4: Document & Ship
- Architecture documentation
- Cost analysis
- Demo and write-up
- Retrospective

---

## Claude Prompts

### Planning
```
/plan-week

Starting Month 9 on cloud deployment. I want to deploy to AWS.
Help me plan the architecture and deployment approach.
```

### Building
```
/ship-mvp

I've deployed my model to SageMaker endpoint. It's working but:
- Latency is 500ms
- Cost is higher than expected
What should I optimize?
```

### Review
```
/harden

Review my cloud deployment for:
- Security (IAM, secrets)
- Cost efficiency
- Reliability
- Monitoring
```

### Research
```
Researcher, compare SageMaker, Azure ML, and Vertex AI for
deploying a transformer model. What are the trade-offs?
```

---

## How to Publish

### Demo
- Show live API call
- Demonstrate monitoring dashboard
- Walk through architecture

### Write-up
- "Deploying ML to the Cloud: Lessons Learned"
- Include architecture diagram
- Share cost analysis

---

## Resources

### AWS
- [SageMaker Documentation](https://docs.aws.amazon.com/sagemaker/)
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/)

### Azure
- [Azure ML Documentation](https://docs.microsoft.com/azure/machine-learning/)
- [Azure Architecture Center](https://docs.microsoft.com/azure/architecture/)

### GCP
- [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)
- [GCP Architecture Center](https://cloud.google.com/architecture)

---

## Next Month Preview

**Month 10**: Observability — Set up monitoring, logging, and alerting for ML systems.
