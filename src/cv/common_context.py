from cv.utils import b

common_context = {
    "name": "Alex Smith",
    "title": "DevOps Engineer",
    "subtitle": "Infrastructure Specialist",
    "summary": f"I'm a DevOps Engineer with over {b('seven years')} of commercial experience and a strong background in cloud technologies, recently "
    f"focusing on {b('Infrastructure as Code')}. I am passionate about building reliable, scalable systems and automating processes. "
    f"I believe that robust {b('CI/CD pipelines')} and monitoring solutions are crucial for "
    f"maintaining system reliability and developer productivity. Recently, I have been exploring {b('Kubernetes')} and {b('GitOps')} "
    f"to further improve the deployment and management of containerized applications.",
    "phone": "XXX-XXX-XXX",
    "email": "devops@example.com",
    "github_link": "github.com/alexdevops",
    "linkedin_link": "linkedin.com/in/alexdevops",
    "certificates": [
        f"{b('AWS Certified DevOps Engineer - Professional')}",
        f"{b('Certified Kubernetes Administrator (CKA)')}",
        f"{b('HashiCorp Certified: Terraform Associate')}",
        f"{b('Linux Foundation Certified System Administrator (LFCS)')}",
        f"Red Hat Certified Engineer ({b('RHCE')})",
    ],
    "education": [
        {
            "date": "09.2012 - 06.2016",
            "institution": "Tech University",
            "degree": "Bachelor's degree in Computer Science",
        }
    ],
    "languages": [f"English – {b('fluent')}", f"Spanish – {b('B1')}"],
}
