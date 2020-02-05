gabops.logrotate
=========
[![Build Status](https://travis-ci.org/gabops/ansible-role-logrotate.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-logrotate)

Installs and configures logrotate.

Requirements
------------

None.

Role Variables
--------------

| Variable | Default value | Description |
| :--- | :--- | :--- |
| logrotate_packages | [] |  |
| logrotate_enable_repo | "" |  |
| logrotate_apply_global_config | false |  |
| logrotate_global_config | [] |  |
| logrotate_config_files | [] |  |

Dependencies
------------

None.

Example Playbook
----------------

```yaml
    - hosts: servers
      vars:
        logrotate_apply_global_config: true
        logrotate_global_config:
          - weekly
          - rotate 4
          - create
          - dateext
          - include /etc/logrotate.d

        logrotate_config_files:
          - name: messages
            path: /var/log/messages
            directives: |
              rotate 5
              weekly
              postrotate
                /usr/bin/killall -HUP syslogd
              endscript

          - name: httpd
            path:
              - /var/log/httpd/access.log
              - /var/log/httpd/error.log
            directives: |
              rotate 5
              mail www@my.org
              size 100k
              sharedscripts
              postrotate
                /usr/bin/killall -HUP httpd
              endscript

      roles:
         - role: gabops.logrotate
```

License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
