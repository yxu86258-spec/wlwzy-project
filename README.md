# Karpathy风格长上下文知识库

这是一个基于Andrej Karpathy理念的个人知识库系统，使用长上下文LLM直接阅读整个知识库，无需RAG。

## 核心理念

- **无向量检索**: 纯Markdown存储，避免复杂的向量化流程
- **长上下文直读**: LLM读取完整知识库，实现完美召回
- **架构极简**: 零基础设施，只需文本编辑器和LLM API

## 功能特性

### 核心功能 (85分)

| 功能 | 描述 | 技术要点 |
|------|------|--------|
| **Ingest** | 多格式文档导入 | PDF解析、网页爬取、图片OCR |
| **Compile** ⭐ | LLM自动编译 | 实体识别、链接生成、Frontmatter元数据 |
| **Wiki管理** | Markdown组织 | 结构化存储、命名规范、双向链接 |
| **Query** | 长上下文问答 | 多轮对话、引用溯源、对话历史 |
| **Visualization** | 知识图谱 | PNG/GraphML/D3.js/HTML格式 |
| **Export** | 多格式导出 | HTML/Markdown/PDF |
| **Documentation** | 实验报告 | 架构设计、对比分析、案例展示 |

### 进阶功能 (15分)

| 功能 | 描述 |
|------|------|
| **Incremental Compile** | 增量编译：只更新改变的文件 |
| **Auto-Lint** | 自动健康检查：死链、孤立页面、元数据 |
| **Multi-session Chat** | 对话历史持久化 |
| **Knowledge Graph Export** | Gephi/D3.js格式导出 |

## 项目结构

```
wlwzy/
├── raw/                          # 原始资料
│   ├── *.pdf                    # PDF文件
│   ├── *.md                     # Markdown文件
│   └── _ingest_log.json         # 导入日志
├── wiki/                         # 编译后的wiki（Markdown）
├── scripts/                      # 核心脚本
│   ├── ingest.py               # 数据导入
│   ├── compile.py              # 知识编译
│   ├── query.py                # 问答系统
│   ├── visualize.py            # 图谱生成
│   ├── export.py               # 格式导出
│   ├── lint.py                 # 自动检查
│   ├── incremental_check.py    # 增量编译检查
│   ├── wiki_compiler.py        # 编译引擎
│   ├── wiki_linter.py          # Lint引擎
│   ├── chat_session.py         # 对话管理
│   └── incremental_compiler.py # 增量编译引擎
├── config/
│   └── config.yaml             # 配置文件
├── docs/                        # 输出文档
│   ├── experiment_report.md    # 实验报告
│   ├── knowledge_graph.png     # 图谱可视化
│   ├── knowledge_graph.graphml # Gephi格式
│   ├── knowledge_graph_d3.json # D3.js格式
│   ├── knowledge_graph.html    # HTML交互式图谱
│   └── chat_*.md               # 对话记录
├── tests/                       # 单元测试
├── kb_manager.py               # 中央管理工具
└── requirements.txt            # 依赖清单
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置API

编辑 `config/config.yaml`:

**选项A: 使用OpenAI**
```yaml
llm:
  provider: openai
  api_key: sk-xxxxx
  model: gpt-4
```

**选项B: 使用DeepSeek (推荐，更便宜)**
```yaml
llm:
  provider: deepseek
  api_key: sk-xxxxx
  model: deepseek-chat
  base_url: https://api.deepseek.com
```

**选项C: 使用本地Ollama (免费)**
```yaml
llm:
  provider: ollama
  base_url: http://localhost:11434
  model: llama2
