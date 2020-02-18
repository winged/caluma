from rest_framework import VERSION as VERSION, exceptions as exceptions, serializers as serializers, status as status
from rest_framework.compat import INDENT_SEPARATORS as INDENT_SEPARATORS, LONG_SEPARATORS as LONG_SEPARATORS, SHORT_SEPARATORS as SHORT_SEPARATORS, coreapi as coreapi, coreschema as coreschema, pygments_css as pygments_css, yaml as yaml
from rest_framework.exceptions import ParseError as ParseError
from rest_framework.request import is_form_media_type as is_form_media_type, override_method as override_method
from rest_framework.settings import api_settings as api_settings
from rest_framework.utils import encoders as encoders, json as json
from rest_framework.utils.breadcrumbs import get_breadcrumbs as get_breadcrumbs
from rest_framework.utils.field_mapping import ClassLookupDict as ClassLookupDict
from typing import Any, Optional

def zero_as_none(value: Any): ...

class BaseRenderer:
    media_type: Any = ...
    format: Any = ...
    charset: str = ...
    render_style: str = ...
    def render(self, data: Any, accepted_media_type: Optional[Any] = ..., renderer_context: Optional[Any] = ...) -> None: ...

class JSONRenderer(BaseRenderer):
    media_type: str = ...
    format: str = ...
    encoder_class: Any = ...
    ensure_ascii: Any = ...
    compact: Any = ...
    strict: Any = ...
    charset: Any = ...
    def get_indent(self, accepted_media_type: Any, renderer_context: Any): ...
    def render(self, data: Any, accepted_media_type: Optional[Any] = ..., renderer_context: Optional[Any] = ...): ...

class TemplateHTMLRenderer(BaseRenderer):
    media_type: str = ...
    format: str = ...
    template_name: Any = ...
    exception_template_names: Any = ...
    charset: str = ...
    def render(self, data: Any, accepted_media_type: Optional[Any] = ..., renderer_context: Optional[Any] = ...): ...
    def resolve_template(self, template_names: Any): ...
    def get_template_context(self, data: Any, renderer_context: Any): ...
    def get_template_names(self, response: Any, view: Any): ...
    def get_exception_template(self, response: Any): ...

class StaticHTMLRenderer(TemplateHTMLRenderer):
    media_type: str = ...
    format: str = ...
    charset: str = ...
    def render(self, data: Any, accepted_media_type: Optional[Any] = ..., renderer_context: Optional[Any] = ...): ...

class HTMLFormRenderer(BaseRenderer):
    media_type: str = ...
    format: str = ...
    charset: str = ...
    template_pack: str = ...
    base_template: str = ...
    default_style: Any = ...
    def render_field(self, field: Any, parent_style: Any): ...
    def render(self, data: Any, accepted_media_type: Optional[Any] = ..., renderer_context: Optional[Any] = ...): ...

class BrowsableAPIRenderer(BaseRenderer):
    media_type: str = ...
    format: str = ...
    template: str = ...
    filter_template: str = ...
    code_style: str = ...
    charset: str = ...
    form_renderer_class: Any = ...
    def get_default_renderer(self, view: Any): ...
    def get_content(self, renderer: Any, data: Any, accepted_media_type: Any, renderer_context: Any): ...
    def show_form_for_method(self, view: Any, method: Any, request: Any, obj: Any): ...
    def get_rendered_html_form(self, data: Any, view: Any, method: Any, request: Any): ...
    def render_form_for_serializer(self, serializer: Any): ...
    def get_raw_data_form(self, data: Any, view: Any, method: Any, request: Any): ...
    def get_name(self, view: Any): ...
    def get_description(self, view: Any, status_code: Any): ...
    def get_breadcrumbs(self, request: Any): ...
    def get_extra_actions(self, view: Any, status_code: Any): ...
    def get_filter_form(self, data: Any, view: Any, request: Any): ...
    def get_context(self, data: Any, accepted_media_type: Any, renderer_context: Any): ...
    accepted_media_type: Any = ...
    renderer_context: Any = ...
    def render(self, data: Any, accepted_media_type: Optional[Any] = ..., renderer_context: Optional[Any] = ...): ...

class AdminRenderer(BrowsableAPIRenderer):
    template: str = ...
    format: str = ...
    accepted_media_type: Any = ...
    renderer_context: Any = ...
    error_form: Any = ...
    error_title: Any = ...
    def render(self, data: Any, accepted_media_type: Optional[Any] = ..., renderer_context: Optional[Any] = ...): ...
    def get_context(self, data: Any, accepted_media_type: Any, renderer_context: Any): ...
    def get_result_url(self, result: Any, view: Any): ...

class DocumentationRenderer(BaseRenderer):
    media_type: str = ...
    format: str = ...
    charset: str = ...
    template: str = ...
    error_template: str = ...
    code_style: str = ...
    languages: Any = ...
    def get_context(self, data: Any, request: Any): ...
    def render(self, data: Any, accepted_media_type: Optional[Any] = ..., renderer_context: Optional[Any] = ...): ...

class SchemaJSRenderer(BaseRenderer):
    media_type: str = ...
    format: str = ...
    charset: str = ...
    template: str = ...
    def render(self, data: Any, accepted_media_type: Optional[Any] = ..., renderer_context: Optional[Any] = ...): ...

class MultiPartRenderer(BaseRenderer):
    media_type: str = ...
    format: str = ...
    charset: str = ...
    BOUNDARY: str = ...
    def render(self, data: Any, accepted_media_type: Optional[Any] = ..., renderer_context: Optional[Any] = ...): ...

class CoreJSONRenderer(BaseRenderer):
    media_type: str = ...
    charset: Any = ...
    format: str = ...
    def __init__(self) -> None: ...
    def render(self, data: Any, media_type: Optional[Any] = ..., renderer_context: Optional[Any] = ...): ...

class _BaseOpenAPIRenderer:
    def get_schema(self, instance: Any): ...
    def get_parameters(self, link: Any): ...
    def get_operation(self, link: Any, name: Any, tag: Any): ...
    def get_paths(self, document: Any): ...
    def get_structure(self, data: Any): ...

class CoreAPIOpenAPIRenderer(_BaseOpenAPIRenderer):
    media_type: str = ...
    charset: Any = ...
    format: str = ...
    def __init__(self) -> None: ...
    def render(self, data: Any, media_type: Optional[Any] = ..., renderer_context: Optional[Any] = ...): ...

class CoreAPIJSONOpenAPIRenderer(_BaseOpenAPIRenderer):
    media_type: str = ...
    charset: Any = ...
    format: str = ...
    def __init__(self) -> None: ...
    def render(self, data: Any, media_type: Optional[Any] = ..., renderer_context: Optional[Any] = ...): ...

class OpenAPIRenderer(BaseRenderer):
    media_type: str = ...
    charset: Any = ...
    format: str = ...
    def __init__(self) -> None: ...
    def render(self, data: Any, media_type: Optional[Any] = ..., renderer_context: Optional[Any] = ...): ...

class JSONOpenAPIRenderer(BaseRenderer):
    media_type: str = ...
    charset: Any = ...
    format: str = ...
    def render(self, data: Any, media_type: Optional[Any] = ..., renderer_context: Optional[Any] = ...): ...
