# Cross-User Stories Test Case Generation

This project is designed to analyze and compare user stories extracted from Word documents, using natural language processing (NLP) techniques and clustering. The project consists of two main features:

1. **Feature 1: Analysis of Differences Between User Stories**
2. **Feature 2: Clustering of User Stories by Topics**

## Prerequisites

Make sure you have the following installed on your machine:

- Python 3.x
- `pip` for installing Python packages
- [virtualenv](https://pypi.org/project/virtualenv/) to create a virtual environment

### Installing Dependencies

1. Clone this repository to your local machine.
2. Navigate to the project directory:
   ```bash
   cd cross-user-stories-test-case-generation


### Create a virtual environment:

- python -m venv myenv

### Activate the virtual environment:
### On Windows:

.\myenv\Scripts\activate

### On macOS/Linux:

source myenv/bin/activate

### Install the required dependencies:

- pip install -r requirements.txt

### Project Structure

driver.py: The main file that runs the feature1_difference.py and feature2_topics.py scripts, processes the results, and organizes the outputs into the appropriate files.
feature1_difference.py: Script to extract and compare user stories by identifying the differences between them.
feature2_topics.py: Script to perform clustering of user stories based on topics identified by LDA (Latent Dirichlet Allocation).
User stories/Paquet 1/: Directory containing the Word (.docx) files of the user stories to be analyzed.
Usage
Place your Word files containing the user stories in the User stories/Paquet 1/ folder.

### Run the driver.py file:


python driver.py
The results will be stored in files within the cross-user-stories-test-case-generation directory:

cluster_<number>_stories.txt: Contains the user stories grouped by clusters.
cluster_<number>_differences.txt: Contains the differences identified between the user stories in the same cluster.
Running the Individual Scripts
You can also run the feature1_difference.py and feature2_topics.py scripts separately if needed:

### To analyze differences:

python feature1_difference.py

### To perform clustering of the user stories:

python feature2_topics.py

### Customization

You can customize the file paths and parameters directly in the driver.py file or in the individual scripts according to your needs.

### Common Issues 

Virtual Environment Activation
If you encounter issues activating the virtual environment on Windows, ensure that script execution is allowed. You can run this command in PowerShell as an administrator:


Set-ExecutionPolicy RemoteSigned
Import Errors
Ensure that all dependencies are installed correctly with pip install -r requirements.txt.

### Contribution

Contributions are welcome! Feel free to suggest improvements or report issues via pull requests or issues.

License
This project is licensed under the MIT License. See the LICENSE file for details.

markdown
Copy code

### Notes

- This `README.md` file serves as a basic guide and can be adapted to your specific needs.
- If you need to add any additional dependencies, be sure to include them in the `requirements.txt` file.
- Ensure that the paths and filenames in your code match what you actually have in your project.


## Workflow Overview
The diagram below illustrates the end-to-end workflow for generating test cases based on user stories provided by the user through the AAQE platform. The process is automated through the execution of several Python scripts, which analyze and cluster the user stories and then generate a set of outputs, including test cases.

![Workflow Diagram](C:\\Users\YacineKHITER\\cross-user-stories-test-case-generation\\Workflow end-to-end test cases_page-0001.jpg)


### Workflow Steps:

Input User Stories:  The user inputs one or multiple user stories into the AAQE platform.

Execution of driver.py:

This script automates the execution of the feature scripts and queries the Large Language Model (LLM) to generate insights and test cases.

Execution of feature1_differences.py:

This script extracts and compares the user stories, identifying differences between them.
Output: It generates a feature1_difference.txt file containing the content of the user stories along with the identified differences.

Execution of feature2_topics.py:

This script identifies the topics of the user stories and groups them into clusters using the LDA (Latent Dirichlet Allocation) algorithm.

Output: It generates a feature2_topics.txt file containing the topics assigned to each user story and the cluster to which they belong.

Query Execution to LLM:

The system queries the LLM (such as LLaMA, GPT, etc.) using the IBM Cloud platform, particularly leveraging WatsonX instances on the TechZone.

Output: This step results in the generation of a text file containing end-to-end test cases.

Final Output:

The final outputs include:
feature1_difference.txt: Details of the user stories and their differences.
feature2_topics.txt: Clustered user stories with assigned topics.
cluster_X_stories.txt: Contains the content of the user stories within the same cluster.
cluster_X_differences.txt: Contains the comparison of the user stories within the same cluster.
A text file with the generated end-to-end test cases.