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
| logrotate_packages | [] | Defines the list of packages to be installed in order to install logrotate. Note that **this role handles the packages to install already**, however, this variable exists for allowing you to declare your own list of packages if required.|
| logrotate_enable_repo | "" | Defines the repo to be enabled when installing the packages defined in `logrotate_packages` variable. Note that this option only works in RedHat family distributions. |
| logrotate_global_config | [] | Defines the configuration to be applied on `/etc/logrotate.conf` note that if this variable is empty as it is by default, the file `logtorate.conf` will not be modified at all. |
| logrotate_config_files | [] | Defines the individual logrotate configurations to be applied. See `Notes` and `Example playbook` for more information. |

### Notes:
- All configurations defined in `logrotate_config_files` will be applied over the default directory `/etc/logrotate.d`. This behaviour can be changed if in the variable `logrotate_global_config` you declare the `include` directive. So, for example, if you define:

```yaml
logrotate_global_config:
  - include
  - weekly
  - rotate 4
  - create
  - dateext
  - include /etc/customdir
```

The role will detect automatically the path on the `include` directive and will use that instead of the default `/etc/logrotate.d`.

- The configurations defined in `logrotate_config_files` will be added into individual files using as filename the string defined in the `name` parameter prefixed with ansible_". The prefix is added for making safe and easy to control the state (present, absent) of a definition.

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