```

### 3. 准备资料

将PDF、Markdown文件放入 `raw/` 目录:
```bash
cp your_documents.pdf raw/
```

### 4. 完整工作流

**方式1: 使用管理工具**
```bash
python kb_manager.py ingest       # 导入资料
python kb_manager.py compile      # 编译知识库
python kb_manager.py query        # 启动问答
python kb_manager.py visualize    # 生成图谱
python kb_manager.py lint         # 健康检查
```

**方式2: 直接运行脚本**
```bash
python scripts/ingest.py
python scripts/compile.py
python scripts/query.py
python scripts/visualize.py
python scripts/lint.py
```

## 详细命令

### 导入 (Ingest)

```bash
python scripts/ingest.py
```

支持的格式：
- `.pdf` - PDF文档 (自动提取文本和表格)
- `.md` - Markdown文件
- `.jpg / .png` - 图片 (自动OCR)
- `url_*.txt` - 网页URL (自动爬取)

输出: `raw/*.txt` 包含提取的文本

### 编译 (Compile)

```bash
# 完整编译
python scripts/compile.py

# 增量编译（检查变化）
python scripts/incremental_check.py
```

**编译流程:**
1. 读取 `raw/` 中所有文本
2. 使用LLM进行实体识别和链接生成
3. 生成Frontmatter元数据
4. 保存结构化wiki页面到 `wiki/`

**Compile示例输出:**
```markdown
---
title: 人工智能
created: 2026-04-13
tags: [AI, technology]
related: [机器学习, 深度学习]
---

# 人工智能

人工智能是...

## 相关概念
- [[机器学习]]
- [[深度学习]]
```

### 问答 (Query)

```bash
python scripts/query.py
```

**功能:**
- 单轮问答
- 多轮对话 (自动保存历史)
- 引用溯源 (显示参考页面)
- 会话管理 (保存/导出对话)

**示例:**
```
问题: 什么是人工智能?
回答: AI是...

📚 参考来源:
   1. 人工智能.md
   2. 机器学习.md

选项: [c]继续 [s]保存会话 [h]查看历史 [q]退出
```

### 可视化 (Visualization)

```bash
python scripts/visualize.py
```

生成多种格式的知识图谱：
- `docs/knowledge_graph.png` - PNG图片（高清）
- `docs/knowledge_graph.graphml` - Gephi格式
- `docs/knowledge_graph_d3.json` - D3.js数据
- `docs/knowledge_graph.html` - 交互式HTML

在Gephi中打开GraphML文件进行高级分析：
```bash
# 在Gephi中打开
open docs/knowledge_graph.graphml
```

### 健康检查 (Lint)

```bash
python scripts/lint.py
```

**检查项:**
- 🔗 死链检测 ([[不存在的页面]])
- 🏝️ 孤立页面 (没有被引用)
- 📝 Frontmatter检查 (必需字段)
- 📋 重复内容检测
- 🔀 链接建议 (内容多但链接少)

输出: `docs/lint_report.json`

### 导出 (Export)

```bash
# HTML导出
python scripts/export.py --format html

# Markdown导出
python scripts/export.py --format markdown

# PDF导出 (需要wkhtmltopdf)
python scripts/export.py --format pdf
```

## 配置详解

### config.yaml

```yaml
llm:
  provider: deepseek              # LLM提供者
  api_key: YOUR_KEY              # API密钥
  model: deepseek-chat           # 模型名称
  base_url: https://api.deepseek.com  # API地址
  max_tokens: 32768              # 最大token数

paths:
  raw_dir: raw/                  # 原始资料目录
  wiki_dir: wiki/                # Wiki输出目录
  scripts_dir: scripts/          # 脚本目录

compile:
  prompt_template: |
    你是知识库编译器...          # Compile提示词
    
query:
  system_prompt: |
    你是知识库助手...            # 问答系统提示词
```

## 工作原理

### Karpathy方案 vs 传统RAG

| 方面 | Karpathy方案 | 传统RAG |
|------|------------|--------|
| 存储 | 纯Markdown | 向量数据库 |
| 检索 | LLM完整阅读 | 向量检索Top-K |
| 信息完整性 | 100% | 70-80% |
| 跨文档推理 | 自动 | 困难 |
| 架构复杂度 | 低 | 高 |
| 成本 | 高(长上下文) | 中 |

### 编译链流

```
原始资料 (raw/)
    ↓ [Ingest]
文本提取 (raw/*.txt)
    ↓ [Compile]
- 实体识别
- 链接生成
- Frontmatter添加
    ↓
结构化Wiki (wiki/*.md)
    ↓ [三个并行方向]
    ├→ [Query] 问答系统
    ├→ [Visualize] 图谱展示
    └→ [Export] 多格式导出
```

### 增量编译策略

- **首次编译**: 完整编译所有文件
- **变化<5文件**: 增量编译 (只更新相关wiki页面)
- **变化≥5文件**: 完整编译

## 评分标准 (100分)

### 核心功能 (85分)

- **Ingest** (10分): 支持多格式 ✓
- **Compile** (25分): 实体识别、链接生成 ✓
- **Wiki管理** (10分): 结构化组织 ✓
- **Query** (20分): 多轮对话、引用溯源 ✓
- **Visualization** (10分): 多格式图谱 ✓
- **Export** (5分): HTML/Markdown ✓
- **Documentation** (5分): 实验报告 ✓

### 进阶功能 (15分)

- **Incremental Compile** (5分): ✓
- **Auto-Lint** (5分): ✓
- **Multi-session Chat** (3分): ✓
- **Knowledge Graph Export** (2分): ✓

## 实验报告

见 `docs/experiment_report.md`

## 常见问题

**Q: API费用太高怎么办?**
A: 使用DeepSeek或本地Ollama。DeepSeek费用仅为OpenAI的1/10。

**Q: 知识库太大超出上下文窗口怎么办?**
A: 
- 分层编译：按主题分库
- 混合方案：长上下文 + 轻量级索引

**Q: 如何在Obsidian中查看?**
A: 直接打开 `wiki/` 目录即可，Obsidian会自动识别双向链接。

**Q: 如何提高Compile质量?**
A: 调整 `config.yaml` 中的提示词，或提供更多示例。

## 依赖

- Python 3.8+
- openai / deepseek (LLM客户端)
- pdfplumber (PDF解析)
- networkx (图论)
- matplotlib (图表)

## 许可证

MIT License

## 致谢

灵感来自Andrej Karpathy的"LLM Knowledge Base"概念。