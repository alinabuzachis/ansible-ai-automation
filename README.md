# AWS Generative AI and MLOps Automation with Ansible (`amazon.ai` Collection)

This repository contains the executable Ansible playbooks featured in the blog post, "[Automation Unleashed: Managing Generative AI with the New amazon.ai Ansible Collection]".

The playbooks demonstrate Infrastructure-as-Code (IaC) principles applied to **Amazon Bedrock Agents**, **Foundation Model invocation**, and **Amazon DevOps Guru monitoring**.

## Prerequisites

1.  **Ansible Core** (v2.17 or newer recommended).
2.  **Python** (v3.9 or newer).
4.  **Boto3 and Botocore** Python libraries.

## Installation and Setup

### 1. Install Required Ansible Collections

This project requires modules from three different collections. For detailed documentation and prerequisites (such as Python dependencies like `boto3`), **refer to the documentation for each respective collection.**

The following `requirements.yml` file defines these necessary dependencies:

```yaml
collections:
  # Contains all Amazon Bedrock and DevOps Guru modules
  - name: amazon.ai
  
  # Required for core AWS resource management (IAM, Lambda, S3)
  - name: amazon.aws
  
  # Required for auxiliary AWS services (SNS, SQS)
  - name: community.aws
```

## Playbook Execution Guide

All playbooks are located in the ``playbooks/`` directory and can be run using ``ansible-playbook <filename>``.

- **usecase_1_agent_lifecycle.yml**: Full IT Support Agent Deployment - Provisions IAM/Lambda, creates the Bedrock Agent, configures the Action Group, sets an Alias, validates the agent flow, and audits the final config.

- **usecase_2_model_invoke.yml**: Personalized Content Generation.

- **usecase_3_devops_guru.yml**: Monitoring Configuration & Incident Audit - Configures DevOps Guru resource collection via tags, sets up SNS notifications, queries recent insights/recommendations, and outputs the full diagnostic audit.

## Running a Playbook

Set your AWS region, ensure IAM roles are prepared, and run the playbook:

```
# Example: Deploying the DevOps Guru configuration
export AWS_REGION='us-east-1'
ansible-playbook playbooks/usecase_3_devops_guru.yml
````

## License

This project is licensed under the GPL-3.0 License.
