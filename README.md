# Modular RAG MCP Server

一个可插拔、可观测的模块化 RAG（检索增强生成）服务框架，通过 MCP（Model Context Protocol）协议对外暴露工具接口，支持 Copilot / Claude 等 AI 助手直接调用。

---

## 核心能力

| 模块 | 能力 |
|------|------|
| **Ingestion Pipeline** | PDF → Markdown → Chunk → Transform → Encoding → Upsert，支持多模态图片描述 |
| **Hybrid Search** | Dense (向量) + Sparse (BM25) + RRF Fusion + Rerank 两段式检索 |
| **MCP Server** | 标准 MCP 协议暴露工具：`query_knowledge_hub`、`list_collections`、`get_document_summary` |
| **Dashboard** | Streamlit 六页面管理平台：系统总览 / 数据浏览 / Ingestion 管理 / 摄取追踪 / 查询追踪 / 评估面板 |
| **Evaluation** | Ragas + Custom 评估体系，支持 Golden Test Set 回归测试 |
| **Observability** | 全链路追踪，Ingestion 与 Query 两条链路每一中间状态透明可见 |

---

## 技术亮点

- **全链路可插拔架构**：LLM / Embedding / Reranker / Splitter / VectorStore / Evaluator 每个环节均定义抽象接口，通过配置文件一键切换后端，零代码修改。
- **混合检索 + 重排**：BM25 稀疏检索 + Dense Embedding 语义检索，RRF 融合后可选 Cross-Encoder / LLM Rerank 精排。
- **多模态图像处理**：Vision LLM 自动生成图片描述并缝合进 Chunk，复用纯文本 RAG 链路实现"搜文字出图"。
- **MCP 生态集成**：遵循 Model Context Protocol 标准，可直接对接 GitHub Copilot、Claude Desktop 等 MCP Client。
- **可视化管理 + 自动化评估**：Streamlit Dashboard 提供完整数据管理与链路追踪，集成 Ragas 等评估框架。

---

## 快速开始

### 1. 安装依赖

```bash
pip install -e ".[dev]"
```

### 2. 配置

编辑 `config/settings.yaml`，填入 LLM API Key 及所需 Provider 配置：

```yaml
llm:
  provider: "deepseek"        # 可选: openai / azure / ollama / deepseek
  api_key: "YOUR_API_KEY_HERE"

embedding:
  provider: "ollama"          # 可选: openai / azure / ollama
  model: "nomic-embed-text"
  base_url: "http://localhost:11434"
```

> 使用 Ollama Embedding 时，需先启动 Ollama 并拉取模型：`ollama pull nomic-embed-text`

### 3. 摄取文档

```bash
# 摄取单个文件
python scripts/ingest.py --path ./your_doc.pdf --collection my_collection

# 摄取整个目录
python scripts/ingest.py --path ./docs/ --collection my_collection

# 强制重新处理已摄取的文件
python scripts/ingest.py --path ./your_doc.pdf --collection my_collection --force
```

### 4. 查询

```bash
python scripts/query.py --query "你的问题" --collection my_collection
```

### 5. 启动 MCP Server

`main.py` 以 stdio 模式运行，专供 AI 客户端（Copilot / Claude Desktop）调用：

```bash
python main.py
```

**接入 VS Code Copilot**（在 `settings.json` 中添加）：

```json
"mcp": {
  "servers": {
    "modular-rag": {
      "type": "stdio",
      "command": "python",
      "args": ["main.py"],
      "cwd": "/path/to/project"
    }
  }
}
```

### 6. 启动 Dashboard（可选）

```bash
python scripts/start_dashboard.py
# 浏览器访问 http://localhost:8501
```

---

## 项目结构

```
src/
├── core/           # 核心类型、配置加载
├── ingestion/      # 文档摄取管线（chunking / encoding / storage / transform）
├── providers/      # 可插拔 Provider 实现（llm / embedding / reranker / vector_store 等）
├── retrieval/      # 混合检索层（dense / sparse / fusion / rerank / query_processor）
├── response/       # 响应构建（引用生成、多模态组装）
├── mcp_server/     # MCP Server 与 Tool 定义
└── observability/  # 日志、追踪、Dashboard、评估

config/
├── settings.yaml           # 主配置文件
└── prompts/                # LLM Prompt 模板

scripts/
├── ingest.py               # 文档摄取脚本
├── query.py                # 查询脚本
├── evaluate.py             # 评估脚本
└── start_dashboard.py      # 启动 Dashboard
```

---

## 切换 Provider

编辑 `config/settings.yaml` 即可切换，无需修改代码：

```yaml
llm:
  provider: "openai"     # deepseek / openai / azure / ollama
  api_key: "sk-..."

embedding:
  provider: "openai"     # openai / azure / ollama
  model: "text-embedding-3-small"
```

新增 Provider：① 在 `src/providers/` 对应目录实现 Provider 类；② 在工厂中注册；③ 更新 `settings.yaml`。

---

## 运行测试

```bash
# 单元测试（无外部依赖）
pytest tests/unit/

# 集成测试（需要配置好的外部服务）
pytest tests/integration/

# 全量测试
pytest
```

---

## 架构与设计

详见 [DEV_SPEC.md](DEV_SPEC.md).
