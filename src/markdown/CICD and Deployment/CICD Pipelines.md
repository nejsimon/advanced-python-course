# CI/CD Pipelines

Continuous Integration (CI) and Continuous Deployment/Delivery (CD) are crucial practices in modern software development. They ensure that code is tested, validated, and deployed automatically, reducing the risk of regressions and speeding up delivery.

## Key Concepts
### Continuous Integration (CI)

Definition: Automatically integrating code changes into a shared repository and validating them with automated builds and tests.

Goals:
- Catch errors early.
- Ensure consistent build/test environments.
- Provide fast feedback to developers.
- Typical Tools: GitHub Actions, GitLab CI, Jenkins, CircleCI, Travis CI.

### Continuous Delivery (CD)

Definition: Automating the release process so that code is always in a deployable state.

- Key Practices:
- Automated testing pipelines.
- Staging environment deployments.
- Versioning and artifact management.

### Continuous Deployment

Definition: Every change that passes the pipeline is automatically deployed to production.

- Requires: High test coverage, strong monitoring, and rollback strategies.
- Example Pipeline Steps
- A typical Python project CI/CD pipeline might include:
- Linting & Formatting
- Run flake8, black, or ruff for code style and static checks.
- Testing
  - Run unit and integration tests via pytest.
  - Generate coverage reports.
- Build
  - Package the project using setuptools, poetry, or pip-tools.
  - Build a Docker image (if containerized).
- Deployment
  - Push the package to PyPI (for libraries).
  - Deploy to cloud (AWS, GCP, Azure, Heroku).
  - Use IaC (Infrastructure as Code) tools like Terraform or Ansible.

## Example: GitHub Actions Workflow
name: Python CI/CD

```yaml
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Lint with flake8
        run: flake8 .

      - name: Run tests
        run: pytest --maxfail=1 --disable-warnings -q

      - name: Build package
        run: python -m build

      - name: Deploy (example to PyPI)
        if: github.ref == 'refs/heads/main'
        env:
          TWINE_USERNAME: ${{ secrets.PYPI_USERNAME }}
          TWINE_PASSWORD: ${{ secrets.PYPI_PASSWORD }}
        run: |
          pip install twine
          twine upload dist/*
```

## Best Practices
- Keep pipelines fast – long-running jobs reduce feedback quality.
- Use caching (e.g., pip cache, Docker layers).
- Run tests in parallel where possible.
- Secure secrets with environment variables or secrets managers.
- Always include rollback and monitoring for CD pipelines.