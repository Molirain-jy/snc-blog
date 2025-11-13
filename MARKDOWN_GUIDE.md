# Markdown 使用指南

本博客系统支持完整的 Markdown 语法，以下是常用语法示例：

## 标题

```markdown
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
```

## 文本样式

```markdown
**粗体文本**
*斜体文本*
~~删除线~~
`行内代码`
```

效果：
- **粗体文本**
- *斜体文本*
- ~~删除线~~
- `行内代码`

## 列表

### 无序列表
```markdown
- 项目 1
- 项目 2
  - 子项目 2.1
  - 子项目 2.2
- 项目 3
```

### 有序列表
```markdown
1. 第一项
2. 第二项
3. 第三项
```

## 链接和图片

```markdown
[链接文字](https://example.com)
![图片描述](图片URL)
```

## 引用

```markdown
> 这是一段引用文字
> 可以有多行
```

效果：
> 这是一段引用文字
> 可以有多行

## 代码块

### 行内代码
使用反引号包裹：`const name = 'Vue'`

### 代码块
使用三个反引号：

```javascript
function hello() {
  console.log('Hello, World!')
}
```

```python
def hello():
    print("Hello, World!")
```

```bash
npm install
npm run dev
```

## 表格

```markdown
| 标题1 | 标题2 | 标题3 |
|-------|-------|-------|
| 内容1 | 内容2 | 内容3 |
| 内容4 | 内容5 | 内容6 |
```

效果：

| 标题1 | 标题2 | 标题3 |
|-------|-------|-------|
| 内容1 | 内容2 | 内容3 |
| 内容4 | 内容5 | 内容6 |

## 分隔线

```markdown
---
或
***
```

---

## 任务列表

```markdown
- [x] 已完成任务
- [ ] 未完成任务
- [ ] 另一个任务
```

## 完整示例

```markdown
# Vue 3 组合式 API 教程

## 简介

Vue 3 带来了全新的 **组合式 API**，让我们的代码更加灵活和可维护。

## 核心概念

### 1. setup 函数

\`setup\` 函数是组合式 API 的入口点：

\`\`\`javascript
import { ref, computed } from 'vue'

export default {
  setup() {
    const count = ref(0)
    const double = computed(() => count.value * 2)
    
    return { count, double }
  }
}
\`\`\`

### 2. 响应式 API

主要的响应式 API 包括：

- `ref()` - 创建响应式引用
- `reactive()` - 创建响应式对象
- `computed()` - 计算属性
- `watch()` - 侦听器

> **提示**: 在 `<script setup>` 中不需要手动 return

## 最佳实践

1. 使用 `<script setup>` 语法
2. 合理拆分组合函数
3. 注意响应式引用的 `.value`

---

更多信息请访问 [Vue 官方文档](https://vuejs.org)
\`\`\`

## 编辑器功能

在博客编辑器中：
1. 在"正文"输入框中输入 Markdown 文本
2. 点击"👁️ 预览"按钮查看渲染效果
3. 点击"📝 编辑"返回编辑模式
4. 保存后前台会自动渲染为 HTML

## 技巧提示

1. **代码高亮**: 在代码块中指定语言（如 \`\`\`javascript）可以获得更好的语法高亮
2. **换行**: 在段落之间留空行可以创建新段落
3. **转义**: 使用反斜杠 `\` 可以转义特殊字符
4. **HTML**: 如果需要，也可以直接使用 HTML 标签

## 注意事项

- 保存前建议预览确认效果
- 代码块建议指定编程语言
- 图片 URL 必须是可访问的地址
- 大型图片建议压缩后再使用

---

愉快地写作吧！✍️
