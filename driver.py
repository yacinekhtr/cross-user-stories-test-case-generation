import subprocess
import sys
import os
import re

def execute_script(script_path, output_file):
    try:
        result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
        output = result.stdout
        if result.stderr:
            output += "\nError:\n" + result.stderr
        
        # Write the output to a file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(output)
        
        # Print the output to the terminal
        print(output)
    except Exception as e:
        print(f"An error occurred: {e}")

# Path to the feature1 script
feature1_script = 'feature1_difference.py'
# Path to the output file for feature1
output_file_feature1 = 'feature1_results.txt'

# Execute the feature1 script and write the output to a file
execute_script(feature1_script, output_file_feature1)

# Path to the feature2 script
feature2_script = 'feature2_topics.py'
# Path to the output file for feature2
output_file_feature2 = 'feature2_results.txt'

# Execute the feature2 script and write the output to a file
execute_script(feature2_script, output_file_feature2)


# Define paths for input and output files
feature1_results_path = 'C:\\Users\\YacineKHITER\\cross-user-stories-test-case-generation\\feature1_results.txt'
feature2_results_path = 'C:\\Users\\YacineKHITER\\cross-user-stories-test-case-generation\\feature2_results.txt'
output_folder = 'C:\\Users\\YacineKHITER\\cross-user-stories-test-case-generation'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

def load_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_user_stories_from_feature1(content):
    stories = {}
    current_story = []
    current_id = None
    for line in content.split('\n'):
        if line.startswith('ID '):
            if current_id:
                stories[current_id] = '\n'.join(current_story)
            current_id = line.split(' ')[1]
            current_story = [line]
        else:
            current_story.append(line)
    if current_id:
        stories[current_id] = '\n'.join(current_story)
    return stories

def extract_clusters_from_feature2(content):
    clusters = {}
    current_cluster = None
    for line in content.split('\n'):
        if line.startswith('Cluster:'):
            current_cluster = int(line.split(': ')[1])
            clusters[current_cluster] = []
        elif line.startswith('ID '):
            story_id = line.split(' ')[1]
            if current_cluster is not None:
                clusters[current_cluster].append(story_id)
            else:
                print(f"Error: Found story ID '{line.strip()}' but no current cluster is set.")
        elif line.strip():  # Handle non-empty lines that do not start with 'Cluster:' or 'ID '
            print(f"Warning: Unrecognized line format '{line.strip()}'")
    return clusters

def extract_differences_from_feature1(content):
    differences = {}
    current_diff = []
    current_key = None
    for line in content.split('\n'):
        if line.startswith('Differences between '):
            if current_key:
                differences[current_key] = '\n'.join(current_diff)
            current_key = line.split(':')[0]
            current_diff = [line]
        else:
            current_diff.append(line)
    if current_key:
        differences[current_key] = '\n'.join(current_diff)
    return differences

def write_clustered_stories(clusters, user_stories, output_folder):
    for cluster_id, story_ids in clusters.items():
        with open(os.path.join(output_folder, f'cluster_{cluster_id}_stories.txt'), 'w', encoding='utf-8') as file:
            for story_id in story_ids:
                file.write(user_stories.get(story_id, '') + '\n\n')

def write_clustered_differences(clusters, differences, output_folder):
    for cluster_id, story_ids in clusters.items():
        with open(os.path.join(output_folder, f'cluster_{cluster_id}_differences.txt'), 'w', encoding='utf-8') as file:
            for i in range(len(story_ids)):
                for j in range(i + 1, len(story_ids)):
                    story1 = story_ids[i]
                    story2 = story_ids[j]
                    diff_key = f"Differences between {story1} and {story2}"
                    if diff_key in differences:
                        file.write(differences[diff_key] + '\n\n')

# Load content of both feature result files
feature1_content = load_file_content(feature1_results_path)
feature2_content = load_file_content(feature2_results_path)

# Extract user stories and differences from feature1 results
user_stories = extract_user_stories_from_feature1(feature1_content)
differences = extract_differences_from_feature1(feature1_content)

# Extract clusters from feature2 results
clusters = extract_clusters_from_feature2(feature2_content)

# Write clustered stories and differences to output files
write_clustered_stories(clusters, user_stories, output_folder)
write_clustered_differences(clusters, differences, output_folder)





def extract_and_move_differences(folder_path):
    try:
        # List all files in the folder
        files = os.listdir(folder_path)
        cluster_files = [file for file in files if re.match(r'cluster_\d+_stories\.txt', file)]

        for cluster_file in cluster_files:
            # Define paths for the cluster files
            cluster_stories_path = os.path.join(folder_path, cluster_file)
            cluster_differences_path = os.path.join(folder_path, cluster_file.replace('_stories', '_differences'))

            # Read the content of the cluster stories file
            with open(cluster_stories_path, 'r', encoding='utf-8') as file:
                content = file.readlines()

            # Separate user stories and differences
            user_stories = []
            differences = []
            current_section = user_stories

            for line in content:
                if line.startswith("Differences between "):
                    current_section = differences
                if current_section == differences and line.strip() == "================================================================================":
                    current_section = user_stories

                current_section.append(line)

            # Write user stories back to the stories file
            with open(cluster_stories_path, 'w', encoding='utf-8') as file:
                file.writelines(user_stories)

            # Write differences to the differences file
            with open(cluster_differences_path, 'w', encoding='utf-8') as file:
                file.writelines(differences)

            print(f"Processed {cluster_file} successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Define the folder path
output_folder = 'C:\\Users\\YacineKHITER\\cross-user-stories-test-case-generation'

# Execute the extraction and moving of differences
extract_and_move_differences(output_folder)

