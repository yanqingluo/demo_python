# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dzhyun.zhubi.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dzhyun.zhubi.proto',
  package='dzhyun',
  syntax='proto2',
  serialized_pb=_b('\n\x12\x64zhyun.zhubi.proto\x12\x06\x64zhyun\"f\n\x0bZhubiDangri\x12\n\n\x02Id\x18\x01 \x02(\x03\x12\x0f\n\x07ShiJian\x18\x02 \x02(\x03\x12\x11\n\tZuiXinJia\x18\x03 \x01(\x03\x12\x16\n\x0e\x43hengJiaoLiang\x18\x04 \x01(\x03\x12\x0f\n\x07ZhubiId\x18\x05 \x01(\x03\x42\x12\n\x10\x63om.dzhyun.proto')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ZHUBIDANGRI = _descriptor.Descriptor(
  name='ZhubiDangri',
  full_name='dzhyun.ZhubiDangri',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='dzhyun.ZhubiDangri.Id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ShiJian', full_name='dzhyun.ZhubiDangri.ShiJian', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ZuiXinJia', full_name='dzhyun.ZhubiDangri.ZuiXinJia', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ChengJiaoLiang', full_name='dzhyun.ZhubiDangri.ChengJiaoLiang', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ZhubiId', full_name='dzhyun.ZhubiDangri.ZhubiId', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=132,
)

DESCRIPTOR.message_types_by_name['ZhubiDangri'] = _ZHUBIDANGRI

ZhubiDangri = _reflection.GeneratedProtocolMessageType('ZhubiDangri', (_message.Message,), dict(
  DESCRIPTOR = _ZHUBIDANGRI,
  __module__ = 'dzhyun.zhubi_pb2'
  # @@protoc_insertion_point(class_scope:dzhyun.ZhubiDangri)
  ))
_sym_db.RegisterMessage(ZhubiDangri)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\020com.dzhyun.proto'))
# @@protoc_insertion_point(module_scope)
