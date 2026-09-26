import sys

path = 'e:/Gihub/71.Mobile-Harness/src/index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

replacement = '<button class="header-btn icon-only" id="workspaceBtn" title="Set Agent Workspace" aria-label="Set Agent Workspace">📁</button>\n            <button class="header-btn icon-only" id="exportBtn"'
content = content.replace('<button class="header-btn icon-only" id="exportBtn"', replacement)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
