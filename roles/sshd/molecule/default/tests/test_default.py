import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_openssh_is_installed(host):
    openssh = host.package("openssh")
    assert openssh.is_installed


def test_openssh_is_running_and_enabled(host):
    openssh = host.service("sshd")
    assert openssh.is_running
    assert openssh.is_enabled
