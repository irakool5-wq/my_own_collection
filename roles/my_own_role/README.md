# my_own_role

Role for creating text files using my_own_module from my_own_namespace.yandex_cloud_elk collection.

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `my_own_module_path` | `/tmp/default_file.txt` | Path to the file to create |
| `my_own_module_content` | `Default content...` | Content to write |
| `my_own_module_backup` | `false` | Create backup before overwrite |

## Example Usage

```yaml
- hosts: localhost
  roles:
    - role: my_own_namespace.yandex_cloud_elk.my_own_role
      vars:
        my_own_module_path: /etc/myapp/config.txt
        my_own_module_content: "key=value"