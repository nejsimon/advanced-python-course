# Coding Challenge: CI/CD Pipelines

In this challenge, you will design and implement a CI/CD pipeline for a Python project. The pipeline should enforce code quality, run tests, and optionally build and deploy the project.

## 1. Setup

- Create a sample Python project with at least:
  - One module (math_utils.py) containing simple functions.
  - One test file (test_math_utils.py) using pytest.

## 2. Linting & Formatting

- Add a linter (flake8 or ruff) and a formatter (black).
_ Ensure your pipeline fails if linting/formatting rules are violated.

## 3. Testing

- Configure the pipeline to:
- Run all tests with pytest.
- Generate a coverage report (pytest --cov).

## 4. Packaging

- Add a build step that creates a Python distribution (python -m build).
- Ensure artifacts are stored (e.g., .whl or .tar.gz).

## 5. Deployment (Optional Advanced Task)

- If deploying to PyPI, configure the pipeline to upload only on main branch pushes.
- If using Docker, build and push a Docker image to DockerHub.

## 6. CI/CD Service
 
- Choose one of the following (or another you prefer):
  - GitHub Actions
  - GitLab CI/CD
  - Jenkins
  - CircleCI

Implement the workflow in the corresponding YAML configuration file.

## Example Challenge Extension

- Add matrix builds for multiple Python versions (3.9, 3.10, 3.11).
- Cache dependencies to speed up builds.
- Use environment variables and secrets for credentials.

## Deliverables

- A sample Python project (src/ + tests/).
- A working CI/CD configuration (.github/workflows/ci.yml, .gitlab-ci.yml, or Jenkinsfile).

## Documentation in your project’s README explaining how the pipeline works.

Evaluation Criteria
- Pipeline runs automatically on pushes and pull requests.
- Linting and formatting checks included.
- Tests run and must pass.
- Build artifacts generated.

Bonus: Deployment to PyPI or DockerHub.

## Stretch Goal
Add a stage that runs integration tests in a Dockerized environment (e.g., with a PostgreSQL service container).