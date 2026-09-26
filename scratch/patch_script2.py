import sys
import re

path = 'e:/Gihub/71.Mobile-Harness/src/script.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace `await runStreamingResponse({` with `const ctx = await runStreamingResponse({`
content = re.sub(
    r'(\s+)await runStreamingResponse\(\{\s+payload: chatPayload,',
    r'\1const ctx = await runStreamingResponse({\n\1    payload: chatPayload,',
    content
)

# Insert processWorkspaceArtifacts after runStreamingResponse block in handleChatSubmit
# The end of that block is `});\n        });\n\n        // ========== Append Message ==========`
content = re.sub(
    r'(\s+)(ctx\.responseContainer\.insertAdjacentHTML.*?)\n(\s+)\}\n(\s+)\}\);\n(\s+)\}\);',
    r'\1\2\n\3}\n\4});\n\n\4if (ctx && ctx.fullRawText) {\n\4    await processWorkspaceArtifacts(ctx.fullRawText);\n\4}\n\5});',
    content
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
