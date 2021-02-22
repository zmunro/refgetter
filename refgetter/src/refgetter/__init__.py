from typing import Any

import fire
import requests

def client_cli(seq_id: str = None, help: Any = None) -> None:
    """client_cli
        CLI for retrieving reference metadata from CRAM refget api endpoint
    Args:
        seq_id: (str) CRAM reference sequence ID
        help: (Any) used for optional --help command line flag for usage information
    """
    if help is not None:
        print_usage_message()
        return

    if seq_id is None:
        print_usage_message()
        return

    response = send_get_request(seq_id)
    if response.status_code == 404:
        print("ERROR: no sequence found with that id")
    elif response.status_code >= 500:
        print("INTERNAL SERVER ERROR: refget api endpoint is currently nonfuctional.")
    elif response.status_code == 200:
        json_dict = response.json()
        print_metadata(json_dict["metadata"])


def print_usage_message():
    """print_usage_message prints a message about how to use CLI tool"""
    print("Please supply a reference id to query in the format: --seq_id {sequence_id}")


def send_get_request(seq_id: str) -> requests.Response:
    """send_get_request
        Simple function to send get request for sequence metadata, having this as a function makes
        testing of different responses easier
    Args:
        seq_id: (str) sequence id to retrieve metadata for
    Returns:
        (requests.Response): CRAM metadata endpoint response object
    """
    return requests.get(
        url=f"https://www.ebi.ac.uk/ena/cram/sequence/{seq_id}/metadata",
    )


def print_metadata(metadata_dict: dict) -> None:
    """print_metadata
        prints out the metadata object in a nice format
    Args:
        metadata_dict: (dict) dictionary mapping sequence metadata attributes to values
    """
    print("Metadata:")
    for key, val in metadata_dict.items():
        print(f"\t{key}: {val}")


def main():
    fire.Fire(client_cli)
