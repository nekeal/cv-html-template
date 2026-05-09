from cv.utils import b

context = {
    "experience": [
        {
            "date": "03.2019 - now",
            "position": "Senior DevOps Engineer",
            "company": "TechCloud Solutions",
            "sections": [
                {
                    "section_title": "Cloud Infrastructure Management",
                    "experience": [
                        f"I designed and implemented a {b('multi-region')} infrastructure on {b('AWS')} that improved system reliability, achieving {b('99.99% uptime')} for critical services.",
                        f"I built a comprehensive {b('Infrastructure as Code')} solution using {b('Terraform')} and {b('CloudFormation')}, reducing deployment time by {b('75%')} and eliminating manual configuration errors.",
                        f"I orchestrated the migration of legacy systems to a {b('containerized architecture')} using {b('Kubernetes')}, resulting in {b('40% reduction')} in operational costs.",
                    ],
                },
                {
                    "section_title": "CI/CD Pipeline Optimization",
                    "experience": [
                        f"I developed and maintained {b('GitLab CI/CD')} pipelines that automated testing and deployment, reducing release cycles from {b('weeks to hours')}.",
                        f"I implemented {b('Blue/Green deployment')} strategies and {b('canary releases')}, reducing production incidents by {b('65%')}.",
                        f"I created a custom {b('Jenkins')} plugin to integrate with internal systems, streamlining release approval processes and improving team productivity by {b('30%')}.",
                    ],
                },
                {
                    "section_title": "Monitoring and Observability",
                    "experience": [
                        f"I established a comprehensive monitoring stack using {b('Prometheus')}, {b('Grafana')}, and {b('ELK stack')}, enabling real-time visibility into system performance.",
                        f"I designed and implemented {b('automated alerting')} systems that reduced mean time to detection for critical issues from {b('hours to minutes')}.",
                        f"I created custom {b('dashboards')} and {b('SLO tracking')} tools that helped engineering teams optimize application performance.",
                    ],
                },
            ],
        },
        {
            "date": "04.2017 - 02.2019",
            "position": "DevOps Engineer",
            "company": "InnovateSoft",
            "responsibilities": [
                f"I managed cloud infrastructure on {b('AWS')} and {b('GCP')}, including EC2, S3, RDS, and Kubernetes Engine.",
                f"I implemented {b('continuous integration')} pipelines using {b('Jenkins')} and {b('GitHub Actions')}.",
                f"I automated server provisioning with {b('Ansible')} and {b('Packer')}, reducing configuration time by {b('60%')}.",
            ],
        },
    ],
    "skills": [
        f"{b('Cloud Platforms')}: AWS (EC2, ECS, EKS, S3, RDS, Lambda), GCP (GKE, Cloud Storage, Cloud SQL).",
        f"{b('Infrastructure as Code')}: Terraform, CloudFormation, Pulumi.",
        f"{b('Containers & Orchestration')}: Docker, Kubernetes, Helm, Istio.",
        f"{b('CI/CD')}: Jenkins, GitLab CI, GitHub Actions, ArgoCD.",
        f"{b('Monitoring')}: Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana), Datadog.",
        f"{b('Scripting')}: Bash, Python, Go.",
        f"{b('Version Control')}: Git, GitHub, GitLab, Bitbucket.",
        f"{b('Security')}: Vault, AWS IAM, Secret Management, SAST/DAST tools.",
    ],
    "other_experience": [
        {
            "date": "11.2021",
            "title": "DevOpsDays Conference",
            "place": "Speaker",
            "description": f"I delivered a talk on {b('GitOps principles')} and demonstrated how to implement them with {b('ArgoCD')} and {b('Flux')}.",
        },
        {
            "date": "05.2020",
            "title": "Internal Knowledge Sharing",
            "place": "Workshop Lead",
            "description": f"I conducted a series of workshops on {b('Kubernetes')} for developers, helping bridge the gap between development and operations teams.",
        },
        {
            "date": "09.2019",
            "title": "Open Source Contribution",
            "place": "Project Maintainer",
            "description": f"I contributed to and later maintained an open-source {b('Terraform')} provider for internal services, which has been adopted by several teams across the organization.",
        },
    ],
}
