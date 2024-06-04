# Read and display the content of the JSON file to check for formatting issues
file_path = '/Users/peiwen/Desktop/gabd-project/gbad-project.github.io/gbad/ADD/RG 10-145.json'
with open(file_path, 'r') as file:
    file_content = file.read()

print(file_content)
