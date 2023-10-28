"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error as shared_error
from ..shared import pet as shared_pet
from typing import Dict, List, Optional


@dataclasses.dataclass
class ListPetsRequest:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""How many items to return at one time (max 100)"""
    



@dataclasses.dataclass
class ListPetsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""unexpected error"""
    headers: Optional[Dict[str, List[str]]] = dataclasses.field(default=None)
    pets: Optional[List[shared_pet.Pet]] = dataclasses.field(default=None)
    r"""A paged array of pets"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

