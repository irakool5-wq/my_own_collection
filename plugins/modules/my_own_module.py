#!/usr/bin/python
# Copyright: (c) 2024, Your Name <your.email@example.org>
# GNU General Public License v3.0+

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Creates a text file on remote host

version_added: "1.0.0"

description: 
  - This module creates a text file on the remote host.
  - If the file exists with different content, it will be updated.

options:
    path:
        description: Full path to the file to create.
        required: true
        type: str
    content:
        description: Content to write into the file.
        required: true
        type: str
    force:
        description: Overwrite file even if it exists with different content.
        required: false
        type: bool
        default: true

author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
# Create a simple file
- name: Create config file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/my_config.txt
    content: "Hello from Ansible!"

# Create file with force overwrite
- name: Overwrite existing file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/my_config.txt
    content: "New content"
    force: true
'''

RETURN = r'''
path:
    description: Path of the file that was created/modified.
    type: str
    returned: always
    sample: '/tmp/my_config.txt'
content_length:
    description: Length of the content written.
    type: int
    returned: always
    sample: 25
'''

from ansible.module_utils.basic import AnsibleModule
import os


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True),
        force=dict(type='bool', required=False, default=True)
    )

    result = dict(
        changed=False,
        path='',
        content_length=0
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    file_path = module.params['path']
    content = module.params['content']
    force = module.params['force']

    result['path'] = file_path
    result['content_length'] = len(content)

    # Check mode - no changes
    if module.check_mode:
        file_exists = os.path.exists(file_path)
        if file_exists:
            with open(file_path, 'r') as f:
                current_content = f.read()
            if current_content != content:
                result['changed'] = True
        else:
            result['changed'] = True
        module.exit_json(**result)

    # Main logic
    file_exists = os.path.exists(file_path)
    
    if file_exists:
        with open(file_path, 'r') as f:
            current_content = f.read()
        
        if current_content == content:
            # File exists with same content - idempotent
            module.exit_json(**result)
        elif not force:
            module.fail_json(msg=f"File {file_path} exists with different content and force=False", **result)
    
    # Create/overwrite the file
    try:
        # Ensure directory exists
        dir_path = os.path.dirname(file_path)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, 'w') as f:
            f.write(content)
        result['changed'] = True
    except Exception as e:
        module.fail_json(msg=f"Failed to write file: {str(e)}", **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()