import os

def create_directory_structure(base_path):
    structure = {
        'index.md': '',
        'getting-started.md': '',
        'language-reference': {
            'overview.md': '',
            'syntax': {
                'basic-syntax.md': '',
                'types.md': '',
                'variables.md': '',
                'functions.md': '',
                'control-flow.md': '',
                'collections.md': '',
                'error-handling.md': ''
            },
            'advanced-concepts': {
                'memory-management.md': '',
                'traits.md': '',
                'generics.md': '',
                'operator-overloading.md': ''
            },
            'grammar.md': ''
        },
        'standard-library': {
            'overview.md': '',
            'core-types.md': '',
            'common-functions.md': ''
        },
        'faq.md': ''
    }

    def create_structure(current_path, structure):
        for key, value in structure.items():
            path = os.path.join(current_path, key)
            if isinstance(value, dict):
                os.makedirs(path, exist_ok=True)
                create_structure(path, value)
            else:
                with open(path, 'w') as f:
                    f.write(f"# {key.replace('-', ' ').replace('.md', '').title()}\n\nAdd content for {key} here.\n")

    create_structure(base_path, structure)

# Usage
create_directory_structure('docs')