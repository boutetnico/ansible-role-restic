[![tests](https://github.com/boutetnico/ansible-role-restic/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-restic/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.restic-blue.svg)](https://galaxy.ansible.com/boutetnico/restic)

ansible-role-restic
===================

This role installs [Restic](https://restic.net/).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)

Role Variables
--------------

| Variable                     | Required | Default               | Choices   | Comments                             |
|------------------------------|----------|-----------------------|-----------|--------------------------------------|
| restic_version               | yes      | `0.16.4`              | string    |                                      |
| restic_download_path         | yes      | `/tmp`                | string    |                                      |
| restic_install_path          | yes      | `/usr/local/bin/`     | string    |                                      |
| restic_dependencies          | yes      | `[bzip2]`             | list      |                                      |
| restic_password_files        | yes      | `[]`                  | list      |                                      |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - ansible-role-restic
          restic_password_files:
            - path: /etc/restic/repo-password
              password: secret

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
