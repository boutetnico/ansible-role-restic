ansible-role-restic
===================

This role installs Restic.

[![Build Status](https://travis-ci.org/boutetnico/ansible-role-restic.svg?branch=master)](https://travis-ci.org/boutetnico/ansible-role-restic)

Requirements
------------

Ansible 2.6 or newer.

Supported Platforms
-------------------
- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 16.04 (Xenial Xerus)](http://releases.ubuntu.com/16.04/)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)


Role Variables
--------------

| Variable                     | Required | Default                         | Choices   | Comments                                      |
|------------------------------|----------|---------------------------------|-----------|-----------------------------------------------|
| restic_version               | yes      | `0.9.6`                         | string    |                                               |
| restic_download_path         | yes      | `/tmp`                          | string    |                                               |
| restic_install_path          | yes      | `/usr/local/bin/`               | string    |                                               |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - ansible-role-restic

Testing
-------

## Debian

`molecule --base-config molecule/shared/base.yml test --scenario-name debian`

## Ubuntu

`molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu`

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
