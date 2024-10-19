from contributors import contributors

def generate_readme(contributor, size=100, cols=6):
    md_output = "## Contributors\n\n<table>\n  <tr>\n"
    
    count = 0
    for person in contributor:
        name = person['name']
        username = person['username']
        # Add a new column for each contributor
        md_output += f'<td align="center">\n'
        md_output += f'<img src="https://github.com/{username}.png?size={size}" alt="{name}" />\n'
        md_output += f'<br /><strong>{name}</strong>\n'
        md_output += f'</td>\n'
        count += 1
        
        # After every 5 contributors, close the row and start a new one
        if count % cols == 0:
            md_output += "  </tr>\n  <tr>\n"
    
    # Close any open rows or table tags
    md_output += "  </tr>\n</table>\n"
    
    return md_output

markdown_content = generate_readme(contributors)
print(markdown_content)

with open("README.md", "w") as file:
    file.write(markdown_content)

    
