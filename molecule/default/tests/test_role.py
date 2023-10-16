import pytest


@pytest.mark.parametrize(
    "username,groupname,path",
    [
        ("root", "root", "/usr/local/bin/yace"),
        ("root", "root", "/etc/yace/config.yml"),
        ("root", "root", "/etc/systemd/system/yace.service"),
    ],
)
def test_yace_files(host, username, groupname, path):
    config = host.file(path)
    assert config.exists
    assert config.is_file
    assert config.user == username
    assert config.group == groupname


@pytest.mark.parametrize(
    "username,groupname,path",
    [
        ("root", "root", "/etc/systemd/system/yace.service"),
    ],
)
def test_systemd_config_file_exists(host, username, groupname, path):
    config = host.file(path)
    assert config.exists
    assert config.is_file
    assert config.user == username
    assert config.group == groupname


@pytest.mark.parametrize(
    "name",
    [
        ("yace"),
    ],
)
def test_yace_service_is_running(host, name):
    service = host.service(name)
    assert service.is_enabled
    assert service.is_running


@pytest.mark.parametrize(
    "endpoint",
    [
        ("tcp://127.0.0.1:5000"),
    ],
)
def test_yace_is_reachable(host, endpoint):
    server = host.socket(endpoint)
    assert server.is_listening
