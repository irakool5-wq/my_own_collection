# my_own_namespace.yandex_cloud_elk

> Custom Ansible Collection for file management tasks

[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](LICENSE)

## 📦 Contents

### Modules

#### `my_own_module`
Creates or updates a text file on the remote host.

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `path` | str | ✅ | - | Absolute path to the file |
| `content` | str | ✅ | - | Content to write into the file |
| `backup` | bool | ❌ | `false` | Create timestamped backup before overwrite |

**Example:**
```yaml
- name: Create application config
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /etc/myapp/config.ini
    content: |
      [server]
      host=localhost
      port=8080
    backup: true