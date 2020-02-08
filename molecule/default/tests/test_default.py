import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_logrotate_files(host):
    m = host.file('/etc/logrotate.d/messages')
    f = host.file('/etc/logrotate.d/httpd')
    n = host.file('/etc/logrotate.d/httpd')

    assert m.exists
    assert f.exists
    assert n.exists
