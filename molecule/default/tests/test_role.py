import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('file,user,group', [
  ('/usr/local/bin/restic', 'root', 'staff'),
])
def test_restic_is_installed(host, file, user, group):
    restic = host.file(file)
    assert restic.exists
    assert restic.is_file
    assert restic.user == user
    assert restic.group == group
