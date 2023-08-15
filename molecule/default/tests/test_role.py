import pytest


@pytest.mark.parametrize(
    "file,user,group",
    [
        ("/usr/local/bin/restic", "root", "staff"),
    ],
)
def test_restic_is_installed(host, file, user, group):
    restic = host.file(file)
    assert restic.exists
    assert restic.is_file
    assert restic.user == user
    assert restic.group == group


@pytest.mark.parametrize(
    "file,user,group,mode,content",
    [
        ("/etc/restic/repo-password", "root", "root", 0o400, "secret"),
    ],
)
def test_restic_password_file_exist(host, file, user, group, mode, content):
    restic = host.file(file)
    assert restic.exists
    assert restic.is_file
    assert restic.user == user
    assert restic.group == group
    assert restic.mode == mode
    assert restic.content_string == content
