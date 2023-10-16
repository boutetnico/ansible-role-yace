[![tests](https://github.com/boutetnico/ansible-role-yace/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-yace/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.yace-blue.svg)](https://galaxy.ansible.com/boutetnico/yace)


ansible-role-yace
=================

This role installs and configures [YACE - Yet Another Cloudwatch Exporter](https://github.com/nerdswords/yet-another-cloudwatch-exporter).

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

| Variable                        | Required | Default                             | Choices   | Comments                    |
|---------------------------------|----------|-------------------------------------|-----------|-----------------------------|
| yace_dependencies               | yes      | `[]`                                | list      |                             |
| yace_version                    | yes      | `0.54.1`                            | string    |                             |
| yace_arch                       | yes      | detected automatically              | string    |                             |
| yace_user                       | yes      | `yace`                              | string    |                             |
| yace_group                      | yes      | `yace`                              | string    |                             |
| yace_extra_groups               | yes      | `[]`                                | list      |                             |
| yace_path                       | yes      | `/usr/local/bin/yace       `        | string    |                             |
| yace_config_file                | yes      | `/etc/yace/config.yml`              | string    |                             |
| yace_listen_address             | yes      | `127.0.0.1:5000`                    | string    |                             |
| yace_configuration              | yes      | `{}`                                | dict      |                             |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - ansible-role-yace

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
