import re
import sys

def markdown_to_html(markdown):
    # Headers
    markdown = re.sub(r'(?u)^###\s*(.+)$', r'<h3>\1</h3>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'(?u)^##\s*(.+)$', r'<h2>\1</h2>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'(?u)^#\s*(.+)$', r'<h1>\1</h1>', markdown, flags=re.MULTILINE)

    # Bold
    markdown = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', markdown)

    # Italic
    markdown = re.sub(r'\*(.+?)\*', r'<i>\1</i>', markdown)

    # Numbered list
    markdown = re.sub(r'(?u)^(\d+)\.\s+(.+)$', r'<li>\2</li>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'(?<=<\/li>)(?=<li>)', '\n', markdown)
    markdown = '<ol>\n' + markdown + '</ol>'

    # Links
    markdown = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', markdown)

    # Images
    markdown = re.sub(r'!\[([^\]]+)\]\(([^\)]+)\)', r'<img src="\2" alt="\1"/>', markdown)

    return markdown

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py input_file")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, "r", encoding="utf-8") as file:
        markdown_text = file.read()

    html_output = markdown_to_html(markdown_text)

    with open("output.html", 'w+', encoding='iso-8859-1') as file:
        file.write(html_output)

    print("O HTML foi gerado com sucesso e salvo em 'output.html'.")
