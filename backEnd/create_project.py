import os

def create_project_structure(project_name):
    # Define the folder structure
    structure = {
        'venv': None,
        'templates': {
            'index.html': '<!-- Your HTML content here -->',
        },
        'static': {
            'css': None,
            'js': None,
            'img': None,
        },
        'app.py': 'from flask import Flask, render_template\n\n'
                   'app = Flask(__name__)\n\n'
                   '@app.route("/")\n'
                   'def home():\n'
                   '    return render_template("index.html")\n\n'
                   'if __name__ == "__main__":\n'
                   '    app.run(debug=True)',
        'requirements.txt': '',
        'README.md': '# Project Name\n\nProject description here.',
    }

    # Create the project directory
    os.makedirs(project_name, exist_ok=True)

    # Create the project structure
    for item, content in structure.items():
        item_path = os.path.join(project_name, item)

        if content is None:
            os.makedirs(item_path, exist_ok=True)
        else:
            with open(item_path, 'w') as file:
                if isinstance(content, str):
                    file.write(content)
                else:
                    file.write(str(content))

if __name__ == "__main__":
    project_name = input("Enter project name: ")
    create_project_structure(project_name)
    print(f"Project structure for '{project_name}' created successfully.")
