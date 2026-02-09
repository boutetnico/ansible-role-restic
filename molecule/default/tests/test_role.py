import pytest


@pytest.mark.parametrize(
    "package",
    [
        "bzip2",
    ],
)
def test_dependencies_installed(host, package):
    pkg = host.package(package)
    assert pkg.is_installed


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


def test_restic_is_executable(host):
    cmd = host.run("/usr/local/bin/restic version")
    assert cmd.rc == 0
    assert "restic" in cmd.stdout


@pytest.mark.parametrize(
    "file,user,group,mode,content",
    [
        ("/etc/restic/repo-password", "root", "root", 0o400, "secret"),
        (
            "/home/backup/.restic/backup-password",
            "backup",
            "backup",
            0o400,
            "backup-secret",
        ),
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


@pytest.mark.parametrize(
    "directory,user,group,mode",
    [
        ("/etc/restic", "root", "root", 0o750),
        ("/home/backup/.restic", "backup", "backup", 0o750),
    ],
)
def test_password_directory_exists(host, directory, user, group, mode):
    d = host.file(directory)
    assert d.exists
    assert d.is_directory
    assert d.user == user
    assert d.group == group
    assert d.mode == mode
