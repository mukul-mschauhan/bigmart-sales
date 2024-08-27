# Bigmart-Sales

### Steps to complete the Project

- Step1: Open gitbash and clone the repository by writing the following code in gitbash terminal git clone https://github.com/mukul-mschauhan/bigmart-sales.git

- Step 2: Once the cloning is done, write cd and repository name so that gitbash can go inside the repository for accessing puposes.

- Step 3: open the vscode by writing the following code on gitbash terminal code .

#### How to update the readme file

- step1: write git add . on gitbash
- step2: Pass the following command git commit -m "readme-updated"
- step3: git push origin main
  Refresh the repository and you will see that the readme file is updated.

### Creation of Template for Production Level Code

- Note: We will be using os library to create folders and files. The list of the files created will be
- template.py
- data_ingestion.py
- data_validation.py
- data.transformation.py
- model_trainer.py
- model_evaluation.py
- model_pusher.py

We need the above files for MLOps and here is a small description of each file.

### Core MLOps Components

- **init.py files:** These files, present in several directories, turn them into Python packages. This allows you to organize your code into logical units and easily import functionality between different parts of your project.

- **data_ingestion.py:** Handles the collection and loading of raw data from various sources into your ML pipeline.

- **data_validation.py:** Implements checks to ensure data quality, consistency, and completeness before further processing.

- **data_transformation.py:** Prepares data for modeling by cleaning, transforming, and feature engineering.

- **model_trainer.py:** Trains the ML model using the prepared data and evaluates its performance.

- **model_evaluation.py:** Compares different models or versions to select the best one for deployment.

- **model_pusher.py:** Deploys the trained model into a production environment for inference.

#### Configuration and Management

- **config_entity.py** & **artifact_entity.py:** These files define the structure for storing and managing configurations (like hyperparameters, data paths) and artifacts (like models, metrics) produced during the ML pipeline.
- **constants/**init**.py:** Centralizes important constants used throughout the project, ensuring consistency and easy modification.

#### Error Handling & Logging

- **exception/**init**.py:** Defines custom exceptions for handling errors gracefully within your pipeline.
- **logger/**init**.py:** Sets up logging mechanisms to record important events, errors, and metrics during the ML workflow, aiding debugging and monitoring.

#### Pipeline Orchestration

- **training_pipeline.py & prediction_pipeline.py:** Orchestrate the execution of the various components in the training and prediction phases, respectively.

#### Utilities

- **main_utils.py:** Contains helper functions or reusable code snippets for common tasks across your project.

#### Why so many files?

- Modularity & Reusability: Each file encapsulates a specific functionality, making components easier to understand, maintain, test, and reuse in different projects.
- Collaboration: Modular code promotes collaboration among team members working on different parts of the pipeline.
- Scalability: Modular architecture makes it easier to scale your ML system by adding or modifying components without disrupting the entire pipeline.
- MLOps Best Practices: This structure aligns well with MLOps principles, enabling better version control, continuous integration/continuous deployment (CI/CD), testing, monitoring, and overall management of the ML lifecycle.

  In summary, this modular file structure establishes a solid foundation for ML productionization. It enhances organization, maintainability, collaboration, and adherence to MLOps best practices, making your ML projects more robust and easier to manage in real-world deployment scenarios.

#### Links for the Tools:

- **Github**: www.git-scm.com
- **Flowchart**: https://whimsical.com/templates
- **MLOps Tool**: https://www.evidentlyai.com/

- Note: We will be using evidentlyai for MLOps. MLOps will be used in the next project.
