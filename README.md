# Role Name

Maintain local user accounts and accesss.

## Requirements

None.

## Role Variables

Default variables are set in `defaults/main.yml`.

## Dependencies

No dependency on other Ansible Galaxy roles.

## Example Playbook

```yaml
---
- hosts: servers
  vars:
    uam_groups:
      - name: ansible
      - name: department99
        state: absent
    uam_users:
      - name: ansible
        comment: Ansible NPA
  roles:
    - role: hspaans.uam
      become: true
```

## License

MIT

## Author Information

This role was created in 2020 by [Hans Spaans](https://github.com/hspaans).
