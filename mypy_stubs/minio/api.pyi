from .compat import basestring as basestring, queryencode as queryencode, range as range, urlsplit as urlsplit
from .definitions import Object as Object, UploadPart as UploadPart
from .error import AccessDenied as AccessDenied, InvalidArgumentError as InvalidArgumentError, InvalidSizeError as InvalidSizeError, InvalidXMLError as InvalidXMLError, NoSuchBucket as NoSuchBucket, ResponseError as ResponseError
from .fold_case_dict import FoldCaseDict as FoldCaseDict
from .helpers import DEFAULT_PART_SIZE as DEFAULT_PART_SIZE, MAX_MULTIPART_COUNT as MAX_MULTIPART_COUNT, MAX_PART_SIZE as MAX_PART_SIZE, MAX_POOL_SIZE as MAX_POOL_SIZE, MIN_PART_SIZE as MIN_PART_SIZE, amzprefix_user_metadata as amzprefix_user_metadata, dump_http as dump_http, get_md5_base64digest as get_md5_base64digest, get_s3_region_from_endpoint as get_s3_region_from_endpoint, get_sha256_hexdigest as get_sha256_hexdigest, get_target_url as get_target_url, is_amz_header as is_amz_header, is_non_empty_string as is_non_empty_string, is_supported_header as is_supported_header, is_valid_bucket_name as is_valid_bucket_name, is_valid_bucket_notification_config as is_valid_bucket_notification_config, is_valid_endpoint as is_valid_endpoint, is_valid_policy_type as is_valid_policy_type, is_valid_source_sse_object as is_valid_source_sse_object, is_valid_sse_c_object as is_valid_sse_c_object, is_valid_sse_object as is_valid_sse_object, mkdir_p as mkdir_p, optimal_part_info as optimal_part_info, read_full as read_full
from .parsers import parse_copy_object as parse_copy_object, parse_get_bucket_notification as parse_get_bucket_notification, parse_list_buckets as parse_list_buckets, parse_list_multipart_uploads as parse_list_multipart_uploads, parse_list_objects as parse_list_objects, parse_list_objects_v2 as parse_list_objects_v2, parse_list_parts as parse_list_parts, parse_location_constraint as parse_location_constraint, parse_multi_object_delete_response as parse_multi_object_delete_response, parse_multipart_upload_result as parse_multipart_upload_result, parse_new_multipart_upload as parse_new_multipart_upload
from .select import SelectObjectReader as SelectObjectReader
from .signer import generate_credential_string as generate_credential_string, post_presign_signature as post_presign_signature, presign_v4 as presign_v4, sign_v4 as sign_v4
from .thread_pool import ThreadPool as ThreadPool
from .xml_marshal import xml_marshal_bucket_constraint as xml_marshal_bucket_constraint, xml_marshal_bucket_notifications as xml_marshal_bucket_notifications, xml_marshal_complete_multipart_upload as xml_marshal_complete_multipart_upload, xml_marshal_delete_objects as xml_marshal_delete_objects, xml_marshal_select as xml_marshal_select
from typing import Any, Optional

JSONDecodeError = ValueError

class Minio:
    def __init__(self, endpoint: Any, access_key: Optional[Any] = ..., secret_key: Optional[Any] = ..., session_token: Optional[Any] = ..., secure: bool = ..., region: Optional[Any] = ..., http_client: Optional[Any] = ...) -> None: ...
    def set_app_info(self, app_name: Any, app_version: Any) -> None: ...
    def trace_on(self, stream: Any) -> None: ...
    def trace_off(self) -> None: ...
    def select_object_content(self, bucket_name: Any, object_name: Any, opts: Any): ...
    def make_bucket(self, bucket_name: Any, location: str = ...) -> None: ...
    def list_buckets(self): ...
    def bucket_exists(self, bucket_name: Any): ...
    def remove_bucket(self, bucket_name: Any) -> None: ...
    def get_bucket_policy(self, bucket_name: Any): ...
    def delete_bucket_policy(self, bucket_name: Any) -> None: ...
    def set_bucket_policy(self, bucket_name: Any, policy: Any) -> None: ...
    def get_bucket_notification(self, bucket_name: Any): ...
    def set_bucket_notification(self, bucket_name: Any, notifications: Any) -> None: ...
    def remove_all_bucket_notification(self, bucket_name: Any) -> None: ...
    def listen_bucket_notification(self, bucket_name: Any, prefix: str = ..., suffix: str = ..., events: Any = ...) -> None: ...
    def fput_object(self, bucket_name: Any, object_name: Any, file_path: Any, content_type: str = ..., metadata: Optional[Any] = ..., sse: Optional[Any] = ..., progress: Optional[Any] = ..., part_size: Any = ...): ...
    def fget_object(self, bucket_name: Any, object_name: Any, file_path: Any, request_headers: Optional[Any] = ..., sse: Optional[Any] = ...): ...
    def get_object(self, bucket_name: Any, object_name: Any, request_headers: Optional[Any] = ..., sse: Optional[Any] = ...): ...
    def get_partial_object(self, bucket_name: Any, object_name: Any, offset: int = ..., length: int = ..., request_headers: Optional[Any] = ..., sse: Optional[Any] = ...): ...
    def copy_object(self, bucket_name: Any, object_name: Any, object_source: Any, conditions: Optional[Any] = ..., source_sse: Optional[Any] = ..., sse: Optional[Any] = ..., metadata: Optional[Any] = ...): ...
    def put_object(self, bucket_name: Any, object_name: Any, data: Any, length: Any, content_type: str = ..., metadata: Optional[Any] = ..., sse: Optional[Any] = ..., progress: Optional[Any] = ..., part_size: Any = ...): ...
    def list_objects(self, bucket_name: Any, prefix: str = ..., recursive: bool = ...) -> None: ...
    def list_objects_v2(self, bucket_name: Any, prefix: str = ..., recursive: bool = ..., start_after: str = ...) -> None: ...
    def stat_object(self, bucket_name: Any, object_name: Any, sse: Optional[Any] = ...): ...
    def remove_object(self, bucket_name: Any, object_name: Any) -> None: ...
    def remove_objects(self, bucket_name: Any, objects_iter: Any) -> None: ...
    def list_incomplete_uploads(self, bucket_name: Any, prefix: str = ..., recursive: bool = ...): ...
    def remove_incomplete_upload(self, bucket_name: Any, object_name: Any) -> None: ...
    def presigned_url(self, method: Any, bucket_name: Any, object_name: Any, expires: Any = ..., response_headers: Optional[Any] = ..., request_date: Optional[Any] = ...): ...
    def presigned_get_object(self, bucket_name: Any, object_name: Any, expires: Any = ..., response_headers: Optional[Any] = ..., request_date: Optional[Any] = ...): ...
    def presigned_put_object(self, bucket_name: Any, object_name: Any, expires: Any = ...): ...
    def presigned_post_policy(self, post_policy: Any): ...
