import os
import glob
import argparse
import markdown_it
from bs4 import BeautifulSoup

def main(args):
    """
    Function to convert all Markdown files in the specified directory to HTML files.
    """
    # Turn the specified path into a system path
    system_path = os.path.abspath(args.path)

    # delete all files in the specified directory that end with .html
    for f in glob.glob(f"{system_path}/*.html"):
        os.remove(f)

    # Get a list of all Markdown files in the specified directory
    markdown_files = glob.glob(f"{system_path}/*.md")

    # Loop for each Markdown file
    for path in markdown_files:

        # Read the Markdown file
        with open(path, "r") as file:
            markdown_text = file.read()

        # Initialize the parser
        translator = markdown_it.MarkdownIt()

        # Parse the Markdown text
        parsed_html = translator.render(markdown_text)

        # Initialize the HTML parser
        soup = BeautifulSoup(parsed_html, 'html.parser')

        # Find all anchor elements and add the target="_blank" attribute
        for a in soup.find_all('a'):
            a['target'] = '_blank'

        # Rename the file to -modified.md
        path_list = path.split(".")
        path_list[-1] = "html"
        new_path = ".".join(path_list).replace(".-","-")

        # Save the modified Markdown file
        with open(new_path, 'w') as file:
            file.write(str(soup))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Markdown files to HTML files.')
    parser.add_argument('-p', '--path', type=str, help='Path to the directory containing the Markdown files.')
    args = parser.parse_args()
    main(args)

# How to use:
# python markdown-html-converter.py -p ./EPS/truthfulness
