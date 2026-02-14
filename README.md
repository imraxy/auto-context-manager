# Auto Context Manager

**AI-Powered Automatic Project Context Management with Adaptive Learning**

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-purple)
![ClawdHub](https://img.shields.io/badge/clawdhub-available-orange)

**Smart context switching that learns and adapts to your workflow**

[Features](#features) •
[Installation](#installation) •
[Quick Start](#quick-start) •
[Documentation](#documentation)

</div>

---

## 🎯 Features

### ✨ Core Capabilities

- **🤖 Auto Project Detection** - Automatically detects projects from your messages
- **🔄 Context Switching** - Seamlessly switches between project contexts
- **🧠 Vector Memory** - ChromaDB-powered semantic search
- **🎓 Adaptive Learning** - Learns and improves from your interactions
- **📊 Self-Analysis** - Analyzes performance and suggests improvements

### 🔒 Security & Privacy

- ✅ **100% Local** - No external requests, no cloud dependencies
- ✅ **No API Keys** - Works offline, fully self-contained
- ✅ **No Telemetry** - Zero data collection or analytics
- ✅ **Open Source** - Transparent and auditable code
- ✅ **Data Ownership** - Your data stays on your machine

---

## 📦 Installation

### Method 1: ClawdHub (Recommended)

```bash
clawdhub install auto-context-manager
```

### Method 2: Manual Installation

```bash
# Clone repository
git clone https://github.com/imraxy/auto-context-manager.git
cd auto-context-manager

# Install dependencies
pip install -r requirements.txt

# Initialize
python scripts/init.py
```

### Requirements

- Python 3.8 or higher
- ChromaDB (automatically installed)
- 500MB free disk space (for vector database)

---

## 🚀 Quick Start

### 1. Initialize System

```bash
python scripts/init.py
```

This creates `~/.auto-context/` with all necessary files.

### 2. Configure Projects

Edit `~/.auto-context/projects.json`:

```json
{
  "projects": {
    "my-project": {
      "name": "My Project",
      "keywords": ["keyword1", "keyword2"]
    }
  }
}
```

### 3. Use It

```python
from auto_context_manager import AutoContextManager

acm = AutoContextManager()

# Detect project
project, confidence = acm.detect_project("Your message here")
print(f"Project: {project}")
```

---

## 📖 Documentation

See [docs/](docs/) for complete documentation.

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

<div align="center">

Made with ❤️ by the ClawdHub community

</div>
