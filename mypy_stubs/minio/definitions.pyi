from typing import Any, Optional

class Bucket:
    name: Any = ...
    creation_date: Any = ...
    def __init__(self, name: Any, created: Any) -> None: ...

class Object:
    bucket_name: Any = ...
    object_name: Any = ...
    last_modified: Any = ...
    etag: Any = ...
    size: Any = ...
    content_type: Any = ...
    is_dir: Any = ...
    metadata: Any = ...
    def __init__(self, bucket_name: Any, object_name: Any, last_modified: Any, etag: Any, size: Any, content_type: Optional[Any] = ..., is_dir: bool = ..., metadata: Optional[Any] = ...) -> None: ...

class MultipartUploadResult:
    bucket_name: Any = ...
    object_name: Any = ...
    location: Any = ...
    etag: Any = ...
    def __init__(self, bucket_name: Any, object_name: Any, location: Any, etag: Any) -> None: ...

class CopyObjectResult:
    bucket_name: Any = ...
    object_name: Any = ...
    etag: Any = ...
    last_modified: Any = ...
    def __init__(self, bucket_name: Any, object_name: Any, etag: Any, last_modified: Any) -> None: ...

class IncompleteUpload:
    bucket_name: Any = ...
    object_name: Any = ...
    upload_id: Any = ...
    initiated: Any = ...
    size: int = ...
    def __init__(self, bucket_name: Any, object_name: Any, upload_id: Any, initiated: Any) -> None: ...

class UploadPart:
    bucket_name: Any = ...
    object_name: Any = ...
    upload_id: Any = ...
    part_number: Any = ...
    etag: Any = ...
    last_modified: Any = ...
    size: Any = ...
    def __init__(self, bucket_name: Any, object_name: Any, upload_id: Any, part_number: Any, etag: Any, last_modified: Any, size: Any) -> None: ...
