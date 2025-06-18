# Manai - Linux AI Assistant (Version 2.0)
[Leia esta página em português](https://github.com/ruscorreia/manai/blob/main/README-pt.md)
## Description

`manai` is a Linux command that allows you to interact with manual pages (man pages) intuitively using natural language and artificial intelligence. This version 2.0 integrates with an Azure Function that communicates with an AI agent in Azure AI Foundry.

## Features

### Version 2.0 - Azure AI Integration
- **Real AI Processing**: Uses an AI agent in Azure AI Foundry
- **Multilingual Support**: Accepts questions in any language and responds in the same language
- **Continuous Sessions**: Maintains context between questions for natural conversations
- **Improved Interface**: Enhanced visual feedback and clearer error messages
- **Flexible Configuration**: Supports different environments through environment variables

### Core Features
- **Natural Language Interaction**: Accepts questions in Portuguese, English, or any other language
- **Contextual Responses**: Provides accurate answers based on Linux man pages
- **Session Management**: Maintains conversation context for follow-up questions
- **Simple Configuration**: Easy setup via environment variables

## Installation

### Prerequisites

1. **Python 3.6 or higher**
2. **Requests library**: `pip install requests`

### Installation Steps

1. **Install dependencies**:
   ```bash
   pip install requests
   ```
2. **Clone this repository**:
   ```bash
   git clone https://github.com/ruscorreia/manai.git
   ```
3. **Navigate to the installation folder**:
   ```bash
   cd manai/install/
   ```
4. **Make the scripts executable**:
   ```bash
   chmod +x install_v2.sh
   chmod +x uninstall_v2.sh
   ```
5. **Run the installation script**:
   ```bash
   ./install_v2.sh
   ```
6. **Restart the terminal**
   
7. **Register**:
   ```bash
   manai --register
   ```
8. **Test with an example**:
```bash
# Simple question
manai "how to list hidden files in Linux?"

# Question in Spanish
manai "¿cómo crear un directorio con permisos específicos?"
```
   
## Usage

### Basic Commands

```bash
# man pages
manai memset

# Simple question
manai "how to list hidden files in Linux?"

# Question in English
manai "how to create a directory with specific permissions?"

# View configuration information
manai --config

# Start a new session (ignore previous context)
manai --new-session "how to use the find command?"

# View version
manai --version

# View help
manai --help
```

### Usage Examples

```bash
# Questions about basic commands
manai memset
manai "how to copy files?"
manai "create a directory"
manai "view the contents of a file"

# More specific questions
manai "how to find files modified in the last 24 hours?"
manai "set permissions to 755 for a file"
manai "compress a folder with tar"

# Continuous conversation
manai "how to use the grep command?"
manai "and how can I use grep with regular expressions?"
manai "show only the line number where it was found?"
```

### Session Management

Manai automatically maintains conversation context:

```bash
# First question
manai "how to create a user in Linux?"

# Follow-up question (uses previous context)
manai "and how to set a password for that user?"

# Start a new conversation
manai --new-session "how to install packages with apt?"
```

## Troubleshooting

### Error: "Communication error"

**Possible causes and solutions**:

1. **No internet connection**: Check your connectivity
2. **Incorrect URL**: Confirm the Azure Function URL
3. **Invalid key**: Verify the function key
4. **Inactive Function App**: The function may be "waking up" (cold start)

### Error: "Invalid server response"

**Cause**: The Azure Function returned a non-JSON response.

**Solutions**:
- Check if the Azure Function is running correctly
- Confirm you are using the correct endpoint URL
- Check Azure Function logs for errors

### Session Issues

If sessions are not working:

1. **Check permissions**: The `~/.manai_session` file needs write permissions
2. **Disk space**: Ensure there is available space
3. **Restart session**: Use `--new-session` to start fresh

## Advanced Features

### Session File

Manai saves the thread ID in `~/.manai_session` to maintain context between executions. This file is created automatically and can be deleted to reset all sessions.

### Timeout and Retry

- **Timeout**: 60 seconds per request
- **Retry**: Not implemented (Azure Function has its own retry mechanism)

### Logging

For debugging, you can check:
- Detailed error messages in the terminal
- Azure Function logs in the Azure portal
- Network connectivity

## Development

### Code Structure

- `ManaiClient`: Main class for communication with the Azure Function
- `get_config()`: Configuration management
- `main()`: Command-line interface

### Dependencies

- `requests`: For HTTP communication
- `json`: For data processing
- `argparse`: For command-line interface
- `os`: For environment variables and files

## License

This project is licensed under the [MIT License](LICENSE).

## Support

For issues or suggestions:
1. Check the troubleshooting section
2. Verify the Azure Function configuration
3. Check Azure Function logs in the Azure portal

## Changelog

### Version 2.0.0
- Full integration with Azure Function
- Support for multiple languages
- Improved session system
- Enhanced user interface
- Configuration via environment variables

### Version 1.0.0
- Initial version with basic local processing
