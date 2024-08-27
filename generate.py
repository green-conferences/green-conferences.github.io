import pandas as pd

file_path = 'data.csv'
readme_file_path = 'README.md'


def create_text(row):
    return f"""### {row['Name']}

- **URL**: {row['Url']}
- **Date**: {row['Conference Start Date']}
- **Call for papers Date**: {row['Call for Papers Date'] if pd.notna(row['Call for Papers Date']) else 'N/A'}
- **Location**: {row['Location']}
- **Type**: {row['Type']}
"""


data = pd.read_csv(file_path, delimiter=';')
texts = data.apply(create_text, axis=1)
output_text = "\n".join(texts)

with open(readme_file_path, 'r') as file:
    readme_content = file.read()

split_content = readme_content.split("## Conferences", 1)

new_readme_content = split_content[0] + "## Conferences\n\n" + output_text

with open(readme_file_path, 'w') as file:
    file.write(new_readme_content)