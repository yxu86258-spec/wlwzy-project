#!/usr/bin/env python
"""
快速入门 - 3分钟上手知识库系统
"""

def main():
    print("""
╔════════════════════════════════════════════════════════════╗
║   🚀 Karpathy风格知识库 - 3分钟快速入门                     ║
╚════════════════════════════════════════════════════════════╝

📋 预置要求:
  ✓ Python 3.8+
  ✓ pip已安装

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 第1步: 安装依赖 (1分钟)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

运行:
    pip install -r requirements.txt

核心库:
    ✓ openai         - LLM API支持
    ✓ pdfplumber     - PDF解析
    ✓ networkx       - 图论分析
    ✓ matplotlib     - 数据可视化
    ✓ requests       - 网页爬取
    ✓ pyyaml         - 配置管理

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔑 第2步: 配置API (可选, 1分钟)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

编辑 config/config.yaml:

【方式A】使用OpenAI (最强):
    llm:
      api_key: sk-xxxxx
      model: gpt-4
      base_url: https://api.openai.com/v1

【方式B】使用DeepSeek (推荐, 便宜10倍):
    llm:
      api_key: sk-xxxxx
      model: deepseek-chat
      base_url: https://api.deepseek.com

【方式C】使用本地Ollama (免费):
    llm:
      model: llama2
      base_url: http://localhost:11434

[如果不配置，系统自动使用演示模式 ✓]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📂 第3步: 启动系统 (1分钟)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

完整工作流:

    # 1. 导入资料 (PDF/Markdown/网页)
    python scripts/ingest.py

    # 2. 编译知识库
    python scripts/compile.py

    # 3. 启动问答系统
    python scripts/query.py

    # 4. 生成知识图谱
    python scripts/visualize.py

    # 5. 健康检查
    python scripts/lint.py

或使用管理工具 (推荐):

    python kb_manager.py ingest       # 导入
    python kb_manager.py compile      # 编译
    python kb_manager.py query        # 问答
    python kb_manager.py visualize    # 图谱

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 添加你的资料
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

将你的文档放入 raw/ 目录:

    raw/
    ├── 你的论文.pdf          ← PDF文档
    ├── 学习笔记.md            ← Markdown文件
    ├── paper.pdf              ← 英文论文
    └── url_网站.txt           ← 网页URL

支持格式:
    ✓ .pdf     - PDF文档
    ✓ .md      - Markdown笔记
    ✓ .jpg/.png - 图片 (自动OCR)
    ✓ url_*.txt - 网页链接

然后运行 ingest.py 自动处理!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💬 使用问答系统
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

启动: python scripts/query.py

示例对话:

    问题: 什么是人工智能?
    回答: 人工智能是指由人制造...
    
    📚 参考来源:
       1. 人工智能.md
       2. 机器学习.md
    
    选项: [c]继续 [s]保存会话 [h]查看历史 [q]退出

关键功能:
    ✓ 多轮对话自动保存
    ✓ 引用来源追踪
    ✓ 对话导出为Markdown
    ✓ 会话历史管理

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 查看输出结果
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

编译后的知识库:
    wiki/
    ├── 概念1.md
    ├── 概念2.md
    └── ...

生成的图谱:
    docs/
    ├── knowledge_graph.png        ← 打开查看关系图
    ├── knowledge_graph.html       ← 浏览器打开
    └── knowledge_graph.graphml    ← Gephi分析

对话记录:
    chat_sessions/
    └── *.json                     ← 自动保存

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚙️ 进阶设置
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

增量编译检查:
    python scripts/incremental_check.py

自动健康检查:
    python scripts/lint.py
    # 检查: 死链、孤立页面、元数据完整性

多格式导出:
    python scripts/export.py --format html

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❓ 常见问题
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q: 没有API密钥可以用吗?
A: 可以! 系统自动进入演示模式，提供基本问答功能。

Q: 知识库太大怎么办?
A: 使用增量编译功能，或分层编译 (拆分成多个库)。

Q: 如何在Obsidian中查看?
A: 在Obsidian中打开 wiki/ 文件夹，自动识别双向链接！

Q: 图谱很复杂怎么分析?
A: 用Gephi打开 knowledge_graph.graphml 进行专业分析。

Q: 想要更好的结果?
A: 配置更强的LLM (如DeepSeek)，或优化 config.yaml 中的提示词。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📖 更多信息
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📄 完整文档:
    README.md              ← 详细使用指南
    docs/experiment_report.md  ← 技术报告
    docs/COMPLETION_REPORT.md  ← 功能总结

🎓 学习资源:
    scripts/*.py           ← 源代码注释
    demo.py               ← 功能演示

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ 开始使用吧!

  # 一键启动
  python kb_manager.py ingest
  python kb_manager.py compile
  python kb_manager.py query

祝您使用愉快! 🎉
""")

if __name__ == '__main__':
    main()