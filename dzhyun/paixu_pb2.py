# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dzhyun.paixu.proto

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
  name='dzhyun.paixu.proto',
  package='dzhyun',
  syntax='proto2',
  serialized_pb=_b('\n\x12\x64zhyun.paixu.proto\x12\x06\x64zhyun\"1\n\x05PaiXu\x12\x0b\n\x03Obj\x18\x01 \x02(\t\x12\r\n\x05Value\x18\x02 \x01(\x03\x12\x0c\n\x04Text\x18\x03 \x01(\t\"C\n\x07PaiMing\x12\x0b\n\x03Obj\x18\x01 \x02(\t\x12\r\n\x05Value\x18\x02 \x01(\x03\x12\x0c\n\x04Text\x18\x03 \x01(\t\x12\x0e\n\x06MingCi\x18\x04 \x01(\x03\x42\x12\n\x10\x63om.dzhyun.proto')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PAIXU = _descriptor.Descriptor(
  name='PaiXu',
  full_name='dzhyun.PaiXu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Obj', full_name='dzhyun.PaiXu.Obj', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Value', full_name='dzhyun.PaiXu.Value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Text', full_name='dzhyun.PaiXu.Text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_end=79,
)


_PAIMING = _descriptor.Descriptor(
  name='PaiMing',
  full_name='dzhyun.PaiMing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Obj', full_name='dzhyun.PaiMing.Obj', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Value', full_name='dzhyun.PaiMing.Value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Text', full_name='dzhyun.PaiMing.Text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MingCi', full_name='dzhyun.PaiMing.MingCi', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
  serialized_start=81,
  serialized_end=148,
)

DESCRIPTOR.message_types_by_name['PaiXu'] = _PAIXU
DESCRIPTOR.message_types_by_name['PaiMing'] = _PAIMING

PaiXu = _reflection.GeneratedProtocolMessageType('PaiXu', (_message.Message,), dict(
  DESCRIPTOR = _PAIXU,
  __module__ = 'dzhyun.paixu_pb2'
  # @@protoc_insertion_point(class_scope:dzhyun.PaiXu)
  ))
_sym_db.RegisterMessage(PaiXu)

PaiMing = _reflection.GeneratedProtocolMessageType('PaiMing', (_message.Message,), dict(
  DESCRIPTOR = _PAIMING,
  __module__ = 'dzhyun.paixu_pb2'
  # @@protoc_insertion_point(class_scope:dzhyun.PaiMing)
  ))
_sym_db.RegisterMessage(PaiMing)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\020com.dzhyun.proto'))
# @@protoc_insertion_point(module_scope)
