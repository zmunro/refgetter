import io
import sys
from unittest import mock
from dataclasses import dataclass

import pytest

from refgetter import client_cli, send_get_request, print_metadata


@dataclass
class MockResponseObject:
    status_code: int
    metadata: dict

    def json(self):
        return {'metadata': self.metadata}

@pytest.fixture
def mock_send_get_request():
    """mock_send_get_request mocks the send_get_request function to return a 500 error status"""
    with mock.patch("refgetter.send_get_request") as mock_send_get_request:
        yield mock_send_get_request


def test_client_cli_404(mock_send_get_request):
    """test_client_cli_404 tests to make sure a 404 status code from the refget API return
    the correct error message
    """
    mock_send_get_request.return_value = MockResponseObject(status_code=404, metadata=dict())
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    client_cli(seq_id="bad-seq-id")
    sys.stdout = sys.__stdout__
    expected_error_message = "ERROR: no sequence found with that id"
    actual_output = capturedOutput.getvalue()
    assert actual_output.strip() == expected_error_message, (
        f"Error, expected to get message '{expected_error_message}'"
        f" but instead got '{actual_output}'"
    )


def test_client_cli_500(mock_send_get_request):
    """test_client_cli_500 tests to make sure a 500 status code from the refget API return
    the correct error message
    """
    mock_send_get_request.return_value = MockResponseObject(status_code=500, metadata=dict())
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    client_cli(seq_id="any-seq-id")
    sys.stdout = sys.__stdout__
    expected_error_message = (
        "INTERNAL SERVER ERROR: refget api endpoint is currently nonfuctional."
    )
    actual_output = capturedOutput.getvalue()
    assert actual_output.strip() == expected_error_message, (
        f"Error, expected to get message '{expected_error_message}'"
        f" but instead got '{actual_output}'"
    )


def test_client_cli_200(mock_send_get_request):
    """test_client_cli_200 tests to make sure the correct output gets printed when a valid seq_id
        is passed and a 200 status code is returned
    """
    test_metadata = {
        "id": "3050107579885e1608e6fe50fae3f8d0",
        "md5": "3050107579885e1608e6fe50fae3f8d0",
        "trunc512": None,
        "length": 7156,
        "aliases": [],
    }
    mock_send_get_request.return_value = MockResponseObject(status_code=200, metadata=test_metadata)
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    client_cli(seq_id="vali-seq-id")
    sys.stdout = sys.__stdout__
    expected_output = "Metadata:"
    for key, value in test_metadata.items():
        expected_output += f"\n\t{key}: {value}"
    actual_output = capturedOutput.getvalue()
    assert actual_output.strip() == expected_output, (
        f"Error, expected to get message '{expected_output}'"
        f" but instead got '{actual_output}'"
    )

def test_client_cli_help_command():
    """test_client_cli_help_command tests to make sure the correct message is printed when
    client asks for help with the --help flag
    """
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    client_cli(help="test")
    sys.stdout = sys.__stdout__
    expected_help_message = (
        "Please supply a reference id to query in the format: --seq_id {sequence_id}"
    )
    actual_output = capturedOutput.getvalue()
    assert actual_output.strip() == expected_help_message, (
        f"Error, expected to get message '{expected_help_message}'"
        f" but instead got '{actual_output}'"
    )

def test_client_cli_no_seq_id_command():
    """test_client_cli_no_seq_id_command tests to make sure the correct message is printed when
    client does not provide a seq_id
    """
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    client_cli()
    sys.stdout = sys.__stdout__
    expected_help_message = (
        "Please supply a reference id to query in the format: --seq_id {sequence_id}"
    )
    actual_output = capturedOutput.getvalue()
    assert actual_output.strip() == expected_help_message, (
        f"Error, expected to get message '{expected_help_message}'"
        f" but instead got '{actual_output}'"
    )