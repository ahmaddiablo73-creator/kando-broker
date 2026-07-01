import os
content = """<template>
  <div class='kando-component'>
    <h1>{{ title }}</h1>
    <p>{{ content }}</p>
  </div>
</template>
<script>
export default {
  props: ['title', 'content']
}
</script>"""

path = r"D:\BIO-WEB\src\components\KandoPanel.vue"
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("File successfully injected.")
