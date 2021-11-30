# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: comments.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="comments.proto",
    package="comments",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0e\x63omments.proto\x12\x08\x63omments",\n\x07\x43omment\x12\x10\n\x08tweet_id\x18\x01 \x01(\x05\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t"7\n\x13PostCommentResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08"%\n\x11GetCommentRequest\x12\x10\n\x08tweet_id\x18\x01 \x01(\x05"J\n\x12GetCommentResponse\x12#\n\x08\x63omments\x18\x01 \x03(\x0b\x32\x11.comments.Comment\x12\x0f\n\x07success\x18\x02 \x01(\x08\x32\x99\x01\n\x08\x43omments\x12\x41\n\x0bPostComment\x12\x11.comments.Comment\x1a\x1d.comments.PostCommentResponse"\x00\x12J\n\x0bGetComments\x12\x1b.comments.GetCommentRequest\x1a\x1c.comments.GetCommentResponse"\x00\x62\x06proto3',
)


_COMMENT = _descriptor.Descriptor(
    name="Comment",
    full_name="comments.Comment",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="tweet_id",
            full_name="comments.Comment.tweet_id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="comment",
            full_name="comments.Comment.comment",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=28,
    serialized_end=72,
)


_POSTCOMMENTRESPONSE = _descriptor.Descriptor(
    name="PostCommentResponse",
    full_name="comments.PostCommentResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="message",
            full_name="comments.PostCommentResponse.message",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="success",
            full_name="comments.PostCommentResponse.success",
            index=1,
            number=2,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=74,
    serialized_end=129,
)


_GETCOMMENTREQUEST = _descriptor.Descriptor(
    name="GetCommentRequest",
    full_name="comments.GetCommentRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="tweet_id",
            full_name="comments.GetCommentRequest.tweet_id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=131,
    serialized_end=168,
)


_GETCOMMENTRESPONSE = _descriptor.Descriptor(
    name="GetCommentResponse",
    full_name="comments.GetCommentResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="comments",
            full_name="comments.GetCommentResponse.comments",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="success",
            full_name="comments.GetCommentResponse.success",
            index=1,
            number=2,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=170,
    serialized_end=244,
)

_GETCOMMENTRESPONSE.fields_by_name["comments"].message_type = _COMMENT
DESCRIPTOR.message_types_by_name["Comment"] = _COMMENT
DESCRIPTOR.message_types_by_name["PostCommentResponse"] = _POSTCOMMENTRESPONSE
DESCRIPTOR.message_types_by_name["GetCommentRequest"] = _GETCOMMENTREQUEST
DESCRIPTOR.message_types_by_name["GetCommentResponse"] = _GETCOMMENTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Comment = _reflection.GeneratedProtocolMessageType(
    "Comment",
    (_message.Message,),
    {
        "DESCRIPTOR": _COMMENT,
        "__module__": "comments_pb2"
        # @@protoc_insertion_point(class_scope:comments.Comment)
    },
)
_sym_db.RegisterMessage(Comment)

PostCommentResponse = _reflection.GeneratedProtocolMessageType(
    "PostCommentResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _POSTCOMMENTRESPONSE,
        "__module__": "comments_pb2"
        # @@protoc_insertion_point(class_scope:comments.PostCommentResponse)
    },
)
_sym_db.RegisterMessage(PostCommentResponse)

GetCommentRequest = _reflection.GeneratedProtocolMessageType(
    "GetCommentRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETCOMMENTREQUEST,
        "__module__": "comments_pb2"
        # @@protoc_insertion_point(class_scope:comments.GetCommentRequest)
    },
)
_sym_db.RegisterMessage(GetCommentRequest)

GetCommentResponse = _reflection.GeneratedProtocolMessageType(
    "GetCommentResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETCOMMENTRESPONSE,
        "__module__": "comments_pb2"
        # @@protoc_insertion_point(class_scope:comments.GetCommentResponse)
    },
)
_sym_db.RegisterMessage(GetCommentResponse)


_COMMENTS = _descriptor.ServiceDescriptor(
    name="Comments",
    full_name="comments.Comments",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=247,
    serialized_end=400,
    methods=[
        _descriptor.MethodDescriptor(
            name="PostComment",
            full_name="comments.Comments.PostComment",
            index=0,
            containing_service=None,
            input_type=_COMMENT,
            output_type=_POSTCOMMENTRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="GetComments",
            full_name="comments.Comments.GetComments",
            index=1,
            containing_service=None,
            input_type=_GETCOMMENTREQUEST,
            output_type=_GETCOMMENTRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_COMMENTS)

DESCRIPTOR.services_by_name["Comments"] = _COMMENTS

# @@protoc_insertion_point(module_scope)
