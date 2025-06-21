# ManAI - Intelligent Linux Assistant

<div align="center">

![ManAI Logo](https://img.shields.io/badge/ManAI-v2.0-blue?style=for-the-badge)
[![Python](https://img.shields.io/badge/Python-3.6+-green?style=for-the-badge&logo=python)](https://python.org)
[![Azure](https://img.shields.io/badge/Azure-Functions-blue?style=for-the-badge&logo=microsoft-azure)](https://azure.microsoft.com)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

**Transform your Linux command experience through artificial intelligence**

[🚀 Installation](#installation) • [📖 Documentation](#usage) • [🤝 Contributing](#contributing) • [🇵🇹 Português](README-pt.md)

</div>

---

## 🎯 Overview

**ManAI** revolutionizes how you interact with Linux systems by transforming natural language queries into precise, contextualized responses about commands and system functionality. Developed by Rosco Edutec, ManAI eliminates the barrier between technical knowledge and effective terminal usage.

### 🔍 The Problem We Solve

How many times have you found yourself in these situations?

- Needed a specific command but couldn't remember the exact syntax
- Spent time navigating through extensive man pages to find a simple functionality
- Had difficulty understanding complex command options
- Wanted a clear, contextualized explanation instead of dense technical documentation

ManAI was created precisely to solve these challenges, offering an intuitive interface that understands your needs and provides immediate, practical answers.

### ✨ Why Choose ManAI?

**Advanced Artificial Intelligence**: Leverages the power of Azure AI Foundry to understand and respond to your questions with exceptional precision.

**Multilingual by Nature**: Accepts questions in Portuguese, English, Spanish, French, German, Italian, Japanese, Chinese, Russian, and Arabic, always responding in the language of the question.

**Persistent Context**: Maintains the context of your conversations, allowing natural follow-up questions like "and how can I do that with specific permissions?"

**Simplicity of Use**: A single Python dependency and automated installation make ManAI accessible to all Linux users.

**Robust Cloud Integration**: Benefits from the scalability and reliability of Azure infrastructure, ensuring fast responses and constant availability.

## 🚀 Key Features

### 🧠 Advanced AI Processing
ManAI uses state-of-the-art language models hosted on Azure AI Foundry, ensuring accurate, contextualized, and up-to-date responses. The system understands not only basic commands but also complex scenarios and advanced workflows.

### 🌐 Complete Multilingual Support
Communicate in your preferred language. ManAI automatically detects the language of your question and responds in the same language, maintaining technical accuracy and explanation clarity.

### 💬 Intelligent Session Management
The system maintains the context of your conversations, enabling natural and progressive dialogues. You can ask follow-up questions, request clarifications, or explore related topics without losing the thread of conversation.

### ⚡ Optimized Performance
With optimized response times and intelligent caching, ManAI provides quick answers even for complex queries, maintaining your workflow productivity.

### 🔒 Robust User System
Includes complete registration, authentication, and profile management system, with support for different access levels and premium features.

## 📋 Prerequisites

Before installing ManAI, ensure your system meets the following requirements:

### Operating System
- **Linux**: Any modern distribution (Ubuntu 18.04+, Debian 10+, CentOS 7+, Fedora 30+, Arch Linux)
- **Architecture**: x86_64 (AMD64) or ARM64

### Software
- **Python**: Version 3.6 or higher
- **pip**: Python package manager (usually included with Python)
- **curl**: For HTTP communication (pre-installed on most distributions)

### Connectivity
- **Internet Connection**: Required for communication with Azure services
- **Ports**: HTTPS access (port 443) for API communication

### Environment Verification

Run the following commands to verify your system is ready:

```bash
# Check Python version
python3 --version

# Check if pip is available
pip3 --version

# Check connectivity
curl -s https://httpbin.org/ip
```

## 🛠 Installation

### Recommended Method: Automatic Script

The simplest and safest way to install ManAI:

```bash
# 1. Clone the repository
git clone https://github.com/ruscorreia/manai.git
cd manai

# 2. Navigate to installation directory
cd install

# 3. Make script executable
chmod +x install_v2.sh

# 4. Run installation
./install_v2.sh

# 5. Restart terminal or reload profile
source ~/.bashrc  # for bash
# or
source ~/.zshrc   # for zsh
```

### Manual Installation

For users who prefer full control over the process:

```bash
# 1. Install dependencies
pip3 install --user requests

# 2. Clone and configure
git clone https://github.com/ruscorreia/manai.git
cd manai/install

# 3. Copy to local directory
mkdir -p ~/.local/bin
cp manai.py ~/.local/bin/manai
chmod +x ~/.local/bin/manai

# 4. Add to PATH (if necessary)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Installation Verification

Confirm the installation was successful:

```bash
# Check if command is available
which manai

# Test connectivity
manai --test-connection

# Check version
manai --version
```

## 🎮 Getting Started

### 1. User Registration

Before using ManAI, you need to create an account:

```bash
manai --register
```

The system will request:
- **Email**: Your email address (will be your identifier)
- **Password**: Secure password (minimum 8 characters)
- **Name**: First and last name
- **Language**: Preferred language for responses

### 2. First Test

After registration, test the system with a simple question:

```bash
manai "how to list hidden files?"
```

### 3. Explore Features

Try different types of questions:

```bash
# Basic question
manai "how to copy files?"

# Specific question
manai "how to find files modified in the last 24 hours?"

# Question in Spanish
manai "¿cómo comprimir una carpeta con tar?"

# Follow-up question (maintains context)
manai "and how can I exclude certain file types?"
```

## 📚 Detailed Usage

### Basic Commands

#### Simple Questions
```bash
# Fundamental commands
manai "how to create a directory?"
manai "how to view file contents?"
manai "how to change file permissions?"

# Process management
manai "how to see running processes?"
manai "how to kill a process?"
manai "how to run a command in background?"
```

#### Advanced Queries
```bash
# Complex operations
manai "how to do incremental backup with rsync?"
manai "how to set up a cron job to run at 2 AM?"
manai "how to monitor disk usage in real time?"

# Troubleshooting
manai "how to resolve 'permission denied' error?"
manai "how to free up disk space?"
manai "how to diagnose network problems?"
```

### Session Management

#### Continuous Sessions
ManAI automatically maintains context between questions:

```bash
# First question
manai "how to use the grep command?"

# Follow-up question (uses previous context)
manai "and how can I use regular expressions with it?"

# More details
manai "can you give a practical example?"
```

#### New Session
To start a completely new conversation:

```bash
manai --new-session "how to install software on Ubuntu?"
```

### Multilingual Support

#### Examples in Different Languages

**English:**
```bash
manai "how to compress a folder with tar?"
```

**Portuguese:**
```bash
manai "como encontrar ficheiros maiores que 100MB?"
```

**Spanish:**
```bash
manai "¿cómo crear un usuario en Linux?"
```

**French:**
```bash
manai "comment changer le mot de passe d'un utilisateur?"
```

### Management Commands

#### Account Information
```bash
# View account status
manai --status

# View usage statistics
manai --stats

# Check feature access
manai --check-feature "longTermMemory"
```

#### Session Management
```bash
# Login
manai --login

# Logout
manai --logout

# Test connectivity
manai --test-connection
```

## 🔧 Advanced Configuration

### Environment Variables

ManAI can be configured through environment variables:

```bash
# Custom API URL
export MANAI_API_URL="https://your-instance.azurewebsites.net/api"

# Custom function key
export MANAI_FUNCTION_KEY="your-custom-key"

# Default language
export MANAI_DEFAULT_LANGUAGE="en"
```

### Configuration Files

ManAI stores configurations in:
- **Configuration**: `~/.config/manai/config.json`
- **Session**: `~/.config/manai/session.json`

### Customization

#### Useful Aliases
Add to your `.bashrc` or `.zshrc`:

```bash
# Aliases for frequent use
alias m="manai"
alias mhelp="manai --help"
alias mstatus="manai --status"
alias mnew="manai --new-session"
```

## 🚨 Troubleshooting

### Common Issues

#### Error: "Not authenticated"
**Symptom**: Message "Login required first"
**Solution**:
```bash
manai --login
```

#### Error: "Query limit reached"
**Symptom**: Message about daily limit
**Solutions**:
- Wait until the next day
- Consider upgrading to ManAI Pro
- Check statistics: `manai --stats`

#### Error: "Communication error"
**Symptoms**: Timeouts or connection failures
**Diagnosis**:
```bash
# Test basic connectivity
ping google.com

# Test ManAI specific connectivity
manai --test-connection

# Check configuration
manai --status
```

**Solutions**:
1. Check internet connection
2. Confirm no firewall is blocking HTTPS
3. Try again after a few minutes

#### Error: "Invalid server response"
**Cause**: Temporary issue with Azure services
**Solutions**:
1. Wait a few minutes and try again
2. Check Azure services status
3. Contact support if it persists

### Advanced Diagnostics

#### Complete System Check
```bash
# Complete diagnostic script
echo "=== ManAI Diagnostics ==="
echo "Python Version: $(python3 --version)"
echo "ManAI Version: $(manai --version)"
echo "Connectivity:"
manai --test-connection
echo "Account Status:"
manai --status
```

#### Logs and Debug
To get detailed debug information:
```bash
# Run with verbose (if available)
python3 ~/.local/bin/manai --debug "your question"
```

## 🤝 Contributing

### How to Contribute

We welcome community contributions! There are several ways to help:

#### Report Issues
1. Check if the issue has already been reported
2. Create detailed issue on GitHub
3. Include system information and steps to reproduce

#### Suggest Improvements
1. Open discussion on GitHub
2. Describe the proposed feature
3. Explain the benefit to users

#### Contribute Code
1. Fork the repository
2. Create branch for the feature
3. Implement changes with tests
4. Submit pull request

### Development Standards

#### Code Style
- Follow PEP 8 for Python
- Use type hints when possible
- Document functions and classes
- Maintain compatibility with Python 3.6+

#### Testing
- Write tests for new features
- Ensure all tests pass
- Maintain high test coverage

## 📊 Roadmap

### Version 2.1 (Next)
- Local cache for frequent responses
- Support for custom configurations
- User interface improvements
- Performance optimizations

### Version 2.2
- Plugin system for extensions
- Code editor integration
- Support for custom scripts
- Advanced analytics

### Version 3.0 (Future)
- Optional graphical interface
- Support for other operating systems
- Local AI for basic features
- DevOps tools integration

## 📄 License

This project is licensed under the [MIT License](LICENSE). This means you can:

- ✅ Use commercially
- ✅ Modify the code
- ✅ Distribute
- ✅ Use privately

**Conditions:**
- Include license and copyright
- Don't hold authors liable

## 🙏 Acknowledgments

### Development Team
- **Rosco Edutec**: Main development and architecture
- **Community**: Contributions, testing, and feedback

### Technologies Used
- **Python**: Main programming language
- **Azure Functions**: Cloud infrastructure
- **Azure AI Foundry**: Artificial intelligence engine
- **Requests**: HTTP library for Python

### Inspiration
ManAI was inspired by the need to make Linux more accessible to users of all levels, combining the power of traditional commands with the intuitiveness of natural language.

## 📞 Support

### Support Channels

**GitHub Issues**: To report bugs and request features
- [Report Bug](https://github.com/ruscorreia/manai/issues/new?template=bug_report.md)
- [Request Feature](https://github.com/ruscorreia/manai/issues/new?template=feature_request.md)

**Discussions**: For general questions and discussions
- [GitHub Discussions](https://github.com/ruscorreia/manai/discussions)

**Email**: For commercial questions or partnerships
- rusacorreia@hotmail.com

### FAQ

**Q: Does ManAI work offline?**
A: No, ManAI requires internet connection to communicate with Azure AI services.

**Q: Is there a usage limit?**
A: Yes, free accounts have daily limits. Contact us for premium options.

**Q: Is my data secure?**
A: Yes, we follow security and privacy best practices. Questions are processed securely and not stored permanently.

**Q: Can I use ManAI in scripts?**
A: Yes, ManAI can be integrated into bash scripts and other automation.

---

<div align="center">

**Developed with ❤️ by [Rosco Edutec](https://github.com/ruscorreia)**

[⬆️ Back to top](#manai---intelligent-linux-assistant)

</div>


