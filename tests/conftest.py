import pytest
from localstack.testing.aws.util import (
    base_aws_client_factory,
    base_aws_session,
    base_testing_aws_client,
)

pytest_plugins = [
    "localstack.testing.pytest.fixtures",
    "localstack_snapshot.pytest.snapshot",
]


@pytest.fixture(scope="session")
def aws_session():
    return base_aws_session()


@pytest.fixture(scope="session")
def aws_client_factory(aws_session):
    return base_aws_client_factory(aws_session)


@pytest.fixture(scope="session")
def aws_client(aws_client_factory):
    return base_testing_aws_client(aws_client_factory)


@pytest.fixture(scope="function")
def snapshot(_snapshot_session):
    return _snapshot_session
